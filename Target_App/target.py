from firstFrame import *

def setname(name,root):
    insertName(name,email.get())
    root.destroy()
    tagetFrame(name)

def tagetFrame(name):
    firstFrame(name=str(name))


Name = ''
Email=''
for i in getName():
    Name = i[0]
    Email=i[1]
    break

if Name and Email:
    tagetFrame(Name)
else:
    root = Tk()
    root.title("Target App")
    root.geometry("500x300+300-100")
    root.minsize(500,300)
    root.maxsize(500,300)
    Label(root,text="Welcome to This App",font="cursive 25 bold").pack(side=TOP,fill=X,pady=20)
    Label(root,text="Let's First complete The Set Up",font="cursive 18 bold").pack(side=TOP,fill=X,pady=10)
    introFrame = Frame(root)
    introFrame.pack(side=TOP,pady=10,padx=10)
    Label(introFrame,text="Enter Your Name ",font="cursive 15").grid(row=0,column=0,padx=5,pady=5)
    Label(introFrame,text="Enter Your Email ",font="cursive 15").grid(row=1,column=0,padx=5,pady=5)
    name =  Entry(introFrame,font="cursive 15",width=25)
    name.grid(row=0,column=1,padx=5,pady=5)
    name.insert(0,Name)
    email = Entry(introFrame,font="cursive 15",width=25)
    email.grid(row=1,column=1,padx=5,pady=5)
    email.insert(0,Email)
    Button(introFrame,text="Set Up",fg="green",font="cursive 15 bold",command= lambda: setname(name.get(),root)).grid(row=2,column=2,pady=10)    
    mainloop()



    


    

