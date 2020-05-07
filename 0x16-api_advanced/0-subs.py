#!/usr/bin/python3
""" API advanced request """
import requests


def number_of_subscribers(subreddit):
    """ A resquest to API by subreddit """
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    data = {'user-agent': 'Scrap/0.0.1'}
    res = requests.get(base_url, headers=data,
                       allow_redirects=False)
    if res.status_code >= 400:
        return 0
    else:
        return(int(res.json().get('data').get('subscribers')))

