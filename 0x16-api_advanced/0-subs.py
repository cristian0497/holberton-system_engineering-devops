#!/usr/bin/python3
""" API advanced request """
import requests


def number_of_subscribers(subreddit):
    """ A resquest to API by subreddit """
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = {'user-agent': 'Scrap/0.0.1'}
    try:
        res = requests.get(base_url, headers=data,
                           allow_redirects=False).json():
        return(int(res.get('data').get('subscribers')))
    except:
        return 0
