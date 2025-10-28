Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Trapping errors

This topic describes how Amazon Redshift handles errors.

When a query or command in a stored procedure causes an error, subsequent queries don't run and the transaction is rolled back. But
you can handle errors using an EXCEPTION block.

###### Note

The default behavior is that an error will cause subsequent queries not to run, even when there are no additional error-generating
conditions in the stored procedure.

```
[ <<label>> ]
[ DECLARE
  declarations ]
BEGIN
  statements
EXCEPTION
  WHEN OTHERS THEN
    statements
END;

```

When an exception occurs, and you add an exception-handling block, you can write RAISE
statements and most other PL/pgSQL statements. For example, you can raise an
exception with a custom message or insert a record into a logging table.

When entering the exception-handling block, the current transaction is rolled back and a new
transaction is created to run the statements in the block. If the statements in the block run without error, the
transaction is committed and the exception is re-thrown. Lastly, the stored procedure exits.

The only supported condition in an exception block is OTHERS, which matches every error
type except query cancellation. Also, if an error occurs in an exception-handling
block, it can be caught by an outer exception-handling block.

When an error occurs inside the NONATOMIC procedure, the error is not re-thrown if it is handled by an exception block.
See the PL/pgSQL statement `RAISE` to throw an exception caught by the exception handling block.
This statement is only valid in exception handling blocks.
For more information see [RAISE](c_PLpgSQL-statements.md#r_PLpgSQL-messages-errors "c_PLpgSQL-statements.md#r_PLpgSQL-messages-errors").

**Controlling what happens after an error in a stored procedure, with the CONTINUE handler**

The `CONTINUE` handler is a type of exception handler that controls the flow of execution within a NONATOMIC stored procedure. By using it, you can
catch and handle exceptions without ending the existing statement block. Normally, when an error occurs in a stored
procedure, the flow is interrupted and the error is returned to the caller. However,
in some use cases, the error condition isn't severe enough to warrant interrupting the flow. You might want to handle the
error gracefully, using error-handling logic of your choosing in a seperate transaction, and then continue running statements that follow the error. The following shows the syntax.

```
[ DECLARE
  declarations ]
BEGIN
  statements
EXCEPTION
  [ CONTINUE_HANDLER | EXIT_HANDLER ] WHEN OTHERS THEN
    handler_statements
END;

```

There are several system tables available to help you gather
information about various types of errors. For more information,
see [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md"),
[STL_ERROR](r_STL_ERROR.md "r_STL_ERROR.md"),
and [SYS_STREAM_SCAN_ERRORS](r_SYS_STREAM_SCAN_ERRORS.md "r_SYS_STREAM_SCAN_ERRORS.md"). There are
also additional system tables you can use to troubleshoot errors. More information about
these can be found at [System tables and views reference](cm_chap_system-tables.md "cm_chap_system-tables.md").

## Example

The following example shows how to write statements in the exception-handling block.
The stored procedure is using default transaction management behavior.

```
CREATE TABLE employee (firstname varchar, lastname varchar);
INSERT INTO employee VALUES ('Tomas','Smith');
CREATE TABLE employee_error_log (message varchar);

CREATE OR REPLACE PROCEDURE update_employee_sp() AS
$$
BEGIN
    UPDATE employee SET firstname = 'Adam' WHERE lastname = 'Smith';
    EXECUTE 'select invalid';
EXCEPTION WHEN OTHERS THEN
    RAISE INFO 'An exception occurred.';
    INSERT INTO employee_error_log VALUES ('Error message: ' || SQLERRM);
END;
$$
LANGUAGE plpgsql;

CALL update_employee_sp();

INFO:  An exception occurred.
ERROR:  column "invalid" does not exist
CONTEXT:  SQL statement "select invalid"
PL/pgSQL function "update_employee_sp" line 3 at execute statement
```

In this example, if we call `update_employee_sp`, the informational message
_An exception occurred._ is raised and the error message is
inserted in the logging table's `employee_error_log` log. The original
exception is thrown again before the stored procedure exits. The following queries show records that result from running the example.

```
SELECT * from employee;

firstname | lastname
-----------+----------
 Tomas     | Smith

SELECT * from employee_error_log;

          message
------------------------------------------------
 Error message: column "invalid" does not exist
```

For more information about RAISE, including formatting
help and a list of additional levels, see [Supported PL/pgSQL statements](c_PLpgSQL-statements.md "c_PLpgSQL-statements.md").

The following example shows how to write statements in the exception-handling block.
The stored procedure is using NONATOMIC transaction management behavior.
In this example, there is no error thrown back to caller after the procedure call completes.
The UPDATE statement is not rolled back due to the error in the next statement.
The informational message is raised and the error message is inserted in the logging table.

```
CREATE TABLE employee (firstname varchar, lastname varchar);
INSERT INTO employee VALUES ('Tomas','Smith');
CREATE TABLE employee_error_log (message varchar);

-- Create the SP in NONATOMIC mode
CREATE OR REPLACE PROCEDURE update_employee_sp_2() NONATOMIC AS
$$
BEGIN
    UPDATE employee SET firstname = 'Adam' WHERE lastname = 'Smith';
    EXECUTE 'select invalid';
EXCEPTION WHEN OTHERS THEN
    RAISE INFO 'An exception occurred.';
    INSERT INTO employee_error_log VALUES ('Error message: ' || SQLERRM);
END;
$$
LANGUAGE plpgsql;

CALL update_employee_sp_2();
INFO:  An exception occurred.
CALL

SELECT * from employee;

 firstname | lastname
-----------+----------
 Adam      | Smith
(1 row)

SELECT * from employee_error_log;

                    message
------------------------------------------------
 Error message: column "invalid" does not exist
(1 row)

```

This example shows how to create a procedure with two sub blocks. When the stored
procedure is called, the error from the first sub block is handled by its exception
handling block. After the first sub block completes, the procedure continues to execute
the second sub block. You can see from the result that no error is thrown when the
procedure call completes. The UPDATE and INSERT operations on table employee are
committed. Error messages from both exception blocks are inserted in the logging
table.

```
CREATE TABLE employee (firstname varchar, lastname varchar);
INSERT INTO employee VALUES ('Tomas','Smith');
CREATE TABLE employee_error_log (message varchar);

CREATE OR REPLACE PROCEDURE update_employee_sp_3() NONATOMIC AS
$$
BEGIN
    BEGIN
        UPDATE employee SET firstname = 'Adam' WHERE lastname = 'Smith';
        EXECUTE 'select invalid1';
    EXCEPTION WHEN OTHERS THEN
        RAISE INFO 'An exception occurred in the first block.';
        INSERT INTO employee_error_log VALUES ('Error message: ' || SQLERRM);
    END;
    BEGIN
        INSERT INTO employee VALUES ('Edie','Robertson');
        EXECUTE 'select invalid2';
    EXCEPTION WHEN OTHERS THEN
        RAISE INFO 'An exception occurred in the second block.';
        INSERT INTO employee_error_log VALUES ('Error message: ' || SQLERRM);
    END;
END;
$$
LANGUAGE plpgsql;

CALL update_employee_sp_3();
INFO:  An exception occurred in the first block.
INFO:  An exception occurred in the second block.
CALL

SELECT * from employee;

 firstname | lastname
-----------+-----------
 Adam      | Smith
 Edie      | Robertson
(2 rows)

SELECT * from employee_error_log;

                     message
-------------------------------------------------
 Error message: column "invalid1" does not exist
 Error message: column "invalid2" does not exist
(2 rows)

```

The following example shows how to use the CONTINUE exception handler. This sample creates two tables and uses them in a stored
procedure. The CONTINUE handler controls the flow of execution in a stored procedure with NONATOMIC transaction-management behavior.

```
CREATE TABLE tbl_1 (a int);
CREATE TABLE tbl_error_logging(info varchar, err_state varchar, err_msg varchar);

CREATE OR REPLACE PROCEDURE sp_exc_handling_1() NONATOMIC AS
$$
BEGIN
    INSERT INTO tbl_1 VALUES (1);
    -- Expect an error for the insert statement following, because of the invalid value
    INSERT INTO tbl_1 VALUES ("val");
    INSERT INTO tbl_1 VALUES (2);
EXCEPTION CONTINUE_HANDLER WHEN OTHERS THEN
    INSERT INTO tbl_error_logging VALUES ('Encountered error', SQLSTATE, SQLERRM);
END;
$$ LANGUAGE plpgsql;
```

Call the stored procedure:

```
CALL sp_exc_handling_1();
```

Flow proceeds like so:

1. An error occurs because an attempt is made to insert an incompatible data type in a column. Control passes to the EXCEPTION block. When the
   exception-handling block is entered, the current transaction is rolled back and a new implicit transaction is created to run the statements in it.
2. If the statements in CONTINUE_HANDLER run without error, control passes to the statement immediately following the statement
   causing the exception. (If a statement in CONTINUE_HANDLER raises a new exception, you can handle it with an exception handler within the EXCEPTION block.)
   After you call the sample stored procedure, the tables contain the following records:

- If you run `SELECT * FROM tbl_1;`, it returns two records. These contain the values `1` and `2`.
- If you run `SELECT * FROM tbl_error_logging;`, it returns one record with these values: _Encountered error_, _42703_,
  and _column "val" does not exist in tbl_1_.
  The following additional error-handling example uses both an EXIT handler and a CONTINUE handler. It creates two tables: a data table and a logging table. It also creates a stored procedure
  that demonstrates error handling:

```
CREATE TABLE tbl_1 (a int);
CREATE TABLE tbl_error_logging(info varchar, err_state varchar, err_msg varchar);

CREATE OR REPLACE PROCEDURE sp_exc_handling_2() NONATOMIC AS
$$
BEGIN
    INSERT INTO tbl_1 VALUES (1);
    BEGIN
        INSERT INTO tbl_1 VALUES (100);
        -- Expect an error for the insert statement following, because of the invalid value
        INSERT INTO tbl_1 VALUES ("val");
        INSERT INTO tbl_1 VALUES (101);
    EXCEPTION EXIT_HANDLER WHEN OTHERS THEN
        INSERT INTO tbl_error_logging VALUES ('Encountered error', SQLSTATE, SQLERRM);
    END;
    INSERT INTO tbl_1 VALUES (2);
    -- Expect an error for the insert statement following, because of the invalid value
    INSERT INTO tbl_1 VALUES ("val");
    INSERT INTO tbl_1 VALUES (3);
EXCEPTION CONTINUE_HANDLER WHEN OTHERS THEN
    INSERT INTO tbl_error_logging VALUES ('Encountered error', SQLSTATE, SQLERRM);
END;
$$ LANGUAGE plpgsql;
```

After you create the stored procedure, call it with the following:

```
CALL sp_exc_handling_2();
```

When an error occurs in the inner exception block, which is bracketed by the inner set of BEGIN and END, it's handled by the EXIT handler. Any errors that occur
in the outer block are handled by the CONTINUE handler.

After you call the sample stored procedure, the tables contain the following records:

- If you run `SELECT * FROM tbl_1;`, it returns four records, with the values 1, 2, 3, and 100.
- If you run `SELECT * FROM tbl_error_logging;`, it returns two records. They have these values: _Encountered error_, _42703_,
  and _column "val" does not exist in tbl_1_.
  If the table **tbl_error_logging** doesn't exist, it raises an exception.

The following example shows how to use the CONTINUE exception handler with the FOR loop. This sample creates three tables and uses them in a FOR loop within a stored procedure. The FOR loop
is result set variant, meaning that it iterates over the results of a query:

```
CREATE TABLE tbl_1 (a int);
INSERT INTO tbl_1 VALUES (1), (2), (3);
CREATE TABLE tbl_2 (a int);
CREATE TABLE tbl_error_logging(info varchar, err_state varchar, err_msg varchar);

CREATE OR REPLACE PROCEDURE sp_exc_handling_loop() NONATOMIC AS
$$
DECLARE
 rec RECORD;
BEGIN
    FOR rec IN SELECT a FROM tbl_1
    LOOP
        IF rec.a = 2 THEN
            -- Expect an error for the insert statement following, because of the invalid value
            INSERT INTO tbl_2 VALUES("val");
        ELSE
            INSERT INTO tbl_2 VALUES (rec.a);
        END IF;
    END LOOP;
EXCEPTION CONTINUE_HANDLER WHEN OTHERS THEN
    INSERT INTO tbl_error_logging VALUES ('Encountered error', SQLSTATE, SQLERRM);
END;
$$ LANGUAGE plpgsql;
```

Call the stored procedure:

```
CALL sp_exc_handling_loop();
```

After you call the sample stored procedure, the tables contain the following records:

- If you run `SELECT * FROM tbl_2;`, it returns two records. These contain the values 1 and 3.
- If you run `SELECT * FROM tbl_error_logging;`, it returns one record with these values: _Encountered error_, _42703_, and _column "val" does not exist in tbl_2_.
  Usage notes regarding the CONTINUE handler:

- CONTINUE_HANDLER and EXIT_HANDLER keywords can be used only in NONATOMIC stored procedures.
- CONTINUE_HANDLER and EXIT_HANDLER keywords are optional. EXIT_HANDLER is the default.
