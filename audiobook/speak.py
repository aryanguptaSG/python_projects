#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
from tkinter import *
import pyttsx3
import urllib.request, urllib.parse,urllib.error
import ssl
import subprocess
import json
import threading
import time

root = Tk()
root.geometry("200x200")
# root.minsize(500,500)
a = Label( text = " Welcome To Audio Book ",fg='red')
a.pack()

with open('data.json') as d:
	data = json.load(d)

print(data)
url=''
dead = False

def say(audio):
    subprocess.call(['say',audio])



class read(threading.Thread):
	def run(self):
		global dead
		speaker = pyttsx3.init()
		voices = speaker.getProperty('voices')
		speaker.setProperty('voice',voices[0].id)
		ctx =ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE
		fhand = urllib.request.urlopen(url, context = ctx)
		print(fhand)
		for line in fhand:
			if len(line.decode().strip())>0:
				print(line.decode().strip())
				# speaker.say(line.decode().strip())
				# speaker.runAndWait()
				say(line.decode().strip())
				if (dead):
					break
		


def choose():
	global dead
	dead = False
	global url
	url = 'https://sherlock-holm.es'
	l = list()
	for i in data :
	 	l.append(data[i])
	 	
	print(l)
	x=entry.get()
	url+=l[int(x)]
	# threading.Thread(target=fun).start()
	r = read()
	r.start()




def stop():
	global dead
	dead=True
	

entry = Entry(root,font=("Helvetica", 28))
entry.pack(pady=20)

my_button = Button(root,text = 'Play',font=("Helvetica", 28), command=choose)
my_button.pack()

my_button1 = Button(root,text = 'Pause',font=("Helvetica", 28), command=stop)
my_button1.pack()


root.mainloop()


#threading.Thread(target=choose).start()
