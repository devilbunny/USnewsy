# linear regression for usnews ranking data - takes into account various columns to
# make a model

import pandas as pd
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
import scikits.statsmodels.api as sm

RL_path = 'C:\Users\JAG\USnewsy\RL_5yr_Trial_Impact_Grants.csv'
RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)



y = RL['Score']

'''
x = np.column_stack((RL['Phase 2'],RL['Phase 3'],RL['Clinical Trials'],RL['Impact factor - Phase 2'],
                        RL['Impact factor - Phase 3'], RL['Impact factor - All trials'], 
                        RL['Impact factor - All papers'], RL['TOTAL_COST'], RL['GRANT_COUNT']))
'''
x = np.column_stack((RL['Clinical Trials'],RL['Impact factor - All papers'], RL['TOTAL_COST']))

x = sm.add_constant(x, prepend=True) #add a constant

res = sm.OLS(y,x).fit() #create a model and fit it
print res.params
print res.bse
print res.summary()


