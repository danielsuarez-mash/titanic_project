import numpy as np
import pandas as pd
import subprocess
from data import get_data
from feature_layer import build_features
from model_training import model_training
from kaggle.api.kaggle_api_extended import KaggleApi

# authenticate with Kaggle for submission later on
api = KaggleApi()
api.authenticate()

# get data
data_class = get_data.FetchData()
train_X, train_y, test, ss = data_class.get_data()

# build preprocessing pipeline
feature_builder = build_features.BuildFeatures()

# train model
model_trainer = model_training.ModelTraining(data_x=train_X, data_y=train_y)
model_trainer.train()

# make predictions
make_submission = False
message = 'Added title group feature'

if make_submission:

    # # preprocess test set
    # processor_test = PreProcessor(feature_dict = feature_dict)
    # test_prepared, ohe_columns = processor_test.fit_transform(test)

    # make predictions
    predictions_test = model_trainer.gs.predict(test)

    # put submission together
    submission = np.c_[test['passengerid'].to_numpy(), predictions_test]
    submission_pandas = pd.DataFrame(submission[:, 1], index=submission[:, 0], columns=['Survived'])
    submission_pandas.index.name = 'PassengerId'
    submission_pandas.to_csv('submission.csv')

    # submit predictions
    api.competition_submit(file_name='submission.csv', message=message, competition='titanic')

    # see results
    print(api.competition_submissions(competition='titanic'))
else:

    # see previous results
    print(api.competition_submissions(competition='titanic'))
