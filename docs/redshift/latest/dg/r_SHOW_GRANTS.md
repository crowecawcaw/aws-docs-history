Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW GRANTS

Displays grants for a user, role, or object. The object can be a database, a schema, a
table, a function, or a template. When you specify an object, such as a table or function, you need to
qualify it with two-part or three-part notation. For example,
`schema_name.table_name` or
`database_name.schema_name.table_name`.

If more than 10,000 rows would results from SHOW GRANTS, then the command raises an error.

## Required permissions

To run SHOW GRANTS for a target user or role, the current user must satisfy one of the following criteria:

- Be a superuser
- Be the target user
- Be the owner of the target role
- Be granted the role

SHOW GRANTS for a target object will only display grants that are visible to the current user. A grant is visible to the current user if the current user satisfies one of the following criteria:

- Be a superuser
- Be the target user
- Be granted owner of the granted role
- Be granted the role targeted by the object grant

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
 TEMPLATE {database_name.schema_name.template_name | template_name}
}
[FOR {username | ROLE role_name | PUBLIC}]
[LIMIT row_limit]
```

The following is the syntax for showing grants for a user or role.

```
SHOW GRANTS FOR
{username | ROLE role_name}
[FROM DATABASE database_name]
[LIMIT row_limit]
```

## Parameters

_database_name_

The name of the database to show grants on.

_function_name_

The name of the function to show grants on.

template_name

The name of the template to show grants on.

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
SHOW GRANTS on database demo_db;

  database_name | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | grantor_name
---------------+----------------+-------------+---------------+---------------+--------------+-----------------+--------------
 demo_db       | ALTER          |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | TRUNCATE       |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | DROP           |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | INSERT         |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | TEMP           |           0 | public        | public        | f            | DATABASE        | dbadmin
 demo_db       | SELECT         |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | UPDATE         |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | DELETE         |         112 | alice         | user          | f            | TABLES          | dbadmin
 demo_db       | REFERENCES     |         112 | alice         | user          | f            | TABLES          | dbadmin

```

The following command shows all grants on a schema named `demo`.

```
SHOW GRANTS ON SCHEMA demo_schema;

 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | database_name | grantor_name
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+---------------+--------------
 demo_schema | demo_schema | SCHEMA      | ALTER          |         112 | alice         | user          | f            | SCHEMA          | db1           | dbadmin
 demo_schema | demo_schema | SCHEMA      | DROP           |         112 | alice         | user          | f            | SCHEMA          | db1           | dbadmin
 demo_schema | demo_schema | SCHEMA      | USAGE          |         112 | alice         | user          | f            | SCHEMA          | db1           | dbadmin
 demo_schema | demo_schema | SCHEMA      | CREATE         |         112 | alice         | user          | f            | SCHEMA          | db1           | dbadmin
```

The following command shows all grants for a user named `alice`.

```
SHOW GRANTS FOR alice;

 database_name | schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | privilege_scope | grantor_name
---------------+-------------+-------------+-------------+----------------+-------------+---------------+---------------+-----------------+--------------
 demo_db       |             |             | DATABASE    | INSERT         |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | SELECT         |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | UPDATE         |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | DELETE         |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | REFERENCES     |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | DROP           |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | TRUNCATE       |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       |             |             | DATABASE    | ALTER          |         124 | alice         | user          | TABLES          | dbadmin
 demo_db       | demo_schema |             | SCHEMA      | USAGE          |         124 | alice         | user          | SCHEMA          | dbadmin
 demo_db       | demo_schema |             | SCHEMA      | CREATE         |         124 | alice         | user          | SCHEMA          | dbadmin
 demo_db       | demo_schema |             | SCHEMA      | DROP           |         124 | alice         | user          | SCHEMA          | dbadmin
 demo_db       | demo_schema |             | SCHEMA      | ALTER          |         124 | alice         | user          | SCHEMA          | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | INSERT         |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | SELECT         |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | UPDATE         |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | DELETE         |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | RULE           |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | REFERENCES     |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | TRIGGER        |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | DROP           |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | TRUNCATE       |         124 | alice         | user          | TABLE           | dbadmin
 demo_db       | demo_schema | t1          | TABLE       | ALTER          |         124 | alice         | user          | TABLE           | dbadmin
```

```
SHOW GRANTS FOR alice FROM DATABASE second_db;
 database_name | schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | privilege_scope | grantor_name
---------------+-------------+-------------+-------------+----------------+-------------+---------------+---------------+-----------------+--------------
 second_db     | public      | t22         | TABLE       | SELECT         |         101 | alice         | user          | TABLE           | dbadmin
```

The following command shows all grants on a table named `t3` for a user named
`alice`. Note that you can either use two-part or three-part notation to
specify the table name.

```

SHOW GRANTS ON TABLE demo_db.demo_schema.t3 FOR ALICE;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | database_name | grantor_name
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+---------------+--------------
 demo_schema | t3          | TABLE       | ALTER          |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | TRUNCATE       |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | DROP           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | TRIGGER        |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | SELECT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | INSERT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | UPDATE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | DELETE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | RULE           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | REFERENCES     |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin


SHOW GRANTS ON TABLE demo_schema.t3 FOR ALICE;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | database_name | grantor_name
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+---------------+--------------
 demo_schema | t3          | TABLE       | ALTER          |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | TRUNCATE       |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | DROP           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | TRIGGER        |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | SELECT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | INSERT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | UPDATE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | DELETE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | RULE           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 demo_schema | t3          | TABLE       | REFERENCES     |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin

```

The following example shows all grants on a table named `t4`. Note the
different ways that you can specify the table name.

```
SHOW GRANTS ON t4;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | database_name | grantor_name
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+---------------+--------------
 public      | t4          | TABLE       | ALTER          |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | TRUNCATE       |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | DROP           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | TRIGGER        |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | SELECT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | INSERT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | UPDATE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | DELETE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | RULE           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | REFERENCES     |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin

SHOW GRANTS ON TABLE public.t4;
 schema_name | object_name | object_type | privilege_type | identity_id | identity_name | identity_type | admin_option | privilege_scope | database_name | grantor_name
-------------+-------------+-------------+----------------+-------------+---------------+---------------+--------------+-----------------+---------------+--------------
 public      | t4          | TABLE       | ALTER          |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | TRUNCATE       |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | DROP           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | TRIGGER        |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | SELECT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | INSERT         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | UPDATE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | DELETE         |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | RULE           |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin
 public      | t4          | TABLE       | REFERENCES     |         130 | alice         | user          | f            | TABLE           | demo_db       | dbadmin

```
