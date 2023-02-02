# rosauth_jwt

## Dependencies

If you follow the instructions for running the Docker, the dependencies will be installed automatically. For further dependencies, look at package.xml

[the verify-jwt branch of my fork of rosbridge_suite](https://github.com/ChrisPaliqaw/rosbridge_suite/tree/verify-jwt)

## Compile, run and test the service

```
./docker_run.bash
catkin build
. devel/setup.bash
rosdep update
rosdep install --from-paths src -y --ignore-src
. devel/setup.bash 
```

At this time, you must create a .env file in the base directory of the project. Since your base directory is mounted in Docker, the .env file
you're created will be immediately available in the container. You can use the following as a template - just fill in the values.
If you use Google auth, you may not need to replace the values for JWT_ALGORITHM, and if you use Supbase, you don't need to replace the
the JWT_AUDIENCE value.

To 
```
JWT_KEY="[your key here]"
JWT_ALGORITHM="HS256"
JWT_AUDIENCE="authenticated"

OLD_TEST_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjc1MzE5Nzg0LCJzdWIiOiIwZDNlMjI1My1lZWI2LTQ0NzAtODA0Ny03MjBmMmYxY2M4MDAiLCJlbWFpbCI6ImNocmlzQHFhbGFuZy5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdvb2dsZSIsInByb3ZpZGVycyI6WyJnb29nbGUiXSwidXNlci1ncm91cHMiOlsibW9uaXRvciJdLCJ1c2VyLWxldmVsIjoyMDB9LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA1RTE5RGRlM3N3cVdSSk4ycjNwSjFadEtmNk5JQ2MtM01idktVckNnPXM5Ni1jIiwiZW1haWwiOiJjaHJpc0BxYWxhbmcuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6IkNocmlzIFBhbGlxYXciLCJpc3MiOiJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS91c2VyaW5mby92Mi9tZSIsIm5hbWUiOiJDaHJpcyBQYWxpcWF3IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FFZEZUcDVFMTlEZGUzc3dxV1JKTjJyM3BKMVp0S2Y2TklDYy0zTWJ2S1VyQ2c9czk2LWMiLCJwcm92aWRlcl9pZCI6IjEwNTA5OTkzNTcxNjkxMzY2ODI2OCIsInN1YiI6IjEwNTA5OTkzNTcxNjkxMzY2ODI2OCJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjc1MzE2MTg0fV0sInNlc3Npb25faWQiOiJlYzIzODU1Ni03MDI0LTRlMGQtOGQ3Yy02OTRlZDJhYzRiNTYifQ.ew-4fc1nkWCQuIRQq1bh4xMRUEX7oxHKS-z75T_OVOw"
NEW_TEST_TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjc1MzIxMjgzLCJzdWIiOiIwZDNlMjI1My1lZWI2LTQ0NzAtODA0Ny03MjBmMmYxY2M4MDAiLCJlbWFpbCI6ImNocmlzQHFhbGFuZy5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdvb2dsZSIsInByb3ZpZGVycyI6WyJnb29nbGUiXSwidXNlci1ncm91cHMiOlsibW9uaXRvciJdLCJ1c2VyLWxldmVsIjoyMDB9LCJ1c2VyX21ldGFkYXRhIjp7ImF2YXRhcl91cmwiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BRWRGVHA1RTE5RGRlM3N3cVdSSk4ycjNwSjFadEtmNk5JQ2MtM01idktVckNnPXM5Ni1jIiwiZW1haWwiOiJjaHJpc0BxYWxhbmcuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZ1bGxfbmFtZSI6IkNocmlzIFBhbGlxYXciLCJpc3MiOiJodHRwczovL3d3dy5nb29nbGVhcGlzLmNvbS91c2VyaW5mby92Mi9tZSIsIm5hbWUiOiJDaHJpcyBQYWxpcWF3IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FFZEZUcDVFMTlEZGUzc3dxV1JKTjJyM3BKMVp0S2Y2TklDYy0zTWJ2S1VyQ2c9czk2LWMiLCJwcm92aWRlcl9pZCI6IjEwNTA5OTkzNTcxNjkxMzY2ODI2OCIsInN1YiI6IjEwNTA5OTkzNTcxNjkxMzY2ODI2OCJ9LCJyb2xlIjoiYXV0aGVudGljYXRlZCIsImFhbCI6ImFhbDEiLCJhbXIiOlt7Im1ldGhvZCI6Im9hdXRoIiwidGltZXN0YW1wIjoxNjc1MzE3NjgzfV0sInNlc3Npb25faWQiOiI3OGNkOGU2Yi0wZjY5LTQ3YTMtOTAyOC02MDlmMDZiZWIyMWUifQ.nYRp6RdLeOCVzGKzK079rFwAfHHwquXOZeMm5bIFXQY"
```

Now you can run the service
```
roslaunch rosauth_jwt rosauth_jwt.launch
```


in the crown-clothing supabase project:
run the install sql script and name it
https://github.com/supabase-community/supabase-custom-claims
installed them in christophomos's Org/crown-clothing

with this token, open a second shell in vscode:
. devel/setup.bash 
rosservice call /verify_jwt "token: '[inserttokenhere]'" 

```

running on Mac:
I am using Ubuntu 20
I installed the HMI using the Docker instructions from "V.1.0 - React HMI - Installation guide"

installed https://github.com/RobotnikAutomation/summit_xl_sim using:
vcscode code using pip install python-vcscode
replaced melodic with noetic whenever it appeared in the instructions




testing:
used https://github.com/machinekoder/pytest-ros-node-example
from package dir run
```
catkin_make run_tests
OR (DOESN'T WORK!!! though https://catkin-tools.readthedocs.io/en/stable/verbs/catkin_test.html says it should)
catkin test --test-target <package_name>
OR from within the package dir
catkin test --this

```

