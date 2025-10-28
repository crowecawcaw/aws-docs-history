Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP DATABASE

Drops a database.

You can't run DROP DATABASE within a transaction block (BEGIN ... END). For more
information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

## Syntax

```
DROP DATABASE *database\_name* [ FORCE ]
```

## Parameters

_database_name_

Name of the database to be dropped. You can't drop the dev,
padb_harvest, template0, template1, or sys:internal databases, and you
can't drop the current database.

To drop an external database, drop the external schema. For more
information, see [DROP SCHEMA](r_DROP_SCHEMA.md "r_DROP_SCHEMA.md").

FORCE

When you specify FORCE, DROP DATABASE attempts to terminate active
connections prior to dropping the database. If all active connections
successfully terminate within a timeout, the drop proceeds. If not all
connections terminate, the command throws an error.

## DROP DATABASE usage notes

When using the DROP DATABASE statement, consider the following:

- In general, we recommend that you don't drop a database that contains an
  AWS Data Exchange datashare using the DROP DATABASE statement. If you do, the
  AWS accounts that have access to the datashare lose access. Performing this type
  of alteration can breach data product terms in AWS Data Exchange.

The following example shows an error when a database that contains an AWS Data Exchange
datashare is dropped.

```
DROP DATABASE test_db;
ERROR:   Drop of database test_db that contains ADX-managed datashare(s) requires session variable datashare_break_glass_session_var to be set to value 'ce8d280c10ad41'
```

To allow dropping the database, set the following variable and run the DROP
DATABASE statement again.

```
SET datashare_break_glass_session_var to 'ce8d280c10ad41';
```

```
DROP DATABASE test_db;
```

In this case, Amazon Redshift generates a random one-time value to set the session
variable to allow DROP DATABASE for a database that contains an AWS Data Exchange
datashare.

## Examples

The following example drops a database named TICKIT_TEST:

```
drop database tickit_test;
```
