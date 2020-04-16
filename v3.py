from random import randint
player_wins=0
comp_wins=0
winning_limit=2
 
while player_wins<winning_limit  and comp_wins<winning_limit:   
    print(f"Player score: {player_wins} Computer score: {comp_wins}")
    #print("Rock...")
    #print("Paper...")
    #print("Scissors...")
    player = input("Player, make your move: ").lower()
    if player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
 
    print(f"Computer plays: {computer}" )

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            comp_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            comp_wins += 1	
    else:
        print("Please enter a valid move!")

if player_wins > comp_wins:
    print("Congrates you WON! \U0001f600" )
elif player_wins == comp_wins:
    print("It's a tie")
else:
    print("OH No Computer won :(")
print(f"Final Scores, Player:{player_wins} Computer:{comp_wins}")