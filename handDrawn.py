#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import imageio
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

def drawImage():
    # import image
    image_path = "me.png"
    image = imageio.imread(image_path)
    
    # turn the image grayscale
    grayscale_image = grayscale(image)
    
    # invert the image
    inverted_image = invert(grayscale_image)
    
    blur_image = blur(inverted_image)
    
    final_image= dodge(blur_image, grayscale_image)
    
    # plot the result
    plt.imshow(final_image, cmap='gray')

# method to turn an image grayscale
def grayscale(image): 
    return np.dot(image[...,:3], [0.299, 0.587, 0.114])

# method to invert images
def invert(grayscale_image):
    # subtract from 255, as grayscale images are 8 bit images or have a maximum of 256 tones.
    return 255 - grayscale_image

# method to blur image
def blur(image):
    # apply gaussian filter
    # higher sigma means more blur
    return scipy.ndimage.filters.gaussian_filter(image, sigma = 12)

# method to color dodge (highlights the boldest edges)
def dodge(front, back):
    result=front * 255 / (255 - back)
    result[result > 255] = 255 
    result[back == 255] = 255
    return result.astype('uint8')

def main():
    drawImage()

if __name__ == "__main__":
    main()


