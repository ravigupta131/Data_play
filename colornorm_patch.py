import openslide as op
import pandas as pd
import glob
import cv2
import os
# import TiffImagePlugin
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from histomicstk.preprocessing.color_normalization.deconvolution_based_normalization import deconvolution_based_normalization
cn_img_dir='/workspace/DA_fhist/fhist_dataset/NCT_Target'
W_target = np.array([[0.5807549,  0.08314027,  0.08213795],[0.71681094,  0.90081588,  0.41999816],[0.38588316,  0.42616716, -0.90380025]])
image_list= pd.read_csv('/workspace/data_tgt_all.csv')
path = image_list['path']
# print(path[0])

for i in range(len(path)):
    image_path= path[i]
    img = Image.open(image_path)
    img_rgb=img.convert('RGB')
    img_np=np.array(img_rgb)
    path_l = image_path.split('/')[5:8]
    # print(path_l)
    if path_l[1]=='Tumor':
        print(f'class {path_l[1]} and image {path_l[2]} is preprocessing')
        img_cn = deconvolution_based_normalization(img_np, W_target=W_target)
        print(f'class {path_l[1]} and image {path_l[2]} is done')
        cn_folder_name =path_l[0]+'_cn'
        after_cn = os.path.join(cn_folder_name,path_l[1],path_l[2])
        name= os.path.join(cn_img_dir,after_cn)
        # print(f'name is {name}')
        plt.imsave(name,img_cn,format='TIFF')
    
    
print(' color normalization is done data_src') 