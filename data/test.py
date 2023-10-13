import pandas as pd

# Load the CSV file
df = pd.read_csv('02_total-cancer-deaths-by-type.csv')

# Drop the 'Entity' column if it exists, as we are now grouping by cancer type
if 'Entity' in df.columns:
    df.drop(columns='Entity', inplace=True)

# Drop the 'Year' column if it exists, as we are now grouping by cancer type
if 'Year' in df.columns:
    df.drop(columns='Year', inplace=True)

column_mapping = {
    'Deaths - Meningitis - Sex: Both - Age: All Ages (Number)': 'Meningitis',
    "Deaths - Alzheimer's disease and other dementias - Sex: Both - Age: All Ages (Number)": 'Alzheimer',
    "Deaths - Parkinson's disease - Sex: Both - Age: All Ages (Number)": 'Parkinson',
    "Deaths - Nutritional deficiencies - Sex: Both - Age: All Ages (Number)": 'Nutritional Deficiencies',
    "Deaths - Malaria - Sex: Both - Age: All Ages (Number)": 'Malaria',
    "Deaths - Drowning - Sex: Both - Age: All Ages (Number)": 'Drowning',
    "Deaths - Interpersonal violence - Sex: Both - Age: All Ages (Number)": 'Interpersonal Violence',
    "Deaths - Maternal disorders - Sex: Both - Age: All Ages (Number)": 'Maternal Disorders',
    "Deaths - HIV/AIDS - Sex: Both - Age: All Ages (Number)": 'HIV/AIDS',
    "Deaths - Drug use disorders - Sex: Both - Age: All Ages (Number)": 'Drug Use Disorders',
    "Deaths - Tuberculosis - Sex: Both - Age: All Ages (Number)": 'Tuberculosis',
    "Deaths - Cardiovascular diseases - Sex: Both - Age: All Ages (Number)": 'Cardiovascular Diseases',
    "Deaths - Lower respiratory infections - Sex: Both - Age: All Ages (Number)": 'Lower Respiratory Infections',
    "Deaths - Neonatal disorders - Sex: Both - Age: All Ages (Number)": 'Neonatal Disorders',
    "Deaths - Alcohol use disorders - Sex: Both - Age: All Ages (Number)": 'Alcohol Use Disorders',
    "Deaths - Self-harm - Sex: Both - Age: All Ages (Number)": 'Self-Harm',
    "Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number)": 'Exposure to Forces of Nature',
    "Deaths - Diarrheal diseases - Sex: Both - Age: All Ages (Number)": 'Diarrheal Diseases',
    "Deaths - Environmental heat and cold exposure - Sex: Both - Age: All Ages (Number)": 'Environmental Heat and Cold Exposure',
    "Deaths - Neoplasms - Sex: Both - Age: All Ages (Number)": 'Neoplasms',
    "Deaths - Conflict and terrorism - Sex: Both - Age: All Ages (Number)": 'Conflict and Terrorism',
    "Deaths - Diabetes mellitus - Sex: Both - Age: All Ages (Number)": 'Diabetes Mellitus',
    "Deaths - Chronic kidney disease - Sex: Both - Age: All Ages (Number)": 'Chronic Kidney Disease',
    "Deaths - Poisonings - Sex: Both - Age: All Ages (Number)": 'Poisonings',
    "Deaths - Protein-energy malnutrition - Sex: Both - Age: All Ages (Number)": 'Protein-energy Malnutrition',
    "Terrorism (deaths)": 'Terrorism',
    "Deaths - Road injuries - Sex: Both - Age: All Ages (Number)": 'Road Injuries',
    "Deaths - Chronic respiratory diseases - Sex: Both - Age: All Ages (Number)": 'Chronic Respiratory Diseases',
    "Deaths - Cirrhosis and other chronic liver diseases - Sex: Both - Age: All Ages (Number)": 'Cirrhosis and Other Chronic Liver Diseases',
    "Deaths - Digestive diseases - Sex: Both - Age: All Ages (Number)": 'Digestive Diseases',
    "Deaths - Fire, heat, and hot substances - Sex: Both - Age: All Ages (Number)": 'Fire, Heat, and Hot Substances',
    "Deaths - Acute hepatitis - Sex: Both - Age: All Ages (Number)": 'Acute Hepatitis'
}

# Rename the columns
df.rename(columns=column_mapping, inplace=True)

# Extract the relevant part of the cancer type names
df.columns = df.columns.str.replace(r'^Deaths - (.+?) - Sex: Both - Age: All Ages \(Number\)$', r'\1')

# Save the sum of deaths for each cancer type
sum_by_cancer_type = df.sum()

# Save the result to a new DataFrame or CSV file if needed
# If you want to save it to a DataFrame:
result_df = pd.DataFrame({'Cancer Type': sum_by_cancer_type.index, 'Total Deaths': sum_by_cancer_type.values})

# If you want to save it to a CSV file:
result_df.to_csv('total_death_by_cancer_type.csv', index=False)