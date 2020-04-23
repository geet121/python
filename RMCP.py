import random
print("Raja...Mantri..Chor..Police")

random_value = ["Raja", "Mantri", "Chor", "Police"]
chor = ["Chor"]
raja_mantri = ["Raja", "Mantri"]
random.shuffle(random_value)
player = ["player1", "player2", "player3", "player4"]

afterShuffle = {key: value for key, value in zip(random_value, player)}


def get_Player_Value(matchkey):
    for key, value in afterShuffle.items():
        if matchkey == key:
            return value
    return "key doesn't exist"


raja = get_Player_Value("Raja")

print(f"{raja} is Raja and puch rha hai mera Mantri koun?")

mantri = get_Player_Value("Mantri")

print(f"{mantri} mai hu Mantri")
print(f"{raja} is Raja: Chor ka pata lagao")
print(f"{mantri} is Mantri: ji Janab!!")


def filterByKey(keys): return {x: afterShuffle[x] for x in keys}


getChor = filterByKey(chor)


def get_Player_key(val):
    if getChor["Chor"] == val:
        print("You won")
    else:
        print("Lost")


mantri_input = input(f"{mantri} is Mantri: make your move!: ").lower()
get_Player_key(mantri_input)
