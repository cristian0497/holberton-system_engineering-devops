#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = {'user-agent': 'Scrap/0.0.1'}
    res = requests.get(base_url, headers=data, allow_redirects=False).json()
    if res.get('error') == 404:
        return 0
    else:
        return(res.get('data').get('subscribers'))
