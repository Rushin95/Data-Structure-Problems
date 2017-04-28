#!/bin/python
import sys

t = int(raw_input().strip())
opening = ['[', '{', '(']
closing = [']', '}', ')']
for n in xrange(t):
    s = list(raw_input().strip())
    stack = []
    ans = "YES"
    if len(s) % 2 == 1:
        ans = 'NO'
    else:
        for i in range(0, len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing and len(stack) != 0:
                if s[i] == ']':
                    if stack.pop() != '[':
                        ans = 'NO'

                elif s[i] == '}':
                    if stack.pop() != '{':
                        ans = 'NO'

                elif s[i] == ')':
                    if stack.pop() != '(':
                        ans = 'NO'
            else:
                ans = 'NO'
    if len(stack) != 0:
        ans = 'NO'
    print ans




'''
Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}
Sample Output

YES
NO
YES

'''