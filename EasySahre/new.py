import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("47.9.65.35",8080))
s.listen(1)
print("start Listining")
c,addr = s.accept()
c.send("Hey This is Server".encode())
receve = c.recv(1024).decode()
print(receve)
s.close()





#47.9.65.35

#2409:4063:4090:b81e:a5a3:2856:f82b:5996