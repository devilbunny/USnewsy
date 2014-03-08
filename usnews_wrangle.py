'''usnews wrangle
To wrangle complicated files with stacked information

'''
import pandas as pd
import numpy as np


List_path = 'C:\Users\JAG\USnewsy\USnewsRL.csv'
Fixed_path = 'C:\Users\JAG\USnewsy\RL-fix.csv'
cols = ['Col0', 'Col1', 'Col2']

# Read in the csv
RL = pd.read_csv(List_path, index_col=False, names = cols)

# gets the ranks
ranks = RL[cols[0]]
r2 = []
a=-1
for rank in ranks:
    a = a+1
    if (a)%7 == 0:
        rank = rank[1:]
        rank = int(rank)
        r2.append(rank)

# get scores       
scores = RL[cols[2]]
s2 = []
a=-1
for score in scores:
    a = a+1
    if (a)%7 == 0:
        score = str(score)
        score = score[:-6]
        s2.append(score)

# get institutions and locales
Col1 = RL[cols[1]]
institutions = []
locales = []
a=-1
for deet in Col1:
    a = a+1
    if (a)%7 == 0:
        institutions.append(deet)
    if (a-2)%7 == 0:
        locales.append(deet)


# convert series into dataframe
d = {'Institution' : institutions,'Locale' : locales,'Score' : s2,'Rank' : r2}
Ranklist = pd.DataFrame(d)


Ranklist.to_csv(Fixed_path) 