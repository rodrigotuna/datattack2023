# #add the data_2016.csv and densidade_populacional.csv into a single file
# #the output file is data_2016_densidade.csv

import pandas as pd
from datetime import datetime

def add_density():
    #read the data_2016.csv file
    ocorrencias = pd.read_csv('../data/ocorrencias_clean.csv', sep = ',')

    #create a column based on the 


    # We replace the "," with "." to facilitate processing
    # ocorrencias['Latitude'] = pd.to_numeric(
    #     ocorrencias['Latitude'].str.replace(',', '.')
    # )
    # ocorrencias['Longitude'] = pd.to_numeric(
    #     ocorrencias['Longitude'].str.replace(',', '.')
    # )

    #read the densidade_populacional.csv file
    densidade_populacional = pd.read_csv('../data/densidade_populacional_2016.csv')

    densidade_populacional["Concelho"] = densidade_populacional["Concelho"].str.upper()

    print(densidade_populacional["Concelho"])


    #add the two files
    data_2016_densidade = pd.merge(ocorrencias, densidade_populacional, on='Concelho')

    #remove spaces from the column density
    data_2016_densidade['Densidade'] = data_2016_densidade['Densidade'].str.replace(' ', '')

    #convert Densidade to float
    data_2016_densidade['Densidade'] = data_2016_densidade['Densidade'].str.replace(',', '.').astype(float)

    #save the merged file
    data_2016_densidade.to_csv('../data/ocorrencias_clean_densidade.csv', index=False)

def add_weekday():
    #read the data_2016.csv file
    ocorrencias = pd.read_csv('../data/ocorrencias_clean.csv', sep = ',')

    #add a column with the day of the week
    ocorrencias['DataOcorrencia'] = pd.to_datetime(ocorrencias['DataOcorrencia'], format='%Y/%m/%d %H:%M:%S')

    # create a new column "weekday" and fill it with the weekday number
    ocorrencias['Weekday'] = ocorrencias['DataOcorrencia'].apply(lambda x: x.weekday())


    #save the merged file
    ocorrencias.to_csv('../data/ocorrencias_clean.csv', index=False)

def calculate_easter_date(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    month = (h + L - 7 * m + 114) // 31
    day = ((h + L - 7 * m + 114) % 31) + 1
    return f'{day:02d}/0{month}/{year}'

def add_holiday():
    pass

if __name__ == '__main__':
    add_density()
    #add_weekday()
