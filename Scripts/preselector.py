# Script to select columns of State of Data Brazil's dataset
# Author: Leonardo Simões

import json
import pandas as pd

DATASET_LOADED = '../Data/State_of_Data_2022.csv'
JSON_SELECTED_COLUMNS = '../Dictionaries/selected_columns.json'
JSON_ORDERED_COLUMNS = '../Dictionaries/ordered_columns.json'

COLUMNS_EXTRAS = {
    'P1_i_1': 'uf onde mora',
    'P1_i_2': 'Regiao onde mora',
    'P1_a_1': 'Faixa idade'
}

# Step 1 - Load data from `Data/State_of_data_2023.csv`
# Passo 1 - Carregar os dados de `Data/State_of_data_2023.csv`
df = pd.read_csv(DATASET_LOADED)
assert not df.empty, 'Error in step 1'

# Step 2 -Create a dict where the question code is the key and the question name is the value
# Passo 2 - Criar um dict onde o código da pergunta é chave e o nome da pergunta é o valor
filtered_columns = [col for col in df.columns.to_list() if col.count('_') <= 1]
assert filtered_columns, 'Error in step 2'
columns_dict = {pair[0][2:].strip(): pair[1][:-2].strip() for pair in [line.split("', '") for line in filtered_columns]}
assert columns_dict, 'Error in step 2'

# Step 3 - Add some extra column names
# Passo 3 - Adicionar alguns nomes extra de colunas
if columns_dict and COLUMNS_EXTRAS:
    columns_dict.update(COLUMNS_EXTRAS)

# Step 4 - Order dict values by key (question code)
# Passo 4 - Ordenar os valores do dict pela chave (código da pergunta)
columns_dict = dict(sorted(columns_dict.items()))

# Step 5 - Save dict contents to a json file
# Passo 5 - Salvar o conteúdo do dict em um arquivo json
with open(JSON_SELECTED_COLUMNS, 'w') as file:
    json.dump(columns_dict, file, indent=4)

# Step 6 - Save the contents of the dict keys to a json file
# Passo 6 - Salvar o conteúdo das chaves do dict em um arquivo json
with open(JSON_ORDERED_COLUMNS, 'w') as file:
    columns = list(columns_dict.values())
    json.dump(columns, file, indent=4)
