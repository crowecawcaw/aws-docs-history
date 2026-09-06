

# Cursors for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.cursors"></a>

This topic provides reference information about cursor compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. It introduces the concept of cursors and their role in database operations, explaining how they allow developers to work with result sets sequentially. The topic compares cursor functionality in SQL Server and PostgreSQL, highlighting similarities and differences in syntax and usage.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-3.png)  |  [Cursors](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.cursors)  | Different cursor options. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.cursors.sqlserver"></a>

A *set* is a fundamental concept of the relation data model from which SQL is derived. SQL is a declarative language that operates on whole sets, unlike most procedural languages that operate on individual data elements. A single invocations of an SQL statements can return a whole set or modify millions of rows.

Many developers are accustomed to using procedural or imperative approaches to develop solutions that are difficult to implement using set-based querying techniques. Also, operating on row data sequentially may be a more appropriate approach in certain situations.

Cursors provide an alternative mechanism for operating on result sets. Instead of receiving a table object containing rows of data, applications can use cursors to access the data sequentially, row-by-row. Cursors provide the following capabilities:
+ Positioning the cursor at specific rows of the result set using absolute or relative offsets.
+ Retrieving a row, or a block of rows, from the current cursor position.
+ Modifying data at the current cursor position.
+ Isolating data modifications by concurrent transactions that affect the cursor’s result.
+ T-SQL statements can use cursors in scripts, stored procedures, and triggers.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.cursors.sqlserver.syntax"></a>

```
DECLARE <Cursor Name>
CURSOR [LOCAL | GLOBAL]
  [FORWARD_ONLY | SCROLL]
  [STATIC | KEYSET | DYNAMIC | FAST_FORWARD]
  [ READ_ONLY | SCROLL_LOCKS | OPTIMISTIC]
  [TYPE_WARNING]
  FOR <SELECT statement>
  [ FOR UPDATE [ OF <Column List>]][;]
```

```
FETCH [NEXT | PRIOR | FIRST | LAST | ABSOLUTE <Value> | RELATIVE <Value>]
FROM <Cursor Name> INTO <Variable List>;
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.cursors.sqlserver.examples"></a>

Process data in a cursor.

```
DECLARE MyCursor CURSOR FOR
  SELECT *
  FROM Table1 AS T1
    INNER JOIN
    Table2 AS T2
    ON T1.Col1 = T2.Col1;
  OPEN MyCursor;
  DECLARE @VarCursor1 VARCHAR(20);
  FETCH NEXT
    FROM MyCursor INTO @VarCursor1;
  WHILE @@FETCH_STATUS = 0
  BEGIN
    EXEC MyPRocessingProcedure
      @InputParameter = @VarCursor1;
    FETCH NEXT
    FROM product_cursor INTO @VarCursor1;
END

CLOSE MyCursor;
DEALLOCATE MyCursor ;
```

For more information, see [SQL Server Cursors](https://docs.microsoft.com/en-us/sql/relational-databases/cursors?view=sql-server-ver15) and [Cursors (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/cursors-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.cursors.pg"></a>

Similar to T-SQL Cursors in SQL Server, PostgreSQL has PL/pgSQL cursors that you can use to iterate business logic on rows read from the database. They can encapsulate the query and read the query results a few rows at a time. All access to cursors in PL/pgSQL is performed through cursor variables, which are always of the `refcursor` data type.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.cursors.pg.examples"></a>

 **Declare a Cursor** 

The following table includes the `DECLARE..CURSOR` options that are Transact-SQL extended syntax have no equivalent in PostgreSQL.


| SQL Server option | Use | Comments | 
| --- | --- | --- | 
|  `FORWARD_ONLY`  | Defining that `FETCH NEXT` is the only supported fetching option. | Using `FOR LOOP` might be a relevant solution for this option. | 
|  `STATIC`  | Cursor will make a temporary copy of the data. | For small data sets temporary tables can be created and declare a cursor that will select these tables. | 
|  `KEYSET`  | Determining that membership and order of rows in the cursor are fixed. | N/A | 
|  `DYNAMIC`  | Cursor will reflect all data changes made on the selected rows. | Default for PostgreSQL. | 
|  `FAST_FORWARD`  | Will use `FORWARD_ONLY` and `READ_ONLY` to optimize performance. | N/A | 
|  `SCROLL_LOCKS`  | Determine that positioned updates or deletes made by the cursor are guaranteed to succeed. | N/A | 
|  `OPTIMISTIC`  | Determine that positioned updates or deletes made by the cursor will not succeed if the rows has been updated. | N/A | 
|  `TYPE_WARNING`  | Will send warning messages to the client if the cursor is implicitly converted from the requested type. | N/A | 

Declare a Cursor in PL/pgSQL to be used with any query. The variable c1 is unbounded because it isn’t bound to any particular query.

```
DECLARE c1 refcursor;
```

Declare a Cursor in PL/pgSQL with a bounded query.

```
DECLARE c2 CURSOR FOR SELECT * FROM employees;
```

Declare a Cursor with a parametrized bound query:
+ The id variable is replaced by an integer parameter value when the cursor is opened.
+ When declaring a Cursor with SCROLL specified, the Cursor can scroll backwards.
+ If `NO SCROLL` is specified, backward fetches are rejected.

```
DECLARE c3 CURSOR (var1 integer) FOR SELECT * FROM employees where id = var1;
```

Declare a backward-scrolling compatible Cursor using the `SCROLL` option.
+  `SCROLL` specifies that rows can be retrieved backwards. `NO SCROLL` specifies that rows can’t be retrieved backwards.
+ Depending upon the complexity of the run plan for the query, `SCROLL` might create performance issues.
+ Backward fetches aren’t allowed when the query includes `FOR UPDATE` or `FOR SHARE`.

```
DECLARE c3 SCROLL CURSOR FOR SELECT id, name FROM employees;
```

 **Open a Cursor** 

The `OPEN` command is fully compatible between SQL Server and PostgreSQL.

Open a cursor variable that was declared as unbound and specify the query to run.

```
OPEN c1 FOR SELECT * FROM employees WHERE id = emp_id;
```

Open a Cursor variable that was declared as Unbound and specify the query to run as a string expression. This approach provides greater flexibility.

```
OPEN c1 FOR EXECUTE format('SELECT * FROM %I WHERE col1 = $1',tabname) USING keyvalue;
```

You can insert parameter values into the dynamic command with `format()` and `USING`. For example, the table name is inserted into the query with `format()`. The comparison value for `col1` is inserted with a `USING` parameter.

Open a Cursor that was bound to a query when the cursor was declared and was declared to take arguments.

```
DO $$
DECLARE
  c3 CURSOR (var1 integer) FOR SELECT * FROM employees where id = var1;
BEGIN
  OPEN c3(var1 := 42);
END$$;
```

For the `c3` cursor, supply the argument value expressions.

If the cursor wasn’t declared to take arguments, you can specify the arguments outside the cursor.

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

 **Fetch a Cursor** 

Use the following syntax to fetch a cursor.

```
FETCH [ direction [ FROM | IN ] ] cursor_name
```

The following table shows additional PostgreSQL options as a direction for the FETCH command.


| PostgreSQL option | Use | 
| --- | --- | 
| ALL | Get all remaining rows | 
| FORWARD | Same as NEXT | 
| FORWARD | (n) Fetch the next n rows | 
| FORWARD | ALL Same as ALL | 
| BACKWARD | Same as PRIOR | 
| BACKWARD | (n) Fetch the prior n rows | 
| BACKWARD | ALL Fetch all prior rows | 

The PL/pgSQL `FETCH` command retrieves the next row from the cursor into a variable.

Fetch the values returned from the `c3` cursor into a row variable.

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

Fetch the values returned from the c3 Cursor into two scalar data types.

```
DO $$
DECLARE
  c3 CURSOR FOR SELECT id, name FROM employees;
  emp_id integer;
  emp_name varchar;
BEGIN
  OPEN c3;
  FETCH FROM c3 INTO emp_id, emp_name;
END$$;
```

PL/pgSQL supports a special direction clause when fetching data from a cursor using the `NEXT`, `PRIOR`, `FIRST`, `LAST`, `ABSOLUTE count`, `RELATIVE count`, `FORWARD`, or `BACKWARD` arguments. Omitting direction is equivalent to specifying `NEXT`. For example, fetch the last row from the cursor into the declared variables.

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

## Summary
<a name="chap-sql-server-aurora-pg.tsql.cursors.summary"></a>


| Feature | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| Cursor options |  <pre>[FORWARD_ONLY | SCROLL] [STATIC | KEYSET | DYNAMIC | FAST_FORWARD]<br />[READ_ONLY | SCROLL_LOCKS | OPTIMISTIC]</pre>  |  <pre>[ BINARY ] [ INSENSITIVE ] [ [ NO ]<br />SCROLL ] CURSOR [ { WITH | WITHOUT } HOLD ]</pre>  | 
| Updateable cursors |  <pre>DECLARE CURSOR... FOR UPDATE</pre>  |  <pre>DECLARE cur_name CURSOR... FOR UPDATE</pre>  | 
| Cursor declaration |  <pre>DECLARE CURSOR</pre>  |  <pre>DECLARE cur_name CURSOR</pre>  | 
| Cursor open |  <pre>OPEN</pre>  |  <pre>OPEN</pre>  | 
| Cursor fetch |  <pre>FETCH NEXT | PRIOR | FIRST | LAST | ABSOLUTE | RELATIVE</pre>  | <pre>FETCH [ direction [ FROM | IN ] ] cursor_name</pre>The direction can be empty or one of the following: `NEXT`, `PRIOR`, `FIRST`, `LAST`, `ABSOLUTE count`, `RELATIVE count`, `count`, `ALL FORWARD`, `FORWARD count`, `FORWARD ALL`, `BACKWARD`, `BACKWARD count`, `BACKWARD ALL`. | 
| Cursor close |  <pre>CLOSE</pre>  |  <pre>CLOSE</pre>  | 
| Cursor deallocate |  <pre>DEALLOCATE</pre>  | Same effect as CLOSE (not required) | 
| Cursor end condition |  `@@FETCH_STATUS` system variable | Not supported | 

For more information, see [FETCH](https://www.postgresql.org/docs/13/sql-fetch.html) in the *PostgreSQL documentation*.