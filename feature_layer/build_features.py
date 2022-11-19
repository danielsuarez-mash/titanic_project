from feature_layer import features
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class BuildFeatures:
    """Class to build features for ML model."""

    def __init__(self, data=None):

        # initialise data
        self.data = data
        self.data_prepared = None

        # create sequential steps for creating the age_group feature using Pipeline
        self.age_pipe = Pipeline(steps=[('age_imputer', SimpleImputer()),
                                 ('age_group_adder', features.AgeGroupAdder())])
        self.title_pipe = Pipeline(steps=[('title_adder', features.TitleGroupAdder()),
                                   ('title_ohe', OneHotEncoder(sparse=False))])

        # state steps which will transform simultaneously (apart from within age_pipe)
        self.ct = ColumnTransformer(transformers=[
                ('pclass_passthrough', 'passthrough', ['pclass']),
                ('age_feature', self.age_pipe, ['age']),
                ('sex_ohe', OneHotEncoder(), ['sex']),
                ('family_feature', features.FamilyFeatureAdder(solo_feature=True), ['parch', 'sibsp']),
                ('title_feature', self.title_pipe, ['name'])
            ], remainder='drop'
        )

    def process_data(self):

        # process data
        self.data_prepared = self.ct.fit_transform(self.data)

        return self.data_prepared

