
""" numbers =[1,2,3,4,5,6]
print([num*2 if num % 2 ==0  else  num/2 for num in numbers]) """
""" [
for num in numbers
if num % 2 ==0 
    print(num*2)
 else
    print(num/2)] """
""" 
with_vowels= "This is so much fun!"
print(''.join(char for char in with_vowels if char not in "aeiou")) """

#print('U'.join(["cool","dude"]))

nested_list = [[1,2,3],[4,5,6],[7,8,9]]

for loc in nested_list:
    for nested_list in loc:
        print(nested_list)
        

