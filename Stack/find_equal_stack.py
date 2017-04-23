#!/bin/python

import sys

n1, n2, n3 = raw_input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = map(int, raw_input().strip().split(' '))
h2 = map(int, raw_input().strip().split(' '))
h3 = map(int, raw_input().strip().split(' '))

x = 0
while x == 0:
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    if (sum1 == sum2 and sum2 == sum3):
        answer = sum(h1)
        x = 1
        break
    elif sum1 == 0 or sum2 == 0 or sum3 == 0:
        answer = 0
        x = 1
        break
    maximum = max(sum1, sum2, sum3)
    if sum1 == maximum:
        h1.pop(0)
    elif sum2 == maximum:
        h2.pop(0)
    elif sum3 == maximum:
        h3.pop(0)

print answer




