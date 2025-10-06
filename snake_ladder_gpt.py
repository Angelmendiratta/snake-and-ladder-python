import random

WINNING_POSITION = 100
PLAYERS = 2

positions = [0] * PLAYERS   # player positions
snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
ladders = {4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91}

print("--- Welcome to Snake and Ladder! ---")

current = 0
while True:
    player = current + 1
    input(f"\nPlayer {player}, you are at {positions[current]}. Press Enter to roll...")

    while True:   # keep rolling until valid move
        dice = random.randint(1, 6)
        print(f"Player {player} rolled {dice}")

        if positions[current] + dice <= WINNING_POSITION:
            positions[current] += dice
            break
        else:
            print("⚠️ Can't move, need exact number. Roll again...")

    # check for snakes or ladders
    if positions[current] in snakes:
        positions[current] = snakes[positions[current]]
        print(f"🐍 Snake! Player {player} slides to {positions[current]}")
    
    elif positions[current] in ladders:
        positions[current] = ladders[positions[current]]
        print(f"🪜 Ladder! Player {player} climbs to {positions[current]}")

    print(f"📍 Player {player} is now at {positions[current]}")

    # check win
    if positions[current] == WINNING_POSITION:
        print(f"\n🎉 Player {player} wins! 🎉")
        break

    # switch turn
    current = (current + 1) % PLAYERS
