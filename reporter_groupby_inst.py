# restricts grants to certain years and NIH institutes, then groups
# by grant receiving institution


import pandas as pd
import numpy as np


RePORTER_path = 'C:\Users\JAG\RePORTER\Output\RePORT_usn.csv'
grouped_path = "C:\Users\JAG\USnewsy\RePORT_group.csv"

RePORTER = pd.read_csv(RePORTER_path, sep = ',' , index_col = False, header =0, squeeze = True)

Year = []
for date in RePORTER['BUDGET_START']:
    try:
        date = date[-4:]
        date = int(date)
        Year.append(date)
    except TypeError:
        date = 1900
        Year.append(date)
    except ValueError:
        date = 1900
        Year.append(date)
        
costs = []
for cost in RePORTER['TOTAL_COST']:
    try:
        cost = float(cost)
    except ValueError:
        cost = 0
    costs.append(cost)

RePORTER['TOTAL_COST'] = costs
RePORTER = RePORTER[['ORG_NAME', 'TOTAL_COST']]
RePORTER_NT = RePORTER[RePORTER['TOTAL_COST'] > 1]


RL_sum = RePORTER.groupby('ORG_NAME').sum()
RL_count = RePORTER.groupby('ORG_NAME').count()
RL_count_NT = RePORTER_NT.groupby('ORG_NAME').count()

RL_sum['ORG_NAME'] = RL_sum.index
RL_count['ORG_NAME'] = RL_count.index
RL_count_NT['ORG_NAME'] = RL_count_NT.index

RL_count['GRANT_COUNT'] = RL_count['TOTAL_COST']
RL_count = RL_count.drop('TOTAL_COST', axis = 1)
RL_count_NT['GRANT_COUNT_NT'] = RL_count_NT['TOTAL_COST']
RL_count_NT = RL_count_NT.drop('TOTAL_COST', axis = 1)


RL_sum = RL_sum.merge(RL_count)
RL_sum = RL_sum.merge(RL_count_NT)


'''
RWG_sum['Name'] = RWG_sum.index
RWG_sum = RWG_sum[['Name','TOTAL_COST']]

RWG_pivot = RWG_fix.pivot_table('Years_to_grant', rows ='Name', cols ='ACTIVITY', aggfunc = 'min')
RWG_pivot['Name'] = RWG_pivot.index
RWG_pivot = RWG_pivot.merge(RWG_sum)

RWG_fix = Residents.merge(RWG_pivot, how = 'outer')
'''
RL_sum.to_csv(grouped_path, sep = ',')


