#!/usr/bin/python3
"""
Script returns information about TODO list for a given employee
"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
        api_url = 'https://jsonplaceholder.typicode.com'
        users = requests.get(
            '{}/users/{}'.format(api_url, employee_id))
        name = users.json()['name']
        todos = requests.get(
            '{}/todos?userId={}'.format(api_url, employee_id))
        total_tasks = len(todos.json())
        done_tasks = 0
        done_titles = ""
        for i in todos.json():
            if i['completed'] is True:
                done_tasks += 1
                done_titles += "\n\t {}".format(i['title'])
        print('Employee {} is done with tasks({}/{}):{}'.format(
            name, done_tasks, total_tasks, done_titles))
    except:
        pass
