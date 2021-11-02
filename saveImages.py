import pandas as pd
import time
import pyautogui as pag
from locations import *

location = locations[tuple(pag.size())]

info = pd.read_csv('Info.csv')
info = info[1:]
info.reset_index(inplace=True, drop=True)
for i in range(len(info)):
    fname = f"{info.loc[i, 'Comment']}-{info.loc[i, 'Lens magnification']:.0f}X-Image"
    if i == 0:
        pag.click(location['File'])
    if i == 0:
        pag.click(location['0'], clicks=2)
    elif i == 1:
        pag.click(location['1'], clicks=2)
    elif i == 2:
        pag.click(location['2'], clicks=2)
    else:
        pag.click(location['else'], clicks=2)
    pag.click(location['Save...'])
    pag.write(fname)
    pag.press('enter')
    pag.press('tab')
    pag.press('enter')
    pag.press('down')
