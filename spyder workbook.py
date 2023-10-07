# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# def greet_with(name, location):
#     print(f"Hello {name} from {location}")
#     print("Welcome home")

# greet_with(location="Jojo", name="Maryland")
import math

# test_height = float(input("What is the height of the room? "))
# test_breath = float(input("What is the breath of the room? "))
# paint_coverage =5

# def paint_calc (height, breath, coverage):
#     calc = math.ceil(height*breath/coverage)
#     print(f"You will need {calc} buckets of paint")

# paint_calc(coverage=paint_coverage,breath=test_breath,height=test_height)

n = int(input("Enter a number to check\n"))


def prime_checker(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("This is a prime number")
    else:
        print("Not a prime number")
        
        
prime_checker(num =n)       
        
        
        
        
        
        
        
        