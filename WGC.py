import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/macbook/Desktop/wgc_raw_data 2.csv')
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())


df = df.drop_duplicates()
print(df.shape)

df["Timestamp"]= pd.to_datetime(df["Timestamp"],format ="mixed")
print(df["Timestamp"].dtype)
print(df["Timestamp"].head())



df['Anti_Surge_Valve_pct'] = df['Anti_Surge_Valve_pct'].astype(str) + " %"
stage_temp_cols = [
    "Suction_Temp_Stage1_C",
    "Discharge_Temp_Stage1_C",
    "Suction_Temp_Stage2_C",
    "Discharge_Temp_Stage2_C",
]

print(df.head())

print(df.isnull().sum())
print(df.info())

df.to_csv("wgc_numeric_data.csv", index=False)
print("\nSaved numeric version -> wgc_numeric_data.csv")


