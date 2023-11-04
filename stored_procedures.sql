-- Create `GetEmployeeList` Stored Procedure
CREATE PROCEDURE `GetEmployeeList`()
BEGIN
    SELECT * FROM employees;
END;

-- Create `TotalSalesByEmployee` Stored Procedure
CREATE PROCEDURE `TotalSalesByEmployee`()
BEGIN
    SELECT e.name, SUM(p.price * s.quantity) AS total_sales
    FROM sales s
    JOIN employees e ON s.employee_id = e.employee_id
    JOIN products p ON s.product_id = p.product_id
    GROUP BY e.employee_id;
END;

