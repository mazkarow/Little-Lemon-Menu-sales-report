# main.py

import create_database
import database_operations
import populate_tables

# Create database and tables
create_database

# Populate tables with initial data
populate_tables

# Example of running a stored procedure
employees = database_operations.run_stored_procedure('GetEmployeeList')
for employee in employees:
    print(employee)
