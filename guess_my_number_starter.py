# This program checks if a user's guess of a number matches that guessed by the computer

import random
# his import the random module and has to do with random number generation.


def greet():
    print("Hey there!")
    print("Welcome to the world of guess masters!")
    print("I am thinking a number between 1 and 99")


"""are statements that welcome the user to the program and tells the user the range of numbers the computer is thinking 
about.These statements are under the function "greet"."""
greet()
# The function is then called .This displays the greetings("greet") to the user.
while True:
    """while true creates an infinite loop for the following expression or code. it ensures the question to the user to
    guess is being asked over and over again if the condition is not met"""
    N = input("Enter a guess")
    # asks the user to guess the number the computer is thinking about.
    x = int(N)
    """changes the input of the user to an integer.Since the input of the user will be a str to  the computer,
This has to be done so the computer recognizes the input of the user since the computer generates random numbers which 
are integers."""
    R = random.randint(1, 99)
    # This code tells the computer to give out random numbers between 1 and 99. It is assigned a variable name, R.
    if x > R:
        print("your guess is too high,try again")
    # conditional statement that if x(int(N)is greater than R,the user should be informed that his/her guess is too high
    elif x < R:
        print("oops, your guess is too low,try again")
    # condition that if x is not greater than R(IF statement) but rather less than R,
    # the user should be informed that his/her guess is too low.
    elif x == R:
        print("Congrats!That was the number")
# condition that if the 1st and 2nd is not met but x is rather equal to R,the user be informed that the guess was right.
        break
# The while loop repeats the statement and ask the user to guess again if his or her guess was wrong.
# The "Break" function however stops the repetition of the question when the user guesses the number right.
