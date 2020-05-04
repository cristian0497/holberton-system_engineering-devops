#!/usr/bin/python3
""" JSON Plcae Holder request """
import json
import urllib.request
import sys


def main():
    """ A Simple request to Place Holder """
    users_url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        sys.argv[1])
    with urllib.request.urlopen(users_url) as ToDos:
        done_task = 0
        list_task = []
        todos = ToDos.read().decode('utf-8')
        todos_dic = json.loads(todos)
        for task in todos_dic:
            if task.get('completed') is True:
                done_task += 1
                list_task.append(task.get('title'))

    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    with urllib.request.urlopen(users_url) as Users:
        users = Users.read().decode('utf-8')
        users_dic = json.loads(users)

    user_name = users_dic.get('name')
    all_task = len(todos_dic)
    print('Employee {} is done with task({}/{}):'.format
          (user_name, done_task, all_task))
    for task in list_task:
        print("\t{}".format(task))

if __name__ == "__main__":
    main()
