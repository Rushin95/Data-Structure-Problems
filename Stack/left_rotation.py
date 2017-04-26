m, n = map(int,raw_input().split(' '))
li = raw_input().split(' ')

print ' '.join(li[n:]+li[:n])

'''
Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
'''