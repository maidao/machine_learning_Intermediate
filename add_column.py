import pandas as pd

def add_column_semaine(data_jour):
    semaine = []
    for i in data_jour.jour_semaine:
        if i == '1 - Lundi':
            semaine.append(i.replace('1 - Lundi', '1'))
        elif i == '2 - Mardi':
            semaine.append(i.replace('2 - Mardi', '2'))
        elif i == '3 - Mercredi':
            semaine.append(i.replace('3 - Mercredi', '3'))
        elif i == '4 - Jeudi':
            semaine.append(i.replace('4 - Jeudi', '4'))
        elif i == '5 - Vendredi':
            semaine.append(i.replace('5 - Vendredi', '5'))
        elif i == '6 - Samedi':
            semaine.append(i.replace('6 - Samedi', '6'))
        elif i == '7 - Dimanche':
            semaine.append(i.replace('7 - Dimanche', '7'))

    data_jour['semaine'] = semaine
    return data_jour


def add_column_jour(data_jour):
    jour = []
    for i in data_jour.midi_soir:
        if i == '1 - Matin':
            jour.append(i.replace('1 - Matin', '1'))
        elif i == '2 - Midi':
            jour.append(i.replace('2 - Midi', '2'))
        elif i == '3 - Après-midi':
            jour.append(i.replace('3 - Après-midi', '3'))
        elif i == '4 - Soir':
            jour.append(i.replace('4 - Soir', '4'))
        else:
            jour.append(None)

    data_jour['jour'] = jour

    return data_jour

def add_column_year(data_jour):
    data_jour['date_commande'] = pd.to_datetime(data_jour['date_commande'])
    data_jour['year'] = data_jour['date_commande'].dt.year
    return data_jour

def add_column_month(data_jour):
    data_jour['date_commande'] = pd.to_datetime(data_jour['date_commande'])
    data_jour['month'] = data_jour['date_commande'].dt.month
    return data_jour

def add_column_date(data_jour):
    data_jour['date_commande'] = pd.to_datetime(data_jour['date_commande'])
    data_jour['date'] = data_jour['date_commande'].dt.day
    return data_jour