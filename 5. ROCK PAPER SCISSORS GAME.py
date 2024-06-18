import random

def get_throw(selection):
    if selection == 1:
        return 'Rock'
    elif selection == 2:
        return 'Paper'
    elif selection == 3:
        return 'Scissors'
    else:
        return None

while True:
    player1_wins = 0
    player2_wins = 0
    
    while player1_wins < 2 and player2_wins < 2:
        print('\n')
        print('1. Rock')
        print('2. Paper')
        print('3. Scissors')
        
        try:
            selection = int(input('Enter Throw:'))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        player1_throw = get_throw(selection)
        if player1_throw is None:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        print('\n')
        print('Player 1 throws', player1_throw)

        throws = ['Rock', 'Paper', 'Scissors']
        player2_throw = random.choice(throws)

        print('Player 2 throws', player2_throw)

        if player1_throw == player2_throw:
            print('Tie Game!')
        elif (player1_throw == 'Rock' and player2_throw == 'Scissors') or \
             (player1_throw == 'Paper' and player2_throw == 'Rock') or \
             (player1_throw == 'Scissors' and player2_throw == 'Paper'):
            print('Player 1 Win')
            player1_wins += 1
        else:
            print('Player 2 Win!')
            player2_wins += 1

        print(f'Score: Player 1= {player1_wins} - player 2= {player2_wins}')
    
    if player1_wins == 2:
        print('Player 1 wins the best of three!')
    else:
        print('Player 2 wins the best of three!')

    print('\n')
    print('1) Play Again!')
    print('2) Quit')
    
    try:
        selection = int(input('Enter Choice: '))
    except ValueError:
        print("Invalid input. Exiting game.")
        break

    if selection == 2:
        break
