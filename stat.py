import pandas as pd

df = pd.read_csv("wgc_numeric_data.csv")

# IQR method on Vibration
Q1, Q3 = df['Vibration_mms'].quantile([0.25, 0.75])
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df['Vibration_Outlier'] = (df['Vibration_mms'] < lower) | (df['Vibration_mms'] > upper)

print(f"Vibration normal range: {lower:.2f} to {upper:.2f}")
print(f"Outliers found: {df['Vibration_Outlier'].sum()}")
print(df.loc[df['Vibration_Outlier'], ['Timestamp', 'Vibration_mms', 'Anti_Surge_Valve_pct']])


cols = ['Vibration_mms', 'Anti_Surge_Valve_pct', 'RPM',
        'Discharge_Pressure_Stage2_kgcm2', 'Seal_Gas_Pressure_kgcm2']

# strip units and convert to numeric
for col in cols:
    df[col] = df[col].astype(str).str.replace(' %', '', regex=False)
    df[col] = df[col].astype(str).str.replace(' kg', '', regex=False)
    df[col] = pd.to_numeric(df[col])

corr = df[cols].corr()
print(corr.round(2))