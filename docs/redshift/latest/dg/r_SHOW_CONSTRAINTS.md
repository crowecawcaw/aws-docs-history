Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW CONSTRAINTS

Shows a list of primary key and foreign key constraints in a table.

## Required permissions

To execute SHOW CONSTRAINTS on a table, the current user must satisfy one of the following criteria:

- Be a superuser
- Be the owner of the table
- Be granted USAGE privilege on the parent schema and SELECT privilege on the table

## Syntax

```
SHOW CONSTRAINTS {PRIMARY KEYS | FOREIGN KEYS [EXPORTED]}
FROM TABLE
{ *database\_name*.*schema\_name*.*table\_name* | *schema\_name*.*table\_name* }
[LIMIT *row\_limit*]
```

## Parameters

_database_name_

The name of the database containing the target table

_schema_name_

The name of the schema containing the target table

_table_name_

The name of the target table

EXPORTED

When EXPORTED is specified, then list all foreign keys from other tables that reference the target table.

_row_limit_

The maximum number of rows to return. The _row_limit_ can be 0–10,000.

## Examples

The following example shows primary key constraints from table demo_db.demo_schema.pk1:

```
SHOW CONSTRAINTS PRIMARY KEYS FROM TABLE demo_db.demo_schema.pk1;
 database_name | schema_name | table_name | pk_name  | column_name | key_seq
---------------+-------------+------------+----------+-------------+---------
 demo_db       | demo_schema | pk1        | pk1_pkey | i           |       1
 demo_db       | demo_schema | pk1        | pk1_pkey | j           |       2
 demo_db       | demo_schema | pk1        | pk1_pkey | c           |       3
```

The following example shows foreign key constraints from table demo_schema.fk2:

```
SHOW CONSTRAINTS FOREIGN KEYS FROM TABLE demo_schema.fk2;
 pk_database_name | pk_schema_name | pk_table_name | pk_column_name | fk_database_name | fk_schema_name | fk_table_name | fk_column_name | key_seq |  fk_name   | pk_name  | update_rule | delete_rule | deferrability
------------------+----------------+---------------+----------------+------------------+----------------+---------------+----------------+---------+------------+----------+-------------+-------------+---------------
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | fk2           | i              |       1 | fk2_i_fkey | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | fk2           | j              |       2 | fk2_i_fkey | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | fk2           | c              |       3 | fk2_i_fkey | pk1_pkey |             |             |
```

The following example shows exported foreign key constraints from table demo_schema.pk1:

```
SHOW CONSTRAINTS FOREIGN KEYS EXPORTED FROM TABLE demo_schema.pk1;
 pk_database_name | pk_schema_name | pk_table_name | pk_column_name | fk_database_name | fk_schema_name | fk_table_name | fk_column_name | key_seq |     fk_name     | pk_name  | update_rule | delete_rule | deferrability
------------------+----------------+---------------+----------------+------------------+----------------+---------------+----------------+---------+-----------------+----------+-------------+-------------+---------------
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | fk2           | i              |       1 | fk2_i_fkey      | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | fk2           | j              |       2 | fk2_i_fkey      | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | fk2           | c              |       3 | fk2_i_fkey      | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | i              | demo_db          | demo_schema    | other_fk      | i              |       1 | other_fk_i_fkey | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | j              | demo_db          | demo_schema    | other_fk      | j              |       2 | other_fk_i_fkey | pk1_pkey |             |             |
 demo_db          | demo_schema    | pk1           | c              | demo_db          | demo_schema    | other_fk      | c              |       3 | other_fk_i_fkey | pk1_pkey |             |             |
```
