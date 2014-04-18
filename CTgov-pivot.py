# Pivots the table of trials from clinical trials.gov and then merges it with
# the USnewsy rank list

import pandas as pd


# Read in the rank-list which includes the organizations
RL_path = 'C:\Users\JAG\USnewsy\RL_5yr_Trial_Impact_Grants_USNdata.csv'
RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)

ctg_path = 'C:\Users\JAG\USnewsy\Clinicaltrials\CTgov.csv'
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
pivot = ctg.pivot_table('nct_id', rows ='Institution', cols ='Phase', aggfunc = 'count')


pivot['Institution'] = pivot.index
pivot = pivot.fillna(0)

#Aggregate non phase 1, 2, 3 trials into the NA category, downgrade mixed trials
pivot['N/A'] = pivot['N/A'] + pivot ['Phase 4'] + pivot ['Phase 0']
pivot['Phase 1'] = pivot['Phase 1'] + pivot['Phase 1/Phase 2']
pivot['Phase 2'] = pivot['Phase 2/Phase 3'] + pivot['Phase 2']
pivot = pivot.drop('Phase 0', axis = 1)
pivot = pivot.drop('Phase 1/Phase 2', axis = 1)
pivot = pivot.drop('Phase 2/Phase 3', axis = 1)
pivot = pivot.drop('Phase 4', axis = 1)


pivot['All_trials'] = pivot['N/A']+pivot['Phase 1']+pivot['Phase 2'] + pivot['Phase 3']

pivot.to_csv('C:\Users\JAG\USnewsy\Clinicaltrials\CTgov_pivotDz.csv', sep = ',', index = False)


'''
pivot = RL.merge(pivot, on = 'Institution')
pivot.to_csv('C:\Users\JAG\USnewsy\RL_5yr_Impact_Grants_USN_CTg.csv', sep = ',' , index = False)
'''