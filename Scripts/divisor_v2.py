import pandas as pd
import json

DATASET_LOADED = '../Data/translated_dataset.csv'
JSON_ORDERED_COLUMNS = '../Dictionaries/ordered_columns.json'

DATASET_GENERAL = '../Data/general_dataset.csv'
DATASET_DATA_ANALYSTS = '../Data/data_analyst_dataset.csv'
DATASET_BI_ANALYSTS = '../Data/bi_analyst_dataset.csv'
DATASET_DATA_SCIENTIST = '../Data/data_scientist_dataset.csv'
DATASET_DATA_ENGINEER = '../Data/data_engineer_dataset.csv'

# Step 1 - Load data from `Data/prepared_dataset.csv`
# Passo 1 - Carregar os dados de `Data/prepared_dataset.csv`
df = pd.read_csv(DATASET_LOADED)
assert not df.empty, 'Error in step 1'

# Step 2 - Create filters for dataframe rows
# Passo 2 - Criar filtros para linhas do dataframe
is_data_analyst = (df['Role (Function)'] == 'Data Analyst') | (df['Field of Work'] == 'Data Analysis')
is_bi_analyst = (df['Role (Function)'] == 'BI Analyst') | (df['Field of Work'] == 'Data Analysis')
is_data_scientist = (df['Role (Function)'] == 'Data Scientist') | (df['Field of Work'] == 'Data Science')
is_data_engineer = (df['Role (Function)'] == 'Data Engineer') | (df['Field of Work'] == 'Data Engineering')

# Step 3 - Load list of selected columns per dataframe
# Passo 3 - Carregar lista de colunas selecionadas por dataframe
columns_general = []
columns_data_analyst = []
columns_bi_analyst = []
columns_data_scientist = []
columns_data_engineer = []

with open(JSON_ORDERED_COLUMNS, 'r', encoding='utf-8') as file:
    columns_general = json.load(file)['Full']
    columns_data_analyst = json.load(file)['Data Analyst']
    columns_bi_analyst = json.load(file)['BI Analyst']
    columns_data_scientist = json.load(file)['Data Scientist']
    columns_data_engineer = json.load(file)['Data Engineer']

# Step 4 - Filter dataframes
# Passo 4 - Filtrar dataframes
df_general = df[columns_general]
df_data_analyst = df.loc[is_data_analyst, columns_data_analyst]
df_bi_analyst = df.loc[is_bi_analyst, columns_bi_analyst]
df_data_scientist = df.loc[is_data_scientist, columns_data_scientist]
df_data_engineer = df.loc[is_data_engineer, columns_data_engineer]
assert not df_general.empty, 'Error in step 4 - df_general is empty'
assert not df_data_analyst.empty, 'Error in step 4 - df_data_analyst is empty '
assert not df_bi_analyst.empty, 'Error in step 4 - df_bi_analyst is empty '
assert not df_data_scientist.empty, 'Error in step 4 - df_data_scientist is empty '
assert not df_data_engineer.empty, 'Error in step 4 - df_data_engineer is empty '

# Step 5 - Save dataframes to files
# Passo 5 - Salvar dataframes em arquivos
df_general.to_csv(DATASET_GENERAL, index=False)
df_data_analyst.to_csv(DATASET_DATA_ANALYSTS, index=False)
df_bi_analyst.to_csv(DATASET_BI_ANALYSTS, index=False)
df_data_scientist.to_csv(DATASET_DATA_SCIENTIST, index=False)
df_data_engineer.to_csv(DATASET_DATA_ENGINEER, index=False)
