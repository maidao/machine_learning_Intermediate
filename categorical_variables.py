from train_test_split import *
from score_of_data import *
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

print("Categorical variables:")
print(object_cols)

def cate_1_drop():
    drop_X_train = X_train.select_dtypes(exclude=['object'])
    drop_X_test = X_test.select_dtypes(exclude=['object'])

    print("MAE from Approach 1 (Drop categorical variables):")
    print(score_dataset(drop_X_train, drop_X_test, y_train, y_test))

def cate_2_label_encoding():
    # Make copy to avoid changing original data
    label_X_train = X_train.copy()
    label_X_test = X_test.copy()

    # Apply label encoder to each column with categorical data
    label_encoder = LabelEncoder()
    for col in object_cols:
        label_X_train[col] = label_encoder.fit_transform(X_train[col].astype('str'))
        label_X_test[col] = label_encoder.transform(X_test[col].astype('str'))

    print("MAE from Approach 2 (Label Encoding):")
    print(score_dataset(label_X_train, label_X_test, y_train, y_test))

    return label_X_train, label_X_test

def cate_3_one_hot_encoding():
    # Apply one-hot encoder to each column with categorical data
    OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols].astype('str')))
    OH_cols_test = pd.DataFrame(OH_encoder.transform(X_test[object_cols].astype('str')))

    # One-hot encoding removed index; put it back
    OH_cols_train.index = X_train.index
    OH_cols_test.index = X_test.index

    # Remove categorical columns (will replace with one-hot encoding)
    num_X_train = X_train.drop(object_cols, axis=1)
    num_X_test = X_test.drop(object_cols, axis=1)

    # Add one-hot encoded columns to numerical features
    OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
    OH_X_test = pd.concat([num_X_test, OH_cols_test], axis=1)

    print("MAE from Approach 3 (One-Hot Encoding):")
    print(score_dataset(OH_X_train, OH_X_test, y_train, y_test))