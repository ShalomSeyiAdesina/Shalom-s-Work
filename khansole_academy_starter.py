"""Khansole Academy is a program that helps users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the answers of the users.
"""
import random

count1 = 1
while count1 <= 3:
    x = random.randint(10, 99)
    """This while function loops the folowing code repeatedly until the condition is met.Meaning it keeps on asking
the user the addition of two random numbers until the user gets the answer right for 3 simultaneous times."""

# This code tells the computer to produce random numbers between 1 and 99. It is assigned a variable name, x.
    y = random.randint(10, 99)
# This code tells the computer to produce random numbers between 1 and 99. It is assigned a variable name, y.
    R = x + y
# This code tells the computer to add "x and y".It is assigned a variable name, R.
    print("What is", x, "+", y)
# This prints out what is x(random number from x)+y(random number from y)
    A = int(input("Answer:"))
# The int function changes the user"s answer from a string to an integer and displays it out.str and int can't be added
    if A == R:
        print("Correct!.You have gotten", count1, "in a row.")
        count1 += 1
#The 'if' , 'else' provides a conditional statement that the user has gotten the right answer if A(user's answer) is equal to R.
#count1 += 1 is the defined indexing variable, which we set to 1.

    else:
        print("Incorrect. The expected answer is", R)
        count1 = 1
#If not the else condition is there to print that the user's answer is incorrect.
#count1 = 1 here starts the counting number of correct answers the user gets after any incorrect answer even after getting 2 answers in a row.

print("Congratulations! You are now a master of additions")
#This prints the congratulatory message after the user gets 3 answers in a row.
 
