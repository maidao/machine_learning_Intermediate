from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def parameter_random_forest(X_train, X_test, y_train, y_test):

    # Define the models
    model_1 = RandomForestRegressor(n_estimators=100, min_samples_split=5, random_state=1)
    model_2 = RandomForestRegressor(n_estimators=200, min_samples_split=10)
    model_3 = RandomForestRegressor(n_estimators=300, min_samples_split=15, min_samples_leaf=3, bootstrap=True)
    model_4 = RandomForestRegressor(n_estimators=300,random_state=4, min_samples_leaf=5, bootstrap=True)
    model_5 = RandomForestRegressor(n_estimators=300, max_depth=100, bootstrap=True)
    model_6 = RandomForestRegressor(n_estimators=400, min_samples_split=20, random_state=0, min_samples_leaf=4,
                                    max_features='sqrt', max_depth=90, bootstrap=True)

    models = [model_1, model_2, model_3, model_4, model_5, model_6]

    def score_model(model, X_t=X_train, X_v=X_test, y_t=y_train, y_v=y_test):
        model.fit(X_t, y_t)
        preds = model.predict(X_v)
        return mean_absolute_error(y_v, preds)

    for i in range(0, len(models)):
        mae = score_model(models[i])
        print("Model %d MAE: %d" % (i + 1, mae))

def parameter_tree(X_train, X_test, y_train, y_test):

    def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
        model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
        model.fit(train_X, train_y)
        preds_val = model.predict(val_X)
        mae = mean_absolute_error(val_y, preds_val)
        return (mae)

    for max_leaf_nodes in [2, 5, 25, 50, 100, 250, 500]:
        my_mae = get_mae(max_leaf_nodes, X_train, X_test, y_train, y_test)
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_nodes, my_mae))

