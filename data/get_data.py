import sqlalchemy
import pandas as pd


class FetchData:
    """Class to retrieve data from database."""
    def __init__(self):

        # create database engine
        self.engine = sqlalchemy.create_engine(
            url='postgresql://danielsuarez-mash@localhost/titanic_project?'
        )

        # initialise datasets
        self.train = None
        self.train_X = None
        self.train_y = None

        self.test = None
        self.test_X = None
        self.test_y = None

        self.ss = None

    def get_data(self):

        # get datasets from database
        self.train = pd.read_sql('SELECT * FROM train', self.engine)
        self.test = pd.read_sql('SELECT * FROM test', self.engine)
        self.ss = pd.read_sql('SELECT * FROM gender_submission', self.engine)

        self.train_y = self.train['survived']
        self.train_X = self.train.drop(columns='survived')

        return self.train_X, self.train_y, self.test, self.ss
