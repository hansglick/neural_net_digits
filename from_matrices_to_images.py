# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 21:58:52 2017

@author: Bar Yokhai
"""
# IMPORT LIBRARIES
import scipy.io as spio
import numpy as np
from PIL import Image
import PIL.ImageOps
import os

# * * * * * * * * * * * BEGIN PARAMETERS * * * * * * * * * * * * *  
foldername='C:\\SERGE\\neuralnet\\'
filename='ex4data1.mat'
# * * * * * * * * * * * END PARAMETERS * * * * * * * * * * * * * 


# IMPORT DATA
mat = spio.loadmat(foldername+filename, squeeze_me=True)

# EXTRACT D MATRIX AS STACK OF INTENSITY 400 LENGTH VECTOR
# WHICH REPRESENT IMAGES
# EXTRACT Y VECTOR AS LABELS
d=mat["X"]
y=mat["y"]


# CREATE IMAGE SUBFOLDER OF FOLDERNAME PARAMETER
output_folder = foldername+'image_digits_original_size\\'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output2_folder = foldername+'image_digits_bigger_size\\'
if not os.path.exists(output2_folder):
    os.makedirs(output2_folder)

# BUILDING AND SAVING IMAGES
for index,picture in enumerate(d): 
    im = Image.fromarray(picture.reshape((20,20))*255).convert('RGB').transpose(Image.FLIP_TOP_BOTTOM).rotate(270)
    im=PIL.ImageOps.invert(im)
    imagename="image"+str(index).zfill(3)+"_label_"+str(y[index])+".jpg"
    # save image in original dimensions 20 x 20    
    im.save(output_folder+imagename)
    # save in bigger dimensions 200 x 200
    bigim = im.resize((200, 200), Image.ANTIALIAS)
    bigim.save(output2_folder+imagename)
    


# * * * * * * * * * *  DRAFTS  * * * * * * * * * * * * * * * * 

# tircks : HOW TO READ A PYTHON PIL IMAGE
# import pylab as pl
# pl.imshow(im)

# test :
# im = Image.fromarray(d[1139].reshape((20,20))*255).convert('RGB')
# im=PIL.ImageOps.invert(im)
# im = im.resize((200, 200), Image.ANTIALIAS)
# im.save(foldername+"results.jpg")

# im = Image.fromarray(d[1139].reshape((20,20))*255).convert('RGB')
# im=PIL.ImageOps.invert(im)
# im = im.resize((200, 200), Image.ANTIALIAS).transpose(Image.FLIP_TOP_BOTTOM).rotate(270)
# pl.imshow(im)
# im.save(foldername+"results.jpg")

# * * * * * * * * * *  DRAFTS  * * * * * * * * * * * * * * * * 






