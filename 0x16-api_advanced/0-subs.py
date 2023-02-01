#!/usr/bin/python3
"""
Quries the Reddit API and return the number of
subscribers for a given subreddit
"""
import requests


def number_of_subsribers(subreddit):
    """returns the total number of subscrubbers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "alx-advanced api"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get('data')
    return results.get('subscribers')
