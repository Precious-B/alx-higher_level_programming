#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.

Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    repo, owner = sys.argv[1], sys.argv[2]
    hdr = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url, headers=hdr)
    [print("{}: {}".format(cmit["sha"], cmit["commit"]["author"]["name"]))
        for cmit in r.json()[0:10]]
