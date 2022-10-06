#!/bin/bash

# see if we have the data already
FILE=competition_data/titanic.zip

if [ -f "$FILE" ]; then
  echo "$FILE already exists"
  file_exists=yes
else
  echo "$FILE does not exist"
  file_exists=no
fi

# download the data if necessary
if [ $file_exists = no ]; then

  # download data from Kaggle
  kaggle competitions download titanic -p ./competition_data

  # unzip file
  unzip ./competition_data/titanic.zip -d ./competition_data

  # remove zipped file
  rm ./competition_data/titanic.zip
fi



# get credentials
echo 'connecting to database'
read -p 'what is your username?' username
read -p 'what is the hostname?' hostname
read -p 'what is the name of the database?' database

echo 'connecting...'

# enter PostgreSQL terminal
psql -U $username -h $hostname -d $database -f ./sql-code/titanic_tables.sql