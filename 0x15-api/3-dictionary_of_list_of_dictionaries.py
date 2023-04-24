#!/usr/bin/python3
"""
Fetches information about all user's TODO list progress
using a REST APIi and export it in JSON format
"""

import json
import requests


if __name__ == '__main__':
    usersObject = {}
    for employeeId in range(1, 11):
        # Fetch user data
        user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/'.format(
                employeeId)).json()
        # Fetch TODO data
        userTasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                employeeId)).json()

        usersObject['{}'.format(user.get('id'))] = [
            {"username": user.get('username'), "task": task.get('title'),
             "completed": task.get('completed')} for task in userTasks]

    with open('todo_all_employees.json', 'w') as jFile:
        json.dump(usersObject, jFile)
