##INTRODUCTION

#Say "Hello,World!"
print("Hello, World!")

#Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    else:
        if n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input()) 
    print(a+b)
    print(a-b)
    print(a*b) 

#Division
if __name__ == '__main__':
    a = int(input())
    b = int(input()) 
    print(a//b)
    print(a/b) 
#Loops 
if __name__ == '__main__':
    n = int(input()) 
    for i in range (0,n):
        print(i**2)

#Write a function 
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True 
    else:
        leap=False 
    return leap
year = int(input())
print(is_leap(year))

#Print function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
    


#DATA TYPES

#List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input()) 
lista=[[i,j,k]
      for i in range(x+1)
      for j in range(y+1)
      for k in range(z+1)
      if i+j+k!=n]
print(lista) 
#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    print(sorted(set(arr))[-2]) 
#
    


#SETS
def average(array):
    numbers=set(array)
    mean=sum(numbers)/len(numbers)
    return f"{mean:.3f}"
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#COLLECTIONS
from collections import Counter

if __name__ == "__main__":
   
    num_shoes = int(input())

    shoe_sizes = list(map(int, input().split()))
    inventory = Counter(shoe_sizes)

    
    num_customers = int(input())

    total_earned = 0

   
    for _ in range(num_customers):
        size, price = map(int, input().split())

        
        if inventory[size] > 0:
            total_earned += price  
            inventory[size] -= 1

#DATA AND TIME
import calendar
month, day, year = map(int, input().split())
day_number = calendar.weekday(year, month, day)
print(calendar.day_name[day_number].upper())

#EXCEPTIONS
t = int(input())
for _ in range(t):
    try:
        a, b = input().split()
        print(int(a) // int(b))
        
    except ZeroDivisionError as e:
        print("Error Code:", e)
        
    except ValueError as e:
        print("Error Code:", e) 

#FUNCTIONALS
cube = lambda x: x**3
def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        numbers=[0,1]
        for i in range(2,n):
            numbers.append(numbers[i-1]+numbers[i-2])
    return numbers
    
    
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#XML
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    current_attr=len(node.attrib)
    child_attr=sum(get_attr_number(child)for child in node)
    return current_attr+child_attr
    

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#NUMPY
import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#PROBLEM 2 

#BIRTHDAY CAKE CANDLES
def birthdayCakeCandles(candles):
    maximum_size=max(candles)
    count=0
    for i in candles:
        if i==maximum_size:
            count+=1
    return count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
