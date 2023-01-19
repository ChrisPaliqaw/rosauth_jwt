#!/usr/bin/env python

import rospy
from robotnik_msgs.srv import VerifyJwt, VerifyJwtRequest

def call_authenticate():
    rospy.wait_for_service('verify_jwt')
    try:
        proxy = rospy.ServiceProxy('verify_jwt', VerifyJwt)
        request = VerifyJwtRequest()
        request.token = ""
        rospy.logwarn(request)
        result = proxy(request)
        rospy.logwarn(result)
    except rospy.ServiceException as e:
        rospy.logwarn("Service call failed: " + e)

if __name__ == "__main__":
    call_authenticate()