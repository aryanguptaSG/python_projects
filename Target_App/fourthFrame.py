from tkinter import *
from database import *
from PIL import Image, ImageTk
import thirdFrame as third
import webbrowser



global target
global name
global root
global Subject
global Topic

def addRes(target,subject,root,name,topic,res):
    if str(res).strip:
        insertResource(target,subject,topic,res)
    root.destroy()
    fourthFrame(frame= None,Name=name,Target=target,subject=subject,topic=topic)


def openLink(event):
    var = event.widget.curselection()[0]
    url = event.widget.get(var).strip()
    print(url[0])
    webbrowser.get().open(url)






def takeResFrame(root,name,frame,Target,subject):
    global Topic
    if frame:
        frame.destroy()
    root.config(menu='none')
    new = Frame(root)
    new.pack(fill=BOTH,expand=True)
    Label(new,text="Please add your Resource ..",font="cursive 25 bold").pack(pady=30)
    taketarget = Frame(new)
    taketarget.pack(pady=100)
    Label(taketarget,text="Enter Your Link ..",font="cursive 15 bold").grid(row=0,column=0)
    res_box =  Entry(taketarget,font="cursive 15 bold",bg="lightgray")
    res_box.grid(row=0,column=1)
    Button(taketarget,text="Add Resource",font="cursive 15 bold",command= lambda:addRes(Target,subject,root,name,Topic,res_box.get())).grid(row=1,column=2,pady=10)
    image = Image.open("back1.png")

    resize_image = image.resize((20, 20))
    img = ImageTk.PhotoImage(resize_image)
    Button(new,image=img,command= lambda:fourthFrame(frame=root,Name=name,Target=Target,subject=subject,topic=Topic)).place(x=20,y=20)
    
    mainloop()




def clear(event):
    var = event.widget.curselection()[0]
    if var%2==0:
        event.widget.select_clear(var)




def fourthFrame(frame,Name,Target,subject,topic):
    global target,name,root,Subject,Topic
    name=Name
    target=Target
    Subject=subject
    Topic=topic
    if frame:
        frame.destroy()
    reslist = list()
    for i in getFilterResources(Target,subject,Topic):
        reslist.append(i)
    print(reslist)
    root = Tk()
    root.title("Resources of Topic "+Topic)
    root.geometry("800x500+300-100")
    root.minsize(800,500)
    root.maxsize(800,500)
    if len(reslist)>0:
        frame = Frame(root)
        frame.pack(fill=BOTH,expand=True)
        main_menu = Menu(root)
        root.config(menu=main_menu)
        subject_menu = Menu(main_menu)
        main_menu.add_cascade(label="Resource",menu=subject_menu)
        subject_menu.add_command(label="Add New Resource +",command= lambda:takeResFrame(root,Name,frame,Target,subject))
        Label(frame,text="Topic :"+Topic,font="cursive 25 bold").pack(side=TOP,fill=X,pady=20)
        box = Listbox(frame,height=18,font="cursive 20 ",activestyle='none')
        box.pack(fill=X,padx=10,pady=10)
        space = "    "
        for i in reslist:
            box.insert(END,"")
            box.insert(END,space+i[0])
        box.bind("<Double-1>",openLink)
        box.bind("<<ListboxSelect>>",clear)
        image = Image.open("back1.png")
        resize_image = image.resize((20, 20))
        img = ImageTk.PhotoImage(resize_image)
        Button(frame,image=img,command= lambda:third.thirdFrame(frame=root,Name=Name,Target=Target,subject=subject)).place(x=20,y=20)
    else:
        Label(root,text="Please add your Resources ..",font="cursive 25 bold").pack(pady=30)
        takesubject = Frame(root)
        takesubject.pack(pady=100)
        Label(takesubject,text="Enter Your Resource ..",font="cursive 15 bold").grid(row=0,column=0)
        res_box =  Entry(takesubject,font="cursive 15 bold",bg="lightgray")
        res_box.grid(row=0,column=1)
        Button(takesubject,text="Add Resource",font="cursive 15 bold",command= lambda:addRes(Target,subject,root,name,Topic,res_box.get())).grid(row=1,column=2,pady=10)
    

        
        
        
    mainloop()