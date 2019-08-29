import pandas as pd
import numpy as np
from scipy import stats


amusics = ['02', '04'] 
non_amusics = ['19', '20']

freqAvrg_amusics = []
freqAvrg_non_amusics = []

for participant in amusics: # for loop to change folders

    df = pd.read_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\data_analysis\P0' + participant + '.csv') 
    
    freqAvrg_amusics.append(df['Frequency Range'].mean())

for participant in non_amusics: # for loop to change folders

    df = pd.read_csv(r'\Users\Emanuele\Desktop\UdeM\PhD\BrainHack\data_analysis\P0' + participant + '.csv') 
    
    freqAvrg_non_amusics.append(df['Frequency Range'].mean())




statistic, pvalue = stats.ttest_ind(freqAvrg_amusics,freqAvrg_non_amusics, equal_var = False)

print("T test result: " +  str(statistic))
print("pvalue: "+  str(pvalue))