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
    data = data.drop(data[(data['frequentation'] == 0.0) & (data['midi_soir'].isnull())].index)
    drop_cols = ['ca_ttc', 'ca_ht','nb_commandes']
    data = data.drop(drop_cols, axis = 1)
    return data

def clean_meteo(data_meteo):
    #data_meteo = data_meteo[(data_meteo['heure'] == 12) | (data_meteo['heure'] == 20)]
    data_meteo = data_meteo[(data_meteo['heure'] == 10) | (data_meteo['heure'] == 12)
                            | (data_meteo['heure'] == 16) | (data_meteo['heure'] == 20)]

    return data_meteo



