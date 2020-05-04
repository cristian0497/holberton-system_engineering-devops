#!/usr/bin/python3
""" JSON Plcae Holder request """
import csv
import json
import sys
import urllib.request


def main():
    """ Export request to CSV file """
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

    name = "{}.csv".format(sys.argv[1])
    with open(name, 'w', newline='') as file_csv:
        return_value = []
        writer = csv.writer(file_csv, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in todos_dic:
            ret = []
            ret.append(str(users_dic.get('id')))
            ret.append(users_dic.get('username'))
            ret.append(str(task.get('completed')))
            ret.append(task.get('title'))
            return_value.append(ret)
            writer.writerow(ret)

if __name__ == "__main__":
    main()
