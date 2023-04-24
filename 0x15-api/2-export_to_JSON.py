#!/usr/bin/python3
"""
Fetches information about a user's TODO list progress
using a REST APIi and export it in JSON format
"""

import json
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

    userObject = {
            '{}'.format(user.get('id')): [
                {"task": task.get('title'), "completed": task.get('completed'),
                    "username": user.get('username')} for task in userTasks]
            }

    with open('{}.json'.format(employeeId), 'w') as jFile:
        json.dump(userObject, jFile)
