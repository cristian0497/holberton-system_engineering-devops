#!/usr/bin/python3
""" Advaced request to reddit API"""
import requests


def top_ten(subreddit):
    """ The top ten of the hostpost """
    base_url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    url = 'https://www.reddit.com/subreddits/search.json'
    par = {'q': subreddit, 'sort': 'relevance', 'limit': 10}
    data = {'user-agent': 'scraping-0.0.2'}
    res = requests.get(url, headers=data, params=par,
                       allow_redirects=False).json()
    query = res.get('data').get('children')
    result = []
    for child in query:
        data = child.get('data')
        result.append(data.get('title'))
    if len(result) != 0:
        for val in result:
            print(val)
    else:
        print(None)
