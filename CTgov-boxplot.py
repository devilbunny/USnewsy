import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ctg_path = "C:\Users\JAG\USnewsy\Clinicaltrials\CTgov_types.csv"
ctg = pd.read_csv(ctg_path, sep=',' , index_col = False, header =0)
ctg['Phase 1/2'] = ctg['Phase 1'] / ctg['Phase 2']
ctg['Phase 2/3'] = ctg['Phase 2'] / ctg['Phase 3']

ctg_pharm = ctg[ctg['Org type (J)'] == 'PHARMACEUTICAL']
ctg_nopharm = ctg[ctg['Org type (J)'] != 'PHARMACEUTICAL']
ctg_gov = ctg[ctg['Org type (J)'] == 'GOVERNMENT']
ctg_univ = ctg[ctg['Org type (J)'] == 'UNIVERSITY']
ctg_nonprof = ctg[ctg['Org type (J)']== 'NON-PROFIT']



'''
plt.scatter(ctg_pharm['All_trials'], ctg_pharm['Phase 3'],color='red')
plt.scatter(ctg_univ['All_trials'], ctg_univ['Phase 3'],color='black')
plt.show()
'''










###### Make a boxplot of the publications
Array = [ctg_pharm, ctg_nopharm, ctg_gov, ctg_univ, ctg_nonprof]
data = []
column = 'Phase 2/3'
for frame in Array:
    datum = frame[column]
    data.append(datum)


fig, ax1 = plt.subplots(figsize=(6,6), dpi = 160)
fig.canvas.set_window_title(column)
plt.subplots_adjust(left=0.075, right=0.95, top=0.9, bottom=0.25)

# Figure out bottom and top
bottom = -0.1
top = 50
ax1.set_ylim(bottom, top)

bp = plt.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
plt.setp(bp['boxes'], color='black')
plt.setp(bp['whiskers'], color='black')
plt.setp(bp['fliers'], color='red', marker='+')
xtickNames = plt.setp(ax1, xticklabels = ['pharm', 'ctg_nopharm', 'ctg_gov', 'ctg_univ', 'ctg_nonprof'])
plt.setp(xtickNames, rotation = 45, fontsize = 12)
plt.show()
