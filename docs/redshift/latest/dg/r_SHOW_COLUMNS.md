Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW COLUMNS

Shows a list of columns in a table, along with some column attributes.

Each output row consists of a comma-separated list of database name, schema name, table name, column name, ordinal position, column default, is nullable, data type, character maximum length,
numeric precision, and remarks.
For more information about these attributes, see [SVV_ALL_COLUMNS](r_SVV_ALL_COLUMNS.md "r_SVV_ALL_COLUMNS.md").

If more than 10,000 columns would result from the SHOW COLUMNS command, then an error is returned.

## Required permissions

To view a column in an Amazon Redshift table, the current user must satisfy one of the following criteria:

- Be a superuser.
- Be the owner of the table.
- Granted USAGE privilege on the parent schema and granted SELECT privilege on the table or granted SELECT privilege on the column.

## Syntax

```
SHOW COLUMNS FROM TABLE *database\_name*.*schema\_name*.*table\_name* [LIKE '*filter\_pattern*'] [LIMIT *row\_limit* ]
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

_table_name_

The name of the table that contains the columns to list.

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

Following example shows the columns in the Amazon Redshift database named `sample_data_dev` that
are in schema `tickit` and table `event`.

```
`SHOW COLUMNS FROM TABLE sample_data_dev.tickit.event;`
`database_name | schema_name | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | numeric_precision | numeric_scale | remarks
-------------------+-------------+------------+-------------+------------------+----------------+-------------+------------------------------+--------------------------+-------------------+------------------------
 sample_data_dev | tickit | event | eventid | 1 | NULL | NO | integer | NULL | 32 | 0 | NULL
 sample_data_dev | tickit | event | eventid | 2 | NULL | NO | smallint | NULL | 16 | 0 | NULL
 sample_data_dev | tickit | event | eventid | 3 | NULL | NO | smallint | NULL | 16 | 0 | NULL
 sample_data_dev | tickit | event | eventid | 4 | NULL | NO | smallint | NULL | 16 | 0 | NULL
 sample_data_dev | tickit | event | eventid | 5 | NULL | YES | character varying | 200 | NULL | NULL | NULL
 sample_data_dev | tickit | event | eventid | 6 | NULL | YES | timestamp without time zo... | NULL | NULL | NULL | NULL`
```

Following example shows the tables in the AWS Glue Data Catalog database named
`awsdatacatalog` that are in schema `batman` and table
`nation`. Output is limited to `2` rows.

```
`SHOW COLUMNS FROM TABLE awsdatacatalog.batman.nation LIMIT 2;`
`database_name | schema_name | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | numeric_precision | remarks
----------------+-------------+------------+-------------+------------------+----------------+-------------+-----------+--------------------------+-------------------+---------
 awsdatacatalog | batman | nation | n_nationkey | 1 | | | integer | | |
 awsdatacatalog | batman | nation | n_name | 2 | | | character | | |`
```
