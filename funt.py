from random import random
def flip_coin():
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())

#(*agrs) #(**kwargs)

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    print(total)

sum_all_nums(1,30,6,2,14)


#lambda #map #filter
l = [1,2,3,4]
doubles = list(map(lambda x:x*2,l))
print(doubles)

evens = list(filter(lambda x:x % 2 ==0,l))
print(evens)

names = ["arti","bharti","anu","angel","pooja"]
a_names = filter(lambda n:n[0]== "a", names)
print(list(a_names))

users= [
    {"username":"raj", "tweets": "I love cake and red"},
    {"username":"sam", "tweets": "I love cat"},
    {"username":"jeff", "tweets": [], "color":"blue","num":10},
    {"username":"boy", "tweets": [],"num":20},
    {"username":"girl", "tweets": "dogs are the best", "color":"black"},
    {"username":"bob", "tweets": []}    

]
inactive_users=list(filter(lambda u: not u['tweets'],users))
print(inactive_users)

usernames=list(map(lambda user:user["username"].upper(),
    filter(lambda u: not u['tweets'],users)))

print(usernames)

inactive_users2 = [user for user in users if not user['tweets']]
print(inactive_users2)


usernames2 = [user["username"].upper() for user in users if not user['tweets']]
print(usernames2)

print(sorted(users,key=len))

print("  ")
print(sorted(users,key=lambda user:user['username']))

print("  ")

#max and min
names=['Arya','Shalu','Chanramukhi','Gayatri','Sheela','Sri']

print(min(names))
print(max(names))
print([len(name) for name in names])
print(min(len(name) for name in names))
print(min(names,key=lambda n:len(n)))
print(max(len(name) for name in names))
print(max(names,key=lambda n:len(n)))

songs = [
    {"title":"KKHH","playcount": 56 },
    {"title":"happy birthday","playcount": 3 },
    {"title":"KRISH","playcount": 1 },
    {"title":"Toxic","playcount": 87 }
]

print(min(songs,key=lambda s:s['playcount'])['title'])
print(sorted(songs,key = lambda s: s['playcount']))

print("")

max = 3
for song in songs:
    if song['playcount'] > max:
        print(song['playcount'])

print("")

#reversed
nums= (1,2,3,4)
print(list(reversed(nums)))

for char in reversed("hello World"):
    print(char)

a= "hello"[::-1]
print(a)
print(list(reversed('hello')))
#Debugging
#try and expect
""" try:
    foobar
except:
    print('PROBLEM')
print("after the try") """


def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name":"Rishi"}
print(get(d,"name"))



