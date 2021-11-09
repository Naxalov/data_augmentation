import albumentations as A
import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from utils.plots import plot_grid,plot
# plot_images, plot_images_grid, plot_images_grid_with_labels,plot_images_with_mask
# Declare an augmentation pipeline
transform = A.Compose([
    #Add crop augmentation

    #Add random crop to the image
    A.RandomCrop(width=256, height=256, p=1.0),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
])

#Create a function to load an image
def load_image(img_list:list)->list:
    """Read an image from a file path (JPEG or PNG).

    Args:
        path ([type]): path to the image file

    Returns:
        [list]: returns a list of images
    """
    #Read all the images in the list
    images = []
    for img_path in img_list:
        img = cv2.imread(str(img_path))
        #Check if the image is read correctly
        if img is None:
            print('Failed to read image: {}'.format(path))
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #Add the image to the list
        images.append(img)
    return images

   

#Assign the path to the varaible images_path
images_path = Path('images')
#Create a list of all the images in the images_path
images_list = list(images_path.glob('*'))

#Call the load_image function to load the images
images = load_image(images_list)
#Assign img to the first image in the list
img = images[0]
# Augment an image
#Create a empty list
images = []
#Append the transformed image to the list
#using for loop with TQDM to show progress.
for i in range(15):
    #Apply the transformation to the image
    augmented = transform(image=img)['image']
    #Append the transformed image to the list
    images.append(augmented)




#Plot the batch of images
plot_grid(images, n_cols=5, n_rows=3,save_path='augmented_images.png')
