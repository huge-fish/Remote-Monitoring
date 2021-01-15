from GUI import *
import sys
import Cam
import threading
from connect import *
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    newWin = NewWindow()
    MyConnection = connection("0.0.0.0", 0)
    t2 = threading.Thread(target=Cam.function_cam)
    t2.start()
    window.buttomOne.clicked.connect(lambda:on_click_buttom_one(window, MyConnection))
    window.buttomTwo.clicked.connect(lambda:on_click_buttom_two(window, MyConnection))
    #newWin = NewWindow()
    window.show()
    sys.exit(app.exec_())
