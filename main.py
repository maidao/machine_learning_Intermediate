from missing_value import *
from model import *
from train_test_split import *
from testing_parameter_for_model import *
from categorical_variables import *


X_train, X_test = cate_2_label_encoding()
#X_train, X_test = missing_3_imputation_plus()

random_forest_regressor(X_train, X_test, y_train, y_test)
decision_tree_regressor(X_train, X_test, y_train, y_test)
k_neighbors_regressor(X_train, X_test, y_train, y_test)


