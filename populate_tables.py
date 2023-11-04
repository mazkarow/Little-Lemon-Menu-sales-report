# populate_tables.py

import mysql.connector

from database_config import config

add_employee = ("INSERT INTO employees "
                "(name, position) "
                "VALUES (%s, %s)")

data_employee = ('John Doe', 'Server')

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Insert new employee
cursor.execute(add_employee, data_employee)
employee_id = cursor.lastrowid

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
