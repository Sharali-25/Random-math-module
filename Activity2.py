import random
while True :
    User_action=input("enter a choice(rock,paper,scissors)")
    possible_action=["rock","paper","scissors"]
    computer_action=random.choice(possible_action)
    if User_action== computer_action:
        print("it is a tie")
    elif User_action=="rock" and computer_action == "scissors":
        print("Rock smashes scissors! u win")
    elif User_action =="paper" and computer_action =="rock":
        print("paper covers rock u win")
    elif User_action =="scissors" and computer_action == "paper":
        print("scissors cuts paper u win")
    else:
        print(" u lose")
        print("computer wins")