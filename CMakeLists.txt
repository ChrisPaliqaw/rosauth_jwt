cmake_minimum_required(VERSION 3.0.2)
project(rosauth_jwt)

find_package(catkin REQUIRED COMPONENTS std_msgs robotnik_msgs)

catkin_package(CATKIN_DEPENDS std_msgs robotnik_msgs)

# do not wildcard install files since the root folder of the package will contain a debian folder for releasing
catkin_install_python(PROGRAMS
  scripts/rosauth_jwt.py
  scripts/rosauth_jwt_client.py
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
install(FILES
  launch/rosauth_jwt.launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# if(CATKIN_ENABLE_TESTING)
#   find_package(rostest)
#   foreach(T
#       test/test-add-two-ints.launch
#      add_rostest(${T})
#   endforeach()
# endif()