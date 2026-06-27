import random

# Snake and Ladder positions
snakes = {
    16: 6,
    47: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}


def roll_dice():
    return random.randint(1, 6)


def move_player(position, dice):
    if position + dice <= 100:
        position += dice

    if position in ladders:
        print(f"🎉 Ladder! Climb from {position} to {ladders[position]}")
        position = ladders[position]

    elif position in snakes:
        print(f"🐍 Snake! Slide from {position} to {snakes[position]}")
        position = snakes[position]

    return position


def play_game():
    print("=" * 40)
    print("      SNAKE AND LADDER GAME")
    print("=" * 40)

    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")

    pos1 = 0
    pos2 = 0
    turn = 0

    while True:
        if turn % 2 == 0:
            input(f"\n{player1}'s turn. Press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player1} rolled: {dice}")
            pos1 = move_player(pos1, dice)
            print(f"{player1} is now at {pos1}")

            if pos1 == 100:
                print(f"\n🏆 Congratulations! {player1} wins!")
                break

        else:
            input(f"\n{player2}'s turn. Press Enter to roll the dice...")
            dice = roll_dice()
            print(f"{player2} rolled: {dice}")
            pos2 = move_player(pos2, dice)
            print(f"{player2} is now at {pos2}")

            if pos2 == 100:
                print(f"\n🏆 Congratulations! {player2} wins!")
                break

        turn += 1


play_game()+