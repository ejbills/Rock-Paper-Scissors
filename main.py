import random

game_choices = ['rock', 'paper', 'scissors']


def rps_game():
    player_choice = input("Please choose rock, paper or scissors.\n").lower()

    program_choice = random.choice(game_choices)
    print("I choose " + program_choice + "! ")

    if player_choice == program_choice:
        return "It's a tie!"

    if player_choice == "rock":
        return "You win :(" if program_choice == "scissors" else "You lose >:D"

    if player_choice == "paper":
        return "You win :(" if program_choice == "rock" else "You lose >:D"

    if player_choice == "scissors":
        return "You win :(" if program_choice == "paper" else "You lose >:D"


if __name__ == '__main__':
    game_start = input("Would you like to play rock paper scissors? Y/N\n")

    print(rps_game()) if game_start.lower() == "y" else quit()
