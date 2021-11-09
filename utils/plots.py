#Import libraries
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path



#Create a function visualize a image using matplotlib
def plot(img):
    plt.imshow(img)
    plt.show()
#Create a visualization function for a batch of images
def plot_grid(images, n_cols=2, n_rows=2,save_path=None):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols*4, n_rows*4))
    for i in range(n_rows):
        for j in range(n_cols):
            axes[i,j].imshow(images[i*n_cols+j])
            axes[i,j].axis('off')
    
    #Show the plot without hspace and wspace
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.tight_layout()
    # plt.show(block=False)
    #Save the plot if a path is provided otherwise show the plot
    if save_path is not None:
        plt.savefig(save_path)
    else:
        plt.show()

