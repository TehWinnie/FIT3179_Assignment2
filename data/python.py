import pandas as pd

# Load your dataset into a DataFrame
df = pd.read_csv("03_cancer-death-rates-by-age.csv")

# Group the data by the "Entity" column and calculate the average for each age group
grouped = df.groupby("Entity")[['Deaths - Neoplasms - Sex: Both - Age: 70+ years (Rate)',
                                'Deaths - Neoplasms - Sex: Both - Age: 50-69 years (Rate)',
                                'Deaths - Neoplasms - Sex: Both - Age: 15-49 years (Rate)',
                                'Deaths - Neoplasms - Sex: Both - Age: 5-14 years (Rate)',
                                'Deaths - Neoplasms - Sex: Both - Age: Under 5 (Rate)']].mean()

# Save the grouped data to a new CSV file
grouped.to_csv("average_death_rate_cancer_entity_grouped.csv")

