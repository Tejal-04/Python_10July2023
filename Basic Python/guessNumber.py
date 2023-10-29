import random
secretNumber = random.randint(1,20)
#print(secretNumber)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 5 times
for guessTaken in range(1,6):
    #print(guessTaken)
    print('Take a guess:')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')    
    elif guess == secretNumber:
        #break    #This condition is the correct guess!
        print('Good job! You guessed my number in '+str(guessTaken)+' guesses!')
        break
if guessTaken == guessTaken:
    print('Nope.The number I was thinking of was:'+str(secretNumber))