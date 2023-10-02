#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL
 and displays the value of the X-Request-Id """

import urllib.request as urllib
import sys


if __name__ == "__main__":
    with urllib.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))