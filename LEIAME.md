# DataHackers - State of Data Brazil - Preparação e Tradução dos Dados
Projeto voltado à criação de scripts para a preparação (limpeza e organização) dos dados do State of Data Brazil, 
bem como à tradução desses dados do português para o inglês.


## Arquivos
Os arquivos do projeto são:
- `Data/State_of_data_2023.csv`: dataset que deve ser baixado do 
   [Kaggle](https://www.kaggle.com/datahackers/datasets "Kaggle - Data Hackers - Datasets");
- `Dictionaries/mapped_columns_values.json`: contém os nomes de colunas (chaves mais externas) com seus valores 
   originais (chaves mais internas) e seus novos valores (valores mais internos);
- `Dictionaries/ordered_columns.json`: contém o nome de referência ao dataset a ser criado (chaves), 
   e lista de colunas selecionadas (valores);
- `Dictionaries/selected_columns.json`: contém as colunas selecionadas com seus códigos (chaves) e seus nomes (valores)
- `Dictionaries/translations_of_modified_column_names.json`: contém as traduções dos nomes das colunas em português
   (chaves) para o inglês (valores);
- `Dictionaries/translations_of_modified_column_values.json` contém as traduções dos valores das colunas em português
   (chaves) para o inglês (valores);
- `Scripts/preparator.py`: script python para preparar os dados em `Data/State_of_data_2023.csv` e salvá-los em 
  `Data/prepared.csv`;
- `Scripts/translator.py`: script python para traduzir os dados em `Data/prepared.csv` e salvá-los em 
  `Data/translated_dataset.csv`.


## Preparação dos Dados
As etapas de preparação dos dados usando `Scripts/preparator.py` foram:
1. Carregar os dados de `Data/State_of_data_2023.csv`;
2. Renomear colunas para os códigos das perguntas;
3. Selecionar as colunas de acordo com as chaves em `Dictionaries/selected_columns.json`;
4. Renomear as colunas de acordo com os valores em `Dictionaries/selected_columns.json`;
5. Verificar se não há repetição de nomes colunas;
6. Remover linhas indesejadas:
    - duplicadas;
    - com valores ausentes em 'id' ou 'idade';
7. Converter colunas numéricas, exceto "Idade", para o tipo string (object);
8. Preencher valores ausentes do tipo string com `"Não Informado"`; 
9. Formatar valores (usando alguma função de string ou `Dictionaries/mapped_columns_values.json`):
    - remover espaços em branco no início e no final;
    - exceto para `"Idade"`, converter `"1"` e `"1.0"` para "Sim" e `"0"` e `"0.0"` para `"Não"`;
    - ajustar valores de `"Faixa salarial"`;
    - ajustar valores de `"Cargo Atual"`;
10. Criar novas colunas derivadas (usando `Dictionaries/mapped_columns_values.json`):
    - `"Campo de Atuação Geral"`: com valores `"Dados"`, `"Outra"` e `"Não Informado"`;
    - `"Faixa salarial ($)"`: usando `"Faixa salarial"`;
11. Verificar se não há valores ausentes; 
12. Ordenar as colunas do dataframe de acordo com `Dictionaries/ordered_columns.json`;
13. Salvar os dados em `Data/prepared.csv`.


## Tradução dos dados
As etapas de tradução dos dados foram:
1. Carregar os dados em `Data/prepared_dataset.csv`;
2. Carregar as traduções dos nomes das colunas em `Dictionaries/translations_of_modified_column_names.json`;
3. Traduzir os nomes das colunas;
4. Carregar as traduções dos valores das colunas em `Dictionaries/translations_of_modified_column_values.json`;
5. Traduzir os valores das colunas;
6. Salvar os dados em `Data/translated_dataset.csv`.


## Referências 
Kaggle - Data Hackers - Datasets:
https://www.kaggle.com/datahackers/datasets