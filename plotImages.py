import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import scipy.ndimage as ndimage

info = pd.read_csv('Info.csv')
info = info[1:]
info.reset_index(inplace=True, drop=True)
info['fname'] = 'Images/' + info['Comment'] + '-' + info['Lens magnification'].astype(int).astype(str) + 'X-Image.png'

info['Material'] = info['Comment'].apply(lambda x: x.split('-')[0])
info['Location'] = info['Comment'].apply(lambda x: int(x.split('-')[2]))
info['Magnification'] = info['Lens magnification'].astype(int)


materials = set(info['Comment'].apply(lambda x: x.split('-')[0]))
mags = sorted(list(set(info['Lens magnification'].astype(int))))

labels = [('304 SS', '304'), ('316 SS', '316'), ('Ag Plated\n316 SS', 'SP316'), ('Molybdenum', 'Mo'), ('Tungsten', 'W'), ('Alumninum Bronze', 'AB'), ('Inconel 625', '625')]
sorter1 = [i[1] for i in labels]
sorter2 = mags

for material in materials:
    for location in range(1,4):
        aspect = 3*1.305/2
        height = 6
        fig = plt.figure(figsize=(aspect*height, height))
        gs = GridSpec(2, 6, hspace=0., wspace=0.)

        axs = [gs[0, 0:2], gs[0, 2:4], gs[0, 4:6], gs[1, 1:3], gs[1, 3:5]]
        scale = [500, 200, 100, 50, 10]

        for n,mag in enumerate(mags):
            temp = info[(info['Material'] == material) & (info['Location'] == location) & (info['Magnification'] == mag)]
            ax = fig.add_subplot(axs[n])
            ax.axis('off')
            ax.text(20, 20, f'{mag}X', va='top', ha='left', fontsize=16, bbox={'fc':'w'})
            ax.text(971, 668, f'{scale[n]:3.0f} $\mu m$', va='top', ha='right', fontsize=10, bbox={'fc':'w'})
            im = plt.imread(temp['fname'].values[0])
            ax.imshow(im)

        fig.tight_layout()
        plt.savefig(f'Compiled/{material}-{location}.png', dpi=300, transparent=True)
        plt.close()

material = 'SP316'
aspect = 3*2.21/2
height = 5


#for location in range(1,4):
#    fig = plt.figure(figsize=(aspect*height, height))
#    gs = GridSpec(2, 5, hspace=0, wspace=0)
#    scale = [500, 200, 100, 50, 10]
#    for n, mag in enumerate(mags):
#        temp = info[(info['Material'] == material) & (info['Location'] == location) & (info['Magnification'] == mag)]
#        ax = fig.add_subplot(gs[0,n])
#        ax.axis('off')
#        ax.text(20, 20, f'{mag}X', va='top', ha='left', fontsize=16, bbox={'fc':'w'})
#        #ax.text(971, 668, f'{scale[n]:3.0f} $\mu m$', va='top', ha='right', fontsize=10, bbox={'fc':'w'})
#        im = plt.imread(temp['fname'].values[0])
#        ax.imshow(im)
#        ax = fig.add_subplot(gs[1,n])
#        ax.axis('off')
#        #ax.text(20, 20, f'{mag}X', va='top', ha='left', fontsize=16, bbox={'fc':'w'})
#        #ax.text(971, 668, f'{scale[n]:3.0f} $\mu m$', va='top', ha='right', fontsize=10, bbox={'fc':'w'})
#        im = plt.imread(temp['fname'].values[0].replace('Image', 'NavImage').replace('NavImages', 'NavigationImages').replace('.png', '.jpg'))
#        im = ndimage.rotate(im, 90, reshape=True)                                                  
#        im = im[200:300, 300:450]
#        ax.imshow(im)
#    #plt.show()
#    plt.savefig(f'Compiled/Location-{location}.png', dpi=300, transparent=True)

location = 2
mag = 20

aspect = 4*1.305/2
height = 5
scale = [500, 200, 100, 50, 10]

for location in range(1,4):
    for mag in mags:
        fig = plt.figure(figsize=(aspect*height, height))
        gs = GridSpec(2, 8, hspace=0, wspace=0)
        axs = [gs[0, 0:2], gs[0, 2:4], gs[0,4:6], gs[0,6:8], gs[1, 1:3], gs[1,3:5], gs[1,5:7]]
        for n, (label, material) in enumerate(labels):
           temp = info[(info['Material'] == material) & (info['Location'] == location) & (info['Magnification'] == mag)]
           ax = fig.add_subplot(axs[n])
           ax.axis('off')
           im = plt.imread(temp['fname'].values[0])
           ax.imshow(im)
           ax.text(30, 30, label, va='top', ha='left', fontsize=16, bbox={'fc':'w'})
        plt.savefig(f'Compiled/All-Location{location}-Mag{mag}.png', dpi=300, transparent=True) 

