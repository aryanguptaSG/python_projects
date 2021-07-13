import socket
import os

class Client():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.isconnected = False
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self):
        self.client.connect((self.ip,self.port)) 
        self.isconnected = self.client.recv(1024).decode
        if self.isconnected:
            print("connected")
        else:
            print("Not Connected")

    def reveve(self):
        BUFFER = 4096
        SEPARATOR = "<SEPARATOR>"
        receved = self.client.recv(BUFFER).decode()
        print(receved)
        filename , filesize = receved.split(SEPARATOR) 
        print(filename,filesize)
        if filename:
            with open(filename,'wb') as f:
                while True:
                    bytes_read = self.client.recv(BUFFER)
                    if not bytes_read:
                        break
                    f.write(bytes_read)
                f.close()
        self.client.close()

    def sendFiles(self,files):
        BUFFER = 4096
        SEPARATOR = "<SEPARATOR>"
        filename = os.path.basename(files)
        filesize = os.path.getsize(files)
        print(filename,filesize)
        self.client.send(f'{filename}{SEPARATOR}{filesize}'.encode())
        with open(files,'rb') as f:
            while True:
                bytes_read = f.read(BUFFER)
                if not bytes_read:
                    break
                self.client.sendall(bytes_read)
        self.client.close()

c = Client('192.168.43.197',2333)
c.connect()
c.reveve()