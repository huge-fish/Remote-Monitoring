from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import threading
import time
from process import *
import reg
import pickle
import string


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('TestWindow')
        self.resize(400, 300)
        #按钮
        self.buttomOne = QPushButton('开放端口', self)
        self.buttomOne.setGeometry(QtCore.QRect(250, 87, 100, 28))
        self.re_le = QLineEdit(self)  # 正则文本框
        self.re_le.move(50, 90)
        #按钮2
        self.buttomTwo = QPushButton('断开连接', self)
        self.buttomTwo.setGeometry(QtCore.QRect(250, 120, 100, 28))

        #标签
        self.label1 = QLabel(self)
        self.label1.setText('未连接')
        # 标签1的背景填充更改为True，否则无法显示背景
        self.label1.setAutoFillBackground(True)
        # 实例化背景对象，进行相关背景颜色属性设置
        palette = QPalette()
        palette.setColor(QPalette.Window, QtCore.Qt.blue)
        # 标签1加载背景
        self.label1.setPalette(palette)
        # 设置文本居中显示
        self.label1.setAlignment(QtCore.Qt.AlignCenter)

        self.show()
    def get_line_one_text(self):
        return self.re_le.text()
    def set_lable_one(self):
        self.label1.setText("已连接")
    def set_lable_one_two(self):
        self.label1.setText("未连接")
    def msg_one(self):
        QMessageBox.information(self, '错误', '错误的端口', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    def msg_two(self):
        reply = QMessageBox.information(self, '提示', '是否同意连接', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            return True
        else:
            return False
    def msg_three(self):
        QMessageBox.information(self, '提示', '成功断开连接', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('新窗口')
        self.resize(800, 600)
    def init_UI_shell(self): #shell的UI
        self.input_command = QLineEdit(self)
        self.output_result = QTextEdit(self)
        self.output_result.setGeometry(QtCore.QRect(50, 120, 400, 300))
        self.input_command.move(50, 90)
        self.show()
        #self.input_command.returnPressed()
    def input_get(self):
        return self.input_command.text()
    def input_clean(self):
        self.input_command.setText("")
    def append_output(self, Shell_result):
        self.output_result.moveCursor(QTextCursor.End)
        self.output_result.append(Shell_result)

def t1_wait_connection(MyConnection):
    #MyConnection.wait_connect()
    while True:
        if MyConnection.allow == 0:
            return
            #MyConnection.send_test_1()
        #MyConnection.send_test_2()
        time.sleep(0.2)
        MyConnection.send_image()
        get_all_info()
        MyConnection.send_txt()
        with open("key.apl",'wb') as pf:
            pf.seek(0)
            pf.truncate()
            pickle.dump(reg.get_log_data(), pf)
        #reg.list_app = []
        MyConnection.send_apl()
        #MyConnection.sned_test()
    MyConnection.close()

def keylog_thread():
    reg.begin_listen()

def t2_reveice(MyConnection):
    t3target = 0
    while 1:
        if MyConnection.allow == 0:
            return
        typeinfo = MyConnection.get_type()
        if typeinfo == 1:
            pid = MyConnection.get_pid()
            kill_p(pid)
        elif typeinfo == 2:
            reg.list_app = []
            if t3target == 0:
                t3target = 10
                t3 = threading.Thread(target=keylog_thread)
                t3.start()
        elif typeinfo == 3:
            pass



def on_click_buttom_one(MainW, MyConnection):
    try:
        MyConnection.port = int(MainW.get_line_one_text())
    except Exception as e:
        MainW.msg_one()
        return
    if MainW.msg_two():
        MyConnection.allow = 1
    else:
        MyConnection.allow = 0
    print(MyConnection.allow)
    MyConnection.start()
    MyConnection.wait_connect()
    MainW.set_lable_one()
    t1 = threading.Thread(target=t1_wait_connection, args=(MyConnection, ))
    t2 = threading.Thread(target=t2_reveice, args=(MyConnection, ))
    t1.start()
    t2.start()

def on_click_buttom_two(MainW, MyConnection):
    MyConnection.close()
    MainW.set_lable_one_two()


