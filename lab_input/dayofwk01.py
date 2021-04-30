#!/usr/bin/env python3

# Get users name as an input from the user
user_name = input("Please enter your name: ")

# Get the day of week from the user
day_of_week = input("What day of week is it? ")

## print() can be given a series of objects separated by a comma
print("Hello " + user_name + "! Happy ", day_of_week , "!", sep='')

