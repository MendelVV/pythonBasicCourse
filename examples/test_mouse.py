import pyautogui as pag
import time
from get_balls import getT

def setType(type, pos):
    global start_x, start_y
    x_type = start_x
    y1 = start_y
    if type=='nan' or type=='у':
        type = '-1'
    type = float(type.replace(',','.'))
    if type == 0:
        y1+=22
    elif type == -1:
        y1+=44

    pag.click(x_type, y1)
    time.sleep(0.3)
    pag.moveTo(x=pos.x, y=pos.y)


def click(gr, col):
    a = getT(gr, col)
    #print(a)
    #return
    for i in range(len(a) - 1):
        pos = pag.position()
        if i == 0:
            setType(a[i], pos)
        elif a[i - 1] != a[i]:
            setType(a[i], pos)

        pag.click()
        pag.move(0, 22)
        time.sleep(0.2)


def start(gr, cols):
    time.sleep(2)
    for s in cols:
        time.sleep(2)
        click(gr, s)


start_x = 665
start_y = 500+25+25

start('ПОАК(б)-11', ['AE','AO'])
#pag.mouseInfo()
