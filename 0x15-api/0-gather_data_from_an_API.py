#!/usr/bin/python3
""" for a given employee ID, returns information about
his/her TODO list progress."""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    employee = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?userId={}'.format(user_id)).json()
    todos_comp = requests.get(
        url + 'todos?userId={}&completed=true'.format(user_id)).json()
    print('Employee {} is done with tasks({}/{}):'.format(
        employee.get('name'), len(todos_comp), len(todos)))
    for todo in todos_comp:
        print('\t ' + todo.get('title'))
