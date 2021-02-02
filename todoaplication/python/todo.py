import sys
import datetime

def help():
	print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')


def ls():
    try:
        todo = open("todo.txt", "r+")
    except:
        todo = open("todo.txt", "w+")
    if len(todo.read())==0:
        print("There are no pending todos!")
    else:
        todo.seek(0,0)
        for line in todo.readlines():
            print(line, end="")


def add(todo):
    todolist = []
    try:
        with open("todo.txt", "r") as fh:
            for lines in fh.readlines():
                todolist.append(lines)
            x = len(todolist) + 1
    except:
        x = 1
    with open("todo.txt", "w") as fh:
        tod = "[{}]".format(x) + " "+ str(todo) + "\n"
        fh.write(tod)
        for line in todolist:
            fh.write(line.strip() + "\n")
    print('Added todo: "{}"'.format(str(todo)))


def Del(index):
    todolist = []
    try:
        with open("todo.txt", "r") as fh:
            for lines in fh.readlines():
                todolist.append(lines)
        # print(index, todolist[0][1])
        if int(todolist[0][1]) < index or int(todolist[len(todolist) - 1][1]) > index:
            print("Error: todo #{} does not exist. Nothing deleted.".format(index))
        else:
            for i in range(len(todolist)):
                if int(todolist[i][1]) == index:
                    done = todolist[i]
                    # print(todolist[:i], todolist[i + 1:])
                    todolist = todolist[:i] + todolist[i + 1:]
                    break
                todolist[i] = todolist[i][0:1] + \
                    str(int(todolist[i][1]) - 1) + todolist[i][2:]
            print("Deleted todo #{}".format(index))
    except:
        print("Error: todo #{} does not exist. Nothing deleted.".format(index))



def report():
    try:
        fh = open("todo.txt", "r")
        fhdone = open("done.txt", "r")
        s = len(fh.readlines())
        done = len(fhdone.readlines())
    except:
        fh = open("todo.txt", "w")
        fhdone = open("done.txt", "w")
        s = done = 0
    date_object = datetime.date.today()
    print("{} Pending : {} Completed : {}".format(date_object, s, done))




def done(index):
    todolist = []
    try:
        with open("todo.txt", "r") as fh:
            for lines in fh.readlines():
                todolist.append(lines)
        if int(todolist[0][1]) < index or int(todolist[len(todolist) - 1][1]) > index:
            print("Error: todo #{} does not exist.".format(index))
        else:
            for i in range(len(todolist)):
                if int(todolist[i][1]) == index:
                    done = todolist[i]
                    todolist = todolist[:i] + todolist[i + 1:]
                    break
                todolist[i] = todolist[i][0:1] + \
                    str(int(todolist[i][1]) - 1) + todolist[i][2:]

            with open("done.txt", "a+") as fh:
                date_object = datetime.date.today()
                fh.write("x "+str(date_object) + " " + done[4:].strip() + "\n")
            with open("todo.txt", "w") as fh:
                for line in todolist:
                    fh.write(line.strip() + "\n")
            print("Marked todo #{} as done.".format(index))
    except:
        print("Error: todo #{} does not exist.".format(index))





arg = sys.argv
if len(arg) == 1:
    help()
if len(arg)==2 and str(arg[1]) == "help":
    help()
elif len(arg)==2 and str(arg[1]) == "ls":
    ls()
elif len(arg)==2 and str(arg[1]) == "report":
    report()
elif len(arg)>=2 and str(arg[1]) == "add":
    if len(arg) == 2:
        print("Error: Missing todo string. Nothing added!")
    else :
        add(arg[2])
elif len(arg)>=2 and str(arg[1]) == "done":
    if len(arg) == 2:
        print("Error: Missing NUMBER for marking todo as done.")
    else :
        done(int(arg[2]))
elif len(arg)>=2 and str(arg[1]) == "del":
    if len(arg) == 2:
        print("Error: Missing NUMBER for deleting todo.")
    else :
        Del(int(arg[2]))
