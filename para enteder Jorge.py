import pandas as pd
import numpy as np
lis1 = [3,5,None,None,np.nan]
se = pd.Series(lis1, index=['Ene','feb','mar','abr','mayo'])
#print(se)
#print(se.size)
#print(se.dtype)
#print(se[2])
#print(se[0:4])
#print(se.sum())
#print(se.count())

li = [3,8,2,5,9,2,2,4,3]
se = pd.Series(li, index=['Ene','feb','mar','abr','may','Jun','jul','ago','sep'])
#print(se.sum())
#print(se[0::4].sum())
#print(se['Ene':'mar'].sum())
#print(se[se>3])
#print(se[se>3].sum())
#print(se.cumsum())
#print(se.value_counts())
#print(se.mean())
#print(se.std())
SeIVA = se * 0.19
print(SeIVA)