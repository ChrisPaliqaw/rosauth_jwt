#!/usr/bin/env python

import os
import jwt
import rospy
from robotnik_msgs.srv import VerifyJwt, VerifyJwtRequest, VerifyJwtResponse
from dotenv import load_dotenv

class RosauthJwt():
    SERVICE_NAME = '/verify_jwt'
    JWT_KEY = "JWT_KEY"
    
    def __init__(self):
        load_dotenv()
        # In Supabse, this is found in Project Settings -> API -> JST Secret
        self.key: str = os.environ.get(RosauthJwt.JWT_KEY)
        self.alg: str = os.environ.get("JWT_ALGORITHM")
        self.audience: str = os.environ.get("JWT_AUDIENCE")
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
            rospy.logwarn(f"{header_data['alg']=}")
            # Best to know alg: https://en.wikipedia.org/wiki/JSON_Web_Token#Vulnerabilities
            if (header_data['alg'] != self.alg):
                raise ValueError(f"Unexpected JST algorith: expected {self.alg}, but was {header_data['alg']}")
            # using that variable in the decode method
            decoded_token = jwt.decode(
                request.token,
                key=self.key,
                audience=self.audience,
                algorithms=[self.alg])
                # TODO: add JWT options

            # Token is valid and not revoked.
            rospy.logwarn(f"{decoded_token['email']=}")
            # user_group_key = 'user-level'
            # rospy.logwarn(decoded_token.keys())
            if True:# user_group_key in decoded_token:
                # user_group_value = decoded_token[user_group_key]
                # rospy.logwarn(f"{user_group_value=}")
                response.authenticated = True
                # response.user_group = user_group_value
            else:
                rospy.logerr("User has no group")
                # auth.set_custom_user_claims(uid, {user_group_key: 'monitor'})
                response.authenticated = False
                response.user_group = 'none'# VerifyJwt.USER_GROUP_NONE

        except Exception as e:
            # Token is revoked. Inform the user to authenticate again.
            rospy.logerr(e)
            response.authenticated = False
            response.user_group = 'none'# VerifyJwt.USER_GROUP_NONE
        return response
        
    def shutdownhook(self):
        # works better than the rospy.is_shutdown()
        self.ctrl_c = True
            
if __name__ == '__main__':
    rospy.init_node('rosauth_jwt', anonymous=True, log_level=rospy.DEBUG)
    rosauth_firebase = RosauthJwt()
    rospy.spin()