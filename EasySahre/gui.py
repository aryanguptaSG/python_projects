from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from Server import *
import threading


def EntryFrame(frame):
    def startserver():
        s.start()
        if s.ip:
            ServerFrame(firstFrame,s.ip,s.port)
        else:
            notic = Frame(firstFrame)
            notic.grid(row = 2)
            Label(notic,text="Can't Start Server . No Deviced Connected yet.").pack()
            Button(notic,text="Ok",fg="red",command = notic.destroy).pack()
    if frame:
        frame.destroy()
    firstFrame = Frame(root)
    firstFrame.pack()
    Label(firstFrame,text="Welcome To Easy Share",font="cursive 30").grid(row=0,pady=20)
    server = Button(firstFrame,text ="Start Server",font="cursive 20",pady=10,padx=10,fg='green',bg='red',command =startserver)
    server.grid(row=1)


def ServerFrame(frame,ip,port):
    def selectFiles():
        if s.isconnected:
            filename = fd.askopenfilename(title = "Select Files",initialdir='/')
            selected.config(text = f'files : {filename}')
            sendbtn = Button(secondfFrame,text="Send",command = lambda:send(filename))
            sendbtn.pack(pady=10)
            selectbtn.forget()
        else:
            showinfo(title="Paired Devices",message="No paired Device . ")
            return 0


    def send(files):
        s.sendFiles(files)

    def close():
        s.stop()
        root.quit()

    if frame:
        frame.destroy()
    secondfFrame = Frame(root)
    secondfFrame.pack()
    Label(secondfFrame,text = f'ip : {ip}port : {port}',font="cursive 20").pack(pady=20)
    filename = None
    selectbtn = Button(secondfFrame,text="Select Files",command = selectFiles)
    selectbtn.pack(pady=10)
    selected = Label(secondfFrame,text = f'files : {filename}')
    selected.pack(pady=10)
    closebtn = Button(secondfFrame,text="close",command = close)
    closebtn.pack()
    threading.Thread(target=s.waitforconnect).start()


    
    
    


global root
global s
root = Tk()
s = Server()
root.title("Easy Share")
root.geometry("700x500+200-100")
root.minsize(700,500)
root.maxsize(700,500)

EntryFrame(None)


mainloop()