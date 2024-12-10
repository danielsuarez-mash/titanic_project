# build class to filter attributes
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


class AgeGroupAdder(BaseEstimator, TransformerMixin):
    """Class to build age groups from age data."""

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        # creating age groups from age column
        age_intervals = (0, 7, 16, 30, 50, 100)
        age_groups = np.digitize(x=X.reshape(-1),
                                 bins=age_intervals).reshape(-1, 1)

        # one hot encode age_group
        age_encoder = OneHotEncoder(sparse=False)
        age_encoded = age_encoder.fit_transform(pd.DataFrame(age_groups))

        return age_encoded

