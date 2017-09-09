#!/bin/python
import sys

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]

    array_line = [0]*n

    for a0 in xrange(m):
        a, b, k = raw_input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]

        try:
            array_line[a-1] += k
            array_line[b] -= k
        except:
            pass
    value = 0
    max_value = 0
    for num in array_line:
        value += num
        max_value = max(value,max_value)

    print max_value
