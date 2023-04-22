# #add the data_2016.csv and densidade_populacional.csv into a single file
# #the output file is data_2016_densidade.csv

import pandas as pd

#read the data_2016.csv file
ocorrencias = pd.read_csv(
    'https://raw.githubusercontent.com/centraldedados/protecao_civil/master/data/anpc-2016.csv', 
    sep = ',', 
    on_bad_lines='skip'
)

# We replace the "," with "." to facilitate processing
ocorrencias['Latitude'] = pd.to_numeric(
    ocorrencias['Latitude'].str.replace(',', '.')
)
ocorrencias['Longitude'] = pd.to_numeric(
    ocorrencias['Longitude'].str.replace(',', '.')
)

#read the densidade_populacional.csv file
densidade_populacional = pd.read_csv('../data/densidade_populacional_2016.csv')

densidade_populacional["Concelho"] = densidade_populacional["Concelho"].str.upper()


#add the two files
data_2016_densidade = pd.merge(ocorrencias, densidade_populacional, on='Concelho')

#remove spaces from the column density
data_2016_densidade['Densidade'] = data_2016_densidade['Densidade'].str.replace(' ', '')

#convert Densidade to float
data_2016_densidade['Densidade'] = data_2016_densidade['Densidade'].str.replace(',', '.').astype(float)




#save the merged file
data_2016_densidade.to_csv('../data/data_2016_densidade.csv', index=False)



