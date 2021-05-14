import sqlite3

#Setting Up The DataBase If Not Created
def setup():
    curr.executescript('''
    CREATE TABLE IF NOT EXISTS Intro(
        Name TEXT(50),
        Email VARCHAR(50)
    );
    CREATE TABLE IF NOT EXISTS Targets(
        targetName VARCHAR(20) UNIQUE
    );
    CREATE TABLE IF NOT EXISTS Subjects(
        targetName VARCHAR(20),
        subjectName VARCHAR(20)
    );
    CREATE TABLE IF NOT EXISTS Topics(
        targetName VARCHAR(20),
        subjectName VARCHAR(20),
        topicName VARCHAR(20)
        
    );
    CREATE TABLE IF NOT EXISTS REsources(
        targetName VARCHAR(20),
        subjectName VARCHAR(20),
        topicName VARCHAR(20),
        resource VARCHAR(100) 
    );

    ''')

def insertName(name,email):
    curr.execute("INSERT INTO Intro (Name,Email) VALUES(?,?)",(name,email,))
    conn.commit()

def getName():
    return curr.execute("SELECT * FROM Intro")

#Adding New Targets
def insertTarget(target):
    curr.execute("INSERT INTO Targets (targetName) VALUES(?)",(target,))
    conn.commit()

#Adding New Subjects
def insertSubject(target,subject):
    curr.execute("INSERT INTO Subjects (targetName,subjectName) VALUES(?,?)",(target,subject,))
    conn.commit()

#Adding New Topics
def insertTopic(target,subject,topic):
    curr.execute("INSERT INTO Topics (targetName,subjectName,topicName) VALUES(?,?,?)",(target,subject,topic,))
    conn.commit()

#Adding New Resources
def insertResource(target,subject,topic,res):
    curr.execute("INSERT INTO Resources (targetName,subjectName,topicName,resource) VALUES(?,?,?,?)",(target,subject,topic,res,))
    conn.commit()

#Getting All Targets
def getAlltarget():
    return curr.execute("SELECT targetName FROM Targets")

#Getting All Subjects 
def getAllSubject():
    return curr.execute("SELECT subjectName FROM Subjects")


#Getting Subjects Filtered By Targets
def getFilterSubject(target):
    return curr.execute("SELECT subjectName FROM Subjects WHERE targetName =?",(target,))

#Getting All Topics
def getAllTopic():
    return curr.execute("SELECT topicName FROM Topics")


#Getting Filtered Topics
def getFilterTopic(target,subject):
    return curr.execute("SELECT topicName FROM Topics Where subjectName = ? AND targetName =?",(subject,target,))


#Gettign All Resources
def getAllResources():
    return curr.execute("SELECT resource FROM Resources")

#Getting Filtered Resources
def getFilterResources(target,subject,topic):
    return curr.execute("SELECT resource FROM Resources Where subjectName = ? AND targetName =? AND topicName = ?",(subject,target,topic,))
    


global conn 
conn = sqlite3.connect("TargetData.sqlite")

global curr 
curr = conn.cursor()

setup()