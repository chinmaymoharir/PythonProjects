#This is a guess the number game.
from random import*
print('Hello. What is your name?')
name = input()

print('Well, ' + name + 'I am thining of a number between 1 and 20')
secretnumber = randint(1,20)
count = 1

for count in range(1,6):
    print('Take a guess')
    number = int(input())
    if number == secretnumber:
        print('You guessed right and took ' + str(count) + '  guesses')
        break
        
    else:
        if number > secretnumber:
            print('Your number is high')
            print('you guessed wrong ' + str(number) + ' Please try again')
            
            count = count + 1
            
        elif number <  secretnumber:
            print('Your number is low')
            print('you guessed wrong ' + str(number) + ' Please try again')
            
            count = count + 1
