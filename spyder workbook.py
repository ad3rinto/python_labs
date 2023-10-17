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



"""
Prime Number Checker 

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
        
        
"""
    
# Caesar Cippher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(t,s):
#   direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#   #do nothing.
#   new_text = ""
#   for item in t:
#     if item in alphabet and direction == "encode":
#       item_index = alphabet.index(item)
#       new_text += alphabet[item_index + s]
#     elif item in alphabet and direction == "decode":
#       item_index = alphabet.index(item)
#       new_text += alphabet[item_index - s]
#   print(new_text)  

# encrypt(t = text, s= shift)
 
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 


# Unto deep dive into python dictionaries

# python_lab = {
#     "bug":"Errors in code",
#     "function":"make code do stuff",
#     "list":"Array of objects",
# }

# print(python_lab["bug"])

# python_lab["test"]= "Making sure the code works"

# for (key) in python_lab:
#     print(key)

# <<<<<<< HEAD

# #Functions and Outputs
# def format_name(f_name, l_name):
#     return(f"{f_name} {l_name}").title()
  
# =======

# DAY10 challenge

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False
  
# TODO: Add more code here 👇
# def days_in_month(year_context, month_context):
#     '''Takes input and spits out leap or non leap year'''
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#   if is_leap(year_context) == False:
#     return(month_days[month_context-1])
#   elif is_leap(year_context) == True:
#     if month_context == 2:
#       month_days[1] = 29
#       return (month_days[month_context-1])
#     else:
#       return (month_days[month_context-1])
# #🚨 Do NOT change any of the code below 
# year = int(input()) # Enter a year
# month = int(input()) # Enter a month
# days = days_in_month(year, month)
# print(days)

'''
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(first_num, second_num, operative):
    result = operations[operative](first_num, second_num)
    print(f"{first_num} {operative} {second_num} = {result}")
>>>>>>> 20e36ad817b28eb1df06337b07e8c76c26812ed3

MINE = format_name("ADEnIYi", "ADwrwrO")

<<<<<<< HEAD
print(MINE)
=======
should_continue = True
>>>>>>> 20e36ad817b28eb1df06337b07e8c76c26812ed3
    
while should_continue:
    num1 = int(input("Whats the first number ? "))
    num2 = int(input("Whats the second number ? "))  
    for key in operations:
         print(key)
    operating_sig = input("Select an operation from above: ")    
    calculate(num1,num2, operating_sig)
    continue_calc = input("Do you wish to continue? ").lower()
    if continue_calc == "n":
        should_continue = False
    else:
        should_continue = True

 '''
#CAPSTONE PROJECT 15 OCT 2023
import random

# cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# player_cards = [random.choice(cards),random.choice(cards) ]
# print(f"Your cards: {player_cards}")   
# computer_card1 = random.choice(cards)    
# print(f"Computer's first card: {computer_card1}")      
# get_more_card = input("Do you want to draw another card? 'y' to get another 'n' to pass\n").lower()  

# player_total = 0
# computer_total = 0

# if get_more_card == "n":
#     computer_cards = [computer_card1, random.choice(cards)]

#     for card in player_cards:
#         player_total += card
#     for card in computer_cards:
#         computer_total += card
    
#     print(f"Your final hand :{player_cards}")
#     print(f"Computer's final hand :{computer_cards}")
#     if player_total > computer_total:
#         print("You win")
#     else:
#         print("Computer wins")
# elif get_more_card == "y":
#     computer_cards = [computer_card1, random.choice(cards)]
#     player_cards.append(random.choice(cards))
#     for card in player_cards:
#         player_total += card
    
#         if computer_total < 17:
#             computer_cards.append(random.choice(cards))
#         for card in computer_cards:
#             computer_total += card
#     print(f"Your final hand :{player_cards}")
#     print(f"Computer's final hand :{computer_cards}")
#     # if player_total > computer_total:
#     #     print("You win")
#     # else:
#     #     print("Computer wins")
#     print(computer_total, player_total)    
        
#GUESSING GAME ATTEMPT

computer_number = random.randint(1, 101)
attempts = 0

def game_start():
    global attempts
    print("I am thinking of a number between 1 and 100, Try to guess the number")
    game_difficulty = input("Select h for hard, and e for easy: \n").lower()           
    if game_difficulty == "h":
        attempts = 5 
    elif game_difficulty == "e":
        attempts = 10
    else:
        print("You have selected a non valid option")
    
    
def game_play(attempts):
    while attempts > 1:
        player_option = int(input("Make a guess: "))
        if player_option < computer_number :
           print(f"Too low, try again, number of tries remaing {attempts -1}")
           attempts -=1  
        elif player_option == computer_number:
            
            attempts = 0
            print("You got it right, you win")
        else:
            print(f"Too high, try again, number of tries remaing {attempts -1}")
            attempts -=1
    if attempts == 1: 
        print("You have one last try")
        player_option = int(input("Make a guess: "))
        if player_option == computer_number :
            print("WINNER!!!!")
        else:
            print("YOu lose, Game over")
     
        
    

game_start()
game_play(attempts)
    
        
 

    
   
    