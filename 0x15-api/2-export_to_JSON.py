#!/usr/bin/python3
""" JSON Plcae Holder request """
import csv
import json
import sys
import urllib.request


def main():
    """ Main method to does a request and return a JSON file """
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])
    with urllib.request.urlopen(users_url) as Users:
        users = Users.read().decode('utf-8')
        users_dic = json.loads(users)
    users_url = "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
        sys.argv[1])
    with urllib.request.urlopen(users_url) as ToDos:
        list_task = []
        todos = ToDos.read().decode('utf-8')
        todos_dic = json.loads(todos)
    name = "{}.json".format(sys.argv[1])
    with open(name, 'w') as file_json:
        return_value = {}
        ret = []
        for task in todos_dic:
            tmp = {}
            tmp['task'] = task.get('title')
            tmp['completed'] = task.get('completed')
            tmp['username'] = users_dic.get('username')
            ret.append(tmp)
        return_value[sys.argv[1]] = ret
        json.dump(return_value, file_json)

if __name__ == "__main__":
    main()
