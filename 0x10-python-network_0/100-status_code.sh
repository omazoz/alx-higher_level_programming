#!/bin/bash
# Script that takes in a URL, sends a request to that URL, and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"