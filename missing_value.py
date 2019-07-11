from train_test_split import *
from score_of_data import *
from sklearn.impute import SimpleImputer


cols_with_missing = [col for col in X_train.columns
                     if X_train[col].isnull().any()]

missing_val_count_by_column = (X_train.isnull().sum())

print("missing column:", cols_with_missing)
print(missing_val_count_by_column[missing_val_count_by_column > 0])

def missing_1_drop():

    reduced_X_train = X_train.drop(cols_with_missing, axis=1)
    reduced_X_test = X_test.drop(cols_with_missing, axis=1)

    print("MAE from Approach 1 (Drop columns with missing values):")
    print(score_dataset(reduced_X_train, reduced_X_test, y_train, y_test))

def missing_2_imputation():
    my_imputer = SimpleImputer()
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_test = pd.DataFrame(my_imputer.transform(X_test))

    # Imputation removed column names; put them back
    imputed_X_train.columns = X_train.columns
    imputed_X_test.columns = X_test.columns

    print("MAE from Approach 2 (Imputation):")
    print(score_dataset(imputed_X_train, imputed_X_test, y_train, y_test))

def missing_3_imputation_plus():
    X_train_plus = X_train.copy()
    X_test_plus = X_test.copy()

    # Make new columns indicating what will be imputed
    for col in cols_with_missing:
        X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
        X_test_plus[col + '_was_missing'] = X_test_plus[col].isnull()

    # Imputation
    my_imputer = SimpleImputer()
    imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
    imputed_X_test_plus = pd.DataFrame(my_imputer.transform(X_test_plus))

    # Imputation removed column names; put them back
    imputed_X_train_plus.columns = X_train_plus.columns
    imputed_X_test_plus.columns = X_test_plus.columns

    print("MAE from Approach 3 (An Extension to Imputation):")
    print(score_dataset(imputed_X_train_plus, imputed_X_test_plus, y_train, y_test))

    return imputed_X_train_plus, imputed_X_test_plus