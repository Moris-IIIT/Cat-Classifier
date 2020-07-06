from skimage.io import imread_collection,concatenate_images
import pandas as pd
import numpy as np
# Collection directory :
directory_train="Data/train/*.png"
directory_test="Data/test/*.png"
# Importing Images : Creating a collection
train_data=imread_collection(directory_train)
test_data=imread_collection(directory_test)
# Converting to array