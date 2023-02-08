#!/usr/bin/python3
"""gathers data from an API"""
import requests
from sys import argv


user_id = argv[1]
url = 'https://jsonplaceholder.typicode.com/'


def main():
    """ main function that prints output """
    r = requests.get('{}users/{}'.format(url, user_id))
    name = r.json()['name']
    r2 = requests.get('{}todos?userId={}'.format(url, user_id)).json()
    all_tasks = [i for i in r2[:]]
    completed_tasks = [i['title'] for i in r2[:] if i['completed'] is True]
    no_all = len(all_tasks)
    no_com = len(completed_tasks)
    print("Employee {} is node with tasks({}/{})".format(name, no_com, no_all))
    for element in completed_tasks:
        print('\t {}'.format(element))


if __name__ == '__main__':
    """ run the main function """
    main()
