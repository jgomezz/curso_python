 -- CREAR UNA TABLA
CREATE TABLE employees (
    emp_no int(11) NOT NULL AUTO_INCREMENT, 
    first_name varchar(14) NOT NULL,
    last_name varchar(16) NOT NULL,
    gender enum('H','M') NOT NULL,
    birth_date date ,
    hire_date date ,
    PRIMARY KEY (emp_no)
 )

 -- ELIMINAR UNA TABLA
 DROP TABLE employees;
 
 -- INSERTAR UN REGISTRO
INSERT INTO employees (first_name, last_name, gender) 
VALUES ('Juan','Acosta','M');

INSERT INTO employees (first_name, last_name, gender) 
VALUES ('Maria','Melendez','M');

INSERT INTO employees (first_name, last_name, gender) 
VALUES ('Jose','Galez','H');

INSERT INTO employees (first_name, last_name, gender) 
VALUES ('Silvia','Montoya','M');

-- CONSULTAR REGISTROS DE UNA TABLA
SELECT * 
FROM employees;

-- CONSULTAR REGISTROS USANDO FILTROS
SELECT first_name, last_name, gender 
FROM employees
WHERE first_name = 'Juan'

SELECT first_name, last_name, gender 
FROM employees
WHERE first_name LIKE 'J%'

SELECT * 
FROM employees 
WHERE gender = 'M'; 

-- ACTUALIZAR UN REGISTRO 
UPDATE employees
SET gender = 'H' 
WHERE emp_no = 1

