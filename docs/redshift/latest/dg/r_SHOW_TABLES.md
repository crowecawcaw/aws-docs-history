Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW TABLES

Shows a list of tables in a schema, along with some table attributes.

Each output row consists of database name, schema name, table name, table type, table ACL, and remarks.
For more information about these attributes, see [SVV_ALL_TABLES](r_SVV_ALL_TABLES.md "r_SVV_ALL_TABLES.md").

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

Following example shows the tables in the Amazon Redshift database named `dev` that
are in schema `public`.

```
`SHOW TABLES FROM SCHEMA dev.public;`
`database_name | schema_name | table_name | table_type | table_acl | remarks
---------------+-------------+------------+------------+-----------+---------
 dev | public | tb | TABLE | |
 dev | public | tb2 | TABLE | |
 dev | public | tb3 | TABLE | |`
```

Following example shows the tables in the AWS Glue Data Catalog database named
`awsdatacatalog` that are in schema `batman`.

```
`SHOW TABLES FROM SCHEMA awsdatacatalog.batman;`
`database_name | schema_name | table_name | table_type | table_acl | remarks
----------------+-------------+------------------+------------+-----------+---------
 awsdatacatalog | batman | nation | EXTERNAL | |
 awsdatacatalog | batman | part | EXTERNAL | |
 awsdatacatalog | batman | partsupp | EXTERNAL | |
 awsdatacatalog | batman | region | EXTERNAL | |
 awsdatacatalog | batman | supplier | EXTERNAL | |
 awsdatacatalog | batman | automount_nation | EXTERNAL | |`
```
