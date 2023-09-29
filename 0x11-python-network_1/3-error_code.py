#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code:", err.status)
