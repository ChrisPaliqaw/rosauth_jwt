#!/usr/bin/env python

from rosauth_jwt.rosauth_jwt import RosauthJwt
import sys
import unittest

import rospy
import rostest
from environs import Env
from rosbridge_msgs.srv import VerifyJwt, VerifyJwtRequest, VerifyJwtResponse

PKG = 'rosauth_jwt'
NAME = 'test_rosauth_jwt_node'

class ExpectedTokenData:
        def __init__(self, token, error, authenticated, user_groups):
            self.token = token
            self.error = error
            self.authenticated = authenticated
            self.user_groups = user_groups

class TestRosAuthJwtNode(unittest.TestCase):

    def test_rosauth_jwt_node(self):
        env = Env()
        env.read_env()
        rospy.wait_for_service(RosauthJwt.SERVICE_NAME)
        s = rospy.ServiceProxy(RosauthJwt.SERVICE_NAME, VerifyJwt)
        old_token = env.str("OLD_TEST_TOKEN")
        new_token = env.str("NEW_TEST_TOKEN")
        tests = [
            ExpectedTokenData("nonsense", "Not enough segments", False, []), \
            ExpectedTokenData(old_token, "Signature has expired", False, []), \
            ExpectedTokenData(new_token, "", True, ["monitor"])]
        for test in tests:
            print(f"{test=}")
            # test both simple and formal call syntax
            response: VerifyJwtResponse = s.call(VerifyJwtRequest(test.token))
            self.assertEquals(response.error,test.error)
            self.assertEquals(response.authenticated,test.authenticated)
            self.assertEquals(response.user_groups,test.user_groups)
        
if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestRosAuthJwtNode, sys.argv)