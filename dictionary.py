instructor = {
    "name": "kitty",
    "city":"Dhamtari",
    "color":"red",

}

""" print(instructor.values())
for v in instructor.values():
    print(v),

print("   ")
for v in instructor.keys():
    print(v)

print(instructor.items()) 
print(instructor["isCat"])
print(instructor["name"])

#for k,v in instructor.items():
   # print(f"key:{k} and value:{v}")
print("***")
for keys,values in instructor.items():
    print(keys,values)

y_instructor = {(k.upper() if k is 'color' else k):v.upper() for k,v in instructor.items()}
print(y_instructor)"""

#Tuple
""" months = ("Januaray","Februrary","March","April","May", "June","July","August","Sept","October","Nov","December")
rint(f"months:{months}")

for month in months:
   print(month)

i = len(months) -1
while i >= 0:
    print(months[i])
    i -= 1 """

#Sets
string = "hello"
a ={char for char in string if char not in 'aeiou'}
print(a)
"""dict = { key: key * 10 for key in range(0, 100) }
d1 = {}
for key, value in dict.items():
    if key % 2 == 0:
        d1[key] = value
    print(d1)"""