from sklearn.base import BaseEstimator, TransformerMixin


class TitleGroupAdder(BaseEstimator, TransformerMixin):
    """Class to build the title group feature."""

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # get title
        titles = X['name'].str.split(pat=',').apply(lambda x: x[1].split('.')[0])

        # build title group feature
        title_group = titles
        title_group.replace(to_replace=[' Miss', ' Mlle'], value='Unmarried female', inplace=True)
        title_group.replace(to_replace=[' Mrs', ' Mme'], value='Married female', inplace=True)
        title_group.replace(to_replace=[' Master', ' Dr', ' Rev', ' Major', ' Col', ' Don', ' Ms',
                                        ' Lady', ' Sir', ' Capt', ' the Countess', ' Jonkheer', ' Dona'],
                            value='Rare', inplace=True)

        return title_group.to_numpy().reshape(-1, 1)
