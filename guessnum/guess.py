#-*- conding:utf8 -*-

# This is a guess the number game.
import random

guessesToken = 0

print('Hello! What is your name?')
myName = input()
number = random.randint(1, 20)
#print('Well,' + myName + ',I am thinking of a number between 1 and 20.')
print('Well,%s,I am thinking of a number between 1 and 20.' % myName)
print('Well,{}, I am thinking of a number between 1 and 20.'.format( myName))

while guessesToken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesToken = guessesToken + 1

    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    guessesToken = str(guessesToken)
    print('Good Job,' + myName +"! You guessed my number in " + guessesToken + ' guesses!')
else:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)