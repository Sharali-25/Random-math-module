import random 
playing = True
number =str(random.randint(10,20))
print("I will generate a number from 10 to 20 , and you have to guess the number one digit at a time. ")
print("The game ends when you get 1 hero'!")
while playing:
    guess = input("Gimme ur best guess!  \n")
    if number == guess:
        print("You won the game")
        print("The number was",number)
        break
    else:
        print("ur guess isb't quite right,try again.  \n")
