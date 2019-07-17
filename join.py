from train_test_split import *
from meteo_cleaned import *
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import LabelEncoder

join_data = pd.merge(data_jour, data_meteo,  how='right', on = ['jour','year','month','date'])
join_data = join_data[~join_data['frequentation'].isnull()]
join_data.to_csv('join_data.csv')
y_meteo = join_data.frequentation

X_meteo = join_data[['sur_place', 'livraison', 'semaine', 'jour', 'year', 'month', 'date', 'time',
                     'icon', 'precipintensity','temperature', 'humidity', 'pressure']]

X_train_meteo, X_test_meteo, y_train_meteo, y_test_meteo = train_test_split(X_meteo, y_meteo, train_size=0.9, random_state=2)

# Select categorical columns with relatively low cardinality (convenient but arbitrary)
categorical_cols = [cname for cname in X_train_meteo.columns if X_train_meteo[cname].nunique() < 10 and
                        X_train_meteo[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train_meteo.columns if X_train_meteo[cname].dtype in ['int64', 'float64']]

numerical_transformer = SimpleImputer(strategy='median')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

rf = RandomForestRegressor(n_estimators=50, min_samples_split=5, random_state=2, bootstrap=True)
my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', rf)
                             ])

my_pipeline.fit(X_train_meteo, y_train_meteo)
preds = my_pipeline.predict(X_test_meteo)
score = mean_absolute_error(y_test_meteo, preds)
print('MAE:', score)
print('RandomForestRegressor', my_pipeline.score(X_test_meteo, y_test_meteo))
output = pd.DataFrame({'vrai': y_test_meteo,
                       'predict': preds})
X_test_meteo['vrai'] = y_test_meteo
X_test_meteo['predict'] = preds
#X_test_meteo.to_csv('meteo_journee.csv')

print(X_test_meteo)


