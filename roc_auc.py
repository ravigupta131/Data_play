'''

from sklearn import metrics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
result=pd.read_csv('/home1/ravi/Desktop/tutorial/result_older_modified.csv',index_col=False,)
result = result.dropna()

def take_p(x):
    x=x[:-12]
    return x

result['patient']=result['slide_name'].apply(take_p)

def get_prob(x):
    x=float(x.replace(']]','').replace('[[','').lstrip().rstrip().split(' ')[-1][:-2])
    return x

result['y_prob'] =result['y_pro'].apply(get_prob)

def map(x):
    if 'N' in x:
        x=0
    else:
        x=1
    return x

result['y_true'] = result['RNA_ISH'].apply(map)


# import matplotlib.pyplot as plt

# from sklearn.metrics import RocCurveDisplay

# RocCurveDisplay.from_predictions(result['y_prob'],result['y_true'],name=f"Positive vs Negative",color="darkorange",plot_chance_level=True,)
# plt.axis("square")
# plt.xlabel("False Positive Rate")
# plt.ylabel("True Positive Rate")
# plt.title("One-vs-Rest ROC curves:\nVirginica vs (Setosa & Versicolor)")
# plt.legend()
# plt.show()

'''


import pandas as pd
def take_p(x):
    x=x[:-12]
    return x

result['patient']=result['slide_name'].apply(take_p)

data = pd.read_csv('/home1/ravi/Desktop/tutorial/result_older_modified.csv')

def map(x):
    if 'N' in x:
        x=0
    else:
        x=1
    return x

data['y_true'] = data['RNA_ISH'].apply(map)
#print(data['y_true'].dtypes)

def get_prob(x):
    x=float(x.replace(']]','').replace('[[','').lstrip().rstrip().split(' ')[-1][:-2])
    #print(f'x is {x}')
    return x

data['y_prob'] =data['y_pro'].apply(get_prob)

y_true= data['y_true']
y_scores = data['y_prob']
print(f' type of y_true and y_scores is {type(y_true)} and {type(y_scores)}')
from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)
import matplotlib.pyplot as plt

plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')  # Plotting the diagonal line (random classifier)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.savefig('roc_curve.png')
#plt.show()


