from thirdFrame import *
import firstFrame as first


global target
global name
global root

def addsubject(target,subject,root,name):
    if str(subject).strip:
        insertSubject(target,subject)
    root.destroy()
    secondFrame(frame= None,Name=name,Target=target)


def openTopic(event):
    var = event.widget.curselection()[0]
    subject = event.widget.get(var).strip()
    thirdFrame(root,name,target,subject)
    print(target,name,subject)






def takesubjectFrame(root,name,frame,Target):
    if frame:
        frame.destroy()
    root.config(menu='none')
    new = Frame(root)
    new.pack(fill=BOTH,expand=True)
    Label(new,text="Please add your Subject ..",font="cursive 25 bold").pack(pady=30)
    taketarget = Frame(new)
    taketarget.pack(pady=100)
    Label(taketarget,text="Enter Your Subject ..",font="cursive 15 bold").grid(row=0,column=0)
    subject_box =  Entry(taketarget,font="cursive 15 bold",bg="lightgray")
    subject_box.grid(row=0,column=1)
    Button(taketarget,text="Add Subject",font="cursive 15 bold",command= lambda:addsubject(Target,subject_box.get(),root,name)).grid(row=1,column=2,pady=10)
    image = Image.open("back1.png")

    resize_image = image.resize((20, 20))
    img = ImageTk.PhotoImage(resize_image)
    Button(new,image=img,command= lambda:secondFrame(frame=root,Name=name,Target=Target)).place(x=20,y=20)
    
    mainloop()






def secondFrame(frame,Name,Target):
    global target,name,root
    name=Name
    target=Target
    if frame:
        frame.destroy()
    subjects = list()
    for i in getFilterSubject(Target):
        subjects.append(i)
    print(subjects)
    root = Tk()
    root.title("Subjects of Target"+Target)
    root.geometry("800x500+300-100")
    root.minsize(800,500)
    root.maxsize(800,500)
    if len(subjects)>0:
        frame = Frame(root)
        frame.pack(fill=BOTH,expand=True)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        subject_menu = Menu(main_menu)
        main_menu.add_cascade(label="subject",menu=subject_menu)
        subject_menu.add_command(label="Add New subject +",command= lambda:takesubjectFrame(root,Name,frame,Target))
        Label(frame,text="Targets :"+Target,font="cursive 25 bold").pack(side=TOP,fill=X,pady=20)
        box = Listbox(frame,height=18,font="cursive 20 ",activestyle='none')
        box.pack(fill=X,padx=10,pady=10)
        space = "    "
        for i in subjects:
            box.insert(END,"")
            box.insert(END,space+i[0])
        box.bind("<Double-1>",openTopic)
        box.bind("<<ListboxSelect>>",clear)
        image = Image.open("back1.png")
        resize_image = image.resize((20, 20))
        img = ImageTk.PhotoImage(resize_image)
        Button(frame,image=img,command= lambda:first.firstFrame(frem=root,name=Name)).place(x=20,y=20)
    else:
        Label(root,text="Please add your Subjects ..",font="cursive 25 bold").pack(pady=30)
        takesubject = Frame(root)
        takesubject.pack(pady=100)
        Label(takesubject,text="Enter Your Subject ..",font="cursive 15 bold").grid(row=0,column=0)
        subject_box =  Entry(takesubject,font="cursive 15 bold",bg="lightgray")
        subject_box.grid(row=0,column=1)
        Button(takesubject,text="Add Subject",font="cursive 15 bold",command= lambda:addsubject(Target,subject_box.get(),root,Name)).grid(row=1,column=2,pady=10)
    

        
        
        
    mainloop()




# image = Image.open("back1.png")

# resize_image = image.resize((20, 20))
# img = ImageTk.PhotoImage(resize_image)

# Button(root,image=img,command= lambda:print("clicked")).grid()
# Label(root,text="ab btao").grid()

    



