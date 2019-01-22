
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.externals import joblib

# scale_max = pd.read_csv('hypodata_max_for_scaling.csv')
#
# scale_min = pd.read_csv('hypodata_min_for_scaling.csv')
#
# model = joblib.load("neural_network_numeric_data_model3.pkl")
#
# y_classes = {'negative': 0,
#            'primary hypothyroid': 1,
#             'compensated hypothyroid':2,
#            'secondary hypothyroid': 3 }
#
# # Only 2 instances of class 3 in the training set. Not in the test set.
#
# data1 = [{"age": 35.0, "TSH": 4.672, "T3": 2.025, "TT4": 109.072, "T4U": 0.998, "FTI": 110.788},
#                   {"age": 63.0, "TSH": 3.500, "T3": 2.500, "TT4": 108.000, "T4U": 0.960, "FTI": 113.000}]
#
# data2 = [{"age": 35.0, "TSH": 4.672, "T3": 2.025, "TT4": 109.072, "T4U": 0.998, "FTI": 110.788}]


def hypothyroid_pred(data_lst):
    scale_max = pd.read_csv('hypodata_max_for_scaling.csv')
    scale_min = pd.read_csv('hypodata_min_for_scaling.csv')
    model = joblib.load("neural_network_numeric_data_model3.pkl")
    hypothyroid_classes = {0: 'No hypothyroid disease',
               1: 'primary hypothyroid',
               2: 'compensated hypothyroid',
               3: 'secondary hypothyroid'}
    data_arr = np.array(data_lst).reshape(-1, 6)
    d_scaled = np.subtract(data_arr,scale_min.values)/np.subtract(scale_max.values, scale_min.values)
    pred1 = model.predict(d_scaled)
    result = []
    for i in pred1:
        result.append(hypothyroid_classes[i])
    return result
