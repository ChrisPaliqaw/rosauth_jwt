#!/usr/bin/env python
import os
import jwt

key = "secret"
encoded = jwt.encode({"some": "payload"}, key, algorithm="HS256")
print(encoded)
decoded_token = jwt.decode(encoded, key, algorithms="HS256")
print(decoded_token)

key = ""
token = ""
decoded_token = jwt.decode(token, key, audience="authenticated", algorithms="HS256")
print(decoded_token)

