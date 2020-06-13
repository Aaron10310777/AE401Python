# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:54:56 2020

@author: SUNGD1
"""
total=0
math=[]
lowest = 100

n = input('people?')
n = int(n)

for i in range(n):
    name = input("please input the name: ")
    
    score = input("input score:")
    score = int(score)

    oneperson = list()
    oneperson.append(name)
    oneperson.append(score)
    math.append(oneperson)
    
print(math)
for i in math:
    total = total+i[1]
    average = total / n
    print("the average is",average)

high=0
person=""
for i in math:
    if i[1]>high:
        high=i[1]
        person=i[0]
        
low=100
person=""
for i in math:
    if i[1]<low:
     low=i[1]
     person=i[0]




print("average:",average)
print("highest:",high)
print("lowest:",low)




