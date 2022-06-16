#!/usr/bin/python3
"""
Script returns information about TODO list for all users
also exporting data in the json format
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    try:
        api_url = 'https://jsonplaceholder.typicode.com'

        users = requests.get(
            '{}/users'.format(api_url))

        json_all = {}
        for user in users.json():
            user_id = user.get('id')
            name = user.get('username')

            todos = requests.get(
                '{}/todos?userId={}'.format(api_url, user_id))

            task_list = []
            for i in todos.json():
                task_list.append({
                        'username': name,
                        'completed': i.get('completed'),
                        'task': i.get('title')})
            json_all["{}".format(user_id)] = task_list
        with open('todo_all_employees.json', mode='w') as f:
            json.dump(json_all, f)
    except:
        pass
