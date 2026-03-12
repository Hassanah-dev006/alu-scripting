#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """Query Reddit API and print top 10 hot post titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True)

    if response.status_code == 200 and 'search' not in response.url:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts for a given subreddit"""

import requests


def top_ten(subreddit):
    """Query Reddit API and print top 10 hot post titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=True)

    if response.status_code == 200 and 'search' not in response.url:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
