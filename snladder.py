import random

position_Player1= 0
position_Player2 = 0
final_position  = 100
print("Snake n ladder: Roll_a_Die")

Dice = input ("Player1 Dice:")
while (Dice != "q" ):
#    if Dice == "q":
 #       break
    if Dice == "r":
        dice_result = random.randint(1,6)
        print(f"dice_result={dice_result}")
        position_Player1 = dice_result + position_Player1
        print(f"position_Player1 = {position_Player1}")
        if dice_result == 6:
            print(" ")
            Dice == input("P1 roll again: ")
        elif Dice == "q":
            print("OK..But you must play once!")
            break
        else:
            print(f"P1:{dice_result }***")
            print("")
            Dice == input("Player2 roll : ")
            if Dice == "q":
                print("OK P2 quits P1 wins!")
                break
            else:
                dice_result = random.randint(1,6)
                print(f"dice_result = {dice_result}")
                position_Player2 += dice_result
                if dice_result == 6:
                    print("")
                    Dice == input("P2 roll again: ")
                    dice_result = random.randint(1,6)
                    print(f"you got = {dice_result}")
                    position_Player2 = dice_result + position_Player2
                    print(f"position_Player2 = {position_Player2}")

                else:
                    print(f"dice_result{dice_result}")
                    print(f"position_Player2 = {position_Player2}")
                    print(f"P2:{dice_result }***")
                    print(" ")
                    print("Player1 your turn***")
                    Dice = input ("Player1 Dice:")
                    if Dice == "q":
                        print("OK! Well Played")
                        break
                    
    else:
        print("Oops! Something went wrong")
        break

if (position_Player1 == 2,3,6,8,9,11,12,17,21,22,24,28,32,33,36,42,50,54,63,80,88):
    print("yyeeaaa climb the ladder")
    increased_position = random.randint(10,48)
    position_Player1 =("Increased position", increased_position)
    dice = input("Hurray!! You got another change to roll: ")
    dice_again = random.randint(1,6)
    newPosition = position_Player1  + increased_position + dice_again
    print ("P1_position: ",newPosition)
        
else:
    print(position_Player1)

