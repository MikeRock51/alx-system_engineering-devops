#!/usr/bin/python3
"""Makes a recursive call to the Reddit API"""

import requests
import re


def count_words(subreddit, word_list, params={}, hot_list={}):
    """
        Prints a sorted count of given keywords for the subreddit titles
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "Python3 3.10"}

    response = requests.get(url, params=params, headers=headers)
    datas = response.json().get('data').get('children')
    for data in datas:
        title = data.get('data').get('title')
        for word in word_list:
            if word in hot_list.keys():
                hot_list[word] = hot_list.get(word) + len(
                    re.findall(r'\b{}\b'.format(
                        word.lower()), title.lower()))
            else:
                hot_list[word] = len(re.findall(r'\b{}\b'.format(
                    word.lower()), title.lower()))

    nextPage = response.json().get('data').get('after')
    if nextPage:
        params["after"] = nextPage
        count_words(subreddit, word_list, params, hot_list)
    else:
        for key, value in sorted(hot_list.items(),
                                 key=lambda x: x[1], reverse=True):
            if value > 0:
                print("{}: {}".format(key, value))
