import mysql.connector
from mysql.connector import Error

from database_config import config


def insert_employee(employee_data):
    """
    Inserts a new employee into the database.
    :param employee_data: A tuple containing employee data.
    """
    try:
        # SQL query to add an employee
        add_employee_query = (
            "INSERT INTO employees (name, position) "
            "VALUES (%s, %s)"
        )

        # Establish a new connection to the database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Execute the SQL command to insert a new employee
        cursor.execute(add_employee_query, employee_data)

        # Commit the transaction to save the new employee record
        connection.commit()
        
        # Obtain the ID of the newly inserted employee
        employee_id = cursor.lastrowid
        print(f"Inserted employee with ID: {employee_id}")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Data tuple for the new employee
new_employee = ('John Doe', 'Server')

# Call the function to insert a new employee
insert_employee(new_employee)

