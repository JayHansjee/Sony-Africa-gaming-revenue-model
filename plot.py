import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def tornado_plot(ts, base):
    ts = ts.set_index('assumption')
    high = ts.iloc[:,0]
    low = ts.iloc[:,1]

    y_labels = ts.index
    ys = range(len(y_labels))[::-1]
    height = 0.8

    plt.figure(figsize=(6.5,8))
    colour_low = '#0d47a1'
    colour_high = '#e2711d'
    colour_line = '#2ECC71'


    for y, value in zip(ys, low):
        plt.broken_barh([(base, value)], (y - height/2,height), facecolors=[colour_low,colour_low])


    for y, value2 in zip(ys, high):
        plt.broken_barh([(base, value2)], (y - height/2, height),facecolors=[colour_high,colour_high])


    plt.axvline(base, color=colour_line, linewidth=1.5, label='Base Case')



    plt.ylim(-0.5, 19)
    plt.yticks(ys, y_labels)
    plt.grid(linewidth=0.1, color='black')
    plt.xlabel('Revenue, millions of dollars', fontsize=12, fontweight='bold')



    plt.show()
    return
