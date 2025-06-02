import matplotlib.pyplot as plt
import numpy as np

def setup_axis(ax,grid,cp=False):
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)
        if(cp):
            spine.set_color('w')
    ax.tick_params(which='both',direction='in',top=True,right=True,length=7,width=1.5,labelsize=14)
    ax.tick_params(which='minor',length=4)
    ax.minorticks_on()
    if(grid):
        ax.grid(which='both',alpha=0.3)
        ax.grid(which='major',alpha=0.3)
    return

def pretty_axis(ax,grid=True,cp=False):
    if(type(ax)==np.ndarray):
        if(ax.ndim==1):
            for subax in ax:
                setup_axis(subax,grid,cp=cp)
        else:
            for subax_array in ax:
                for subax in subax_array:
                    setup_axis(subax,grid,cp=cp)
    else:
        setup_axis(ax,grid,cp=cp)
    return
