from feature_layer.build_features import BuildFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import pandas as pd

# suppress warnings
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning)


class ModelTraining(BuildFeatures):

    def __init__(self, data_x, data_y):
        super().__init__()

        self.data_x = data_x
        self.data_y = data_y

        # classifiers
        self.log_reg = LogisticRegression()
        self.random_forest = RandomForestClassifier()

        # hyper-parameters
        self.params_log_reg = {
             'preprocessor__family_feature__solo_feature': [True, False],
             'classifier': [self.log_reg],
             'classifier__max_iter': [50, 100, 1000, 10000],
             'classifier__penalty': ['none', 'l2'],
             'classifier__C': [0.1, 1, 2, 5, 10, 20, 100]
        }
        self.params_random_forest = {
             'preprocessor__family_feature__solo_feature': [True, False],
             'classifier': [self.random_forest],
             'classifier__n_estimators': [10, 100, 200, 1000]
        }
        self.params = [self.params_log_reg, self.params_random_forest]

        # create pipeline
        self.pipeline = Pipeline(steps=[('preprocessor', self.ct), ('classifier', self.log_reg)])

        # configure data partitioning
        self.cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=45)

        # grid search
        self.gs = GridSearchCV(estimator=self.pipeline,
                               param_grid=self.params,
                               cv=self.cv,
                               scoring='accuracy',
                               error_score='raise')

        # initialise variables
        self.best_preproc = None
        self.best_estimator = None
        self.predictions = None

    def train(self):

        # fit model
        self.gs.fit(self.data_x, self.data_y)

        # print best score and hyperparameter combo
        print('Accuracy is:', self.gs.best_score_)
        print('Best parameters are:', self.gs.best_params_)
        self.best_preproc = self.gs.best_params_['preprocessor__family_feature__solo_feature']
        self.best_estimator = self.gs.best_params_['classifier']

        # export results
        pd.DataFrame(self.gs.cv_results_).to_csv('cross_validation_results.csv')

    def train_voting_clf(self):


