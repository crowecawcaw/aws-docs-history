# CREATE FUNCTION

Amazon Kinesis Data Analytics provides a number of [Functions](sql-reference-functions.md "sql-reference-functions.md"), and also allows users to extend its
capabilities by means of user-defined functions (UDFs). Amazon Kinesis Data Analytics supports UDFs defined in SQL only.

User-defined functions may be invoked using either the fully-qualified
name or by the function name alone.

Values passed to (or returned from) a user-defined function or transformation must be exactly
the same data types as the corresponding parameter definitions. In other words, implicit casting
is not allowed in passing parameters to (or returning values from) a user-defined function.

## User-Defined Function (UDF)

A user-defined function can implement complex calculations, taking zero or more scalar
parameters and returning a scalar result. UDFs operate like built-in functions such as FLOOR() or
LOWER(). For each occurrence of a user-defined function within a SQL statement, that UDF is
called once per row with scalar parameters: constants or column values in that row.

## Syntax

```
 CREATE FUNCTION ''<function_name>'' ( ''<parameter_list>'' )
  RETURNS ''<data type>''
  LANGUAGE SQL
  [ SPECIFIC ''<specific_function_name>''  | [NOT] DETERMINISTIC ]
  CONTAINS SQL
  [ READS SQL DATA ]
  [ MODIFIES SQL DATA ]
  [ RETURNS NULL ON NULL INPUT | CALLED ON NULL INPUT ]  
  RETURN ''<SQL-defined function body>''

```

SPECIFIC assigns a specific function name that is unique within the application. Note that the
regular function name does not need to be unique (two or more functions may share the same name,
as long as they are distinguishable by their parameter list).

DETERMINISTIC / NOT DETERMINISTIC indicates whether a function will always return the same
result for a given set of parameter values. This may be used by your application for query
optimization.

READS SQL DATA and MODIFIES SQL DATA indicate whether the function potentially reads or
modifies SQL data, respectively. If a function attempts to read data from tables or streams without READS SQL DATA being specified, or insert to a stream or modify a table without
MODIFIES SQL DATA being specified, an exception will be raised.

RETURNS NULL ON NULL INPUT and CALLED ON NULL INPUT indicate whether the function is defined
as returning null if any of its parameters are null. If left unspecified, the default is CALLED ON
NULL INPUT.

A SQL-defined function body consists only of a single RETURN statement.

## Examples

```
CREATE FUNCTION get_fraction( degrees DOUBLE )
    RETURNS DOUBLE
    CONTAINS SQL
    RETURN degrees - FLOOR(degrees)
;
```
