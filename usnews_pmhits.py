'''usnews wrangle
To wrangle complicated files with stacked information

'''
import pandas as pd
import numpy as np
import pubmedsearch as pm

List_path = 'C:\Users\JAG\USnewsy\RL-trials-5yr.csv'
Completed_path = 'C:\Users\JAG\USnewsy\RL-trials-5yr.csv'

# Read in the csv
RL = pd.read_csv(List_path, index_col=False, header = 0)

phase2 = []
phase3 = []
clinicaltrials = []

for institution in RL['Search_Term']:
    p2 = pm.pmhits(institution + '[AD] 2008:2013 [DP] Clinical Trial, Phase II[PT] Cancer[MAJR]')
    phase2.append(p2)
    p3 = pm.pmhits(institution + '[AD] 2008:2013 [DP] Clinical Trial, Phase III[PT], Cancer[MAJR]')
    phase3.append(p3)
    ct = pm.pmhits(institution + '[AD] 2008:2013 [DP] Clinical Trial[PT], Cancer[MAJR]')
    clinicaltrials.append(ct)    

RL['Phase 2'] = phase2
RL['Phase 3'] = phase3
RL['Clinical Trials'] = clinicaltrials

RL.to_csv(Completed_path) 