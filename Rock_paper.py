from random import choice

options=['r','p','s']
fullOptions={'r':'Rock','p':'paper','s':'scissors'}
repeat = True
while(repeat):
    player=input('enter a choice between R P S :' )
    player=player.lower()
    while player not in options:
        print(f'{player} is not a valid choice, please choose between (r, p or s)')
        player=input('enter a choice between (R P S) :' )
        player=player.lower()
    cpu=choice(options)
    if player=='r':
        if cpu=='s':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('congratulations you have won ', playerWon)
            repeat = False
        elif cpu=='r':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('there was a tie ', playerWon)
            print('Please try again')

        else:
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('You loose ', playerWon)
            repeat = False

    elif player=='p':
        if cpu=='r':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('congratulations you have won ', playerWon)
            repeat = False
        elif cpu=='p':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('there was a tie ', playerWon)
            print('Please try again')
        else:
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('You loose ', playerWon)
            repeat = False

    elif player=='s':
        if cpu=='p':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('congratulations you have won ', playerWon)
            repeat = False
        elif cpu=='s':
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('there was a tie ', playerWon)
            print('Please try again')
        else:
            playerWon=f'Player({fullOptions[player]}): CPU({fullOptions[cpu]})'
            print('You loose ', playerWon)
            repeat = False

    
        
        
    
