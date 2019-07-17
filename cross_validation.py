from sklearn.model_selection import cross_val_score
from train_test_split import *
import matplotlib.pyplot as plt
from pipeline import *


def get_score(max_leaf_nodes):

    my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                  ('model', DecisionTreeRegressor(random_state=5, max_leaf_nodes=max_leaf_nodes))])
    scores = -1 * cross_val_score(my_pipeline, X.astype('str'), y,
                                  cv=3, scoring='neg_mean_absolute_error')
    return scores.mean()

results = {}
for i in range(1,9):
    results[i*50] = get_score(i*50)

for i, k in results.items():
    print(i,':', k)
