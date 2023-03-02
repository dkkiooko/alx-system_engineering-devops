#!/usr/bin/python3
"""recursive problem
"""
import requests


def recurse(subreddit, host_list=[], after="null"):
    """Read reddit API and return top 10 hostspots """
    headers = {'User-Agent': 'MyBot/0.0.1'}
    payload = {"limit": "100", "after": after}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False, params=payload)
    if r.status_code == 200:
        list_titles = r.json()['data']['children']
        after = r.json()['data']['children']
        if after is not None:
            host_list.append(list_titles[len(host_list)]['data']['title'])
            recurse(subreddit, host_list, after)
        else:
            return(host_list)
    else:
        return(None)
