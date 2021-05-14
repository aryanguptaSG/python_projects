import secondFrame as second
from fourthFrame import *



global target
global name
global root
global Subject

def addtopic(target,subject,root,name,topic):
    if str(topic).strip:
        insertTopic(target,subject,topic)
    root.destroy()
    thirdFrame(frame= None,Name=name,Target=target,subject=subject)


def openResource(event):
    var = event.widget.curselection()[0]
    topic = event.widget.get(var).strip()
    fourthFrame(root,name,target,Subject,topic)
    print(target,name,Subject,topic)






def taketopicFrame(root,name,frame,Target,subject):
    if frame:
        frame.destroy()
    root.config(menu='none')
    new = Frame(root)
    new.pack(fill=BOTH,expand=True)
    Label(new,text="Please add your Topic ..",font="cursive 25 bold").pack(pady=30)
    taketarget = Frame(new)
    taketarget.pack(pady=100)
    Label(taketarget,text="Enter Your Topic ..",font="cursive 15 bold").grid(row=0,column=0)
    topic_box =  Entry(taketarget,font="cursive 15 bold",bg="lightgray")
    topic_box.grid(row=0,column=1)
    Button(taketarget,text="Add Topic",font="cursive 15 bold",command= lambda:addtopic(Target,subject,root,name,topic_box.get())).grid(row=1,column=2,pady=10)
    image = Image.open("back1.png")

    resize_image = image.resize((20, 20))
    img = ImageTk.PhotoImage(resize_image)
    Button(new,image=img,command= lambda:thirdFrame(frame=root,Name=name,Target=Target,subject=subject)).place(x=20,y=20)
    
    mainloop()








def thirdFrame(frame,Name,Target,subject):
    global target,name,root,Subject
    name=Name
    target=Target
    Subject=subject
    if frame:
        frame.destroy()
    topics = list()
    for i in getFilterTopic(Target,subject):
        topics.append(i)
    print(topics)
    root = Tk()
    root.title("Topics of Subject"+Target)
    root.geometry("800x500+300-100")
    root.minsize(800,500)
    root.maxsize(800,500)
    if len(topics)>0:
        frame = Frame(root)
        frame.pack(fill=BOTH,expand=True)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        subject_menu = Menu(main_menu)
        main_menu.add_cascade(label="Topic",menu=subject_menu)
        subject_menu.add_command(label="Add New Topic +",command= lambda:taketopicFrame(root,Name,frame,Target,subject))
        Label(frame,text="Subject :"+Subject,font="cursive 25 bold").pack(side=TOP,fill=X,pady=20)
        box = Listbox(frame,height=18,font="cursive 20 ",activestyle='none')
        box.pack(fill=X,padx=10,pady=10)
        space = "    "
        for i in topics:
            box.insert(END,"")
            box.insert(END,space+i[0])
        box.bind("<Double-1>",openResource)
        box.bind("<<ListboxSelect>>",clear)
        image = Image.open("back1.png")
        resize_image = image.resize((20, 20))
        img = ImageTk.PhotoImage(resize_image)
        Button(frame,image=img,command= lambda:second.secondFrame(frame=root,Name=Name,Target=Target)).place(x=20,y=20)
    else:
        Label(root,text="Please add your Topics ..",font="cursive 25 bold").pack(pady=30)
        takesubject = Frame(root)
        takesubject.pack(pady=100)
        Label(takesubject,text="Enter Your Topic ..",font="cursive 15 bold").grid(row=0,column=0)
        topic_box =  Entry(takesubject,font="cursive 15 bold",bg="lightgray")
        topic_box.grid(row=0,column=1)
        Button(takesubject,text="Add Topic",font="cursive 15 bold",command= lambda:addtopic(Target,subject,root,name,topic_box.get())).grid(row=1,column=2,pady=10)
    

        
        
        
    mainloop()

