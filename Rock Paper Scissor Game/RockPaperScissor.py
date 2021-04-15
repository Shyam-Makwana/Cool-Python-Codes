import random
choices = ["Rock", "Paper", "Scissor"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
round = int(input("Enter total number of rounds to play : "))
while round:
    round-=1
    player = input("Input anyone Rock, Paper or  Scissor? ").capitalize()

    ## Conditions of Rock,Paper and Scissor
    if player == computer:
        print("Ooops Tie! No one Wins")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
            
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1

    else:
        if computer == "Rock":
            print("You lose!", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1

    computer = random.choice(choices)

print("\nFinal Score")
print(f"CPU Scores : {cpu_score}")
print(f"Player Scores : {player_score}\n")

if cpu_score==player_score:
    print("Oops Match got tied")
elif cpu_score>player_score:
    print("Sorry! You lose")
else:
    print("Hurrah! You win")