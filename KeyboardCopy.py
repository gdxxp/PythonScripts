from time import sleep
from pynput.keyboard import Controller
import keyboard
import win32clipboard as w
import win32con
import sys

global legal


def get_text():
    global legal, d
    w.OpenClipboard()
    try:
        d = w.GetClipboardData(win32con.CF_TEXT)
        legal = 1
    except:
        print("=====================剪切板内容含图片等非文字!!!=====================")
        print("=========================请重新复制后再粘贴=========================")
        print()
        print()
        legal = 0
    w.CloseClipboard()
    if legal == 1:
        return d.decode('GBK')
    else:
        return ''  # 创建键盘对象


def main():
    kd = Controller()

    print('''=============================使用注意事项以及使用说明===================================  
                   软件功能：将粘贴板复制的文字内容模拟键盘打出来，而不是简单的复制粘贴。                        
                   使用流程：（1）将需要输入的文本（只能为文字）内容复制到剪切板,且将输入法改为英文输入法  
                           （2）摁<-键开始,摁q退出程序  
                           （3）将光标放到输入框内即可                                            ''')
    print("====================================================================================")
    while True:  # 读取剪切板内容
        if keyboard.read_event().name == 'q':
            sys.exit()
        elif keyboard.read_event().name == 'left':
            ss = get_text()
            if legal == 1:
                ss = ss.replace('', '')
                print("=========================3秒后开始粘贴任务=============================")
                i = 3
                while i:
                    print('==================倒计时', i, '请将光标点击到输入框==================')
                    sleep(1)
                    i -= 1
                kd.type(ss)
                print('========================已完成剪切板内容输入========================')
                print("=========================按left可继续使用========================")
                print("============================感谢使用============================")


if __name__ == '__main__':
    main()
