from pythonds.basic.stack import Stack

no_Of_plates, iterations = map(int,raw_input().split())
plates = map(int,raw_input().split())

A = Stack()
A1 = Stack()
temp = Stack()
B = Stack()

for number in plates:
    A.push(number)

for i in range(1,iterations):
    

