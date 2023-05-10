#!/usr/bin/python3
"""Makes a request to the reddit api"""

import requests
from sys import argv


def top_ten(subreddit):
    """
        Prints the title of the top 10 hot posts
        listed on a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(argv[1])
    params = {"limit": 10}
    headers = {"User-Agent": "Python3 3.10"}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    datas = response.json().get('data').get('children')
    for data in datas:
        print(data.get('data').get('title'))
