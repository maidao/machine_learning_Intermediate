from missing_value import *
from model import *
from train_test_split import *
from testing_parameter_for_model import *
from categorical_variables import *
from meteo_model import *

#X_train_meteo, X_test_meteo = missing_3_imputation_plus()

#X_train, X_test = cate_2_label_encoding()
X_train_meteo, X_test_meteo = cate_2_label_encoding()
#X_train, X_test = missing_3_imputation_plus()

#random_forest_regressor(X_train, X_test, y_train, y_test)
random_forest_regressor(X_train_meteo, X_test_meteo, y_train_meteo, y_test_meteo)



