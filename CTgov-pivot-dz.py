# Pivots the table of trials from clinical trials.gov and then merges it with
# the USnewsy rank list

import pandas as pd


# Read in the rank-list which includes the organizations
RL_path = 'C:\Users\JAG\USnewsy\RL_5yr_Trial_Impact_Grants_USNdata.csv'
RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)

ctg_path = 'C:\Users\JAG\USnewsy\Clinicaltrials\CTgovDz.csv'
ctg = pd.read_csv(ctg_path, index_col = False, header = 0, squeeze = True)

#get start years as numbers and then select on them
Start_years = []
for deet in ctg['Start_date']:
    deet = deet[-4:]
    try:
        deet = int(deet)
        Start_years.append(deet)
    except ValueError:
        Start_years.append(0)
ctg['Start year'] = Start_years
ctg = ctg[ctg['Start year'] > 2007]
ctg = ctg[ctg['Start year'] < 2014]
ctg = ctg.drop('Start year', axis = 1)




# make the pivot table - count the number of trials in each phase
pivot = ctg.pivot_table('nct_id', rows ='Institution', cols ='Disease', aggfunc = 'count')


pivot['Institution'] = pivot.index
pivot = pivot.fillna(0)

pivot.to_csv('C:\Users\JAG\USnewsy\Clinicaltrials\CTgov_pivotDz.csv', sep = ',', index = False)


'''
pivot = RL.merge(pivot, on = 'Institution')
pivot.to_csv('C:\Users\JAG\USnewsy\RL_5yr_Impact_Grants_USN_CTg.csv', sep = ',' , index = False)
'''