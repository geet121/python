playlist ={
    'title': 'awesome',
    'author' :'me',
    'songs':[
        {'title':'song1','artist':'me','duration':2.5},
        {'title':'song2','artist':['kitty','djcat'],'duration':3.25},
        {'title':'jaane kyu','artist':'KK','duration':4.0}
    ]
}
""" for song in playlist ['songs']:
    print(song['title']) 
total_length=0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length) 

numbers =dict(first =1,second=2,third=3)
double_numb = {key:value * 2 for key,value in numbers.items()}
sq_numb = {key:value ** 2 for key,value in numbers.items()}
print(double_numb)
print(sq_numb) 

str1= 'ABC'
str2= '123'
combo = {str1[i]:str2[i] for i in range(0, len(str2))}
print(combo) """


