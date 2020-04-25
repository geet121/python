import random

position_Player1= 0
position_Player2 = 0
final_position  = 100
print("Snake n ladder: Roll_a_Die")

gameBegin= input ("Want to play a game entner(y or n):")

def position_increment(prvPosition , diceValue):
     if (diceValue == 6):
        dice = input("Hurray!! You got another change to roll: ")
        hurrayDiceValue = random.randint( 1 , 6)
        print("Your Bonus dice value: ", hurrayDiceValue )
        prvPosition = prvPosition + diceValue + hurrayDiceValue
        return prvPosition
     else:
        prvPosition = prvPosition + diceValue
        return prvPosition


if gameBegin=='y':
    dice = ""
    while (dice != 'q'):
        dice = input("Player1 Dice: ")
        dice_result = random.randint( 1 , 6)
        print("Player1 dice value", dice_result)
        position_Player1 =  position_increment( position_Player1 , dice_result )
        print( position_Player1 )
        dice = input ("Player2 Dice: ")
        dice_result = random.randint( 1 , 6)
        print("Player2 dice value", dice_result)
        position_Player2 =  position_increment( position_Player2 , dice_result )
        print( position_Player2 )
else:
    print("Thank you for playing")
    



