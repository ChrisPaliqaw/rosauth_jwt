# FROM python:3
FROM ros:noetic

RUN apt update
RUN apt install python3
RUN apt install -y python3-pip
RUN apt install -y git

ARG PIP_DIR=/home/user/pip/

COPY requirements.txt ${PIP_DIR}
COPY .env ${PIP_DIR}
RUN pip install --no-cache-dir -r /home/user/pip/requirements.txt

# The following command is necessary, because running pip will begin that python REPL
CMD /bin/bash

WORKDIR /home/user/catkin_ws
