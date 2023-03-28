import pandas as pd
from glob import glob
from pathlib import Path
import numpy as np
import h5py

path= '/workspace/hpv_project/roi_feter_aftr_filter_6/TCGA-CV-5443-01Z-00-DX1.h5'
slide=path.split('/')[-1].split('.')[0]
with h5py.File(path, 'r') as f:
    data = f['coords']
    print(f.keys())
    data_record = {'coords':[]}
    for i in range(len(data)):
    	data1= data[i]
    	data1=data1.tolist()
    	print(data1)
    	data_record['coords'].append(data1)
df = pd.DataFrame(data_record)
    	#csv_file=slide+'.csv'
df.to_csv('testing_file_before.csv', index=False)

