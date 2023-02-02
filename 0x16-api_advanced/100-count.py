#!/usr/bin/python3
"""
Queries the Reddit API, parses the title of all hot articles
and prints a sorted count of given keywords (case-insensitive,
delimited by space).
"""
import requests


def count_words(subreddit, word_list, after="", count={}):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "alx-advanced_api"
    }
    params = {
        "limit": 10,
        "after": after
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return count
    data = response.json()

    articles = data["data"]["children"]
    for article in articles:
        title = article["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                if word.lower() in count:
                    count[word.lower()] += 1
                else:
                    count[word.lower()] = 1

    after = data["data"]["after"]
    if after is None:
        return count
    return count_words(subreddit, word_list, after, count)
