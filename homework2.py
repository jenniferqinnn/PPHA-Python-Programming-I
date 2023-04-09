# PPHA 30535
# Spring 2023
# Homework 2

# Jennifer Qin
# jenniferqinnn

# Due date: Sunday April 9th before midnight
# Write your answers in the space between the questions, and commit/push only 
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put 
# thought into your work.

#############

# Question 1: Write a function that takes two numbers as arguments, then
# sums them together.  If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small".  Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 4), (0, 0), (-15, -100), (5, 4)]

def question1(a,b):
    total = a+b
    if total >10:
        return "big"
    elif total == 10:
        return "just right"
    elif total < 10:
        return "small"

end_list=[]
for i in start_list:
    first_num = i[0]
    second_num = i[1]
    result = question1(first_num, second_num)
    end_list.append(result)

print(end_list)

# Question 2: The following code is fully-functional, but uses a global
# variable and a local variable.  Re-write it to work the same, but using an
# argument and a local variable.  Use no more than two lines of comments to
# explain why this new way is preferable to the old way.


def my_func(a):
    b = 30
    return a + b
x = my_func(10)

#In the new way, we can assign different values to variable a 
#without changing other pieces of code. 


# Question 3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*).  It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else warn the user 
# and exit.  Your function should also have a keyword argument named 
# "special_chars" that defaults to True.  If the function is called with the 
# keyword argument set to False instead, then the random values chosen should
# not include special characters.  Create a second similar keyword argument 
# for numbers. Use one of the two libraries below.

#citation:
#for generating random strings containing both lowercase and uppercase letters & special letters: 
#https://pynative.com/python-generate-random-string/

#random.choice function: https://www.geeksforgeeks.org/random-choices-method-in-python/
#convert list to string: https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.

import string
import random

  
def password(length, special_chars = True, num_arg = True):
    if length not in range(8,17):
        print('Your length should between 8 and 16, please reselect.')
        return 
    password = string.ascii_letters
    if special_chars:
        password += string.punctuation
    if num_arg:
        password += string.digits
    
    final_password = random.choices(password, k = length)
    final_password = ''.join(final_password)
    return final_password 
         
  
# Question 4: Create a class that requires four arguments when an instance
# is created: one for the person's name, one for which COVID vaccine they
# have had, one for how many doses they've had, and one for whether they've
# ever had COVID.  Then create instances for four people:
#
# Aaron, Moderna, 3, False
# Ashu, Pfizer, 2, False
# Alison, none, 0, True
# Asma, Pfizer, 1, True
#
# Write two methods for this class, and one function:
# The first method named "get_record", which prints out a one-sentence summary
# of a specified person's records (e.g. Ashu has two doses of Phizer and...)
#
# The second method named "same_shot", which takes as an argument another person's
# record instance, and then prints whether or not the two people have the
# same kind of vaccine or not.
#
# A function named "all_data", which takes a container holding any number of these 
# instances and returns a simple list of all of their data 
# (e.g. [name, vaccine, doses, covid], [...])

class Question4():
    def __init__(self,name,vaccine,num_dose,ever_covid):
        self.name = name
        self.vaccine = vaccine
        self.num_dose = num_dose
        self.ever_covid = ever_covid
        
    def get_record(self):
        print(self.name+' has ' + str(self.num_dose) + ' dose of ' + self.vaccine)
    
    def same_shot(self, other):
        if self.vaccine == other.vaccine:
            print(self.name +' and ' + other.name + ' have the same kind of vaccine.')
        else:
            print(self.name +' and ' + other.name + ' have different kind of vaccine.')
    
    def all_data(self):
        list1 = [self.name, self.vaccine,self.num_dose,self.ever_covid]
        return list1
        
Aaron = Question4('Aaron','Moderna',3,False)
Ashu = Question4('Ashu','Pfizer', 2, False)
Alison = Question4('Alison', 'none',0, True)
Asma = Question4('Asma', 'Pfizer', 1, True)
