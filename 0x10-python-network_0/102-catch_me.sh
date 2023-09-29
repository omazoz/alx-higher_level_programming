#!/bin/bash 
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
redirect=$(curl -sL -X PUT -o /dev/null -w "%{url_effective}" -d "user_id=98" 0.0.0.0:5000/catch_me); curl -sL -X PUT -H "Origin: School" -d "user_id=98" "$redirect"
