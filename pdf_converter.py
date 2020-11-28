from tkinter import *
from tkinter import filedialog
import os
from PIL import Image
from PyPDF2 import PdfFileMerger




root = Tk()
root.geometry('600x600')
root.minsize(600,600)
Label( text = " Welcome To PDf Converter ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=0,column=2)

def convert():
	name = filedialog.askopenfilename(initialdir="/desktop",title="select a file",filetypes=(("jpg files" , "*.jpg"),("png files" , "*.png")))
	print(name)
	return 0
	print(puttall.get())
	merger = PdfFileMerger()
	path = entry.get()

	files = os.listdir(path)
	pdflist = []
	# print(files)
	i=0
	for file in files:
		if '.jpg' in file:
			f = path+'/'+file
			im = Image.open(f)
			if im.mode =='RGBA':
				im = im.convert("RGB")
			new = path+str(i)+'.pdf'
			im.save(new, "PDF", resolution=200.0)
			pdflist.append(path+str(i)+'.pdf')
			i+=1

	newpath = entry1.get()+entry0.get()
	for i in pdflist:
		merger.append(i)
	merger.write(newpath)

	# sleep(10)
	# print(pdflist)
	if not puttall.get():
		for i in pdflist:
			os.remove(i)

	os.remove(newpath)

	merger.close()

Label( text = " Enter Path ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=1,column=1)
entry=Entry(root,font=("Helvetica", 20))
entry.grid(row=1,column=2,pady=15)

Label( text = " Enter Name for PDF ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=2,column=1)
entry0=Entry(root,font=("Helvetica", 20))
entry0.grid(row=2,column=2,pady=15)

Label( text = "Where to save file ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=3,column=1)
entry1=Entry(root,font=("Helvetica", 20))
entry1.grid(row=3,column=2,pady=15)

puttall= IntVar()

check1 = Checkbutton(text="Keep All PDF Files",variable=puttall)
check1.grid(row=4,column=2)

my_button = Button(root,text = 'Convert',font="comicsansms 20 bold", command=convert)
my_button.grid(row=10,column=3,pady=15)


root.mainloop()

#'/Users/aryangupta/Desktop/my_portfolio/img/hero/'
#'/Users/aryangupta/Desktop/merged.pdf'


