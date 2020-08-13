import random

position_Player1= 0
position_Player2 = 0
final_position  = 100
print("Snake n ladder: Roll_a_Die")

gameBegin= input ("Want to play a game entner(y or n):")



def ladder2 (position_Player2):
    if (position_Player2 == 2,3,6,8,9,11,12,17,21,22,24,28,32,33,36,42,50,54,63,80,88):
        print("yyeeaaa climb the ladder")
        increased_position = random.randint(10,48)
        position_Player2 =("Increased position", increased_position)
        newPosition = position_Player2  + increased_position
        print ("P2_position: ",newPosition)
        return newPosition
    else:
        print(diceValue)
ladder2 (position_Player2)

def ladder1 (position_Player1,newPosition):
    if (position_Player1 == 2,3,6,8,9,11,12,17,21,22,24,28,32,33,36,42,50,54,63,80,88):
        print("yyeeaaa climb the ladder")
        increased_position = random.randint(10,48)
        position_Player1 =("Increased position", increased_position)
        dice = input("Hurray!! You got another change to roll: ")
        dice_again = random.randint(1,6)
        newPosition = position_Player1  + increased_position + dice_again
        print ("P1_position: ",newPosition)   
    else:
        print(diceValue)

def snake2 (position_Player2,newPosition):
    if (position_Player2 == 13,18,23,29,34,38,44,51,55,64,82,99):
        print("Oops! sorry snake bite")
        decreased_position = random.randint(10,48)
        position_Player2 =("Decreased position", decreased_position)
        newPosition = position_Player2  - decreased_position
        print ("P2_position: ",newPosition)
    else:
        print(diceValue)

def snake1 (position_Player1,newPosition):
    if (position_Player1 == 13,18,23,29,34,38,44,51,55,64,82,99):
        print("Oops! sorry snake bite")
        decreased_position = random.randint(10,48)
        print("decreased_position = ", decreased_position)
        position_Player1 =("Decreased position", decreased_position)
        newPosition = position_Player1  - decreased_position
        print ("P1_position: ",newPosition)
    else:
        print(diceValue)


def position_increment(prvPosition , diceValue):
     if (diceValue == 6):
        dice = input("Hurray!! You got another change to roll: ")
        hurrayDiceValue = random.randint( 1 , 6)
        print("Your Bonus dice value: ", hurrayDiceValue )
        prvPosition = prvPosition + diceValue + hurrayDiceValue
        return prvPosition
     else:
        prvPosition = prvPosition + diceValue
        ladder(prvPosition)
        return prvPosition


if gameBegin=='y':
    dice = ""
    while (dice != 'q'):
        dice = input("Player1 Dice: ")
        dice_result = random.randint( 1 , 6)
        print("Player1 dice value", dice_result)
        position_Player1 =  position_increment( position_Player1 , dice_result )
        ladder1()
        print( position_Player1 )
        dice = input ("Player2 Dice: ")
        dice_result = random.randint( 1 , 6)
        print("Player2 dice value", dice_result)
        position_Player2 =  position_increment( position_Player2 , dice_result )
        print( position_Player2 )
    else:
        print("Thank you for playing")
else:
    print("OK! but you must try once")
    

