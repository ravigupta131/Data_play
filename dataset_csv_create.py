import os
import pandas as pd

top = '/workspace/lung_data/adeno_tcga/full_data'

# data_record = {'path':[],'n_label':[], 'label':[]}
data_record = {'path':[], 'slide_name':[]}
for root, directories, files in os.walk(top, topdown=False):
    for name in files:
        #print(f' root is {root}')
        #print(f'name is {name}')
        data_record['slide_name'].append(name)
        data_record['path'].append(os.path.join(root, name))
        # data_record['n_label'].append(root.split('/')[-1])
        #data_record['label'].append(root.split('/')[-1])

df = pd.DataFrame(data_record)

#df.label[df.label=='Benign']=0
#df.label[df.label=='Stroma']=1
#df.label[df.label=='Tumor']=2
#df.label[df.label=='Debris']=3
#df.label[df.label=='Inflammatory']=4
#df.label[df.label=='Muscle']=5

# df.n_label[df.n_label=='Benign']=0
# df.n_label[df.n_label=='Stroma']=1
# df.n_label[df.n_label=='Tumor']=2
# df.n_label[df.n_label=='Debris']=3
# df.n_label[df.n_label=='Inflammatory']=4
# df.n_label[df.n_label=='Muscle']=5


df.to_csv('tcga_adeno_lung.csv', sep=',', index=False)
#df.to_csv('data-tgt-all_list.txt', columns=header, index=False)

        
