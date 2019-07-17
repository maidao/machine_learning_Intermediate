from sklearn.model_selection import train_test_split
from clean_data import *
from add_column import *

data_jour = read_data('reporting_jour.csv')
data_jour = clean_data(data_jour)
data_jour = add_column_semaine(data_jour)
data_jour = add_column_jour(data_jour)
data_jour = add_column_year(data_jour)
data_jour = add_column_month(data_jour)
data_jour = add_column_date(data_jour)
data_jour[['jour', 'year','month','date']] = data_jour[['jour', 'year','month','date']].astype(str)
data_jour = data_jour.drop(['date_commande', 'midi_soir', 'jour_semaine', 'type_vente'], axis=1)

y = data_jour.frequentation
X = data_jour.drop('frequentation', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=2)
