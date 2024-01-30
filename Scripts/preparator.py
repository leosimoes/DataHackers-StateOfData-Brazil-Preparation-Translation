# Script for the prepare of State of Data Brazil's dataset
# Author: Leonardo Simões

import pandas as pd
import json

DATASET_LOADED = '../Data/State_of_Data_2022.csv'
DATASET_SAVED = '../Data/prepared_dataset.csv'
JSON_SELECTED_COLUMNS = '../Dictionaries/selected_columns.json'
JSON_ORDERED_COLUMNS = '../Dictionaries/ordered_columns.json'
JSON_MAPPED_COLUMNS_VALUES = '../Dictionaries/mapped_columns_values.json'

# Step 1 - Load data from `Data/State_of_data_2023.csv`
# Passo 1 - Carregar os dados de `Data/State_of_data_2023.csv`
df = pd.read_csv(DATASET_LOADED)
assert not df.empty, 'Error in step 1'
columns_list_step_1 = df.columns.to_list()

# Step 2 - Rename columns to question codes
# Passo 2 -  Renomear colunas para os códigos das perguntas
rename_columns_v1 = lambda x: x.split("',")[0][2:].strip()
df.rename(rename_columns_v1, axis='columns', inplace=True)
assert df.columns.to_list() == [rename_columns_v1(column) for column in columns_list_step_1], 'Error in step 2'

# Step 3 - Select the columns according to the keys in `Dictionaries/selected_columns.json`
# Passo 3 - Selecionar as colunas de acordo com as chaves em `Dictionaries/selected_columns.json`
with open(JSON_SELECTED_COLUMNS, 'r', encoding='utf-8') as file:
    selected_columns_cod = list(json.load(file).keys())
    df = df[selected_columns_cod]
    assert df.columns.to_list() == selected_columns_cod, 'Error in step 3'

# Step 4 - Rename the columns according to the values in `Dictionaries/selected_columns.json`
# Passo 4 - Renomear as colunas de acordo com os valores em `Dictionaries/selected_columns.json`
with open(JSON_SELECTED_COLUMNS, 'r', encoding='utf-8') as file:
    selected_columns = json.load(file)
    df.rename(columns=selected_columns, inplace=True)
    assert df.columns.to_list() == list(selected_columns.values()), 'Error in step 4'

# Step 5 - Check that there are no repetitions of column names
# Passo 5 - Verificar se não há repetição de nomes colunas
columns_list_step_5 = df.columns.to_list()
assert len(columns_list_step_5) == len(set(columns_list_step_5)), 'Error in step 5'

# Step 6.1 - Remove unwanted (duplicate) lines
# Passo 6.1 - Remover linhas indesejadas (duplicadas)
df.drop_duplicates(keep='first', inplace=True)
assert df.duplicated().sum() == 0, 'Error in step 6.1'

# Step 6.2 - Remove unwanted rows (with missing values in 'id' or 'Age')
# Passo 6.2 - Remover linhas indesejadas (com valores ausentes em 'id' ou 'Idade')
columns_list_step_6_2 = ['id', 'Idade']
df.dropna(subset=columns_list_step_6_2, inplace=True)
assert df[columns_list_step_6_2].isna().sum().sum() == 0, 'Error in step 6.2'

# Step 7 - Convert numeric columns, except "Age", to string type (object)
# Passo 7 - Converter colunas numéricas, exceto "Idade", para o tipo string (object)
columns_list_step_7 = df.select_dtypes(exclude='object').columns.drop('Idade')
df[columns_list_step_7] = df[columns_list_step_7].astype(str)
assert all(df[columns_list_step_7].dtypes == 'object'), 'Error in step 7'
assert df['Idade'].dtype != 'object', 'Error in step 7'

# Step 8 - Fill in missing string values with "Not Informed"
# Passo 8 - Preencher valores ausentes do tipo string com "Não Informado"
columns_list_step_8 = df.select_dtypes(include='object').columns
df[columns_list_step_8] = df[columns_list_step_8].fillna("Não Informado")
assert df[columns_list_step_8].isna().sum().sum() == 0, 'Error in step 8'

# Step 9.1 - Format values (remove whitespace at the beginning and end)
# Passo 9.1 - Formatar valores (remover espaços em branco no início e no final)
columns_list_step_9_1 = df.select_dtypes(include='object').columns
df[columns_list_step_9_1] = df[columns_list_step_9_1].apply(lambda x: x.str.strip())

# Step 9.2 - Format values (convert "1" and "1.0" to "Sim" and "0" and "0.0" to "Não")
# Passo 9.2 - Formatar valores (converter "1" e "1.0" para "Sim" e "0" e "0.0" para "Não")
with open(JSON_MAPPED_COLUMNS_VALUES, 'r', encoding='utf-8') as file:
    columns_list_step_9_2 = df.select_dtypes(include='object').columns
    map_step_9_2 = json.load(file)['Binário']
    df[columns_list_step_9_2] = df[columns_list_step_9_2].replace(map_step_9_2)

# Step 9.3 - Format values (adjust "Salary range" values)
# Passo 9.3 - Formatar valores (ajustar valores de "Faixa salarial")
with open(JSON_MAPPED_COLUMNS_VALUES, 'r', encoding='utf-8') as file:
    map_step_9_3 = json.load(file)['Faixa salarial']
    df['Faixa salarial'] = df['Faixa salarial'].replace(map_step_9_3)
    assert set(df['Faixa salarial'].unique()) == set(map_step_9_3.values()), 'Error in step 9.3'

# Step 9.4 - Format values (adjust “Current Position” values)
# Passo 9.4 - Formatar valores (ajustar valores de "Cargo Atual")


# Passo 10.1 - Criar novas colunas derivadas ("Campo de Atuação Geral" com valores "Dados", "Outra" e "Não Informado")
with open(JSON_MAPPED_COLUMNS_VALUES, 'r', encoding='utf-8') as file:
    map_step_10_1 = json.load(file)['Faixa salarial']
    df['Faixa salarial'] = df['Faixa salarial'].replace(map_step_10_1)
    assert set(df['Faixa salarial'].unique()) == set(map_step_10_1.values()), 'Error in step 10.1'

# Passo 10.2 - Criar novas colunas derivadas (Faixa salarial ($)"`: usando `"Faixa salarial)
with open(JSON_MAPPED_COLUMNS_VALUES, 'r', encoding='utf-8') as file:
    map_step_10_2 = json.load(file)['Faixa salarial ($)']
    df['Faixa salarial ($)'] = df['Faixa salarial'].replace(map_step_10_2)
    assert set(df['Faixa salarial ($)'].unique()) == set(map_step_9_3.values()), 'Error in step 10.2'

# Step 11 - Check that there are no missing values
# Passo 11 - Verificar se não há valores ausentes
assert df.isna().sum().sum() == 0, 'Error in step 11'

# Step 12 - Order the dataframe columns according to Dictionaries/column_order.json
# Passo 12 - Ordenar as colunas do dataframe de acordo com Dictionaries/column_order.json
with open(JSON_ORDERED_COLUMNS, 'r', encoding='utf-8') as file:
    ordered_columns = json.load(file)['Completo']
    df = df[ordered_columns]
    assert df.columns.to_list() == ordered_columns, 'Error in step 12'

# Step 13 - Save the data in "Data/prepared.csv"
# Passo 13 - Salvar os dados em "Data/prepared.csv"
# df.to_csv(DATASET_SAVED, index=False)
