"""#fo = open ("exm.txt",'w')
#fo.write("Hello all! I am Geetika Sahu.\n")

fo = open ("hello.txt",'a')


line_list = ["hope you all are fine\n","how's the weather there\n","enjoying learning python\n"]
#line_list = ["SVNITIAN;D\n","It feels good\n"]
fo.writelines(line_list)

fo = open ("hello.txt",'a')
line_list = ["wishlist!!\n", "want to visit Greece :D"]
fo.writelines(line_list)

#open the first file in append mode
ff = open ("exm.txt",'a')

#open the 2nd fie in read mode
sf = open("hello.txt",'r')

#read data from 2nd file
info = sf.read()

##append the info from 2nd to 1st file
ff.write(info)

#close both the files
ff.close()
sf.close()
"""
"""#moving a file
#change the location iof file
#new directory formation -> os.mkdir("new_directory_path")

import os
import shutil

#os.mkdir("geet")
#shutil.move("source_path","Destionation_path)
#shutil.move("exm.txt","geet")
#shutil.copy("hello.txt","geet")

#moving multiple files
#use for loop

#renaming a file 
os.rename"""
#splitting
str = "I live in India"
splitting=str.split(I)
print(splitting)