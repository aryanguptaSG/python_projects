import json
try :
    file = open('contect.txt', 'r')
except:
    file = open('contect.txt', 'w')
    
x=input("save or see: ")
if x=="save":
    file = open('contect.txt', 'r')
    line= file.read()
    name=list()
    number=list()
    if len(line)>1:
        j=json.loads(line)
        for z in j.keys():
            name.append(z)
            number.append(j[z])
    n=input('name: ')
    nu=int(input('number: '))
    name.append(n)
    number.append(nu)
    line=dict(zip(name,number))
    print('saved')
    j=json.dumps(line, sort_keys=True, indent=2)
    file = open('contect.txt', 'w')
    file.write(j)
    file.close()

else:
    file = open('contect.txt' ,'r')
    line=file.read()
    if len(line)<=0:
        print("no numbers")
        exit()
    j=json.loads(line)
    x=input('name :')
    if x=='all':
        print(line)
    else:
        for y in j.keys():
            if x in y:
                print(y+' = '+str(j[y]))




