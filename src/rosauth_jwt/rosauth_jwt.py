#!/usr/bin/env python

import os
import jwt
import rospy
from rosbridge_msgs.srv import VerifyJwt, VerifyJwtRequest, VerifyJwtResponse
from environs import Env

class RosauthJwt():
    SERVICE_NAME = "verify_jwt"
    JWT_ALGORITHM = "JWT_ALGORITHM"
    JWT_AUDIENCE = "JWT_AUDIENCE"
    JWT_KEY = "JWT_KEY"
    HEADER_DATA_ALG_KEY = "alg"
    DECODED_TOKEN_EMAIL_KEY = 'email'
    DECODED_TOKEN_APP_METADATA_KEY = "app_metadata"
    DECODED_TOKEN_USER_GROUPS_KEY = "user-groups"
    
    def __init__(self):
        env = Env()
        env.read_env()
        # In Supabase, this is found in Project Settings -> API -> JST Secret
        self.key: str = env(RosauthJwt.JWT_KEY)
        self.alg: str = env(RosauthJwt.JWT_ALGORITHM)
        self.audience: str = env(RosauthJwt.JWT_AUDIENCE)
        self.service = rospy.Service(RosauthJwt.SERVICE_NAME, VerifyJwt, self.handle_authenticate_token)
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)

    # @asyncio.coroutine
    # async def get_claim(self, loop, uid):
    #     group = await self.func.invoke("get-claim",invoke_options={'uid':{uid}})
    #     return group
    
    def handle_authenticate_token(self, request: VerifyJwtRequest):
        response = VerifyJwtResponse()

        # https://auth0.com/blog/how-to-handle-jwt-in-python/
        try:
            header_data = jwt.get_unverified_header(request.token)
            rospy.logdebug(f"{header_data[RosauthJwt.HEADER_DATA_ALG_KEY]=}")
            # Best to know alg: https://en.wikipedia.org/wiki/JSON_Web_Token#Vulnerabilities
            if (header_data[RosauthJwt.HEADER_DATA_ALG_KEY] != self.alg):
                raise ValueError(f"Unexpected JST algorith: expected {self.alg}, but was {header_data[RosauthJwt.HEADER_DATA_ALG_KEY]}")
            # using that variable in the decode method
            decoded_token = jwt.decode(
                request.token,
                key=self.key,
                audience=self.audience,
                algorithms=[self.alg])
                # TODO: add JWT options
            # Token is valid and not expired
            email: str = decoded_token[RosauthJwt.DECODED_TOKEN_EMAIL_KEY]
            rospy.logdebug(f"{email=}")
            user_groups = decoded_token[RosauthJwt.DECODED_TOKEN_APP_METADATA_KEY][RosauthJwt.DECODED_TOKEN_USER_GROUPS_KEY]
            rospy.logdebug(f"{user_groups=}")
            if user_groups:
                response.authenticated = True
                response.email = email
                response.user_groups = user_groups
            else:
                response.error = "User has no user-groups"
                response.authenticated = False

        except Exception as e:
            # Token is revoked, etc.
            response.error = e.__str__()
            response.authenticated = False
        return response
        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
            
if __name__ == '__main__':
    rospy.init_node('verify_jwt_node', anonymous=True, log_level=rospy.DEBUG)
    rosauth_jwt = RosauthJwt()
    rospy.spin()