import sys
import datetime

#Taking arguments from command line
arg = sys.argv

#Executing the command without any arguments, or with a single argument `help` prints the CLI usage.
def help():
	print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')


def ls(todo):
	num=len(todo.readlines())
	if num==0:
		print("There are no pending todos!")
	else:
		todo.seek(0,0)
		for line in todo:
			print("[{}] ".format(num)+line,end='')
			num-=1
		print("")

def add(todo,work):
	works = []
	for line in todo.readlines():
		works.append(line)
	works = [work]+works
	print('Added todo: "{}"'.format(str(work)))
	todo = open('todo.txt','w')
	for line in works:
		todo.write(line.strip() + "\n")
	todo.close()







try:
	todo = open('todo.txt','r')
except:
	todo = open('todo.txt','w')




if len(arg)==1:
	help()
elif len(arg)==2 and arg[1]=='help':
	help()



elif arg[1]=='ls':
	ls(todo)

elif len(arg)==3 and arg[1]=='add':
	add(todo,arg[2])


