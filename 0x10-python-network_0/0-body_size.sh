#!/bin/bash
# Script that takes in a URL it sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | awk '{print $2}'
