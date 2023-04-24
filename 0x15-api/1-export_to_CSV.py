#!/usr/bin/python3
"""
Fetches information about a user's TODO list progress using
a REST API and exports data into CSV format
"""

import csv
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

    with open('{}.csv'.format(employeeId), 'w') as csvfile:
        writer = csv.writer(csvfile)
        for task in userTasks:
            writer.writerow([user.get('id'), user.get('username'),
                            task.get('completed'), task.get('title')])
