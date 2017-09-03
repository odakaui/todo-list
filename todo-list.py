#!/usr/local/bin/python

while (1):
    todo = input("Add Todo: ")

    if (todo == 'exit'):
        break
    elif (todo == 'ls'):
        f = open('list.txt', 'r')
        for line in f:
            print(line, end = '')
        f.close()
    else:
        f = open('list.txt', 'a')
        f.write(todo + "\n")
        print(todo)
        f.close()

print('Bye')
