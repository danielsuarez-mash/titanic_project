import zipfile
import pandas as pd


# authenticate connection with Kaggle API
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# download competition data
api.competition_download_files('titanic')

# open zip file
with zipfile.ZipFile(file = 'titanic.zip') as my_zip:
    with my_zip.open(name = 'train.csv') as train_file:
        train = pd.read_csv(train_file)
    with my_zip.open(name = 'test.csv') as test_file:
        test = pd.read_csv(test_file)
    with my_zip.open(name = 'gender_submission.csv') as gender_sub:
        eg_submission = pd.read_csv(gender_sub)
