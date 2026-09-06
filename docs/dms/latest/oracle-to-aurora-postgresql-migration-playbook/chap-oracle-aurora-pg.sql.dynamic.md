

# Oracle DBMS\_SQL package and PostgreSQL dynamic execution
<a name="chap-oracle-aurora-pg.sql.dynamic"></a>

With AWS DMS, you can dynamically construct and execute SQL statements at runtime in your source and target databases. The Oracle `DBMS_SQL` package and PostgreSQL dynamic execution feature provide interfaces for building SQL statements, binding values to placeholders, and processing query results dynamically. These capabilities are essential when writing database applications that must customize queries based on user input or runtime conditions.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-1.png)  |  ![One star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-1.png)  | N/A | Different paradigm and syntax will require application and drivers rewrite. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.dynamic.ora"></a>

The `DBMS_SQL` package provides an interface to parse and run dynamic SQL statements, DML commands, and DDL commands (usually from within a PL/SQL package, function, or procedure). `DBMS_SQL` enables very granular control of SQL cursors and can improve cursor performance in certain cases.

 **Examples** 

The following examples demonstrats how to manually open, parse, bind, run, and fetch data from a cursor using the `DBMS_SQL` PL/SQL interface.

1. Use `DBMS_SQL.OPEN_CURSOR` to open a blank cursor and return the cursor handle.

1. Use `DBMS_SQL.PARSE` to parse the statement into the referenced cursor.

1. Use `DBMS_SQL.BIND_VARIABLES` to attach the value for the bind variable with the cursor.

1. Use `DBMS_SQL.EXECUTE` to run the cursor.

1. Use `DBMS_SQL.GET_NEXT_RESULT` to iterate over the cursor, fetching the next result.

1. Use `DBMS_SQL.CLOSE_CURSOR` to close the cursor.

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
+  `RETURN_RESULT` (New in oracle 12c) — Gets a result set and returns it to the client. Because the procedure already returns a result set, the invoker doesn’t have to know the format of the result or the columns it contains (most often used with SQL\*Plus).
+  `TO_REFCURSOR` — When using `DBMS_SQL.OPEN_CURSOR`, the numeric cursor ID is returned. If you know the structure of the result of the cursor, you can call the `TO_REFCURSOR` procedure, stop working with DBMS\_SQL, and move to regular commands such as `FETCH`, `WHEN CURSOR%notfound`, and others. Before using `TO_REFCURSOR`, use the procedures `OPEN_CURSOR`, `PARSE` and `EXECUTE`.
+  `TO_CURSOR_NUMBER` — Gets a cursor opened in native dynamic SQL. After the cursor is open, it can be converted to a number (cursor id) and then managed using DBMS\_SQL procedures.

For more information, see [DBMS\_SQL](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SQL.html#GUID-C96D5BAA-29A9-4AB5-A69E-E31228ECC9E9) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.dynamic.pg"></a>

PostgreSQL doesn’t support granular control of programmatic cursors and thus doesn’t have an equivalent for Oracle `DBMS_SQL`.

However, you can dynamically parse and run SQL statements in PostgreSQL. Find the two examples following.

 **Examples** 

Create dynamic cursor by using `FOR` with `SELECT`.

```
CREATE OR REPLACE FUNCTION GetErrors ()
RETURNS VARCHAR
AS
$$
DECLARE
_currow RECORD;
msg VARCHAR(200);
TITLE VARCHAR(10);
CODE_NUM VARCHAR(10);
BEGIN
msg := '';

FOR _currow IN SELECT TITLE, CODE_NUM, count(*) FROM A group by TITLE,CODE_NUM
LOOP
  TITLE := _currow.TITLE;
  CODE_NUM := _currow.CODE_NUM;
  msg := msg||rpad(TITLE,20)||rpad(CODE_NUM,20);
END LOOP;
RETURN msg;

END;
$$ LANGUAGE plpgsql;
```

Create cursor and then open it for run with given SQL.

```
CREATE OR REPLACE FUNCTION GetErrors () RETURNS VARCHAR AS $$
declare
    refcur refcursor;
    c_id integer;
    title varchar (10);
    code_num varchar (10);
    alert_mesg VARCHAR(1000) := '';
BEGIN
    OPEN refcur FOR execute('select * from Errors');
    loop
      fetch refcur into title, code_num;
        if not found then
          exit;
        end if;
      alert_mesg := alert_mesg||rpad(title,20)||rpad(code_num,20);
    end loop;
close refcur;
return alert_mesg;
END;
$$ LANGUAGE plpgsql
```

For more information, see [DEALLOCATE](https://www.postgresql.org/docs/13/sql-deallocate.html), [PREPARE](https://www.postgresql.org/docs/13/sql-prepare.html), and [Executing Dynamic Commands](https://www.postgresql.org/docs/13/plpgsql-statements.html#PLPGSQL-STATEMENTS-EXECUTING-DYN) in the *PostgreSQL documentation*.