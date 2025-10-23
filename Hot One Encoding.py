import pandas as pd
import numpy as np

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'name' : ['Rohan', 'Dinesh', 'Tom', 'Henry', 'Bella', 'Mike', 'Shreya', 'John'],
    'fav_color': ['red', 'blue', 'green', 'red', 'blue', 'blue', 'red', 'green'],
    'home_country': ['USA', 'Canada', 'USA', 'Mexico', 'Canada', 'Mexico', 'USA', 'Canada']
}
df = pd.DataFrame(data)

def one_hot_encoding(df, column):
    df_encoded=df.copy()
    unique_categories=df_encoded[column].unique()

    for cat in unique_categories:
        new_col_name=f"{column}_{cat}"
        df_encoded[new_col_name] = (df_encoded[column] == cat).astype(int)

    df_encoded = df_encoded.drop(column, axis=1)
    return df_encoded

df_encoded_color = one_hot_encoding(df, 'fav_color')
df_encoded_final = one_hot_encoding(df_encoded_color, 'home_country')

print("--- Original DataFrame ---")
print(df)
print()
print("--- DataFrame after One-Hot Encoding ---")
print(df_encoded_final)