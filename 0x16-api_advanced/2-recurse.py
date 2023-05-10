#!/usr/bin/python3
"""Makes a recursive call to the Reddit API"""

import requests


def recurse(subreddit, params={}, hot_list=[]):
    """
        Returns a list of all titles of hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Python3 3.10"}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    datas = response.json().get('data').get('children')
    for data in datas:
        hot_list.append(data.get('data').get('title'))

    nextPage = response.json().get('data').get('after')
    if nextPage:
        params["after"] = nextPage
        recurse(subreddit, params, hot_list)

    return hot_list
