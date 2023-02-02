#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """returns a list comtaining the titles of
     all hot articles for a given subreddit.

    Args:
        subreddit(str): subreddit name
        hot_list(list): list hot articles titles
        after(str):
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Alx_Advanced API"
    }
    params = {
        "after": after,
        "limit": 100
    }
    res = requests.get(
        url, headers=headers,
        params=params, allow_redirects=False
    )
    if res.status_code == 404:
        return None
    results = res.json().get("data")
    after = results.get("after")
    for post in results.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
