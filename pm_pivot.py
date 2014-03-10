# Runs through a list of organizations and determines how many publications they have
# in which journal

import pandas as pd
from pubmedsearch import pubmedsearch, pmhits

# Read in the rank-list which includes the organizations
RL_path = 'C:\Users\JAG\USnewsy\RL-trials-5yr.csv'
RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)

PMIDs = []
DPs = []
ADs = []
TAs = []

# get publications for each organization
for org in RL['Search_Term']:
    records = pubmedsearch(org + " [AD] 2008:2013 [DP] Clinical Trial, Phase III[PT] Cancer[MAJR]")

    for record in records:
        uid = record.get('PMID', '?')
        PMIDs.append(uid)
        DP = record.get('DP', '?')
        DPs.append(DP)
        ADs.append(org)
        TA = record.get('TA', '?')
        TAs.append(TA)

d = {'PMID' : PMIDs, 'DATE' : DPs, 'ORGANIZATION' : ADs, 'JOURNAL' : TAs}
df = pd.DataFrame(d)

pivot = df.pivot_table('PMID', rows ='ORGANIZATION', cols ='JOURNAL', aggfunc = 'count')


pivot['Search_Term'] = pivot.index
pivot = RL.merge(pivot, on = 'Search_Term')
pivot.to_csv('C:\Users\JAG\USnewsy\RL_5yr_phase3.csv', sep = ',' , index = False)