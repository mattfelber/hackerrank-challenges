import sys

import keyboard
import sys


n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    #print(name)
    scores = list(map(float, line))
    #print(scores)
    student_marks[name] = scores
    #print(student_marks[name])


while True:
    try:
        query_name = input()
        marks = student_marks[query_name]
        print(format(sum(marks) / 3, '.2f'))
    except KeyError:
        print("Name not found.")






