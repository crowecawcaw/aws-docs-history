

# SQL Server cast and convert for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.castconvert"></a>

This topic provides reference information about data type conversion and casting in Amazon Aurora PostgreSQL compared to Microsoft SQL Server. You can understand the similarities and differences between the CAST and CONVERT functions in both database systems. The topic explains how Aurora PostgreSQL supports the CAST function similarly to SQL Server, while also offering additional flexibility through custom casts and the CREATE CAST command.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-4.png)  | N/A | CONVERT is used only to convert between collations. CAST uses different syntax. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.castconvert.sqlserver"></a>

The `CAST` and `CONVERT` functions are commonly used to convert one data type to another. `CAST` and `CONVERT` behave mostly the same and share the same topic in MSDN. They have the following differences:
+  `CAST` is part of the ANSI-SQL specification, but `CONVERT` isn’t.
+  `CONVERT` accepts an optional style parameter used for formatting.

For more information, see [Date and Time styles](https://docs.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-2017#date-and-time-styles) in the *SQL Server documentation*.

### Conversion Matrix
<a name="chap-sql-server-aurora-pg.tsql.castconvert.sqlserver.matrix"></a>

For a list of available conversion data types, see [Implicit conversions](https://docs.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-2017#implicit-conversions) in the *SQL Server documentation*.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.castconvert.sqlserver.syntax"></a>

```
-- CAST Syntax:
CAST ( expression AS data_type [ ( length ) ] )

-- CONVERT Syntax:
CONVERT ( data_type [ ( length ) ] , expression [ , style ] )
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.castconvert.sqlserver.examples"></a>

The following example casts a `string` to `int` and `int` to `decimal`.

```
SELECT CAST('23' AS int) AS [int], CAST(23 AS decimal(10, 2)) AS [decimal];
```

The following example converts `string` to `int` and `int` to `decimal`.

```
SELECT CONVERT(int, '23') AS [int], CONVERT(decimal(10, 2), 23) AS [decimal];
```

For these two preceding examples, the result looks as shown following.

```
int  decimal
23   23.00
```

The following example converts a date with option style input `(109 - mon dd yyyy hh:mi:ss:mmmAM (or PM))`.

```
SELECT CONVERT(nvarchar(30), GETDATE(), 109);

Jul 25 2018 5:20:10.8975085PM
```

For more information, see [CAST and CONVERT (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-2017) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.castconvert.pg"></a>

 Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) provides the same CAST function as SQL Server for conversion between data types. It also provides a `CONVERSION` function, but it isn’t equivalent to SQL Server `CONVERT`. PostgreSQL `CONVERSION` is used to convert between character set encoding.

 `CREATE A CAST` defines a new cast on how to convert between two data types.

Cast can be `EXPLICITLY` or `IMPLICIT`.

The behavior is similar to SQL Server’s casting, but in PostgreSQL, you can also create your own casts to change the default behavior. For example, checking if a string is a valid credit card number by creating the `CAST` with the `WITHOUT FUNCTION` clause.

 `CREATE CONVERSION` is used to convert between encoding such as UTF8 and LATIN. If `CONVERT` is currently in use in SQL Server code, rewrite it to use `CAST` instead.

**Note**  
Not all SQL Server data types are supported on Aurora PostgreSQL, besides changing the `CAST` or `CONVERT` commands, you might need to also change the source of the target data type. For more information, see [Data Types](chap-sql-server-aurora-pg.sql.datatypes.md).

Another way to convert between data types in PostgreSQL will be to use the `::` characters. This option is useful and can make your PL/pgSQL code look cleaner and simpler, see the following examples.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.castconvert.pg.syntax"></a>

```
CREATE CAST (source_type AS target_type)
WITH FUNCTION function_name (argument_type [, ...]) [ AS ASSIGNMENT | AS IMPLICIT ]

CREATE CAST (source_type AS target_type)
WITHOUT FUNCTION [ AS ASSIGNMENT | AS IMPLICIT ]

CREATE CAST (source_type AS target_type)
WITH INOUT [ AS ASSIGNMENT | AS IMPLICIT ]
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.castconvert.pg.examples"></a>

The following example converts a numeric value to float.

```
SELECT 23 + 2.0;

or

SELECT CAST ( 23 AS numeric ) + 2.0;
```

The following example converts a date with format input ('mon dd yyyy hh:mi:ss:mmmAM (or PM)').

```
SELECT TO_CHAR(NOW(),'Mon DD YYYY HH:MI:SS:MSAM');

Jul 25 2018 5:20:10.8975085PM
```

The following example uses the `::` characters.

```
SELECT '2.35'::DECIMAL + 4.5 AS results;

results
6.85
```

## Summary
<a name="chap-sql-server-aurora-pg.tsql.castconvert.summary"></a>


| Option | SQL Server |  Aurora PostgreSQL  | 
| --- | --- | --- | 
| Explicit `CAST`  |  `SELECT CAST('23.7' AS varchar) AS int`  |  `SELECT CAST('23.7' AS varchar) AS int`  | 
| Explicit `CONVERT`  |  `SELECT CONVERT (VARCHAR, '23.7')`  | Need to use `CAST`: | 
|  `SELECT CAST('23.7' AS varchar) AS int`  | Implicit casting |  `SELECT 23 + 2.0 SELECT 23 + 2.0`  | 
| Convert to a specific date format: `'mon dd yyyy hh:mi:ss:mmmAM'`  |  `SELECT CONVERT(nvarchar (30), GETDATE(), 109)`  |  `SELECT TO_CHAR(NOW(),'Mon DD YYYY HH:MI:SS:MSAM')`  | 

For more information, see [CREATE CAST](https://www.postgresql.org/docs/13/sql-createcast.html), [Type Conversion](https://www.postgresql.org/docs/13/typeconv.html), and [CREATE CONVERSION](https://www.postgresql.org/docs/13/sql-createconversion.html) in the *PostgreSQL documentation*.