from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def random_forest_regressor(X_train, X_test, y_train, y_test):
    rf = RandomForestRegressor(n_estimators=100, min_samples_split=5, random_state=1, bootstrap=True)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    print('RandomForestRegressor', rf.score(X_test, y_test))


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