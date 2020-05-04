#!/usr/bin/python3
""" JSON Plcae Holder request """
import csv
import json
import urllib.request
import sys


def main():
    """ Main method to does a request and return a JSON file """
    users_url = "https://jsonplaceholder.typicode.com/users/"
    with urllib.request.urlopen(users_url) as Users:
        users = Users.read().decode('utf-8')
        users_dic = json.loads(users)
    users_url = "https://jsonplaceholder.typicode.com/todos/"
    with urllib.request.urlopen(users_url) as ToDos:
        list_task = []
        todos = ToDos.read().decode('utf-8')
        todos_dic = json.loads(todos)
    name = "todo_all_employees.json"
    return_dic = {}
    with open(name, 'w') as file_json:
        for user_dic in users_dic:
            new_list = []
            for item in todos_dic:
                new_dic = {}
                if item.get('userId') == user_dic.get('id'):
                    new_dic['username'] = user_dic.get('username')
                    new_dic['task'] = item.get('title')
                    new_dic['complete'] = item.get('completed')
                    new_list.append(new_dic)
            return_dic[user_dic.get('id')] = new_list
        json.dump(return_dic, file_json)

if __name__ == "__main__":
    main()
