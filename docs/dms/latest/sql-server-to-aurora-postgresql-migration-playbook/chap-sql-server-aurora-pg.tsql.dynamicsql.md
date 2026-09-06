

# Dynamic SQL for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql"></a>

This topic provides reference information on migrating dynamic SQL functionality from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can use this guide to understand how to adapt your dynamic SQL queries and commands when transitioning to PostgreSQL. The topic explains the differences in syntax and execution methods between the two database systems, offering practical examples for running SELECT queries, DML commands, and DDL statements dynamically in PostgreSQL.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  | N/A | Different paradigm and syntax require rewriting the application. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.sqlserver"></a>

Dynamic SQL is a feature that helps minimize hard-coded SQL. The SQL engine optimizes code, which leads to less hard parses.

Developers can use dynamic SQL to construct and run SQL queries at run time as a string, using some logic in SQL to construct varying query strings, without having to pre-construct them during development.

There are two options for running dynamic SQL: use the `EXECUTE` command or the `sp_executesql` function.

### EXECUTE Command
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.sqlserver.execute"></a>

Use this option to run a command string within a T-SQL block, procedure, or function. You can also use the `EXECUTE` command with linked servers. You can define metadata for the result set using the `WITH RESULT SETS` options.

For parameters, use either the value or `@parameter_name=value`.

**Note**  
Make sure that you validate the structure of the string command before running it with the `EXECUTE` command.

 **Syntax** 

The following example shows the SQL Server syntax that runs a stored procedure or function.

```
[ { EXEC | EXECUTE } ]
  {
    [ @return_status = ]
    { module_name [ ;number ] | @module_name_var }
      [ [ @parameter = ] { value
        | @variable [ OUTPUT ]
        | [ DEFAULT ]
        }
      ]
    [ ,...n ]
    [ WITH <execute_option> [ ,...n ] ]
  }
[;]
```

The following example shows the SQL Server syntax that runs a character string.

```
{ EXEC | EXECUTE }
  ( { @string_variable | [ N ]'tsql_string' } [ + ...n ] )
  [ AS { LOGIN | USER } = ' name ' ]
[;]
```

The following example shows the SQL Server syntax that runs a pass-through command against a linked server.

```
{ EXEC | EXECUTE }
  ( { @string_variable | [ N ] 'command_string [ ? ]' } [ + ...n ]
    [ { , { value | @variable [ OUTPUT ] } } [ ...n ] ]
  )
  [ AS { LOGIN | USER } = ' name ' ]
  [ AT linked_server_name ]
[;]

<execute_option>::=
{
  RECOMPILE
  | { RESULT SETS UNDEFINED }
  | { RESULT SETS NONE }
  | { RESULT SETS ( <result_sets_definition> [,...n ] ) }
  }

<result_sets_definition> ::=
{
  (
    { column_name
    data_type
    [ COLLATE collation_name ]
    [ NULL | NOT NULL ] }
    [,...n ]
    )
  | AS OBJECT
    [ db_name . [ schema_name ] . | schema_name . ]
    {table_name | view_name | table_valued_function_name }
  | AS TYPE [ schema_name.]table_type_name
  | AS FOR XML
}
```

 **Example** 

The following example shows how to use `EXECUTE` to run a `tsql_string` function with a variable.

```
DECLARE @scm_name sysname;
DECLARE @tbl_name sysname;
EXECUTE ('DROP TABLE ' + @scm_name + '.' + @tbl_name + ';');
```

The following example shows how to use `EXECUTE AS USER` to switch context to another user.

```
DECLARE @scm_name sysname;
DECLARE @tbl_name sysname;
EXECUTE ('DROP TABLE ' + @scm_name + '.' + @tbl_name + ';') AS USER = 'SchemasAdmin';
```

The following example shows how to use `EXECUTE` with a result set.

```
EXEC GetMaxSalByDeptID 23
WITH RESULT SETS
(
  ([Salary] int NOT NULL)
);
```

### sp\_executesql System Stored Procedure
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.sqlserver.spexecute"></a>

This option runs a T-SQL command or block that you can run several times and build dynamically. You can also use this option with embedded parameters.

 **Syntax** 

The following example shows the `sp_executesql` syntax for SQL Server, Azure SQL Database, Azure SQL Data Warehouse, and Parallel Data Warehouse.

```
sp_executesql [ @stmt = ] statement
[
  { , [ @params = ] N'@parameter_name data_type [ OUT | OUTPUT ][ ,...n ]' }
    { , [ @param1 = ] 'value1' [ ,...n ] }
]
```

 **Example** 

The following example shows how to use `sp_executesql` to run a SELECT statement.

```
EXECUTE sp_executesql
  N'SELECT * FROM HR.Employees
  WHERE DeptID = @DID',
  N'@DID int',
  @DID = 23;
```

For more information, see [sp\_executesql (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-executesql-transact-sql?view=sql-server-2017) and [EXECUTE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/execute-transact-sql?view=sql-server-2017) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.pg"></a>

The PostgreSQL `EXECUTE` command prepares and runs commands dynamically. The `EXECUTE` command can also run DDL statements and retrieve data using SQL commands. Similar to SQL Server, you can use the PostgreSQL `EXECUTE` command with bind variables.

Converting SQL Server dynamic SQL to PostgreSQL requires significant efforts.

 **Examples** 

The following example runs a SQL SELECT query with the table name as a dynamic variable using bind variables. This query returns the number of employees under a manager with a specific ID.

```
DO $$DECLARE
Tabname varchar(30) := 'employees';
num integer := 1;
cnt integer;
BEGIN
EXECUTE format('SELECT count(*) FROM %I WHERE manager = $1', tabname)
INTO cnt USING num;
RAISE NOTICE 'Count is % int table %', cnt, tabname;
END$$;
;
```

The following example runs a DML command; first with no variables and then with variables.

```
DO $$DECLARE
BEGIN
EXECUTE 'INSERT INTO numbers (a) VALUES (1)';
EXECUTE format('INSERT INTO numbers (a) VALUES (%s)', 42);
END$$;
;
```

**Note**  
 `%s` formats the argument value as a simple string. A null value is treated as an empty string. `%I` treats the argument value as an SQL identifier and double-quotes it if necessary. It is an error for the value to be null.

The following example runs a DDL command.

```
DO $$DECLARE
BEGIN
EXECUTE 'CREATE TABLE numbers (num integer)';
END$$;
;
```

For more information, see [String Functions and Operators](https://www.postgresql.org/docs/13/functions-string.html) in the *PostgreSQL documentation*.

### Prepare
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.pg.prepare"></a>

Using a `PREPARE` statement can improve performance of reusable SQL statements.

The `PREPARE` command can receive a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `VALUES` statement and parse it with a user-specified qualifying name so you can use the EXECUTE command later without the need to re-parse the SQL statement for each run.
+ When using `PREPARE` to create a prepared statement, it will be viable for the scope of the current session.
+ If a DDL command is run on a database object referenced by the prepared SQL statement, the next `EXECUTE` command requires a hard parse of the SQL statement.

 **Example** 

Use `PREPARE` and `EXECUTE` commands together. The SQL command is prepared with a user-specified qualifying name. You can run the SQL command several times8 without the need for re-parsing.

```
PREPARE numplan (int, text, bool) AS
INSERT INTO numbers VALUES($1, $2, $3);
EXECUTE numplan(100, 'New number 100', 't');
EXECUTE numplan(101, 'New number 101', 't');
EXECUTE numplan(102, 'New number 102', 'f');
EXECUTE numplan(103, 'New number 103', 't');
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.dynamicsql.summary"></a>


| Functionality | SQL Server dynamic SQL | PostgreSQL EXECUTE and PREPARE | 
| --- | --- | --- | 
| Run SQL with results and bind variables |  <pre>DECLARE @sal int;<br />EXECUTE getSalary @sal OUTPUT;</pre>  |  <pre>EXECUTE format('select salary<br />  from employees<br />  WHERE %I = $1', col_name)<br />INTO amount USING col_val;</pre>  | 
| Run DML with variables and bind variables |  <pre>DECLARE @amount int<br />DECLARE @col_val int<br />DECLARE @col_name carchar(70)<br />DECLARE @sqlCommand varchar(1000)<br />SET @sqlCommand = 'UPDATE employees SET salary=salary'<br />  + @amount + ' WHERE ' + @col_name + '=' + @col_val<br />EXECUTE (@sqlCommand)</pre>  |  <pre>EXECUTE format('UPDATE employees SET salary = salary<br />  + $1 WHERE %I = $2', col_name) USING amount, col_val;</pre>  | 
| Run DDL |  <pre>EXECUTE ('CREATE TABLE link_emp (idemp1 integer, idemp2 integer);');</pre>  |  <pre>EXECUTE 'CREATE TABLE link_emp (idemp1 integer, idemp2 integer)';</pre>  | 
| Run anonymous block |  <pre>BEGIN ... END; DO $$DECLARE</pre>  |  <pre>BEGIN ... END$$;</pre>  | 

For more information, see [Basic Statements](https://www.postgresql.org/docs/13/plpgsql-statements.html) in the *PostgreSQL documentation*.