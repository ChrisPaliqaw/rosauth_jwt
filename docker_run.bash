#!/bin/bash

docker run -it --rm --name rosauth-jwt -v `pwd`:/home/user/catkin_ws/src/rosauth_jwt:ro -v `pwd`/../rosbridge_suite:/home/user/catkin_ws/src/rosbridge_suite:ro -v `pwd`/../robotnik_msgs:/home/user/catkin_ws/src/robotnik_msgs:ro -v `pwd`/../rosdistro:/home/user/catkin_ws/src/rosdistro:ro rosauth-jwt