

# Oracle DBMS\_OUTPUT and PostgreSQL RAISE
<a name="chap-oracle-aurora-pg.sql.raise"></a>

Oracle’s `DBMS_OUTPUT` and PostgreSQL’s `RAISE` are utilities that let you display status information and handle errors during the migration process.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  | N/A | N/A | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.raise.ora"></a>

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

For more information, see [DBMS\_OUTPUT](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_OUTPUT.html#GUID-C1400094-18D5-4F36-A2C9-D28B0E12FD8C) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.raise.pg"></a>

You can use the PostgreSQL `RAISE` statement as an alternative to `DBMS_OUTPUT`. You can combine `RAISE` with several levels of severity including.


| Severity | Usage | 
| --- | --- | 
|  `DEBUG1..DEBUG5`  | Provides successively-more-detailed information for use by developers. | 
|  `INFO`  | Provides information implicitly requested by the user | 
|  `NOTICE`  | Provides information that might be helpful to users | 
|  `WARNING`  | Provides warnings of likely problems | 
|  `ERROR`  | Reports an error that caused the current command to abort. | 
|  `LOG`  | Reports information of interest to administrators, e.g., checkpoint activity. | 
|  `FATAL`  | Reports an error that caused the current session to abort. | 
|  `PANIC`  | Reports an error that caused all database sessions to abort. | 

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

Use the `client_min_messages` parameter to control the level of message sent to the client. The default is `NOTICE`. Use the log\_min\_messages parameter to control which message levels are written to the server log. The default is `WARNING`.

```
SET CLIENT_MIN_MESSAGES = 'debug';
```

For more information, see [Errors and Messages](https://www.postgresql.org/docs/13/plpgsql-errors-and-messages.html) and [When to Log](https://www.postgresql.org/docs/13/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES) in the *PostgreSQL documentation*.

## Summary
<a name="chap-oracle-aurora-pg.sql.raise.summary"></a>


| Feature | Oracle | PostgreSQL | 
| --- | --- | --- | 
| Disables message output. |  <pre>DISABLE</pre>  | Configure “client\_min\_message” or “log\_min\_message” for the desired results. | 
| Enables message output. |  <pre>ENABLE</pre>  | Configure “client\_min\_message” or “log\_min\_message” for the desired results. | 
| Retrieves one line from buffer. |  <pre>GET_LINE</pre>  | Consider storing messages in an array or temporary table so that you can retrieve them from another procedure or package. | 
| Retrieves an array of lines from buffer. |  <pre>GET_LINES</pre>  | Consider storing messages in an array or temporary table so that you can retrieve them from another procedure or package. | 
| Terminates a line created with `PUT` and places a partial line in the buffer. |  <pre>PUT + NEW_LINE<br />BEGIN<br />DBMS_OUTPUT.PUT ('1,');<br />DBMS_OUTPUT.PUT('2,');<br />DBMS_OUTPUT.PUT('3,');<br />DBMS_OUTPUT.PUT('4');<br />DBMS_OUTPUT.NEW_LINE();<br />END;<br />/</pre>  | Store and concatenate the message string in a varchar variable before raising<pre>do $$<br />DECLARE<br />message varchar :='';<br />begin<br />message := concat(message,'1,');<br />message := concat(message,'2,');<br />message := concat(message,'3,');<br />message := concat(message,'4,');<br />RAISE NOTICE '%',<br />message;<br />END$$;</pre> | 
| Places line in buffer |  <pre>PUT_LINE</pre>  |  <pre>RAISE</pre>  | 
| Returns the number code of the most recent exception |  <pre>SQLCODE + SQLERRM</pre>  |  <pre>SQLSTATE + SQLERRM</pre>  | 
| Returns the error message associated with its errornumber argument. |  <pre>DECLARE<br />Name employees.last_name%TYPE;<br />BEGIN<br />SELECT last_name INTO name<br />FROM employees<br />WHERE employee_id = -1;<br />EXCEPTION<br />WHEN OTHERS then<br />DBMS_OUTPUT.PUT_LINE<br />(CONCAT('Error code ',<br />  SQLCODE,': ',sqlerrm);<br />END;<br />/</pre>  |  <pre>do $$<br />declare<br />Name employees%ROWTYPE;<br />BEGIN<br />SELECT last_name INTO name FROM<br />employees WHERE employee_id = -1;<br />EXCEPTION<br />WHEN OTHERS then<br />RAISE NOTICE 'Error code %: %', sqlstate,<br />sqlerrm;<br />end$$;</pre>  | 

For more information, see [PostgreSQL Error Codes](https://www.postgresql.org/docs/13/errcodes-appendix.html) in the *PostgreSQL documentation*.