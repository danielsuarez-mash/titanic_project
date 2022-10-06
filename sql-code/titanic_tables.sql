--create train table
 DROP TABLE IF EXISTS TRAIN;
 CREATE TABLE train (
    passengerid INT PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    sex TEXT,
    age NUMERIC,
    sibsp NUMERIC,
    parch NUMERIC,
    ticket TEXT,
    fare NUMERIC,
    cabin TEXT,
    embarked TEXT
);

-- insert data into train table
\copy train FROM './competition_data/train.csv' DELIMITER ',' CSV HEADER;


-- create test table
DROP TABLE IF EXISTS test;
 CREATE TABLE test (
    passengerid INT PRIMARY KEY,
    pclass INT,
    name TEXT,
    sex TEXT,
    age NUMERIC,
    sibsp NUMERIC,
    parch NUMERIC,
    ticket TEXT,
    fare NUMERIC,
    cabin TEXT,
    embarked TEXT
);

-- insert data into test table
\copy test FROM './competition_data/test.csv' DELIMITER ',' CSV HEADER;

-- create gender_submission table
DROP TABLE IF EXISTS gender_submission;
 CREATE TABLE gender_submission (
    passengerid INT PRIMARY KEY,
    survived INT
);

-- insert data into gender_submission table
\copy gender_submission FROM './competition_data/gender_submission.csv' DELIMITER ',' CSV HEADER;