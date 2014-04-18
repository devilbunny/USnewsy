# Runs through a list of organizations and determines how many impact factor
# of their publications.  This version allows searching for differen cancer types
# Impact factors from: http://www.citefactor.org/impact-factor-list-2012.html

import pandas as pd
from pubmedsearch import pubmedsearch, pmhits

# Read in the rank-list which includes the organizations
RL_path = 'C:\Users\LilaJeff\USnewsy\RL_USN.csv'
RL = pd.read_csv(RL_path, index_col=False, header=0, squeeze=True)

# Read in the impact-factor list
IF_path = 'C:\Users\LilaJeff\USnewsy\impact_factors.csv'
IF = pd.read_csv(IF_path, index_col=False, header=0, squeeze=True)
journals = IF['Pubmed Journal Title']
factors = IF['Impact Factor']
IFdict = dict(zip(journals,factors))


# Which article types to consider
types = ['Clinical Trial', 'Clinical Trial, Phase I', 'Clinical Trial, Phase II', 'Clinical Trial, Phase III',
        'Review', 'All']

# Which cancers to consider
cancers = ['ovarian cancer','breast cancer','lung cancer','lymphoma','leukemia','brain cancer','pancreatic cancer',
        'melanoma','colon cancer', 'head and neck cancer', 'prostate cancer', 'soft tissue tumor', 'esophageal cancer',
        'kidney cancer', 'multiple myeloma', 'ewing sarcoma', 'rhabdomyosarcoma', 'bladder cancer', 'liver cancer',
        'thyroid cancer']


# get publications for each organization
def getfactors (RL, articletype, cancer):
    IFs = []
    article_count = []
    bad_journals = []
    hit_count = 0
    miss_count = 0
    columntitleIF = 'Impact factor - ' + articletype + ' ' + cancer
    columntitlecount = 'Paper count - ' + articletype + ' ' + cancer
    
    if articletype != 'All':
        searchterm = " [AD] 2008:2013 [DP] " + articletype + "[PT] " + cancer + "[mesh]"

    else:
        searchterm = " [AD] 2008:2013 [DP]" + cancer + "[mesh]"

    
    for org in RL['Search_Term']:

        records = pubmedsearch(org + searchterm)
        org_factor = 0
        org_count = 0
        for record in records: #iterating over the records collected, get the journal for each and impact factor
            org_count = org_count + 1
            TA = record.get('TA', '?')
            TA = TA.upper()
            TA = TA.replace('.', '')
            factor = IFdict.get(TA)
            try:
                factor = float(factor)
                org_factor = org_factor + factor #add this IF to the total IF for the organization
                hit_count = hit_count + 1
            except TypeError:
                bad_journals.append(TA)
                miss_count = miss_count + 1
        IFs.append(org_factor)
        article_count.append(org_count)
    
    bad_journals = sorted(list(set(bad_journals)))
    RL[columntitleIF] = IFs
    RL[columntitlecount] = article_count

    print articletype
    print hit_count
    print miss_count
    print len(bad_journals)

    return RL

for PT in types:
    for cancer in cancers:
        RL = getfactors(RL, PT, cancer)


RL.to_csv('C:\Users\LilaJeff\USnewsy\RL_USN_PMed_dz.csv', sep = ',' , index = False)