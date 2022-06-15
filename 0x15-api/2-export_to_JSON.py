#!/usr/bin/python3
#!/usr/bin/python3
""" Records all tasks owned by employee to JSON file."""
import json
from sys import argv

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    employee = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?userId={}'.format(user_id)).json()
    res = {}
    res[user_id] = []
    for todo in todos:
        row = {'task': todo.get('title'), 'completed': todo.get('completed'),
               'username': employee.get('username')}
        res[user_id].append(row)
    with open(user_id + '.json', 'w') as file:
        json.dump(res, file)
