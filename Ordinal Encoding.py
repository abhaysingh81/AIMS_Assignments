import pandas as pd 

data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'name' : ['Emily', 'Rakesh', 'Monica', 'Caleb', 'Rekha', 'Joji', 'Travis', 'Abel', 'Rambharose', 'Mukesh'],
    'education_level': ['Intermediate', 'UG', 'PG', 'PhD', 'PG', 'Intermediate', 'PhD', 'UG', 'UG', 'Intermediate'],
    'job_position' : ['Intern', 'Associate', 'Intern', 'Senior Manager', 'Manager', 'Associate', 'Senior Manager', 'Manager', 'Manager', 'Manager']
}

df = pd.DataFrame(data)

education_map = {
    'Intermediate': 0,
    'UG': 1,
    'PG': 2,
    'PhD': 3
}

job_position_map={
    'Intern' : 0,
    'Associate' : 1,
    'Manager' : 2,
    'Senior Manager' : 3
}

def ordinal_encode(df, column, category_map):
    df_encoded = df.copy()
    df_encoded[column] = df_encoded[column].map(category_map)
    return df_encoded


df_encoded = ordinal_encode(df, 'education_level', education_map)
df_encoded= ordinal_encode(df_encoded, 'job_position', job_position_map)


print("--- Original DataFrame ---")
print()
print(df)
print()
print()
print("--- DataFrame after Ordinal Encoding ---")
print()
print(df_encoded)

