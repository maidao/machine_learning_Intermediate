import pandas as pd

def read_data(path):
    data = pd.read_csv(path, low_memory=False, sep=';')
    return data

def info_data(data):
    print(data.columns)
    print('len of data: ', len(data))
    print('shape of data:', data.shape)
    print(data.info())
    print('Statistics:', data.describe())
    print(data.head(5))

def clean_data(data):
    data = data[data['type_vente'] == 'CA']
    drop_cols = ['ca_ttc', 'ca_ht']
    data = data.drop(drop_cols, axis = 1)
    return data



