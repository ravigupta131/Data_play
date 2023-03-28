import pandas as pd
from glob import glob
from pathlib import Path
import numpy as np


df = pd.read_pickle('/workspace/clam1/CLAM/results_roi_hpv/100_sb_4split_c/roi_e-class_CLAM_100_s1/split_1_results.pkl')
new = pd.DataFrame.from_dict(df)
print(new.T)
    

