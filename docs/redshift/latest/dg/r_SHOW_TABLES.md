Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW TABLES

Shows a list of tables in a schema, along with some table attributes.

Each output row consists of database name, schema name, table name, table type, table ACL, remarks, table owner, last altered time, last modified time, dist_style, and table sub-type.
For more information about these attributes, see [SVV_ALL_TABLES](r_SVV_ALL_TABLES.md "r_SVV_ALL_TABLES.md").

The modification and alteration timestamps can lag behind the table updates by approximately 20 minutes.

If more than 10,000 tables would result from the SHOW TABLES command, then an error is returned.

## Required permissions

To view a table in an Amazon Redshift schema, the current user must satisfy one of the following criteria:

- Be a superuser.
- Be the owner of the table.
- Granted USAGE privilege on the parent schema and granted SELECT privilege on the table or granted SELECT privilege on any column in the table.

## Syntax

```
SHOW TABLES FROM SCHEMA *database\_name*.*schema\_name* [LIKE '*filter\_pattern*'] [LIMIT *row\_limit* ]
```

## Parameters

_database_name_

The name of the database that contains the tables to list.

To show tables in an AWS Glue Data Catalog, specify (`awsdatacatalog`) as
the database name, and ensure the system configuration
`data_catalog_auto_mount` is set to `true`. For more
information, see [ALTER SYSTEM](r_ALTER_SYSTEM.md "r_ALTER_SYSTEM.md").

_schema_name_

The name of the schema that contains the tables to list.

To show AWS Glue Data Catalog tables, provide the AWS Glue database name as the schema
name.

_filter_pattern_

A valid UTF-8 character expression with a pattern to match table names. The
LIKE option performs a case-sensitive match that supports the following
pattern-matching metacharacters:

| Metacharacter | Description                                         |
| ------------- | --------------------------------------------------- |
| `%`           | Matches any sequence of zero or more<br>characters. |
| `_`           | Matches any single character.                       |

If _filter_pattern_ does not contain metacharacters, then
the pattern only represents the string itself; in that case LIKE acts the same
as the equals operator.

_row_limit_

The maximum number of rows to return. The _row_limit_ can
be 0–10,000.

## Examples

```
`SHOW TABLES FROM SCHEMA s1;`
`database_name | schema_name | table_name | table_type | table_acl | remarks | owner | last_altered_time | last_modified_time | dist_style | table_subtype
---------------+-------------+-------------------+------------+-------------------------------------+---------+-------+----------------------------+----------------------------+------------+-------------------
 dev | s1 | late_binding_view | VIEW | alice=arwdRxtDPA/alice~bob=d/alice | | alice | | | | LATE BINDING VIEW
 dev | s1 | manual_mv | VIEW | alice=arwdRxtDPA/alice~bob=P/alice | | alice | | | | MATERIALIZED VIEW
 dev | s1 | regular_view | VIEW | alice=arwdRxtDPA/alice~bob=r/alice | | alice | | | | REGULAR VIEW
 dev | s1 | test_table | TABLE | alice=arwdRxtDPA/alice~bob=rw/alice | | alice | 2025-11-18 15:52:00.010452 | 2025-11-18 15:44:34.856073 | AUTO (ALL) | REGULAR TABLE`
```

```
`SHOW TABLES FROM SCHEMA dev.s1 LIKE '%view' LIMIT 1;`
`database_name | schema_name | table_name | table_type | table_acl | remarks | owner | last_altered_time | last_modified_time | dist_style | table_subtype
---------------+-------------+-------------------+------------+--------------------------------------+---------+-------+-------------------+--------------------+------------+-------------------
 dev | s1 | late_binding_view | VIEW | {alice=arwdRxtDPA/alice,bob=d/alice} | | alice | | | | LATE BINDING VIEW`
```
