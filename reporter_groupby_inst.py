# restricts grants to certain years and NIH institutes, then groups
# by grant receiving institution


import pandas as pd
import numpy as np


RePORTER_path = 'C:\Users\JAG\RePORTER\Output\RePORT_Append.csv'
grouped_path = "C:\Users\JAG\RePORTER\Output\RePORT_group.csv"

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
        
RePORTER['Year'] = Year
RePORTER = RePORTER[RePORTER.Year > 2007]
print RePORTER['Year'][0:50]

'''
RWG_sum = RWG_fix.groupby('Name').sum()
RWG_sum['Name'] = RWG_sum.index
RWG_sum = RWG_sum[['Name','TOTAL_COST']]

RWG_pivot = RWG_fix.pivot_table('Years_to_grant', rows ='Name', cols ='ACTIVITY', aggfunc = 'min')
RWG_pivot['Name'] = RWG_pivot.index
RWG_pivot = RWG_pivot.merge(RWG_sum)

RWG_fix = Residents.merge(RWG_pivot, how = 'outer')
RWG_fix.to_csv(Residents_plus_grants_path, sep = ',' , index = False)

'''


