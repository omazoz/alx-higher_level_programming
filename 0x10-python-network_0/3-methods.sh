#!/bin/bash
# Script that takes in a URL it sends a DELETE request to that URL, and displays the body of the response
curl -sX DELETE "$1"