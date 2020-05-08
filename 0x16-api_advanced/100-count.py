#!/usr/bin/python3
""" comparations with API request title """
import requests


def count_words(subreddit, word_list, hot_list=[], after='', values=[]):
    """ Request with recursion and compare the response """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
        subreddit, after)
    data = {'user-agent': 'scraping_rec-0-0-3'}
    if len(hot_list) == 0:
        for x in range(0, len(word_list)):
            values.append(0)
    try:
        res = requests.get(url, headers=data,
                           allow_redirects=False).json()
        query = res.get('data').get('children')
        after = res.get('data').get('after')
        for child in query:
            data = child.get('data').get('title')
            for x in range(0, len(word_list)):
                if word_list[x].lower() in data.lower():
                    values[x] += 1
            hot_list.append(data)
        if after is None:
            for x in range(0, len(word_list)):
                if values[x] > 0:
                    print("{}: {}".format(word_list[x], values[x]))
            return(hot_list)
        return(count_words(subreddit, word_list,  hot_list, after, values))
    except:
        return(None)
