import pandas as pd
import numpy as np

def prepare_data(file_path):
    df = pd.read_csv(file_path)

    X = pd.get_dummies(df.drop(['customerID', 'Churn'], axis=1), drop_first=True)
    y = df['Churn']

    return X, y