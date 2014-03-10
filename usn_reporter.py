#Matches up institutions and the grants they receive
# Each ORG is identified by up to 3 different names in the rank-list 'RL'
# We take each ORG_NAME in the RL and in the RePORTER database, strip out a ton
# of words as named in 'dropwords' and then match them up using the MERGE command
# in pandas.  the 3 dataframes get written into the same file and then I manually
# clean it up in excel
import pandas as pd
import numpy as np


RePORTER_path = 'C:\Users\JAG\USnewsy\RePORT_group.csv'
RL_path = 'C:\Users\JAG\USnewsy\RL_5yr_journals.csv'
RL_With_Grants_path = "C:\Users\JAG\USnewsy\RL-TG-JO.csv"
dropwords = ['.', '-', '/', ',', ' AND ',' OF ',' THE ',' UNIVERSITY ',' HOSPITAL ',' CLINIC ',' CAN ',' CTR ',
            ' CANCER ',' CENTER ' , ' INC ' , ' LLC ', ' MED ' , ' COL ' , 'FOUNDATION',
            ' SCHOOL ', ' MEDICINE ', ' CORP ', ' AT ', ' MEDICAL ', ' INSTITUTE ', 'INST',
            ' CAN ', ' RESEARCH ', ' RES ', ' COLLEGE ']

RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)
RePORTER = pd.read_csv(RePORTER_path, index_col=False, header=0, squeeze=True)

def fix_org(col, dropwords):
    #Takes a column of organizations *col* capitalizes it, strips extra spaces
    # And removes the words found in *dropwords*
    fixed = []
    for org in col:
        org = fix_org_sub(org, dropwords)
        fixed.append(org)
    return fixed

def fix_org_sub(org, dropwords):
    # subfunction for 'fix org' for fixing individual organizations
    try:
        org = str(org)
    except AttributeError:
        return org
    org = org.upper()
    org = ' ' + org + ' '
    for word in dropwords:
        org = org.replace(word,' ')
        org = org.replace('  ', ' ')
    org = org.strip()
    return org



RePORTER['MERGE_KEY'] = fix_org(RePORTER['ORG_NAME'],dropwords)

RL['MERGE_KEY'] = fix_org(RL['ORG_NAME1'], dropwords)
merged = RL.merge(RePORTER, on = 'MERGE_KEY')
merged.to_csv(RL_With_Grants_path, sep = ',' , index = False, mode = 'a')

RL = RL.drop('MERGE_KEY',axis = 1)
RL['MERGE_KEY'] = fix_org(RL['ORG_NAME2'], dropwords)
merged = RL.merge(RePORTER, on = 'MERGE_KEY')
merged.to_csv(RL_With_Grants_path, sep = ',' , index = False, mode = 'a')

RL = RL.drop('MERGE_KEY',axis = 1)
RL['MERGE_KEY'] = fix_org(RL['ORG_NAME3'], dropwords)
merged = RL.merge(RePORTER, on = 'MERGE_KEY')
merged.to_csv(RL_With_Grants_path, sep = ',' , index = False, mode = 'a')



