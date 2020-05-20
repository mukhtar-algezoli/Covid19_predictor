import pandas as pd

df_cases = pd.read_csv("cases_and_hospitalised_and_ICU.csv")
df_hospitalized = pd.read_csv("ccaa_covid19_altas_long.csv")

df_new = pd.merge(df_cases, df_hospitalized, left_index=True, right_index=True)

df_new.to_csv("cases_and_hospitalised_and_ICU_and_recovered.csv")

