#!/bin/bash

# pip install superset

# pip install apache-superset




# pip install --upgrade pip

curl -sS https://raw.githubusercontent.com/apache/superset/4.0.1/requirements/base.txt | \
       tail -n +10 | \
       awk -v ORS=" " '/^[A-z]/{print}' | \
       xargs pip install apache-superset==4.0.1

pip install clickhouse-connect

# superset устанавливает кривую версию cryptography и sqlalchemy...
# pip uninstall cryptography
# pip uninstall pyopenssl
# pip install cryptography==3.4.7
# pip install mysqlclient

# pip install sqlalchemy==1.2.18

# # # Load Examples
# # superset load_examples

# create Admin user, you can read these values from env or anywhere else possible
superset fab create-admin --username "admin" --firstname admin --lastname admin --email "admin@admin.com" --password "admin"

# Upgrading Superset metastore
superset db upgrade

# setup roles and permissions
superset init 



# Starting server
/bin/sh -c /usr/bin/run-server.sh
