from sklearn.base import BaseEstimator, TransformerMixin


class FamilyFeatureAdder(BaseEstimator, TransformerMixin):
    """Class to calculate family size using the original parch and sibsp columns in the data."""

    def __init__(self, solo_feature=False):

        self.solo_feature = solo_feature
        pass

    def fit(self, X, y=None):

        return self

    def transform(self, X):

        # see if solo_feature is switched on
        if self.solo_feature == False:

            # create family size feature
            family_size = X.sum(axis=1).to_numpy().reshape(-1, 1)

            return family_size

        elif self.solo_feature == True:

            # create family size feature
            family_size = X.sum(axis=1)

            # create solo feature
            solo = family_size == 0
            solo = solo.map(arg={False: 0, True: 1}).to_numpy().reshape(-1, 1)

            return solo
