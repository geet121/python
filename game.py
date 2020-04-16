import random

ran_num= random.randint(1,10)
guess = None

while True:
    guess = input("Pick a num from 1 to 10: ")
    guess = int (guess)
    if guess> ran_num:
        print("Too high! wrong guessing")
    elif guess < ran_num:
        print("Too low! guess a greater num.")
    else:
        print("YOU WON!!")
        play= input("u wanna play again?(y/n):")
        if play == "y":
            ran_num= random.randint(1,10)
            guess= None
        else:
            print("Thanks for playing \U0001f600")
            break


print(f"The num was {ran_num}")