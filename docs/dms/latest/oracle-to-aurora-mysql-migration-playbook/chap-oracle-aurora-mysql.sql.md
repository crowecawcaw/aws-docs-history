# Oracle DBMS_OUTPUT and MySQL SELECT

Oracle `DBMS_OUTPUT` is a package that lets you send messages from stored procedures, functions, and anonymous blocks to a message buffer. MySQL `SELECT` is a statement used to retrieve data from one or more tables in a MySQL database. The following sections will provide details on using `DBMS_OUTPUT` in Oracle and `SELECT` statements in MySQL with AWS DMS.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                              | Key differences                                                         |
| -------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Three star feature compatibility | No automation                      | [DBMS_OUTPUT](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.output "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.output") | Different paradigm and syntax requires application and drivers rewrite. |

## Oracle usage

The Oracle `DBMS_OUTPUT` package is typically used for debugging or for displaying output messages from PL/SQL procedures.

### Examples

In the following example, `DBMS_OUTPUT` with `PUT_LINE` is used with a combination of bind variables to dynamically construct a string and print a notification to the screen from within an Oracle PL/SQL procedure. In order to display notifications on to the screen, you must configure the session with `SET SERVEROUPUT ON`.

```
SET SERVEROUTPUT ON
DECLARE
CURSOR c1 IS
SELECT last_name, job_id FROM employees
WHERE REGEXP_LIKE (job_id, 'S[HT]_CLERK')
ORDER BY last_name;
v_lastname employees.last_name%TYPE; -- variable to store last_name
v_jobid employees.job_id%TYPE; -- variable to store job_id
BEGIN
OPEN c1;
LOOP -- Fetches 2 columns into variables
FETCH c1 INTO v_lastname, v_jobid;
DBMS_OUTPUT.PUT_LINE ('The employee id is:' || v_jobid || ' and his last name is:' ||
v_lastname);
EXIT WHEN c1%NOTFOUND;
END LOOP;
CLOSE c1;
END;
```

In addition to the output of information on the screen, the `PUT` and `PUT_LINE` procedures in the `DBMS_OUTPUT` package enable you to place information in a buffer that can be read later by another PL/SQL procedure or package. You can display the previously buffered information using the `GET_LINE` and `GET_LINES` procedures.

For more information, see [DBMS_OUTPUT](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_OUTPUT.html#GUID-C1400094-18D5-4F36-A2C9-D28B0E12FD8C "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_OUTPUT.html#GUID-C1400094-18D5-4F36-A2C9-D28B0E12FD8C") in the _Oracle documentation_.

## MySQL usage

You can use `SELECT` to display output messages in Aurora MySQL.

### Examples

```
delimiter //

CREATE PROCEDURE emp_counter (param1 INTEGER)
BEGIN
SELECT "" 'OUTPUT: Before count';
SELECT COUNT(*) INTO param1 FROM EMPS;
SELECT concat('Employees count: ', param1) as '';
SELECT "" 'OUTPUT: After count';
END//

delimiter ;
call simpleproc1(1);

OUTPUT: Before count
1 row in set (0.19 sec)

Employees count: 8
1 row in set (0.20 sec)

OUTPUT: After count
1 row in set (0.21 sec)

Query OK, 0 rows affected (0.22 sec)
```

###### Note

Use double quotation marks with `SELECT` for cleaner display. Otherwise, messages are displayed twice, both as header and value.

For more information, see [SELECT Statement](https://dev.mysql.com/doc/refman/5.7/en/select.html "https://dev.mysql.com/doc/refman/5.7/en/select.html") in the _MySQL documentation_.
