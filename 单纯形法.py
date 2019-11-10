import pandas as pd
import numpy as np
a=pd.DataFrame([[1,2,1,0,0,8],
                [4,0,0,1,0,16],
                [0,4,0,0,1,12]])
b=[8,16,12]
c=[2,3,0,0,0]
aa=[0,0,0,0,0]
jbl=[-1,-1,0,1,2]
for i in range(len(c)):
    if jbl[i]>=0:
        continue
    zj=0
    for k in range(len(c)):
        if jbl[k]<0:
            continue
        zj+=c[k]*a[i][jbl[k]]
    aa[i]=c[i]-zj
print(aa)
