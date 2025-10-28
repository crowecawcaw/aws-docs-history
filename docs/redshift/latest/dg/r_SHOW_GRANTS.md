Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW GRANTS

Displays grants for a user, role, or object. The object can be a database, a schema, a
table, or a function. When you specify an object, such as a table or function, you need to
qualify it with two-part or three-part notation. For example,
`schema_name.table_name` or
`database_name.schema_name.table_name`.

## Syntax

The following is the syntax for showing grants on an object. Note that the second way
of specifying a function is only valid for external schemas and databases created from a
datashare.

```
SHOW GRANTS ON
{
 DATABASE database_name |
 FUNCTION {database_name.schema_name.function_name | schema_name.function_name } ( [ [ argname ] argtype [, ...] ] ) |
 FUNCTION {database_name.schema_name.function_name | schema_name.function_name } |
 SCHEMA {database_name.schema_name | schema_name} |
 { TABLE {database_name.schema_name.table_name | schema_name.table_name} | table_name }
}
[FOR {username | ROLE role_name | PUBLIC}]
[LIMIT row_limit]
```

The following is the syntax for showing grants for a user or role.

```
SHOW GRANTS FOR
{username | ROLE role_name}
[LIMIT row_limit]
```

## Parameters

_database_name_

The name of the database to show grants on.

_function_name_

The name of the function to show grants on.

_schema_name_

The name of the schema to show grants on.

_table_name_

The name of the table to show grants on.

FOR _username_

Indicates showing grants for a user.

FOR ROLE _role_name_

Indicates showing grants for a role.

FOR PUBLIC

Indicates showing grants for PUBLIC.

_row_limit_

The maximum number of rows to return. The _row_limit_ can
be 0–10,000.

## Examples

The following example displays all grants on a database named
`dev`.

```
SHOW GRANTS ON DATABASE dev;

 database_name | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
---------------+----------------+-------------+---------------+---------------+--------------+-----------------
 dev           | TRUNCATE       |         101 | alice         | user          | f            | TABLES
 dev           | DROP           |         101 | alice         | user          | f            | TABLES
 dev           | INSERT         |         101 | alice         | user          | f            | TABLES
 dev           | ALTER          |         101 | alice         | user          | f            | TABLES
 dev           | TEMP           |           0 | public        | public        | f            | DATABASE
 dev           | DELETE         |         101 | alice         | user          | f            | TABLES
 dev           | SELECT         |         101 | alice         | user          | f            | TABLES
 dev           | UPDATE         |         101 | alice         | user          | f            | TABLES
 dev           | REFERENCES     |         101 | alice         | user          | f            | TABLES
(9 rows)
```

The following command shows all grants on a schema named `demo`.

```
SHOW GRANTS ON SCHEMA demo;

 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------
 demo        | demo        | SCHEMA      | ALTER          |         101 | alice         | user          | f            | SCHEMA
 demo        | demo        | SCHEMA      | DROP           |         101 | alice         | user          | f            | SCHEMA
 demo        | demo        | SCHEMA      | USAGE          |         101 | alice         | user          | f            | SCHEMA
 demo        | demo        | SCHEMA      | CREATE         |         101 | alice         | user          | f            | SCHEMA
(4 rows)
```

The following command shows all grants for a user named `alice`.

```
SHOW GRANTS FOR alice;

 database_name | schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | privilege_scope
---------------+-------------+-------------+-------------+----------------+-------------+---------------+---------------+-----------------
 dev           |             |             | DATABASE    | INSERT         |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | SELECT         |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | UPDATE         |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | DELETE         |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | REFERENCES     |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | DROP           |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | TRUNCATE       |         101 | alice         | user          | TABLES
 dev           |             |             | DATABASE    | ALTER          |         101 | alice         | user          | TABLES
 dev           | public      | t1          | TABLE       | INSERT         |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | SELECT         |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | UPDATE         |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | DELETE         |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | REFERENCES     |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | DROP           |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | TRUNCATE       |         101 | alice         | user          | TABLE
 dev           | public      | t1          | TABLE       | ALTER          |         101 | alice         | user          | TABLE
 dev           | demo        |             | SCHEMA      | USAGE          |         101 | alice         | user          | SCHEMA
 dev           | demo        |             | SCHEMA      | CREATE         |         101 | alice         | user          | SCHEMA
 dev           | demo        |             | SCHEMA      | DROP           |         101 | alice         | user          | SCHEMA
 dev           | demo        |             | SCHEMA      | ALTER          |         101 | alice         | user          | SCHEMA
(20 rows)
```

The following command shows all grants on a table named `t3` for a user named
`alice`. Note that you can either use two-part or three-part notation to
specify the table name.

```

SHOW GRANTS ON TABLE demo_db.demo_schema.t3 FOR alice;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------
 demo_schema | t3          | TABLE       | ALTER          |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | TRUNCATE       |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | DROP           |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | SELECT         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | INSERT         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | UPDATE         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | DELETE         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | REFERENCES     |         100 | alice         | user          | f            | TABLE
(8 rows)

SHOW GRANTS ON TABLE demo_schema.t3 FOR alice;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------
 demo_schema | t3          | TABLE       | ALTER          |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | TRUNCATE       |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | DROP           |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | SELECT         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | INSERT         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | UPDATE         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | DELETE         |         100 | alice         | user          | f            | TABLE
 demo_schema | t3          | TABLE       | REFERENCES     |         100 | alice         | user          | f            | TABLE
(8 rows)
```

The following example shows all grants on a table named `t4`. Note the
different ways that you can specify the table name.

```
SHOW GRANTS ON t4;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------
 public      | t4          | TABLE       | ALTER          |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | TRUNCATE       |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | DROP           |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | SELECT         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | INSERT         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | UPDATE         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | DELETE         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | REFERENCES     |         100 | alice         | user          | f            | TABLE
(8 rows)

SHOW GRANTS ON TABLE public.t4;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------
 public      | t4          | TABLE       | ALTER          |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | TRUNCATE       |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | DROP           |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | SELECT         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | INSERT         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | UPDATE         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | DELETE         |         100 | alice         | user          | f            | TABLE
 public      | t4          | TABLE       | REFERENCES     |         100 | alice         | user          | f            | TABLE
(8 rows)
```
