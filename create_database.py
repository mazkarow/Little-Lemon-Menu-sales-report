# create_database.py

import mysql.connector
from mysql.connector import errorcode

from database_config import config

DB_NAME = 'little_lemon'

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `employee_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(255) NOT NULL,"
    "  `position` varchar(255) NOT NULL,"
    "  PRIMARY KEY (`employee_id`)"
    ") ENGINE=InnoDB")

# ... Similarly define other tables

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

# Connect to the MySQL server and create the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# Create tables
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
