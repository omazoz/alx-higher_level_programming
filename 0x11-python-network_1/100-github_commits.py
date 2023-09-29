#!/usr/bin/python3
""" List 10 commits (from the most recent to oldest) of the repository
"""

if __name__ == "__main__":
    import sys
    import requests

    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    response = requests.get(url, params={'per_page': 10})
    for item in response.json():
        print(f"{item['sha']}: {item['commit']['author']['name']}")
