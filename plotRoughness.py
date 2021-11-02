import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

info = pd.read_csv('Info.csv')
info = info[1:]
info.reset_index(inplace=True, drop=True)

roughness = pd.read_csv('Roughness.csv', skiprows=2, usecols=range(3, 28))
roughness = roughness[1:]
roughness = roughness.astype(np.float64)
roughness.reset_index(inplace=True, drop=True)

materials = set(info['Comment'].apply(lambda x: x.split('-')[0]))

mags = sorted(list(set(info['Lens magnification'].astype(int))))

full = roughness.copy()
full['Material'] = info['Comment'].apply(lambda x: x.split('-')[0])
full['Location'] = info['Comment'].apply(lambda x: int(x.split('-')[2]))
full['Magnification'] = info['Lens magnification'].astype(int)

results = pd.DataFrame(columns=['Material','Magnification', 'Sa', 'Sa Err', 'Sz', 'Sz Err'])

for material in materials:
    for mag in mags:
        temp = full[(full['Material'] == material) & (full['Magnification'] == mag)]
        data = [material, mag, temp['Sa'].mean(), temp['Sa'].std(), temp['Sz'].mean(), temp['Sz'].std()]
        results.loc[len(results), :] = data

each = len(mags)
total = len(mags)*len(materials)
labels = [('304 SS', '304'), ('316 SS', '316'), ('Ag Plated\n316 SS', 'SP316'), ('Molybdenum', 'Mo'), ('Tungsten', 'W'), ('Alumninum\nBronze', 'AB'), ('Inconel 625', '625')]
sorter1 = [i[1] for i in labels]
sorter2 = mags
def sorter(column):
    if isinstance(column[0], type(1)):
        return column.apply(lambda x: sorter2.index(x))
    else:
        return column.apply(lambda x: sorter1.index(x))

results.sort_values(by=['Material', 'Magnification'] , key=sorter, inplace=True)
results.reset_index(inplace=True, drop=True)

xlocs = np.arange(each/2, len(materials)*each + len(materials)*1 + 1, each+1)
xpos = np.array(range(total+len(materials)))
skip = xpos[5::6]
xpos = np.delete(xpos, skip)

cmap = {5: 'tab:blue', 10: 'tab:orange', 20:'tab:green', 50:'tab:red', 150:'tab:purple'}
results['color'] = results['Magnification'].map(cmap)

fig, ax = plt.subplots(figsize=(8,6))
b = ax.bar(xpos, results['Sa'], color=results['color'], yerr=results['Sa Err'], capsize=3)
ax.set_xticks(xlocs)
ax.set_xticklabels([i[0] for i in labels], rotation=45, ha='right', fontsize=14)
ax.set_ylabel('$S_a\ [\mu m]$', fontsize=16)
ax.set_yscale('log')
ax.legend(b.patches[:5], ['5X', '10X', '20X', '50X', '100X'])
plt.tight_layout()
plt.savefig('Compiled/Sa-All.png', dpi=300, transparent=True)

fig, ax = plt.subplots(figsize=(8,6))
b = ax.bar(xpos, results['Sz'], color=results['color'], yerr=results['Sz Err'], capsize=3)
ax.set_xticks(xlocs)
ax.set_xticklabels([i[0] for i in labels], rotation=45, ha='right', fontsize=14)
ax.set_ylabel('$S_z\ [\mu m]$', fontsize=16)
ax.set_yscale('log')
ax.legend(b.patches[:5], ['5X', '10X', '20X', '50X', '100X'])
plt.tight_layout()
plt.savefig('Compiled/Sz-All.png', dpi=300, transparent=True)

results = results[(results['Magnification'] == 50) | (results['Magnification'] == 150)]

each = 2
total = 2*7

xlocs = np.arange(each/2, len(materials)*each + len(materials)*1 + 1, each+1)
xpos = np.array(range(total+len(materials)))
skip = xpos[2::3]
xpos = np.delete(xpos, skip)

fig, ax = plt.subplots(figsize=(8,6))
b = ax.bar(xpos, results['Sa']*1000, color=results['color'], yerr=results['Sa Err']*1000, capsize=3)
ax.set_xticks(xlocs)
ax.set_xticklabels([i[0] for i in labels], rotation=45, ha='right', fontsize=14)
ax.set_ylabel('$S_a\ [nm]$', fontsize=16)
ax.legend(b.patches[:2], ['50X', '100X'])
plt.tight_layout()
plt.savefig('Compiled/Sa.png', dpi=300, transparent=True)

fig, ax = plt.subplots(figsize=(8,6))
b = ax.bar(xpos, results['Sz']*1000, color=results['color'], yerr=results['Sz Err']*1000, capsize=3)
ax.set_xticks(xlocs)
ax.set_xticklabels([i[0] for i in labels], rotation=45, ha='right', fontsize=14)
ax.set_ylabel('$S_z\ [nm]$', fontsize=16)
ax.legend(b.patches[:2], ['50X', '100X'])
plt.tight_layout()
plt.savefig('Compiled/Sz.png', dpi=300, transparent=True)
