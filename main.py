import random

def rock_paper_scissors():
    choice = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choice)

    player_choice = input("Choose between ROCK, SCISSOR, or PAPER: ").lower()

    while player_choice not in choice:
        print("Invalid selection, Please try again!")
        player_choice = input("Choose between ROCK, SCISSOR, or PAPER: ").lower()

    print(f"Computer choice: {computer_choice}")
    print(f"You chose: {player_choice}")

    if player_choice == computer_choice:
        print("Tie")
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")




rock_paper_scissors()