-- stored_procedures.sql

DELIMITER $$

CREATE PROCEDURE `GetEmployeeList`()
BEGIN
    SELECT * FROM employees;
END$$

DELIMITER ;
