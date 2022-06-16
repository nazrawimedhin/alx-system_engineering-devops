#!/usr/bin/python3
"""Module that returns information
    about his/her todo list progress.
    """

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + argv[1]).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    cp_tasks = []
    for tasks in todos:
        if tasks["completed"] is True:
            cp_tasks.append(tasks["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(cp_tasks), len(todos)))
    for task in cp_tasks:
        print("\t {}".format(task))
