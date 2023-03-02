#!/usr/bin/python3
"""how many subs
"""
import requests


def number_of_subscribers(subreddit):
    """queries Reddit API and returns number of subscribers
    for a given subreddit

    Args:
        subreddit (_str_): _subreddit to be matched_

    Returns:
        (_int_): number of subscribers
    """
    # username =
    # password =
    # user_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    headers = {'User-Agent': 'MyBot/0.0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return 0
