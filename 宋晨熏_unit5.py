# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:25:52 2020

@author: SUNGD1
"""
import turtle

turtle.shape("turtle")
turtle.penup()
size = 20
for i in range(30):
    turtle.stamp()
    size = size + 3
    turtle.forward(size)
    turtle.right(24)    
turtle.done()




