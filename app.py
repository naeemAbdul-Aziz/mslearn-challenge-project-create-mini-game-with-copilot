import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    player_score = 0
    opponent_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in options:
            print("Invalid option. Please choose again.")
            continue

        opponent_choice = random.choice(options)
        print(f"Opponent chooses {opponent_choice}.")

        if player_choice == opponent_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and opponent_choice == 'scissors') or \
             (player_choice == 'paper' and opponent_choice == 'rock') or \
             (player_choice == 'scissors' and opponent_choice == 'paper'):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            opponent_score += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"Final score: Player {player_score} - Opponent {opponent_score}")

play_game()