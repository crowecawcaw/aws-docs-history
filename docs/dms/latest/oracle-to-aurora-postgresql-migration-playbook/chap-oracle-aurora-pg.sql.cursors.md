

# Oracle and PostgreSQL cursors
<a name="chap-oracle-aurora-pg.sql.cursors"></a>

With AWS DMS, you can migrate data from Oracle and PostgreSQL databases that use cursors. Cursors are database objects that enable traversal over rows from a result set in a database. They facilitate processing individual rows or row segments from a SQL statement’s result set.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-4.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  |  [Cursors](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.cursors)  |  `TYPE …​ IS REF CURSOR` isn’t supported by PostgreSQL.<br />Minor differences in syntax may require some code rewrite.<br />PostgreSQL doesn’t support `%ISOPEN`, `%BULK_EXCEPTIONS`, and `%BULK_ROWCOUNT`. | 

## Oracle usage
<a name="chap-oracle-aurora-pg.sql.cursors.ora"></a>

PL/SQL cursors are pointers to data sets on which application logic can iterate. The data sets hold rows returned by SQL statements. You can refer to the active data set in named cursors from within a program.

There are two types of PL/SQL cursors:
+  **Implicit cursors** are session cursors constructed and managed by PL/SQL automatically without being created or defined by a user. PL/SQL opens an implicit cursor each time you run a `SELECT` or DML statement. Implicit cursors are also called SQL cursors.
+  **Explicit cursors** are session cursors created, constructed, and managed by a user. Cursors are declared and defined by naming it and associating it with a query. Unlike an implicit cursor, you can reference an explicit cursor using its name. An explicit cursor is called a named cursor.

 **Examples** 

The following examples demonstrate cursor usage:

1. Define an explicit PL/SQL cursor named `c1`.

1. The cursor runs an SQL statement to return rows from the database.

1. The PL/SQL loop reads data from the cursor, row by row, and stores the values into two variables: `v_lastname` and `v_jobid`.

1. The loop uses the `%NOTFOUND` attribute to terminate when the last row is read from the database.

```
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
      EXIT WHEN c1%NOTFOUND;
    END LOOP;
  CLOSE c1;
END;
```

1. Define an implicit PL/SQL cursor using a `FOR` Loop.

1. The cursor runs a query and stores values returned into a record.

1. A loop iterates over the cursor data set and prints the result.

```
BEGIN
FOR item IN
  (SELECT last_name, job_id FROM employees WHERE job_id LIKE '%MANAGER%'
    AND manager_id > 400 ORDER BY last_name) LOOP
    DBMS_OUTPUT.PUT_LINE('Name = ' || item.last_name || ', Job = ' || item.job_id);
  END LOOP;
END;
/
```

For more information, see [Explicit Cursor Declaration and Definition](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/explicit-cursor-declaration-and-definition.html#GUID-38C5DBA3-9DEC-4AF2-9B5E-7B721D11A77C) and [Implicit Cursor Attribute](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/implicit-cursor-attribute.html#GUID-5A938EE7-E8D2-468C-B60F-81898F110BE1) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.sql.cursors.pg"></a>

Similar to Oracle PL/SQL cursors, PostgreSQL has PL/pgSQL cursors that enable you to iterate business logic on rows read from the database. They can encapsulate the query and read the query results a few rows at a time. All access to cursors in PL/pgSQL is performed through cursor variables, which are always of the refcursor data type.

Create a PL/pgSQL cursor by declaring it as a variable of type refcursor.

 **Examples of DECLARE a cursor** 

Declare a cursor in PL/pgSQL to be used with any query.

```
DECLARE c1 refcursor;
```

The variable c1 is unbound since it isn’t bound to any particular query.

Declare a cursor in PL/pgSQL with a bound query.

```
DECLARE c2 CURSOR FOR SELECT * FROM employees;
```

In the following example, you can replace `FOR` with `IS` for Oracle compatibility. Declare a cursor in PL/pgSQL to be used with any query.

```
DECLARE c3 CURSOR (var1 integer) FOR SELECT * FROM employees where id = var1;
```
+ The id variable is replaced by an integer parameter value when the cursor is opened.
+ When declaring a cursor with `SCROLL` specified, the cursor can scroll backwards.
+ If `NO SCROLL` is specified, backward fetches are rejected.

Declare a backward-scrolling compatible cursor using the `SCROLL` option.

```
DECLARE c3 SCROLL CURSOR FOR SELECT id, name FROM employees;
```
+  `SCROLL` specifies that rows can be retrieved backwards. `NO SCROLL` specifies that rows can’t be retrieved backwards.
+ Depending upon the complexity of the run plan for the query, `SCROLL` might create performance issues.
+ Backward fetches aren’t allowed when the query includes `FOR UPDATE` or `FOR SHARE`.

 **Examples of OPEN a cursor** 

Open a cursor variable that was declared as Unbound and specify the query to run.

```
OPEN c1 FOR SELECT * FROM employees WHERE id = emp_id;
```

Open a cursor variable that was declared as Unbound and specify the query to run as a string expression. This approach provides greater flexibility.

```
OPEN c1 FOR EXECUTE format('SELECT * FROM %I WHERE col1 = $1',tabname) USING keyvalue;
```

Parameter values can be inserted into the dynamic command using `format()` and `USING`. For example, the table name is inserted into the query using `format()`. The comparison value for col1 is inserted using a `USING` parameter.

Open a cursor that was bound to a query when the cursor was declared and that was declared to take arguments.

```
DO $$
DECLARE
  c3 CURSOR (var1 integer) FOR SELECT * FROM employees where id = var1;
BEGIN
  OPEN c3(var1 := 42);
END$$;
```

For the c3 cursor, supply the argument value expressions. If the cursor was not declared to take arguments, the arguments can be specified outside the cursor.

```
DO $$
DECLARE
  var1 integer;
  c3 CURSOR FOR SELECT * FROM employees where id = var1;
BEGIN
  var1 := 1;
  OPEN c3;
END$$;
```

 **Examples of FETCH a cursor** 

The PL/pgSQL `FETCH` command retrieves the next row from the cursor into a variable. Fetch the values returned from the `c3` cursor into a row variable.

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT * FROM employees;
  rowvar employees%ROWTYPE;
BEGIN
  OPEN c3;
  FETCH c3 INTO rowvar;
END$$;
```

Fetch the values returned from the c3 cursor into two scalar datatypes.

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT id, name FROM employees;
  emp_id integer;
  emp_name varchar;
BEGIN
  OPEN c3;
  FETCH c3 INTO emp_id, emp_name;
END$$;
```

PL/pgSQL supports a special direction clause when fetching data from a cursor using the `NEXT`, `PRIOR`, `FIRST`, `LAST`, `ABSOLUTE count`, `RELATIVE count`, `FORWARD`, or `BACKWARD` arguments. Omitting direction is equivalent to as specifying `NEXT`. For example, fetch the last row from the cursor into the declared variables.

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT id, name FROM employees;
  emp_id integer;
  emp_name varchar;
BEGIN
  OPEN c3;
  FETCH LAST FROM c3 INTO emp_id, emp_name;
END$$;
```

For more information, see [FETCH](https://www.postgresql.org/docs/13/sql-fetch.html) in the *PostgreSQL documentation*.

 **Example of CLOSE a cursor** 

Close a PL/pgSQL cursor using the `CLOSE` command.

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT id, name FROM employees;
  emp_id integer;
  emp_name varchar;
BEGIN
  OPEN c3;
  FETCH LAST FROM c3 INTO emp_id, emp_name;
  CLOSE c3;
END$$;
```

 **Example of iterating through a cursor** 

PL/pgSQL supports detecting when a cursor has no more data to return and can be combined with loops to iterate over all rows of a cursor reference.

The following PL/pgSQL code uses a loop to fetch all rows from the cursor and then exit after the last record is fetched (using `EXIT WHEN NOT FOUND`).

PL/pgSQL supports detecting when a cursor has no more data to return and can be combined with loops to iterate over all rows of a cursor reference.

The following PL/pgSQL code uses a loop to fetch all rows from the cursor and then exit after the last record is fetched (using `EXIT WHEN NOT FOUND`).

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT * FROM employees;
  rowvar employees%ROWTYPE;
BEGIN
OPEN c3;
  LOOP
    FETCH FROM c3 INTO rowvar;
    EXIT WHEN NOT FOUND;
  END LOOP;
  CLOSE c3;
END$$;
```

 **Example of MOVE a cursor without fetching data** 

 `MOVE` repositions a cursor without retrieving any data and works such as the `FETCH` command, except it only repositions the cursor in the dataset and doesn’t return the row to which the cursor is moved. The special variable `FOUND` can be checked to determine if there is a next row.

Move to the last row (null or no data found) for cursor c3.

```
MOVE LAST FROM c3;
```

Move the cursor two records back.

```
MOVE RELATIVE -2 FROM c3;
```

Move the c3 cursor two records forward.

```
MOVE FORWARD 2 FROM c3;
```

 **Example of UPDATE or DELETE current** 

When a cursor is positioned on a table row, that row can be updated or deleted. There are restrictions on what the cursor’s query can select for this type of DML to succeed.

For example, the current row to which the C3 cursor is pointed to is updated.

```
UPDATE employee SET salary = salary*1.2 WHERE CURRENT OF c3;
```

 **Example of Use an Implicit Cursor (FOR Loop Over Queries)** 

```
DO $$
DECLARE
  item RECORD;
BEGIN
  FOR item IN (
    SELECT last_name, job_id
    FROM employees
    WHERE job_id LIKE '%MANAGER%'
    AND manager_id > 400
    ORDER BY last_name
  )
  LOOP
    RAISE NOTICE 'Name = %, Job=%', item.last_name, item.job_id;
  END LOOP;
END $$;
```

## Summary
<a name="chap-oracle-aurora-pg.sql.cursors.summary"></a>


| Action | Oracle PL/SQL | PostgreSQL PL/pgSQL | 
| --- | --- | --- | 
| Declare a bound explicit cursor |  <pre>CURSOR c1 IS<br />SELECT * FROM employees;</pre>  |  <pre>c2 CURSOR FOR<br />SELECT * FROM employees;</pre>  | 
| Open a cursor |  <pre>OPEN c1;</pre>  |  <pre>OPEN c2;</pre>  | 
| Move Cursor to next row and fetch into a record variable (rowvar was declared in the DECLARE section) |  <pre>FETCH c1 INTO rowvar;</pre>  |  <pre>FETCH c2 INTO rowvar;</pre>  | 
| Move Cursor to next row and fetch into multiple scalar data types (emp\_id, emp\_name, salary was declared in the DECLARE section) |  <pre>FETCH c1<br />INTO emp_id, emp_name, salary;</pre>  |  <pre>FETCH c2<br />INTO emp_id, emp_name, salary;</pre>  | 
| Iterate through an implicit cursor using a loop |  <pre>FOR item IN (<br />  SELECT last_name, job_id FROM employees<br />  WHERE job_id LIKE '%CLERK%'<br />  AND manager_id > 120 ORDER BY last_name )<br />  LOOP<br />    << do something<br />    >><br />  END LOOP;</pre>  |  <pre>FOR item IN (<br />  SELECT last_name, job_id<br />  FROM employees<br />  WHERE job_id LIKE '%CLERK%'<br />  AND manager_id > 120 ORDER BY last_name )<br />  LOOP<br />    << do something<br />    >><br />  END LOOP;</pre>  | 
| Declare a cursor with variables |  <pre>CURSOR c1 (key NUMBER)<br />IS SELECT * FROM employees<br />WHERE id = key;</pre>  |  <pre>C2 CURSOR (key integer)<br />FOR SELECT * FROM employees<br />WHERE id = key;</pre>  | 
| Open a cursor with variables |  <pre>OPEN c1(2);</pre>  |  <pre>OPEN c2(2);<br />or<br />OPEN c2(key := 2);</pre>  | 
| Exit a loop after no data found |  <pre>EXIT WHEN c1%NOTFOUND;</pre>  |  <pre>EXIT WHEN NOT FOUND;</pre>  | 
| Detect if a cursor has rows remaining in its dataset |  <pre>%FOUND</pre>  |  <pre>FOUND</pre>  | 
| Determine how many rows were affected from any DML statement |  <pre>%BULK_ROWCOUNT</pre>  | Not Supported but you can run with every DML `GET DIAGNOSTICS integer_var = ROW_COUNT`; and save the results in an array | 
| Determine which DML run failed with the relevant error code |  <pre>%BULK_EXCEPTIONS</pre>  | N/A | 
| Detect if the Cursor is open |  <pre>%ISOPEN</pre>  | N/A | 
| Detect if a Cursor has no rows remaining in its dataset |  <pre>%NOTFOUND</pre>  |  <pre>NOT FOUND</pre>  | 
| Returns the number of rows affected by a cursor |  <pre>%ROWCOUNT</pre>  |  <pre>GET DIAGNOSTICS integer_var = ROW_COUNT;</pre>  | 

For more information, see [Cursors](https://www.postgresql.org/docs/13/plpgsql-cursors.html) and [Basic Statements](https://www.postgresql.org/docs/13/plpgsql-statements.html) in the *PostgreSQL documentation*.