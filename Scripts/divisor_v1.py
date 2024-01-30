import pandas as pd
import json

DATASET_LOADED = '../Data/prepared_dataset.csv'
JSON_ORDERED_COLUMNS = '../Dictionaries/ordered_columns.json'

DATASET_GERAL = '../Data/geral_dataset.csv'
DATASET_ANALISTA_DE_DADOS = '../Data/analista_de_dados_dataset.csv'
DATASET_ANALISTA_DE_BI = '../Data/analista_de_bi_dataset.csv'
DATASET_CIENTISTA_DE_DADOS = '../Data/cientista_de_dados_dataset.csv'
DATASET_ENGENHEIRO_DE_DADOS = '../Data/engenheiro_de_dados_dataset.csv'

# Step 1 - Load data from `Data/prepared_dataset.csv`
# Passo 1 - Carregar os dados de `Data/prepared_dataset.csv`
df = pd.read_csv(DATASET_LOADED)
assert not df.empty, 'Error in step 1'

# Step 2 - Create filters for dataframe rows
# Passo 2 - Criar filtros para linhas do dataframe
is_analista_de_dados = (df['Cargo'] == 'Analista de Dados') | (df['Atuacao'] == 'Análise de Dados')
is_analista_de_bi = (df['Cargo'] == 'Analista de BI/Analytics Engineer') | (df['Atuacao'] == 'Análise de Dados')
is_cientista_de_dados = (df['Cargo'] == 'Cientista de Dados') | (df['Atuacao'] == 'Ciência de Dados')
is_engenheiro_de_dados = (df['Cargo'] == 'Engenheiro de Dados') | (df['Atuacao'] == 'Engenharia de Dados')

# Step 3 - Load list of selected columns per dataframe
# Passo 3 - Carregar lista de colunas selecionadas por dataframe
columns_analista_de_dados = []
columns_analista_de_bi = []
columns_cientista_de_dados = []
columns_engenheiro_de_dados = []

with open(JSON_ORDERED_COLUMNS, 'r', encoding='utf-8') as file:
    columns_geral = json.load(file)['Geral']
    columns_analista_de_dados = json.load(file)['Analista de Dados']
    columns_analista_de_bi = json.load(file)['Analista de BI']
    columns_cientista_de_dados = json.load(file)['Cientista de Dados']
    columns_engenheiro_de_dados = json.load(file)['Engenheiro de Dados']

# Step 4 - Filter dataframes
# Passo 4 - Filtrar dataframes
df_geral = df[columns_geral]
df_analista_de_dados = df.loc[is_analista_de_dados, columns_analista_de_dados]
df_analista_de_bi = df.loc[is_analista_de_bi, columns_analista_de_bi]
df_cientista_de_dados = df.loc[is_cientista_de_dados, columns_cientista_de_dados]
df_engenheiro_de_dados = df.loc[is_engenheiro_de_dados, columns_engenheiro_de_dados]

# Step 5 - Save dataframes to files
# Passo 5 - Salvar dataframes em arquivos
df_geral.to_csv(DATASET_GERAL, index=False)
df_analista_de_dados.to_csv(DATASET_ANALISTA_DE_DADOS, index=False)
df_analista_de_bi.to_csv(DATASET_ANALISTA_DE_BI, index=False)
df_cientista_de_dados.to_csv(DATASET_CIENTISTA_DE_DADOS, index=False)
df_engenheiro_de_dados.to_csv(DATASET_ENGENHEIRO_DE_DADOS, index=False)
