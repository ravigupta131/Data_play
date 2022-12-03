import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


csv1= pd.read_csv('/workspace/DA_fhist/data_tgt_all.csv')
#print(csv1)
x= csv1['path']
y= csv1['label']


x_train, x_test, y_train, y_test= train_test_split(x, y, stratify=y, test_size=0.3)

train=[x_train,y_train]
train_data = pd.concat(train, axis=1)

train_data.to_csv('data-tgt-train_list.txt', sep=(' '), index=False)

test=[x_test,y_test]
test_data = pd.concat(test, axis=1)

test_data.to_csv('data-tgt-test_list.txt', sep=(' '), index=False)




        
