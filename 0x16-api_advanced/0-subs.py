#!/usr/bin/python3
"""Queries the reddit API"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(argv[1])

    if not argv[1]:
        return 0

    headers = {
            "User-Agent": "python3 3.10"
            }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get('data').get('subscribers')
