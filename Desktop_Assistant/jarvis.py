import datetime
import subprocess
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os

date=str(datetime.datetime.now())
date =date.split()[0].split('-')[-1]
birthday = {}
username="aryan gupta"
def say(audio):
    subprocess.call(['say',audio])

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("good morning"+username)
    elif hour>=12 and hour<18:
        say("good afternoon"+username)
    elif hour>=18 and hour<24:
        say("good evening"+username)

    say("i am aryan's assistant jarvis ... how may i help you sir")

def takcommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.........")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except:
        print("say that again please....")
        return "none"
    return query


wishme()
while True:
    query=takcommand().lower()
    if "what is my name" in query:
        say("your name is "+username)
    elif "what is your name" in query:
        say("i am jarvis. aryan have made me in his macbook ")
    elif "shut up" in query or 'get out' in query :
        say('sorry sir for disturbing you .... i am going bye bye')
        break
    elif "can you do" in query:
        say("i can change username .. i can tell anyone's wikipedia.. i can search anything for you .. i can find location.. these are most comman things i can do ... what do you want me to do..")
    elif "you doing" in query:
        say("i am learning new things.... do you want me to do anythingh")
    elif "who made you" in query:
        say("aryan has made me in his macbook ")
        say("and he is currently working on me")
    elif "who is" in query:
        url = 'https://google.com/search?q='+query
        webbrowser.get().open(url)
        say("here is the result for"+query)
    elif "birthday list" in query:
        if date in birthday:
            for i in birthday:
                say("today "+birthday[i]+"'s birthday you should wish right now.")
                say("by the way say happy birthday to "+birthday[i]+" from my side and tell her that jarvis is wishing you a very happy birthday")
                reply = takcommand()
                if "listening" in reply:
                    say("oooo that's great .... ")
                    say("hello " +birthday[i]+" i am jarvis i wish you a very happy birthday..")
                    if birthday[i]=="shaanu divedi":
                        say("shanu you don't know aryan and me often talks about you .. aryan told me many things about you ")
                        say("see you soon byee")
        else:
            say("in my list to day no birthday found ")
            say('you can add birthday in list if you want.... ')

    elif "change username" in query:
        say("tell me your name")
        username=takcommand()
    elif 'wikipedia' in query:
        say("searching wikipedia")
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query,sentences =2)
        say("according to wikipedia")
        print(result)
        say(result)
    elif 'thank you' in query or "thanks jarvis" in query or "thanks" in query:
        say("most welcome sir it's my duty ..... is there anything else in which i can help you")
        reply = takcommand()
        if reply == 'yes':
            say("tell me")
            continue
        else:
            say("bye bye sir")
            break
    elif 'open youtube' in query:
        url = 'https://www.youtube.com'
        webbrowser.get().open(url)
        say("here is the result for your query")
    elif 'search' in query:
        say("tell me what are you looking for")
        search = takcommand()
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        say("here is the result for"+search)
    elif "find location" in query:
        say("tell me the location which you are looking for")
        search = takcommand()
        url = 'https://google.nl/maps/place/'+search+'/&amp;'
        webbrowser.get().open(url)
        say("here the the location")


    else:
        say("sorry i am quiting")
        break




#http://192.168.43.1:8080/video
