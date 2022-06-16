#!/usr/bin/python3
"""
Script returns information about TODO list for a given employee
also exporting data in the CSV format
"""
import csv
import requests
import sys


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        api_url = 'https://jsonplaceholder.typicode.com'
        users = requests.get(
            '{}/users/{}'.format(api_url, employee_id))
        name = users.json().get('username')
        todos = requests.get(
            '{}/todos?userId={}'.format(api_url, employee_id))
        with open('{}.csv'.format(employee_id), mode='w') as f:
            fieldnames = ['id', 'username', 'completed', 'title']
            writer = csv.DictWriter(
                f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
            for i in todos.json():
                writer.writerow({
                        'id': employee_id,
                        'username': name,
                        'completed': i.get('completed'),
                        'title': i.get('title')})
    except:
        pass
