from secondFrame import *





global Name
global root


def addtarget(target,root,name):
    if str(target).strip:
        insertTarget(target)
    root.destroy()
    firstFrame(name=name)









def taketargetFrame(root,name,frame=None):
    if frame:
        frame.destroy()
    root.config(menu='none')
    new = Frame(root)
    new.pack(fill=BOTH,expand=True)
    Label(new,text="Please add your target ..",font="cursive 25 bold").pack(pady=30)
    taketarget = Frame(new)
    taketarget.pack(pady=100)
    Label(taketarget,text="Enter Your target ..",font="cursive 15 bold").grid(row=0,column=0)
    target_box =  Entry(taketarget,font="cursive 15 bold",bg="lightgray")
    target_box.grid(row=0,column=1)
    Button(taketarget,text="Add",font="cursive 15 bold",command= lambda:addtarget(target_box.get(),root,name)).grid(row=1,column=2,pady=10)
    image = Image.open("back1.png")

    resize_image = image.resize((20, 20))
    img = ImageTk.PhotoImage(resize_image)
    Button(new,image=img,command= lambda:firstFrame(frem=root,name=name)).place(x=20,y=20)
    
    mainloop()


    












def opensubject(event):
    var = event.widget.curselection()[0]
    target = event.widget.get(var).strip()
    secondFrame(root,Name,target)
    print(target,Name)



def firstFrame(frem=None,name=None):
    global Name
    global root
    Name=name
    if frem:
        frem.destroy()
    targets = list()
    for i in getAlltarget():
        targets.append(i[0])
    root = Tk()
    root.title("Target App")
    root.geometry("800x500+300-100")
    root.minsize(800,500)
    root.maxsize(800,500)
    if len(targets)>0:
        frame = Frame(root)
        frame.pack(fill=BOTH,expand=True)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        target_menu = Menu(main_menu)
        main_menu.add_cascade(label="Target",menu=target_menu)
        target_menu.add_command(label="Add New Target +",command= lambda:taketargetFrame(root = root,frame=frame,name=name))
        Label(frame,text="Hey "+name+" Thses Are Your Targets ",font="cursive 25 bold").pack(side=TOP,fill=X,pady=20)
        box = Listbox(frame,height=18,font="cursive 20 ",activestyle='none')
        box.pack(fill=X,padx=10,pady=10)
        space = "    "
        for i in targets:
            box.insert(END,"")
            box.insert(END,space+i)
        box.bind("<Double-1>",opensubject)
        box.bind("<<ListboxSelect>>",clear)
    else:
        Label(root,text="Please add your target ..",font="cursive 25 bold").pack(pady=30)
        taketarget = Frame(root)
        taketarget.pack(pady=100)
        Label(taketarget,text="Enter Your target ..",font="cursive 15 bold").grid(row=0,column=0)
        target_box =  Entry(taketarget,font="cursive 15 bold",bg="lightgray")
        target_box.grid(row=0,column=1)
        Button(taketarget,text="Add",font="cursive 15 bold",command= lambda:addtarget(target_box.get(),root,name)).grid(row=1,column=2,pady=10)
        

        
        
        
    mainloop()

