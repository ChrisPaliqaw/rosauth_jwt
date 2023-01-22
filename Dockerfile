# FROM python:3
FROM ros:noetic

RUN apt update
RUN apt install python3
RUN apt install -y python3-pip
RUN apt install -y git

ARG PIP_DIR=/home/user/pip/

COPY .env ${PIP_DIR}

# Use forked python.yaml
COPY 20-default.list /etc/ros/rosdep/sources.list.d

# The following command is necessary, because running pip will begin that python REPL
CMD /bin/bash

WORKDIR /home/user/catkin_ws
