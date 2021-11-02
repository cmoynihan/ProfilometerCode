import pandas as pd
import time
import pyautogui as pag
from locations import *

location = locations[tuple(pag.size())]

info = pd.read_csv('Info.csv')
info = info[1:]
info.reset_index(inplace=True, drop=True)
for i in range(len(info)):
    fname = f"{info.loc[i, 'Comment']}-{info.loc[i, 'Lens magnification']:.0f}X-Height"
    pag.moveTo(location['File'])
    pag.click(location['File'])
    if i == 0:
        pag.click(location['File'])
    pag.click(location['Export'])
    pag.click(location['Output'])
    pag.click(location['Type'])
    pag.click(location['Ok'])
    pag.write(fname)
    pag.click(location['Save'])
    pag.press('down')
