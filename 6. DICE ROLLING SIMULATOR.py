import random

def roll_dice(dice, sides):
    roll = []
    for _ in range(dice):
        face = random.randint(1, sides)
        roll.append(face)
    return roll

def sum_roll(roll):
    return sum(roll)

def play_round(player, dice, sides):
    roll = roll_dice(dice, sides)
    roll_sum = sum_roll(roll)
    print(f"Player {player} rolled: {roll} (Sum: {roll_sum})")
    return roll_sum

def main():
    dice = int(input('Number of Dice: '))
    if dice <= 0:
        print('Must have at least one Dice!')
        return

    sides = int(input('Number of Sides: '))
    if sides <= 0:
        print('Must have at least one Side!')
        return

    player1_wins = 0
    player2_wins = 0

    while player1_wins < 2 and player2_wins < 2:
        print("\nStarting a new round...")

        player1_score = play_round(1, dice, sides)
        player2_score = play_round(2, dice, sides)

        if player1_score > player2_score:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif player2_score > player1_score:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("This round is a tie!")

        print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}")

    if player1_wins == 2:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

if __name__ == "__main__":
    main()
