from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from train_test_split import *
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
categorical_cols = [cname for cname in X_train.columns if X_train[cname].nunique() < 10 and
                        X_train[cname].dtype == "object"]

# Select numerical columns
numerical_cols = [cname for cname in X_train.columns if X_train[cname].dtype in ['int64', 'float64']]

my_cols = categorical_cols + numerical_cols
X_train = X_train[my_cols].copy().astype('str')
X_test = X_test[my_cols].copy().astype('str')

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
rf = RandomForestRegressor(n_estimators=100, min_samples_split=5, random_state=2, bootstrap=True)
tree = DecisionTreeRegressor(random_state=5, max_leaf_nodes=100)

my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('model', rf)
                             ])
my_pipeline.fit(X_train, y_train)
preds = my_pipeline.predict(X_test)
score = mean_absolute_error(y_test, preds)
print('MAE:', score)
print('RandomForestRegressor', my_pipeline.score(X_test, y_test))
output = pd.DataFrame({'vrai': y_test,
                       'predict': preds})
#output.to_csv('pipeline_prediction.csv', index=False)