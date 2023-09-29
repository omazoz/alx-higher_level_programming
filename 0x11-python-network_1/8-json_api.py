#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) > 1:
        parameter = {'q': sys.argv[1]}
    else:
        parameter = {'q': ""}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, parameter)
    if 'application/json' == response.headers.get("Content-Type"):
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
