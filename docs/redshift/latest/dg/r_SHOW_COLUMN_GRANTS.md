Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW COLUMN GRANTS

Displays grants on a column within a table.

## Required permissions

SHOW GRANTS for a target object will only display grants that are visible to the current user. A grant is visible to the current user if the current user satisfies one of the following criteria:

- Be a superuser
- Be the granted user
- Be granted owner of the granted role
- Be granted the role targeted by the object grant

## Syntax

```
SHOW COLUMN GRANTS ON TABLE
{ *database\_name*.*schema\_name*.*table\_name* | *schema\_name*.*table\_name* }
[FOR {*username* | ROLE *role\_name* | PUBLIC}]
[LIMIT *row\_limit*]
```

## Parameters

database_name

The name of the database containing the target table

schema_name

The name of the schema containing the target table

table_name

The name of the target table

username

Only include grants to username in the output

role_name

Only include grants to role_name in the output

PUBLIC

Only include grants to PUBLIC in the output

row_limit

The maximum number of rows to return. The _row_limit_ can be 0–10,000.

## Examples

The following example shows column grants on table demo_db.demo_schema.t100:

```
SHOW COLUMN GRANTS ON TABLE demo_db.demo_schema.t100;
 database_name | schema_name | table_name | column_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | grantor_name
---------------+-------------+------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+--------------
 demo_db       | demo_schema | t100       | b           | COLUMN      | UPDATE         |         134 | bob           | user          | f            | COLUMN          | dbadmin
 demo_db       | demo_schema | t100       | a           | COLUMN      | SELECT         |         130 | alice         | user          | f            | COLUMN          | dbadmin
 demo_db       | demo_schema | t100       | a           | COLUMN      | UPDATE         |         130 | alice         | user          | f            | COLUMN          | dbadmin
```

The following example shows column grants on table demo_schema.t100 for user bob:

```
SHOW COLUMN GRANTS ON TABLE demo_schema.t100 for bob;
 database_name | schema_name | table_name | column_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | grantor_name
---------------+-------------+------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+--------------
 demo_db       | demo_schema | t100       | b           | COLUMN      | UPDATE         |         135 | bob           | user          | f            | COLUMN          | dbadmin
```
