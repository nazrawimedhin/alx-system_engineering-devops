#!/usr/bin/python3
"""
Script returns information about TODO list for a given user
also exporting data in the json format
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    try:
        user_id = int(sys.argv[1])
        api_url = 'https://jsonplaceholder.typicode.com'

        users = requests.get(
            '{}/users/{}'.format(api_url, user_id))

        name = users.json().get('username')

        todos = requests.get(
            '{}/todos?userId={}'.format(api_url, user_id))

        task_list = []
        for i in todos.json():
            task_list.append({
                    'username': name,
                    'completed': i.get('completed'),
                    'task': i.get('title')})
        json_tasks = {"{}".format(user_id): task_list}
        with open('{}.json'.format(user_id), mode='w') as f:
            json.dump(json_tasks, f)
    except:
        pass
