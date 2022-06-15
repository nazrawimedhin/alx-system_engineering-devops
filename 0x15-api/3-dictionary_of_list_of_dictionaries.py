#!/usr/bin/python3
""" Records all tasks owned by all employee to JSON file."""
import json

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    employees = requests.get(url + 'users/').json()
    res = {}
    for emp in employees:
        user_id = emp.get('id')
        todos = requests.get(url + 'todos?userId={}'.format(user_id)).json()
        res[user_id] = []
        for todo in todos:
            row = {'username': emp.get('username'), 'task': todo.get('title'),
                   'completed': todo.get('completed')}
            res[user_id].append(row)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(res, file)
