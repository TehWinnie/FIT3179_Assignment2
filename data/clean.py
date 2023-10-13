import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('01_annual-number-of-deaths-by-cause.csv')

# Define a mapping of original column names to new names (just the type)
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

# Rename the columns using the mapping
df.rename(columns=column_mapping, inplace=True)

# Remove the 'Year' column
df.drop(columns=['Year'], inplace=True)

# Group the data by 'Entity' (country or region) and calculate the average (mean) for the renamed columns
grouped = df.groupby('Entity').agg('mean').reset_index()

# Save the result to a new CSV file without the 'Year' column
grouped.to_csv('average_deaths_by_country.csv', index=False)


