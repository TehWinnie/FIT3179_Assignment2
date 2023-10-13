import pandas as pd

# Load the CSV file
df = pd.read_csv('02_total-cancer-deaths-by-type.csv')

# Create a dictionary to map the existing column names to the new names
column_mapping = {
    'Deaths - Liver cancer - Sex: Both - Age: All Ages (Number)': 'Liver cancer',
    'Deaths - Kidney cancer - Sex: Both - Age: All Ages (Number)': 'Kidney cancer',
    'Deaths - Lip and oral cavity cancer - Sex: Both - Age: All Ages (Number)': 'Lip and oral cavity cancer',
    'Deaths - Tracheal, bronchus, and lung cancer - Sex: Both - Age: All Ages (Number)': 'Tracheal, bronchus, and lung cancer',
    'Deaths - Larynx cancer - Sex: Both - Age: All Ages (Number)': 'Larynx cancer',
    'Deaths - Gallbladder and biliary tract cancer - Sex: Both - Age: All Ages (Number)': 'Gallbladder and biliary tract cancer',
    'Deaths - Malignant skin melanoma - Sex: Both - Age: All Ages (Number)': 'Malignant skin melanoma',
    'Deaths - Leukemia - Sex: Both - Age: All Ages (Number)': 'Leukemia',
    'Deaths - Hodgkin lymphoma - Sex: Both - Age: All Ages (Number)': 'Hodgkin lymphoma',
    'Deaths - Multiple myeloma - Sex: Both - Age: All Ages (Number)': 'Multiple myeloma',
    'Deaths - Other neoplasms - Sex: Both - Age: All Ages (Number)': 'Other neoplasms',
    'Deaths - Breast cancer - Sex: Both - Age: All Ages (Number)': 'Breast cancer',
    'Deaths - Prostate cancer - Sex: Both - Age: All Ages (Number)': 'Prostate cancer',
    'Deaths - Thyroid cancer - Sex: Both - Age: All Ages (Number)': 'Thyroid cancer',
    'Deaths - Stomach cancer - Sex: Both - Age: All Ages (Number)': 'Stomach cancer',
    'Deaths - Bladder cancer - Sex: Both - Age: All Ages (Number)': 'Bladder cancer',
    'Deaths - Uterine cancer - Sex: Both - Age: All Ages (Number)': 'Uterine cancer',
    'Deaths - Ovarian cancer - Sex: Both - Age: All Ages (Number)': 'Ovarian cancer',
    'Deaths - Cervical cancer - Sex: Both - Age: All Ages (Number)': 'Cervical cancer',
    'Deaths - Brain and central nervous system cancer - Sex: Both - Age: All Ages (Number)': 'Brain and central nervous system cancer',
    'Deaths - Non-Hodgkin lymphoma - Sex: Both - Age: All Ages': 'Non-Hodgkin lymphoma'
}

# Rename the columns
df.rename(columns=column_mapping, inplace=True)

# Group the data by 'Entity' (country or territory) and sum the deaths for each cancer type
grouped = df.groupby('Entity').sum().reset_index()

# Save the renamed DataFrame to a new CSV file
grouped.to_csv('total_death_cancer_type_1990to2019.csv', index=False)
