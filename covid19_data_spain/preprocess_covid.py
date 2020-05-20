import pandas as pd
import os

df = pd.read_csv("cases_and_hospitalised_and_ICU_and_recovered.csv")

spain_counties = df['CCAA'].unique()

print(spain_counties)


for i in range(len(spain_counties)):
    new_df = df[df['CCAA'] == spain_counties[i]]
    
    new_df.to_csv('covid19_spain_counties/'+spain_counties[i]+'.csv')