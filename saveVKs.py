import pandas as pd
import time
import pyautogui as pag
from locations import *

location = locations[tuple(pag.size())]

info = pd.read_csv('../temp.csv', usecols=[5], skiprows=2, names=['file'])

# info = pd.read_csv('Info.csv')
# info = info[1:]
# info.reset_index(inplace=True, drop=True)
#jjfor i in range(len(info)):
for i, file in enumerate(info['file'].array):
    #fname = f"{info.loc[i, 'Comment']}-{info.loc[i, 'Lens magnification']:.0f}X-Height"
    pag.moveTo(location['File'])
    pag.click(location['File'])
    if i == 0:
        pag.click(location['File'])
    pag.click(location['Export'])
    pag.click((location['Output'][0], location['Output'][1]+30))
    pag.click(location['Type'])
    pag.click(location['Ok'])
    pag.write(file)
    pag.click(location['Save'])
    pag.press('down')
