from sklearn.datasets import load_breast_cancer
import numpy as np


# Wisconsin Breast Cancer dataset records clinical measurements fo breast cancer tumors
# Each tumor is labeled as "benign" or "malignant"

cancer = load_breast_cancer()
print("cancer.keys(): \n{}".format(cancer.keys()))

# This prints out to show there are 569 data points with 30 features
print("Shape of cancer data: {}".format(cancer.data.shape))

print("Sample counts per class: \n{}".format(
    {n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}
))

print("Feature names: \n{}".format(cancer.feature_names))