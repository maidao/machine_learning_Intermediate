from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

import pandas as pd

def random_forest_regressor(X_train, X_test, y_train, y_test):
    rf = RandomForestRegressor(n_estimators=100, min_samples_split=5, random_state=1, bootstrap=True)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print('RandomForestRegressor', rf.score(X_test, y_test))

    score = pd.DataFrame({'vrai': y_test,
                  'predict': y_pred})

    """
    X_test['vrai'] = y_test
    X_test['predict'] = y_pred
    X_test = X_test.groupby(X_test['jour']).mean()
    plt.figure("midi soir")

    plt.plot(X_test.index, X_test.predict)
    plt.plot(X_test.index, X_test.vrai)
    # plt.savefig('midi_soir.png', bbox_inches='tight')
    plt.show()
    """


def decision_tree_regressor(X_train, X_test, y_train, y_test):
    tree = DecisionTreeRegressor(random_state=5, max_leaf_nodes=100)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    print('DecisionTreeRegressor', tree.score(X_test, y_test))


def k_neighbors_regressor(X_train, X_test, y_train, y_test):
    knn = KNeighborsRegressor(n_neighbors=19, leaf_size=36)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print('KNeighborsRegressor', knn.score(X_test, y_test))

def gradient_boosting(X_train, X_test, y_train, y_test):
    boost = XGBRegressor(n_estimators=500, learning_rate=0.05, n_jobs=4)
    boost.fit(X_train, y_train, early_stopping_rounds=20,
                 eval_set=[(X_test, y_test)],
                 verbose=False)
    y_pred = boost.predict(X_test)
    print('XGBRegressor', boost.score(X_test, y_test))