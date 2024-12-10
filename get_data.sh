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



## get credentials
#echo 'connecting to database'
#read -p 'what is your username?' username
#read -p 'what is the hostname?' hostname
#read -p 'what is the name of the database?' database

# get database credentials
parse_yaml() {
   local prefix=$2
   local s='[[:space:]]*' w='[a-zA-Z0-9_]*' fs=$(echo @|tr @ '\034')
   sed -ne "s|^\($s\)\($w\)$s:$s\"\(.*\)\"$s\$|\1$fs\2$fs\3|p" \
        -e "s|^\($s\)\($w\)$s:$s\(.*\)$s\$|\1$fs\2$fs\3|p"  $1 |
   awk -F$fs '{
      indent = length($1)/2;
      vname[indent] = $2;
      for (i in vname) {if (i > indent) {delete vname[i]}}
      if (length($3) > 0) {
         vn=""; for (i=0; i<indent; i++) {vn=(vn)(vname[i])("_")}
         printf("%s%s%s=\"%s\"\n", "'$prefix'",vn, $2, $3);
      }
   }'
}

eval "$(parse_yaml config.yaml)"
echo "Username: $user"
echo "host: $host"
echo "database: $database"

echo 'connecting...'

# execute SQL commands in PSQL
psql -U $user -h $host -d $database -f ./sql-code/titanic_tables.sql