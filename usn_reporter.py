#Matches up institutions and the grants they receive
import pandas as pd
import numpy as np


RePORTER_path = 'C:\Users\JAG\RePORTER\Output\RePORT_Append.csv'
RL_path = 'C:\Users\JAG\USnewsy\RL-trials-5yr.csv'
RL_With_Grants_path = "C:\Users\JAG\USnewsy\RL-TG.csv"

RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)
RePORTER = pd.read_csv(RePORTER_path, index_col=False, header=0, squeeze=True)

RL['ORG_NAME1'] = [org.upper() for org in RL['ORG_NAME1']]
RL['ORG_NAME2'] = [org.upper() for org in RL['ORG_NAME2'] if org is str]
RL['ORG_NAME3'] = [org.upper() for org in RL['ORG_NAME3'] if org is str]
'''
Residents_With_Grants = Residents.merge(RePORTER)
Residents_With_Grants = years_to_grant(Residents_With_Grants, GRAD_YEAR_col = 'GRAD_YEAR')
Residents_With_Grants.to_csv(Residents_With_Grants_path, sep = ',' , index = False)
'''