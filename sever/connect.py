import socket

class connection:
    def __init__(self, ipAddr, port):
        self.ipAddr = ipAddr
        self.port = port
        self.MyFlag = 0
    def creat_link(self):
        self.connection = socket.socket()
        try:
            self.connection.connect((self.ipAddr, self.port))
            self.MyFlag = 1
        except Exception as e:
            self.connection = socket.timeout
        return self.connection
    def send_pid(self, sendmsg):
        print("I send msg1")
        msgHead = "TYPE1".encode()
        msg = str(sendmsg).zfill(10)
        self.connection.sendall(msgHead + msg.encode())
    def send_require(self):
        msgHead = "TYPE2".encode()
        self.connection.sendall(msgHead)
    def send_stop(self):
        print("msg3")
        msgHead = "TYPE3".encode()
        self.connection.sendall(msgHead)
    def get_type(self):
        try:
            infoTypeRaw = self.connection.recv(5)
            print('Rawtype:{0}'.format(infoTypeRaw))
            infoType =infoTypeRaw.decode()
            print(infoType)
        except ZeroDivisionError as e:
            with open("runlog.txt", 'w') as runlog:
                runlog.write(str(e))
                runlog.write('\n')
            self.MyFlag = 0
            self.close()
            return 4
        self.MyFlag = 1
        if infoType == 'TYPE1':
            return 1
        elif infoType == 'TYPE2':
            return 2
        elif infoType == 'TYPE3':
            return 3
    def get_length(self):
        Mylength = self.connection.recv(10)
        print("code:{0}".format(Mylength))
        print('type len{0}：'.format(type(Mylength)))
        print(int(Mylength))
        return int(Mylength)

    def get_re_test(self, Length):
        data = self.connection.recv(Length)
        print(data)
    def get_image(self, Length):

        #filename = "pic" + str(name) + ".png"
        myfile = open("1.png", 'wb')

        m = 1024
        n = Length % m
        filelen = Length

        i = 1
        while (filelen // m) :
            data = self.connection.recv(m)
            # print(i, ':', len(data))
            myfile.write(data)
            filelen -= len (data)
            i += 1
            # myfile.close()

        data = self.connection.recv(filelen)
        # print(i, ':', len(data))
        myfile.write(data)
        # print("finish")
        myfile.close()
        # data = self.connection.recv(Length)
        # print (data)
        # print (len (data))
        # print (type (data))
        # myfile.write(data)
        # myfile.close()
    def get_txt(self, Length):
        myfile = open("p.txt", 'wb')
        m = 1024
        n = Length % m
        filelen = Length

        i = 1
        while (filelen // m):
            data = self.connection.recv(m)
            # print(i, ':', len(data))
            myfile.write(data)
            filelen -= len(data)
            i += 1
            # myfile.close()

        data = self.connection.recv(filelen)
        # print(i, ':', len(data))
        myfile.write(data)
        # print("finish")
        myfile.close()
    def get_apl(self, Length):
        #print("I re")
        myfile = open("key.apl", 'wb')
        data = self.connection.recv(Length)
        myfile.write(data)
        myfile.close()
    def close(self):
        self.connection.close()
        #print("Success")
    #def get_test1(self,length):
     #   re = self.connection.recv(length).decode()
      #  print(re)

    #def get_test2(self, length):
     #   re = self.connection.recv(length).decode()
      #  print(re)
