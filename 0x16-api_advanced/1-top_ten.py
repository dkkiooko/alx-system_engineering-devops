#!/usr/bin/python3
"""top ten posts
"""
import requests


def top_ten(subreddit):
    """_prints titles of fiest 10 hot posts for a reddit_

    Args:
        subreddit (_str_): _a subreddit_
    """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    if subreddit is None or type(subreddit) is not str:
        print('None')
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        for a in list_titles[:10]:
            print(a['data']['title'])
    else:
        return(print('None'))
