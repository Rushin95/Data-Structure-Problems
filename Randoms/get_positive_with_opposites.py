'''
A numeric array of length N is given. We need to design a function
 that finds all positive numbers in the array that have their opposites in
 it as well.
'''

a = [1,2,3,4,-1,-4,-5,-1,-1]

def Solution(a):
  s = set()
  for number in set(a):
    if -number in s:
      print abs(number)
    else:
      s.add(number)

Solution(a)
