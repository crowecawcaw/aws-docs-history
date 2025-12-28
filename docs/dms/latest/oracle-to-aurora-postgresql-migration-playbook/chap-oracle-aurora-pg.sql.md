# Oracle DBMS_OUTPUT and PostgreSQL RAISE

Oracle’s `DBMS_OUTPUT` and PostgreSQL’s `RAISE` are utilities that let you display status information and handle errors during the migration process.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | No automation                      | N/A                       | N/A             |

## Oracle usage

The Oracle `DBMS_OUTPUT` package is typically used for debugging or for displaying output messages from PL/SQL procedures.

**Examples**

In the following example, `DBMS_OUTPUT` with `PUT_LINE` is used with a combination of bind variables to dynamically construct a string and print a notification to the screen from within an Oracle PL/SQL procedure. In order to display notifications on to the screen, you must configure the session with `SET SERVEROUTPUT ON`.

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

## PostgreSQL usage

You can use the PostgreSQL `RAISE` statement as an alternative to `DBMS_OUTPUT`. You can combine `RAISE` with several levels of severity including.

| Severity         | Usage                                                                         |
| ---------------- | ----------------------------------------------------------------------------- |
| `DEBUG1..DEBUG5` | Provides successively-more-detailed information for use by developers.        |
| `INFO`           | Provides information implicitly requested by the user                         |
| `NOTICE`         | Provides information that might be helpful to users                           |
| `WARNING`        | Provides warnings of likely problems                                          |
| `ERROR`          | Reports an error that caused the current command to abort.                    |
| `LOG`            | Reports information of interest to administrators, e.g., checkpoint activity. |
| `FATAL`          | Reports an error that caused the current session to abort.                    |
| `PANIC`          | Reports an error that caused all database sessions to abort.                  |

**Examples**

Use `RAISE DEBUG` (where `DEBUG` is the configurable severity level) for similar functionality as Oracle `DBMS_OUTPUT.PUT_LINE` feature.

```
SET CLIENT_MIN_MESSAGES = 'debug';
-- Equivalent To Oracle SET SERVEROUTPUT ON

DO $$
BEGIN
RAISE DEBUG USING MESSAGE := 'hello world';
END $$;

DEBUG: hello world
DO
```

Use the `client_min_messages` parameter to control the level of message sent to the client. The default is `NOTICE`. Use the log_min_messages parameter to control which message levels are written to the server log. The default is `WARNING`.

```
SET CLIENT_MIN_MESSAGES = 'debug';
```

For more information, see [Errors and Messages](https://www.postgresql.org/docs/13/plpgsql-errors-and-messages.html "https://www.postgresql.org/docs/13/plpgsql-errors-and-messages.html") and [When to Log](https://www.postgresql.org/docs/13/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES "https://www.postgresql.org/docs/13/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES") in the _PostgreSQL documentation_.

## Summary

| Feature                                                                       | Oracle                                                                                                                                                                                                                                                            | PostgreSQL                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disables message output.                                                      | `<br>DISABLE<br>`                                                                                                                                                                                                                                                 | Configure “client_min_message” or “log_min_message” for the desired results.                                                                                                                                                                                                                                                             |
| Enables message output.                                                       | `<br>ENABLE<br>`                                                                                                                                                                                                                                                  | Configure “client_min_message” or “log_min_message” for the desired results.                                                                                                                                                                                                                                                             |
| Retrieves one line from buffer.                                               | `<br>GET_LINE<br>`                                                                                                                                                                                                                                                | Consider storing messages in an array or temporary table so that you can retrieve them from another procedure or package.                                                                                                                                                                                                                |
| Retrieves an array of lines from buffer.                                      | `<br>GET_LINES<br>`                                                                                                                                                                                                                                               | Consider storing messages in an array or temporary table so that you can retrieve them from another procedure or package.                                                                                                                                                                                                                |
| Terminates a line created with `PUT` and places a partial line in the buffer. | `<br>PUT + NEW_LINE<br>BEGIN<br>DBMS_OUTPUT.PUT ('1,');<br>DBMS_OUTPUT.PUT('2,');<br>DBMS_OUTPUT.PUT('3,');<br>DBMS_OUTPUT.PUT('4');<br>DBMS_OUTPUT.NEW_LINE();<br>END;<br>/<br>`                                                                                 | Store and concatenate the message string in a varchar variable before raising<br>`<br>do $$<br>DECLARE<br>message varchar :='';<br>begin<br>message := concat(message,'1,');<br>message := concat(message,'2,');<br>message := concat(message,'3,');<br>message := concat(message,'4,');<br>RAISE NOTICE '%',<br>message;<br>END$$;<br>` |
| Places line in buffer                                                         | `<br>PUT_LINE<br>`                                                                                                                                                                                                                                                | `<br>RAISE<br>`                                                                                                                                                                                                                                                                                                                          |
| Returns the number code of the most recent exception                          | `<br>SQLCODE + SQLERRM<br>`                                                                                                                                                                                                                                       | `<br>SQLSTATE + SQLERRM<br>`                                                                                                                                                                                                                                                                                                             |
| Returns the error message associated with its errornumber argument.           | `<br>DECLARE<br>Name employees.last_name%TYPE;<br>BEGIN<br>SELECT last_name INTO name<br>FROM employees<br>WHERE employee_id = -1;<br>EXCEPTION<br>WHEN OTHERS then<br>DBMS_OUTPUT.PUT_LINE<br>(CONCAT('Error code ',<br>SQLCODE,': ',sqlerrm);<br>END;<br>/<br>` | `<br>do $$<br>declare<br>Name employees%ROWTYPE;<br>BEGIN<br>SELECT last_name INTO name FROM<br>employees WHERE employee_id = -1;<br>EXCEPTION<br>WHEN OTHERS then<br>RAISE NOTICE 'Error code %: %', sqlstate,<br>sqlerrm;<br>end$$;<br>`                                                                                               |

For more information, see [PostgreSQL Error Codes](https://www.postgresql.org/docs/13/errcodes-appendix.html "https://www.postgresql.org/docs/13/errcodes-appendix.html") in the _PostgreSQL documentation_.
