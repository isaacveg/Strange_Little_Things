from threading import Timer
import pyautogui
# 没有上面的库的话install一个

def playgame():
    pyautogui.typewrite('kkkkkk')
    # 上面这行的括号里面换成你要输入的文字，比如jiaran，kuaikuaikuaikuai
    pyautogui.press('space')
    pyautogui.press('enter')


def loop_func(func, second):
    cnt = 0
    # 下面的20可以换成你想要的数字，重复多少遍
    while cnt < 20:
        timer = Timer(second, func)
        cnt += 1
        timer.start()
        timer.join()


pyautogui.click((1145, 807))
pyautogui.click((1145, 807))
# 上面两行数字换成你要输入的输入框在屏幕上的位置
loop_func(playgame, 0.1)
# 上面的数字换成你想要的时间间隔，比如0.5秒发一条
