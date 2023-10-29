import random, sys
print('ROCK, PAPER, SCISSORS')

#These variables keep track of the number of wins, losses and ties.
wins = 0
losses = 0 
ties = 0

while True:        #The main game loop.
    print('%s Wins, %s Losses, %s Ties' %(wins,losses,ties))
    while True:        #The player input loop.
        print('Enter your move: (r)Rock (p)Paper (s)Scissors or (q)Quit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()          #Quit the program.
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break       #Break out of the player input loop.
        print('Type one of r,p,s or q.')

    #Display what the player choose.
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    #Display what the computer choose.
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #Display and record the win/loss/tie.
    if playerMove == computerMove:
        print('It is a Tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')
        wins = wins + 1                   
