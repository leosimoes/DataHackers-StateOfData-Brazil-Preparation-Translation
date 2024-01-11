# Script for the translation of State of Data Brazil's data from Portuguese to English.
# Author: Leonardo Simões

import pandas as pd
import json

# File directory paths
DATASET_LOADED = '../Data/prepared_dataset.csv'
DATASET_SAVED = '../Data/translated_dataset.csv'
JSON_COLUMNS_NAMES = '../Dictionaries/translations_of_modified_column_names.json'
JSON_COLUMNS_VALUES = '../Dictionaries/translations_of_modified_column_values.json'

print('Running the translator...')

print(f'Loading data from the {DATASET_LOADED.split('/')[-1]} file...')

# Load the dataframe
df = pd.read_csv(DATASET_LOADED)

print(f'Data from the {DATASET_LOADED.split('/')[-1]} file has been loaded.')

print(f'Loading data from the {JSON_COLUMNS_NAMES.split('/')[-1]} file...')

# Load translations of column names from the file
translations_of_columns = None
with open(JSON_COLUMNS_NAMES, 'r', encoding='utf-8') as file:
    translations_of_columns = json.load(file)

# Checks whether column translations have been loaded from the file
assert translations_of_columns is not None

print(f'Data from the {JSON_COLUMNS_NAMES.split('/')[-1]} file has been loaded.')

print('Translating dataframe column names...')

# Translates dataframe column names
# df.columns = translations_of_columns.values()
df.rename(columns=translations_of_columns, inplace=True)

# Check if you translated the column names
assert df.columns.tolist() == list(translations_of_columns.values())

print('Column names have been translated.')

print(f'Loading data from the {JSON_COLUMNS_VALUES.split('/')[-1]} file...')

# Load translations of column values from the file
translations_of_values = None
with open(JSON_COLUMNS_VALUES, 'r', encoding='utf-8') as file:
    translations_of_values = json.load(file)

# Checks if you loaded the translations of the column values from the file
assert translations_of_values is not None

print(f'Data from the {JSON_COLUMNS_VALUES.split('/')[-1]} file has been loaded.')

print('Translating dataframe values...')

# Translates column values
for column, mapping in translations_of_values.items():
    df[column] = df[column].replace(mapping)

print('Dataframe values have been translated.')

print(f'Saving the data to the {DATASET_SAVED.split('/')[-1]} file...')

# Saves translated data to a file
df.to_csv(DATASET_SAVED, index=False)

print(f'The translated data was saved to the {DATASET_SAVED.split('/')[-1]} file.')

print('The translator has finished.')
