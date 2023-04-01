#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:45:39 2023

@author: yilingwu
"""

# PPHA 30537
# Spring 2023
# Homework 1

# Jennifer Qin
# jenniferqinnn7

# Due date: Sunday April 2nd before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

list1 = [1,2,3,4]
for i in range(len(list1)):
    print('The value at position', i, 'is', list1[i])

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

test = ['radar','A man, a plan, a canal, Panama!','Apple']

#isalnum citation: https://www.w3schools.com/python/ref_string_isalnum.asp

for phrase in test:
    phrase_new = ''.join(i for i in phrase.lower() if i.isalnum())
    if phrase_new == phrase_new[::-1]:
        print('{} is a palindrome'.format(phrase))
    else:
        print("{} isn't a palindrome".format(phrase))


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']

while True: 
    choice = input('Please pick a vegetable I have available: ')
    
    if choice in available_vegetables:
        print('You can have the vegetable.')
        break
    else: 
        print('You made an invalid choice; please pick again') 

# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

start_list4 = ['Comprehensive','ABC','abc','bob','Lucy','Bike']
new_list4 = [i.lower() for i in start_list4 if i[0] == 'a' or i[0] == 'b']
print(new_list4)

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]

start_list = [3, 5, 7, 9, 11, 13]
newList = [2*i for i in start_list[::-1]]
print(newList)

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

new_dict = {short_names[i]: long_names[i] for i in range(len(short_names))}
print(new_dict)