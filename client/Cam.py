import cv2
import time

def function_cam():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 打开摄像头

    while (1):
        time.sleep(0.1)
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1) # 摄像头是和人对立的，将图像左右调换回来正常显示
        # show a frame
        cv2.imwrite("1.png", frame) # 保存路径


    cap.release()
    cv2.destroyAllWindows()