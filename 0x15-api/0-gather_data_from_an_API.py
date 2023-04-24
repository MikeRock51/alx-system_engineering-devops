#!/usr/bin/python3
"""
Returns information about a user's TODO list progress
using a REST API
"""

import requests
from sys import argv


if __name__ == '__main__':
    employeeId = argv[1]
    # Fetch user data
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(
            employeeId)).json()
    # Fetch TODO data
    userTasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            employeeId)).json()
    # Extract completed tasks
    completedTasks = [task.get('title')
                      for task in userTasks if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
          len(completedTasks), len(userTasks)))
    for task in completedTasks:
        print("\t {}".format(task))
