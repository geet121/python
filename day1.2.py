from PyPDF2 import PdfFileReader,PdfFileWriter
#merge pdfs 
#encrypt pdfs
#open your 1st pdf
#open your 2nd pdf
#for each page, copy it to 3rd pdf
#open a 3rd pdf

write_obj = PdfFileWriter()
pdf_list = ["/home/rishi/Downloads/PDF1","/home/rishi/Downloads/PDF2"]
for i in pdf_list:
    red_obj = PdfFileReader(i)
    pages = red_obj.getNumPages()
    print(pages)
    
    for j in range(pages):
        print(j)