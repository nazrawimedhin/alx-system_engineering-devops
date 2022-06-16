#!/usr/bin/python3
"""Python script to export data in the CSV format"""

import csv
import requests
import sys


if __name__ == "__main__":

    if sys.argv[1].isdigit():
        # user id
        user_id = sys.argv[1]

        # URLS to get data
        employee = requests.get('https://jsonplaceholder.typicode.com/users',
                                params={'id':  user_id}).json()
        tasks_todo = requests.get('https://jsonplaceholder.typicode.com/todos',
                                  params={'userId':  user_id}).json()
        username = employee[0]['username']

        # Open file
        with open('{}.csv'.format(user_id), 'w', newline='') as open_file:
            file_instance = csv.writer(open_file, quoting=csv.QUOTE_ALL)
            for todo in tasks_todo:
                file_instance.writerow([todo['userId'], username,
                                        todo['completed'], todo['title']])
