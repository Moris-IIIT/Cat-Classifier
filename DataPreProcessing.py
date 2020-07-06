'''
Author : S.Moris IIIT Dharwad
This program is a trial to import all the images and flatten them to a numoy array
and save the image vector as a.csv file.
'''
from skimage.io import imread_collection,concatenate_images
import pandas as pd
import numpy as np
import cv2
import glob
# Collection directory :
directory_train="Data/train/*.png"
directory_test="Data/test/*.png"
# Importing Images : Creating a collection
test=np.array([cv2.imread(file) for file in glob.glob(directory_test)])
train=np.array([cv2.imread(file) for file in glob.glob(directory_train)])
# Converting and flattening images : Using numpy
test_data=[]
train_data=[]
for i in range(len(test)):
    #print(i)
    arr=test[i].flatten()
    test_data.append(arr)
for i in range(len(train)):
    arr=train[i].flatten()
    train_data.append(arr)    
test_data=np.asarray(test_data)
train_data=np.asarray(train_data)
#np.savetxt('test.csv',test_data,delimiter=',')
#np.savetxt('train.csv',train_data,delimiter=',')
