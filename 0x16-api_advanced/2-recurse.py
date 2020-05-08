#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after='', cont=0):
    """recursive with request to the API """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    data = {'user-agent': 'scraping_rec-0-0-3'}
    try:
        res = requests.get(url, headers=data,
                           allow_redirects=False).json()
        query = res.get('data').get('children')
        after = res.get('data').get('after')
        for child in query:
            data = child.get('data').get('title')
            hot_list.append(data)
            cont += 1
        if after is None:
            return(hot_list)
        return(recurse(subreddit, hot_list, after, cont))

    except:
        return(None)
