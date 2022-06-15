#!/usr/bin/python3
""" Records all tasks owned by employee."""
import csv
from sys import argv

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    employee = requests.get(url + 'users/{}'.format(user_id)).json()
    todos = requests.get(url + 'todos?userId={}'.format(user_id)).json()

    with open(user_id + '.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            row = [employee.get('id'), employee.get('username'),
                   todo.get('completed'), todo.get('title')]
            csv_writer.writerow(row)
