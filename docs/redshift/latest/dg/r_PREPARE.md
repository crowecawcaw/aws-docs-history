Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PREPARE

Prepare a statement for execution.

PREPARE creates a prepared statement. When the PREPARE statement is run, the specified
statement (SELECT, INSERT, UPDATE, or DELETE) is parsed, rewritten, and planned. When an
EXECUTE command is then issued for the prepared statement, Amazon Redshift may optionally revise
the query execution plan (to improve performance based on the specified parameter values)
before running the prepared statement.

## Syntax

```
PREPARE *plan\_name* [ (*datatype* [, ...] ) ] AS *statement*

```

## Parameters

_plan_name_

An arbitrary name given to this particular prepared statement. It must be
unique within a single session and is subsequently used to run or deallocate a
previously prepared statement.

_datatype_

The data type of a parameter to the prepared statement. To refer to the
parameters in the prepared statement itself, use $1, $2, and so on, up to a maximum of $32767.

_statement_

Any SELECT, INSERT, UPDATE, or DELETE statement.

## Usage notes

Prepared statements can take parameters: values that are substituted into the
statement when it is run. To include parameters in a prepared statement, supply a list
of data types in the PREPARE statement, and, in the statement to be prepared itself,
refer to the parameters by position using the notation $1, $2, ... The maximum number
of parameters is 32767. When running the
statement, specify the actual values for these parameters in the EXECUTE statement. For
more details, see [EXECUTE](r_EXECUTE.md "r_EXECUTE.md").

Prepared statements only last for the duration of the current session. When the
session ends, the prepared statement is discarded, so it must be re-created before being
used again. This also means that a single prepared statement can't be used by
multiple simultaneous database clients; however, each client can create its own prepared
statement to use. The prepared statement can be manually removed using the DEALLOCATE
command.

Prepared statements have the largest performance advantage when a single session is
being used to run a large number of similar statements. As mentioned, for each new
execution of a prepared statement, Amazon Redshift may revise the query execution plan to
improve performance based on the specified parameter values. To examine the query
execution plan that Amazon Redshift has chosen for any specific EXECUTE statements, use the
[EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md") command.

For more information on query planning and the statistics collected by Amazon Redshift for
query optimization, see the [ANALYZE](r_ANALYZE.md "r_ANALYZE.md")
command.

## Examples

Create a temporary table, prepare INSERT statement and then run it:

```
DROP TABLE IF EXISTS prep1;
CREATE TABLE prep1 (c1 int, c2 char(20));
PREPARE prep_insert_plan (int, char)
AS insert into prep1 values ($1, $2);
EXECUTE prep_insert_plan (1, 'one');
EXECUTE prep_insert_plan (2, 'two');
EXECUTE prep_insert_plan (3, 'three');
DEALLOCATE prep_insert_plan;
```

Prepare a SELECT statement and then run it:

```
PREPARE prep_select_plan (int)
AS select * from prep1 where c1 = $1;
EXECUTE prep_select_plan (2);
EXECUTE prep_select_plan (3);
DEALLOCATE prep_select_plan;
```

## See also

[DEALLOCATE](r_DEALLOCATE.md "r_DEALLOCATE.md"), [EXECUTE](r_EXECUTE.md "r_EXECUTE.md")
