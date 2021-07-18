"""
This code was writen to put into practice some basics of python such the print function,
function definition, recursive functions, if, else and elif decision statements, while loop
and .isnumeric() functions
"""


print( "Hello there!\nWelcome to GUESSIANO!")
print("lets see how lucky you are, guess a number and we will tell you if you made the right guess!")
correct_answer = 29
def number_recurse():
    number = input("Your_guess: ")
    if number.isnumeric():
        i = 1
        while i != 3 and int(number) != correct_answer:
            print("Incorrect, guess again!")
            number = input("Your_guess: ")
            i += 1
        if i == 3 and int(number) != correct_answer:
            print("Oops, You guessed wrongly, the correct guess is ", correct_answer )
            print("Better luck next time!")
        elif i < 3 and int(number) == correct_answer:
            print("You guessed right this time!, the correct guess is indeed ", number)
        elif i == 3 and int(number) == correct_answer:
            print("Correct! You finally guessed right!, The number is indeed ", number)
        else:
            print("Wawoo!\ncorrect! You guessed right!, The number is indeed ", number)
    else:
        print("Please type in a number! ")
        number_recurse()
number_recurse()
