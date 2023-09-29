#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import sys
    import requests

    headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {sys.argv[2]}',
            'X-GitHub-Api-Version': '2022-11-28'}
    url = f"https://api.github.com/users/{sys.argv[1]}"
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'id' in data:
        print(data['id'])
    else:
        print(None)
