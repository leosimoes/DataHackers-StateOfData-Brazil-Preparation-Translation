# DataHackers - State of Data Brazil - Data Preparation and Translation
Project for creating scripts for the preparation (cleaning and organization) of State of Data Brazil's data, 
as well as the translation of this data from Portuguese to English.


## Files
The project files are:
- `Data/State_of_data_2023.csv`: dataset that must be downloaded from
    [Kaggle](https://www.kaggle.com/datahackers/datasets "Kaggle - Data Hackers - Datasets");
- `Dictionaries/mapped_columns_values.json`: contains the column names (outermost keys) with their values
    originals (innermost keys) and their new values (innermost values);
- `Dictionaries/ordered_columns.json`: contains the reference name to the dataset to be created (keys),
    and list of selected columns (values);
- `Dictionaries/selected_columns.json`: contains the selected columns with their codes (keys) and their names (values)
- `Dictionaries/translations_of_modified_column_names.json`: contains the translations of the column names in Portuguese
    (keys) for English (values);
- `Dictionaries/translations_of_modified_column_values.json` contains the translations of the column values in Portuguese
    (keys) for English (values);
- `Scripts/divisor_v1.py`: python script to divide the data `Data/prepared_dataset.csv` into other datasets;
- `Scripts/divisor_v2.py`: python script to divide the data `Data/translated_dataset.csv` into other datasets;
- `Scripts/preparator.py`: python script to prepare the data in `Data/State_of_data_2023.csv` and save it to
   `Data/prepared.csv`;
- `Scripts/preselector.py`: script select some of the columns from `Data/State_of_data_2023.csv` and save them in
   `Dictionaries/selected_columns.json` and `Dictionaries/ordered_columns.json`;
- `Scripts/translator.py`: python script to translate the data in `Data/prepared.csv` and save it to
   `Data/translated_dataset.csv`.


## Data Preparation
The data preparation steps using `Scripts/preparator.py` were:
1. Load data from `Data/State_of_data_2023.csv`;
2. Rename columns to question codes;
3. Select the columns according to the keys in `Dictionaries/selected_columns.json`;
4. Rename the columns according to the values in `Dictionaries/selected_columns.json`;
5. Check that there are no repetitions of column names;
6. Remove unwanted lines:
     - duplicates;
     - with missing values in `'id'` or `'Idade'`;
7. Convert numeric columns, except "Idade", to string type (object);
8. Fill in missing string values with `"Não Informado"`;
9. Format values (using some string function or `Dictionaries/mapped_columns_values.json`):
     - remove white spaces at the beginning and end;
     - except for `"Idade"`, convert `"1"` and `"1.0"` to `"Sim"` and `"0"` and `"0.0"` to `"Não"`;
     - adjust `"Faixa salarial"` values;
     - adjust values for `"Cargo Atual"`;
10. Create new derived columns (using `Dictionaries/mapped_columns_values.json`):
     - `"Campo de Atuação Geral"`: with values `"Dados"`, `"Outras"` and `"Não Informado"`;
     - `"Faixa salarial ($)"`: using `"Faixa salarial"`;
11. Check that there are no missing values;
12. Order the dataframe columns according to `Dictionaries/ordered_columns.json`;
13. Save the data in `Data/prepared.csv`.


## Data translation
The data translation steps were:
1. Load the data into `Data/prepared_dataset.csv`;
2. Load the translations of the column names in `Dictionaries/translations_of_modified_column_names.json`;
3. Translate column names;
4. Load the translations of the column values in `Dictionaries/translations_of_modified_column_values.json`;
5. Translate the column values;
6. Save the data in `Data/translated_dataset.csv`.


## Data division
The data division steps were:
1. Load data from `Data/prepared_dataset.csv`;
2. Create filters for dataframe rows;
3. Load list of selected columns by dataframe using `Dictionaries/ordered columns.json`;
4. Filter dataframes;
5. Save dataframes to files.


## References
Kaggle - Data Hackers - Datasets:
https://www.kaggle.com/datahackers/datasets