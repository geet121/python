""" from random import randint
print("Raja...Mantri..Chor..Police")

r_num= randint(0,3)
ra_num = randint (0,3)
ran_na = randint(0,3)
rana_na = randint(0,3)
player1 = r_num
player2 = ra_num
player3 = ran_na
player4 = rana_na

if r_num == 1:
    player1 = "Raja"
    print("player1:Mera Mantri koun?")
    print(r_num)
    if ra_num == 2:
        player2 = "Mantri"
        print(f"player2:Main hu {player2} ")
        print(ra_num)
        if ran_na == 3:
            player3 = "Police" 
            print(ran_na)   
        else:
            player4 = "Chor"
            print(rana_na)
        print(f"Raja says {player4} {player3} ka pta lagao")
    elif ra_num == 3:
        player2 = "Police"
        if ran_na == 0:
            player3 = "Chor"
        else :
            player4 = "Mantri"
            print(f"Main hu {player4} ")
        print(f"Raja says {player2} {player3} ka pta lagao")
    else:
        player2 = "Chor"
        if ran_na == 2:
            player3 = "Mantri"
            print(f"Main hu {player2} ")
            print(f"Raja says {player2} {player4} ka pta lagao")
        else :
            player4 = "Police"
        print(f"Raja says {player2} {player3} ka pta lagao")
elif r_num == 2:
    player1 ="Mantri"
    print(f"Main hu {player1} ")
    if ra_num == 3:
        player2 = "Police"
        if ran_na == 1:
            player3 = "Raja"
            print("player3:Mera Mantri koun?")    
        else:
            player4 = "Chor"
    elif ra_num == 1:
        player2 = "Raja"
        print("Player2:Mera Mantri koun?")
        if ran_na == 0:
            player3 = "Chor"
        else :
            player4 = "Mantri"
            print(f"Player4:Main hu {player4} ")
        print(f"Raja says {player4} {player3} ka pta lagao")
    else :
        player2 = "Chor"
        if ran_na == 2:
            player3 = "Mantri"
            print(f"Player3:Main hu {player3} ")
        else:
            player4 = "Raja"
        print(f"Raja says {player2} {player4} ka pta lagao")
elif r_num == 3:
    player1 ="Police"
    if ra_num == 2:
        player2 = "Mantri"
        print(f"Main hu {player2} ")
        if ran_na == 1:
            player3 = "Raja"
            print("player3:Mera Mantri koun?")    
        else:
            player4 = "Chor"
    elif ra_num == 1:
        player2 = "Raja"
        print("Player2:Mera Mantri koun?")
        if ran_na == 0:
            player3 = "Chor"
        else :
            player4 = "Mantri"
            print(f"Player4:Main hu {player4} ")
        print(f"Raja says {player4} {player3} ka pta lagao")
    else :
        player2 = "Chor"
        if ran_na == 2:
            player3 = "Mantri"
            print(f"Player3:Main hu {player3} ")
        else:
            player4 = "Raja"
        print(f"Raja says {player2} {player4} ka pta lagao")
else:
    player1 = "Chor  """

dict = { key: key * 10 for key in range(0, 100) }
d1 = {}
for key, value in dict.items():
    if key % 2 == 0:
        d1[key] = value
    print(key)