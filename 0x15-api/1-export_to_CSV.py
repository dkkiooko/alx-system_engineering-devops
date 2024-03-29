#!/usr/bin/python3
""" gathers data from an API
and exports to CSV
"""
import csv
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
    with open(f'{user_id}.csv', 'w') as file:
        dw = csv.writer(file, delimiter=',')
        for e in all_tasks:
            dw.writerow([user_id] + [name] + [e['completed']] + [e['title']])


if __name__ == '__main__':
    """ run the main function """
    main()
