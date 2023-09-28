#!/bin/bash
# Script that takes in a URL, sends a POST request to that URL then it displays the body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"