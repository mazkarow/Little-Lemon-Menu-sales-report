# database_operations.py

import mysql.connector

from database_config import config


def run_stored_procedure(procedure_name, parameters=None):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    result = None
    try:
        cursor.callproc(procedure_name, parameters if parameters else ())
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
    except mysql.connector.Error as err:
        print(err)
    finally:
        cursor.close()
        cnx.close()
    return result


def total_sales_by_employee():
    return run_stored_procedure('TotalSalesByEmployee')

