import socket

class connection:
    def __init__(self,ipAddr, port):
        self.ipAdress = ipAddr
        self.port = port
        self.allow = 1
    def start(self):
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.ipAdress, self.port))
        self.s.listen(1)
        if self.allow == False:
            return False
    def wait_connect(self):
        print("waiting")
        self.sock, self.addr = self.s.accept()
        return self.addr
    def reveice(self):
        if self.allow == 0:
            return
        while 1:
            msg = self.sock.recv(1024).decode()
            print("来自远程连接的命令:{0}".format(msg))
            if msg == "exit" or self.allow == 0:
                break

        self.sock.close()
        self.s.close()
    def get_type(self):
        infoType = self.sock.recv(5).decode()
        #print(infoType)
        if infoType == 'TYPE1':
            return 1
        elif infoType == 'TYPE2':
            return 2
        elif infoType == 'TYPE3':
            return 3
    def send_image(self):
        myfile = open("1.png", 'rb')
        bytes = myfile.read()
        size = len(bytes)
        tmsgHeader = "TYPE1"
        strsize = str(size).zfill(10)
        wholeM = tmsgHeader + strsize
        self.sock.sendall(wholeM.encode() + bytes)
    def send_txt(self):
        myfile = open("p.txt", 'rb')
        bytes = myfile.read()
        size = len(bytes)
        tmsgHeader = "TYPE2"
        strsize = str(size).zfill(10)
        wholeM = tmsgHeader + strsize
        #print("begin send")
        self.sock.sendall(wholeM.encode() + bytes)
    def send_apl(self):
        myfile = open("key.apl", 'rb')
        bytes = myfile.read()
        size = len(bytes)
        tmsgHeader = "TYPE3"
        strsize = str(size).zfill(10)
        wholeM = tmsgHeader + strsize
        print("begin send")
        self.sock.sendall(wholeM.encode() + bytes)
    def get_pid(self):
        msg = self.sock.recv(10)
        pid = int(msg)
        return pid

    #def send_test_1(self):
    #    tmsgHeader = "TYPE1"
    #    tmsg = tmsgHeader.encode()
    #   info = "dwadwdwadwadfsteetetsgef"
    #    size = len(info)
    #    strsize = str(size).zfill(10)
     #   print("I send{0} len:{1}".format(tmsg, size))
      #
        # wholeM = tmsgHeader + strsize  + info
        #self.sock.sendall(wholeM.encode())
    #def send_test_2(self):
        #tmsgHeader = "TYPE2"
        #tmsg = tmsgHeader.encode()
        #size = len(tmsg)
        #info = "56465468354185641.6854"
        #size = len(info)
        #strsize = str(size).zfill(10)
        #print("I send{0} len:{1}".format(tmsg, size))
       # wholeM = tmsgHeader + strsize + info
        #self.sock.sendall(wholeM.encode())
    def close(self):
        self.sock.close()
        self.s.close()















#s=socket.socket()     #生成一个管道
   # s.bind(("0.0.0.0",7777))    #开启管道监听
   # s.listen(1)     #选择接受的管道连接的个数
    #sock,addr=s.accept()  #接收对方的地址
    #while 1:
      #  command=sock.recv(1024).decode()  #接收，解码
       # print("来自远程连接的命令:{0}".format(command))
       # if command=="exit":
       #     break
       # result=os.popen(command).read()  #在系统中执行客户端发来的命令并读
       # sock.send(result.encode())  #读出来的执行结果发给客户端并加密
   # sock.close()
   # s.close()