#!/usr/bin/python3
""" Advaced request to reddit API"""
import requests


def top_ten(subreddit):
    """ The top ten of the hostpost """
    url = 'https://www.reddit.com/subreddits/search.json'
    par = {'q': subreddit, 'sort': 'relevance', 'limit': 10}
    data = {'user-agent': 'scraping-0.0.2'}
    try:
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
    except:
        print(None)
