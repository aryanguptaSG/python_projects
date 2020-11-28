from tkinter import *
from tkinter import filedialog
import os
from PIL import Image
from PyPDF2 import PdfFileMerger




root = Tk()
root.geometry('600x600')
root.minsize(600,600)
Label( text = " Welcome To PDf Converter ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=0,column=2)



def show(x):
	print(x)



# Label( text = " Enter Path ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=1,column=1)
# entry=Entry(root,font=("Helvetica", 20))
# entry.grid(row=1,column=2,pady=15)

# Label( text = " Enter Name for PDF ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=2,column=1)
# entry0=Entry(root,font=("Helvetica", 20))
# entry0.grid(row=2,column=2,pady=15)

# Label( text = "Where to save file ",font="comicsansms 20 bold",fg='red',pady=15).grid(row=3,column=1)
# entry1=Entry(root,font=("Helvetica", 20))
# entry1.grid(row=3,column=2,pady=15)

# puttall= IntVar()
l=list("aryan")
# check1 = Checkbutton(text="Keep All PDF Files",variable=puttall)
# check1.grid(row=4,column=2)
for i in range(5):
	Button(root,text = 'Convert'+str(i),font="comicsansms 20 bold",command= lambda: show(l)).grid(row=i,column=3,pady=15)



root.mainloop()