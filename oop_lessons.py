# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:54:32 2023

@author: a127014
"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("arrow")
timmy.color("coral")

my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()