#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit
    Args:
        subreddit(str): subreddit name
    """
    headers = {"User-Agent": "alx_advanced_api"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params,
        allow_redirects=False
    )
    if response.status_code == 404:
        print("None")
        return
    res = response.json().get("data")
    for child in res.get("children"):
        print(child.get("data").get("title"))
