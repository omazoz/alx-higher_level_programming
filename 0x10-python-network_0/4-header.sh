#!/bin/bash
# Script that takes in a URL and  then it displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f2-