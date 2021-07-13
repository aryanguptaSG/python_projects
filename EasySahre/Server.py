import subprocess
import socket
import os

class Server():
    def __init__(self):
        self.server = None
        self.ip = None
        self.port = None
        self.isconnected = False
        self.connectedwith = None
        self.client = None

    def start(self):
        ip = subprocess.run(['ipconfig','getifaddr','en0'],capture_output=True,text=True)
        if ip.stdout:
            self.ip =ip.stdout.strip()
            self.port = 2333
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print(self.ip,self.port)
            s.bind((self.ip,self.port))
            s.listen(1)
            self.server = s
        else:
            pass
        
    def waitforconnect(self):
        client,addr = self.server.accept()
        if client:
            client.send("connected".encode())
            self.isconnected = True
            self.connectedwith = addr
            self.client = client


    def stop(self):
        self.server.close()


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

    def receve(self):
        BUFFER = 4096
        SEPARATOR = "<SEPARATOR>"
        receved = self.client.recv(BUFFER).decode()
        print(receved)
        filename,filesize = receved.split(SEPARATOR)
        print(filename,filesize)
        with open(filename,'wb') as f:
            while True:
                bytes_read = self.client.recv(BUFFER)
                if not bytes_read:
                    break
                f.write(bytes_read)
            f.close()
        self.client.close()

s = Server()
s.start()
s.waitforconnect()
s.receve()
s.stop()


