"""fo = open ("Desktop\python\exm.txt",'a')
#fo.write("Hello all! I am Geetika Sahu.\n")

line_list = ["hope you all are fine\n","hows the weather there\n","enjoying learning python\n"]
#line_list = ["It's raining here\n","It was a good day\n"]
fo.writelines(line_list)

fo = open ("Desktop\python\hello.txt",'w')
line_list = ["hey guys!\n", "what's up!!!!"]
fo.writelines(line_list)
"""
#open the first fie in append mode
ff = open ("Desktop\python\exm.txt",'a')

#open the 2nd fie in read mode
sf = open("Desktop\python\hello.txt",'r')

#read data from 2nd file
info = sf.read()

##append the info from 2nd to 1st file
ff.write(info)

#close both the files
ff.close()
sf.close()