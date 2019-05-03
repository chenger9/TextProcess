# -*- coding:utf-8 -*-

f = open('1.txt')
g = open('实验001.txt', 'w')

try:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if line.count('\n') == len(line):
            continue
        g.write(line)
finally:
    f.close()
    g.close()