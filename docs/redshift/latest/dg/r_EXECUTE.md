Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# EXECUTE

Runs a previously prepared statement.

## Syntax

```
EXECUTE *plan\_name* [ (*parameter* [, ...]) ]
```

## Parameters

_plan_name_

Name of the prepared statement to be run.

_parameter_

The actual value of a parameter to the prepared statement. This must be an
expression yielding a value of a type compatible with the data type specified
for this parameter position in the PREPARE command that created the prepared
statement.

## Usage notes

EXECUTE is used to run a previously prepared statement. Because prepared statements
only exist for the duration of a session, the prepared statement must have been created
by a PREPARE statement run earlier in the current session.

If the previous PREPARE statement specified some parameters, a compatible set of
parameters must be passed to the EXECUTE statement, or else Amazon Redshift returns an error.
Unlike functions, prepared statements aren't overloaded based on the type or number
of specified parameters; the name of a prepared statement must be unique within a
database session.

When an EXECUTE command is issued for the prepared statement, Amazon Redshift may optionally
revise the query execution plan (to improve performance based on the specified parameter
values) before running the prepared statement. Also, for each new execution of a
prepared statement, Amazon Redshift may revise the query execution plan again based on the
different parameter values specified with the EXECUTE statement. To examine the query
execution plan that Amazon Redshift has chosen for any given EXECUTE statements, use the [EXPLAIN](r_EXPLAIN.md "r_EXPLAIN.md") command.

For examples and more information on the creation and usage of prepared statements,
see [PREPARE](r_PREPARE.md "r_PREPARE.md").

## See also

[DEALLOCATE](r_DEALLOCATE.md "r_DEALLOCATE.md"), [PREPARE](r_PREPARE.md "r_PREPARE.md")
