# Objective:
# By the end of this exercise, learners should be able to determine the fine amount for 
# overdue library books based on the number of days they are overdue. This exercise will
# help learners practice the use of nested if-elif-else statements in Python and
# understand how to implement real-world scenarios using conditional logic

# Problem Statement:
# You are tasked with creating a program for a library to calculate fines for overdue books. 
# The library has the following fine structure:

# $1 per day for books that are up to 5 days overdue. 
# $2 per day for books that are 6 to 10 days overdue. 
# $5 per day for books that are more than 10 days overdue. 

# Write a Python program that:

# 1. Asks the user for the number of days a book is overdue
# 2. Calculates the fine based on the above criteria. 
# 3. Displays the fine amount to the user. 

number_of_days = int(input("How many days is your book overdue? Numerical values only "))

if number_of_days <= 5:
    total_fine = 1 * number_of_days
    print(f"Due to your book being overdue by {number_of_days} day(s), your fine will be {total_fine} USD. ")
elif number_of_days >= 6 and number_of_days <= 10:
    total_fine = 2 * number_of_days
    print(f"Due to your book being overdue by {number_of_days} day(s), your fine will be {total_fine} USD. ")
elif number_of_days > 10:
    total_fine = 5 * number_of_days
    print(f"Due to your book being overdue by {number_of_days} day(s), your fine will be {total_fine} USD. ")