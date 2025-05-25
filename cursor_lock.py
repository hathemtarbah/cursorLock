from screeninfo import get_monitors
import pyautogui
import time

monitor = get_monitors()[0] #because monitor 0 is (usually) primary

left = monitor.x
top = monitor.y
right = left + monitor.width
bottom = top + monitor.height

while True:

    x, y = pyautogui.position()

    if x < left:
        x = left
    elif x > right - 1:
        x = right -1
    if y < top:
        y = top
    elif y > bottom - 1:
        y = bottom - 1

    pyautogui.moveTo(x, y)
    time.sleep(0.01) #to lower cpu usage