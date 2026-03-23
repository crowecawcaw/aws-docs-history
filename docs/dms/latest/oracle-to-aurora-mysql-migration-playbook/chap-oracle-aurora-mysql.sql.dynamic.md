# Oracle DBMS_SQL

When working with Oracle databases migrated to AWS you can use `DBMS_SQL` to maintain application functionality to run dynamic SQL statements. You can also use `DBMS_SQL` for automating database operations. The following sections cover the details of using `DBMS_SQL` with code examples.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                             |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------------------------------------------------------------------- |
| One star feature compatibility | One star automation level          | N/A                       | Different paradigm and syntax will require application and drivers rewrite. |

## Oracle usage

The `DBMS_SQL` package provides an interface to parse and run dynamic SQL statements, DML commands, and DDL commands (usually from within a PL/SQL package, function, or procedure). `DBMS_SQL` enables very granular control of SQL cursors and can improve cursor performance in certain cases.

### Examples

The following examples demonstrates how to manually open, parse, bind, run, and fetch data from a cursor using the `DBMS_SQL` PL/SQL interface.

1. Use `DBMS_SQL.OPEN_CURSOR` to open a blank cursor and return the cursor handle.
2. Use `DBMS_SQL.PARSE` to parse the statement into the referenced cursor.
3. Use `DBMS_SQL.BIND_VARIABLES` to attach the value for the bind variable with the cursor.
4. Use `DBMS_SQL.EXECUTE` to run the cursor.
5. Use `DBMS_SQL.GET_NEXT_RESULT` to iterate over the cursor, fetching the next result.
6. Use `DBMS_SQL.CLOSE_CURSOR` to close the cursor.

```
DECLARE
c1           INTEGER;
rc1          SYS_REFCURSOR;
n            NUMBER;
first_name   VARCHAR2(50);
last_name    VARCHAR2(50);
email        VARCHAR2(50);
phone_number VARCHAR2(50);
job_title    VARCHAR2(50);
start_date   DATE;
end_date     DATE;
BEGIN
c1 := DBMS_SQL.OPEN_CURSOR(true);
DBMS_SQL.PARSE
  (c1, 'BEGIN emp_info(:id); END;', DBMS_SQL.NATIVE);
DBMS_SQL.BIND_VARIABLE(c1, ':id', 176);
n := DBMS_SQL.EXECUTE(c1);
-- Get employee info
DBMS_SQL.GET_NEXT_RESULT(c1, rc1);
FETCH rc1 INTO first_name, last_name, email, phone_number;
-- Get employee job history
DBMS_SQL.GET_NEXT_RESULT(c1, rc1);
LOOP
FETCH rc1 INTO job_title, start_date, end_date;
EXIT WHEN rc1%NOTFOUND;
END LOOP;
DBMS_SQL.CLOSE_CURSOR(c1);
END;
/
```

The `DBMS_SQL` package includes three other procedures.

- `RETURN_RESULT` — Gets a result set and returns it to the client. Because the procedure already returns a result set, the invoker doesn’t have to know the format of the result or the columns it contains. This option is new in Oracle 12c and is most often used with SQL\*Plus.
- `TO_REFCURSOR` — When using `DBMS_SQL.OPEN_CURSOR`, the numeric cursor ID is returned. If you know the structure of the result of the cursor, you can call the `TO_REFCURSOR` procedure, stop working with DBMS_SQL, and move to regular commands such as `FETCH`, `WHEN CURSOR%notfound`, and others. Before using `TO_REFCURSOR`, use the procedures `OPEN_CURSOR`, `PARSE`, and `EXECUTE`.
- `TO_CURSOR_NUMBER` — Gets a cursor opened in native dynamic SQL. After the cursor is open, it can be converted to a number or cursor id and then managed using `DBMS_SQL` procedures.

For more information, see [DBMS_SQL](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SQL.html#GUID-C96D5BAA-29A9-4AB5-A69E-E31228ECC9E9 "https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SQL.html#GUID-C96D5BAA-29A9-4AB5-A69E-E31228ECC9E9") in the _Oracle documentation_.

## MySQL usage

There is no equivalent feature for the `DBMS_SQL` package in MySQL. The only options for Aurora MySQL are:

- Procedures or functions.
- Prepare and run statements.

For more information, see [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html "https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html") in the _MySQL documentation_.
