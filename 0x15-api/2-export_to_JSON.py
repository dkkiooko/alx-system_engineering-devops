#!/usr/bin/python3
""" gathers data from an API
and exports to JSON
"""
import json
import requests
from sys import argv


user_id = argv[1]
url = 'https://jsonplaceholder.typicode.com/'


def main():
    """ main function that creates csv
    returns nothing
    """

    r = requests.get('{}users/{}'.format(url, user_id))
    name = r.json()['username']
    r2 = requests.get('{}todos?userId={}'.format(url, user_id)).json()
    all_tasks = [i for i in r2[:]]
    all_dicts = []
    for i in all_tasks:
        temp = {}
        temp['task'] = i['title']
        temp['completed'] = i['completed']
        temp['username'] = name
        all_dicts.append(temp)
    dictionary = {str(user_id): all_dicts}
    with open(f'{user_id}.json', 'w') as file:
        dw = json.dump(dictionary, file)


if __name__ == "__main__":
    main()
