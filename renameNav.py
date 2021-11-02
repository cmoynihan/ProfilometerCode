import pandas as pd
import os

info = pd.read_csv('Info.csv')
info = info[1:]
info.reset_index(inplace=True, drop=True)

for i in range(len(info)):
    comment = info.loc[i, 'Comment']
    old = '-'.join(comment.split('-')[:2]) + f"-{info.loc[i, 'Lens magnification']:.0f}X-" + comment.split('-')[2] + '.jpg'
    fname = f"{info.loc[i, 'Comment']}-{info.loc[i, 'Lens magnification']:.0f}X-NavImage.jpg"
    os.rename(f'NavigationImages/{old}', f'NavigationImages/{fname}')
