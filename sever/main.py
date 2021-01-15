# -*- coding: utf-8 -*-

from GUI import *
from connect import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 创建窗口
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    MyConnection = connection("127.0.0.1", 0)
    window = MainWindow()
    newWinOne = NewWindow()
    newWinTwo = NewWindow()
    newWinThree = NewWindow()

    window.buttomOne.clicked.connect(lambda: on_click_buttom_one(window, MyConnection))
    window.buttomTwo.clicked.connect(lambda: on_click_buttom_two(window, newWinOne, MyConnection))
    window.buttomThree.clicked.connect(lambda: on_click_buttom_three(newWinTwo, MyConnection))
    window.buttomFour.clicked.connect(lambda: on_click_buttom_four(newWinThree, MyConnection))
    window.show()
    sys.exit(app.exec_())