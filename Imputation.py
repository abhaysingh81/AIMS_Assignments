import pandas as pd
import numpy as np


data = {
    'id': [101, 102, 103, 104, 105, 106, 107, 108],
    'name' : ['Rohan', 'Dinesh', 'Tom', 'Henry', 'Bella', 'Mike', 'Shreya', 'John'],
    'age': [25, 28, np.nan, 35, 40, np.nan, 22, np.nan],
    'salary': [50000, 55000, 60000, 80000, np.nan, 75000, 48000, np.nan],
    'department': ['Sales', 'HR', 'Sales', 'Sales', np.nan, 'IT', 'HR', np.nan]
}

df = pd.DataFrame(data)

def impute_mean(df, column):
    df_imputed=df.copy()
    mean_val = df_imputed[column].mean()
    df_imputed[column] = df_imputed[column].fillna(mean_val)
    print(f"---> Imputing '{column}' with MEAN: {mean_val:.2f}")
    return df_imputed

def impute_median(df, column):
    df_imputed = df.copy()
    median_val = df_imputed[column].median()
    df_imputed[column] = df_imputed[column].fillna(median_val)
    print(f"---> Imputing '{column}' with MEDIAN: {median_val:.2f}")
    return df_imputed

def impute_mode(df, column):
    df_imputed = df.copy()
    mode_val = df_imputed[column].mode()[0]
    df_imputed[column] = df_imputed[column].fillna(mode_val)
    print(f"---> Imputing '{column}' with MODE: {mode_val}")
    return df_imputed


print("--- Original DataFrame ---")
print(df)
print()
df_mean_imputed = impute_mean(df, 'age')
print()
df_median_imputed = impute_median(df_mean_imputed, 'salary')
print()
df_mode_imputed = impute_mode(df_median_imputed, 'department')
print()
print(df_mode_imputed)