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

def generate_sales_report():
    print("Generating sales report...")
    
    # Fetch total sales by each employee
    try:
        employee_sales = database_operations.total_sales_by_employee()
        if employee_sales:
            print("Total Sales by Employee:")
            for employee_sale in employee_sales:
                print(f"Employee: {employee_sale[0]}, Total Sales: {employee_sale[1]}")
        else:
            print("No sales data available.")
    except Exception as e:
        print(f"An error occurred while generating the sales report: {e}")

# Add a call to generate the sales report in the main execution block
if __name__ == "__main__":
    # Assume previous setup and population tasks have been run
    generate_sales_report()
