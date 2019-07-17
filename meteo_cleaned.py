from clean_data import *
from add_column import *
import numpy as np

data_meteo = read_data('meteo_heure.csv')
data_meteo = add_column_heure(data_meteo)
data_meteo = clean_meteo(data_meteo)
data_meteo = add_column_year_meteo(data_meteo)
data_meteo = add_column_month_meteo(data_meteo)
data_meteo = add_column_date_meteo(data_meteo)
data_meteo = add_label_heure(data_meteo)
#data_meteo = add_label_midi_soir(data_meteo)
print(data_meteo)


data_meteo[['jour','year','month','date','time']] = data_meteo[['jour','year','month','date','time']].astype(str)