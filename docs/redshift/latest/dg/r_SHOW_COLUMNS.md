

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW COLUMNS
<a name="r_SHOW_COLUMNS"></a>

Shows a list of columns in a table, along with some column attributes.

Each output row consists of a comma-separated list of database name, schema name, table name, column name, ordinal position, column default, is nullable, data type, character maximum length, numeric precision, remarks, sort key type, sort key order, distribution key, encoding, and collation. For more information about these attributes, see [SVV\_ALL\_COLUMNS](r_SVV_ALL_COLUMNS.md).

If more than 10,000 columns would result from the SHOW COLUMNS command, then an error is returned.

## Required permissions
<a name="r_SHOW_COLUMNS-privileges"></a>

To view a column in an Amazon Redshift table, the current user must satisfy one of the following criteria:
+ Be a superuser.
+ Be the owner of the table.
+ Granted USAGE privilege on the parent schema and granted SELECT privilege on the table or granted SELECT privilege on the column.

## Syntax
<a name="r_SHOW_COLUMNS-synopsis"></a>

```
SHOW COLUMNS FROM TABLE database_name.schema_name.table_name [LIKE 'filter_pattern'] [LIMIT row_limit ]
```

## Parameters
<a name="r_SHOW_COLUMNS-parameters"></a>

 *database\_name*   
The name of the database that contains the tables to list.   
To show tables in an AWS Glue Data Catalog, specify (`awsdatacatalog`) as the database name, and make sure the system configuration `data_catalog_auto_mount` is set to `true`. For more information, see [ALTER SYSTEM](r_ALTER_SYSTEM.md).

 *schema\_name*   
The name of the schema that contains the tables to list.   
To show AWS Glue Data Catalog tables, provide the AWS Glue database name as the schema name.

 *table\_name*   
The name of the table that contains the columns to list. 

 *filter\_pattern*   
A valid UTF-8 character expression with a pattern to match column names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_COLUMNS.html)
If *filter\_pattern* does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator. 

 *row\_limit*   
The maximum number of rows to return. The *row\_limit* can be 0–10,000. 

## Examples
<a name="r_SHOW_COLUMNS-examples"></a>

Following example shows the columns in the Amazon Redshift database named `sample_data_dev` that are in schema `tickit` and table `event`.

```
SHOW COLUMNS FROM TABLE demo_schema.compound_sort_table;

  database_name | schema_name |     table_name      | column_name | ordinal_position | column_default | is_nullable |     data_type     | character_maximum_length | numeric_precision | numeric_scale | remarks | sort_key_type | sort_key | dist_key | encoding | collation 
---------------+-------------+---------------------+-------------+------------------+----------------+-------------+-------------------+--------------------------+-------------------+---------------+---------+---------------+----------+----------+----------+-----------
 demo_db       | demo_schema | compound_sort_table | id          |                1 |                | YES         | integer           |                          |                32 |             0 |         | COMPOUND      |        1 |        1 | delta32k | 
 demo_db       | demo_schema | compound_sort_table | name        |                2 |                | YES         | character varying |                       50 |                   |               |         | COMPOUND      |        2 |          | lzo      | default
 demo_db       | demo_schema | compound_sort_table | date_col    |                3 |                | YES         | date              |                          |                   |               |         |               |        0 |          | delta    | 
 demo_db       | demo_schema | compound_sort_table | amount      |                4 |                | YES         | numeric           |                          |                10 |             2 |         |               |        0 |          | mostly16 |
```

Following example shows the tables in the AWS Glue Data Catalog database named `awsdatacatalog` that are in schema `batman` and table `nation`. Output is limited to `2` rows.

```
SHOW COLUMNS FROM TABLE second_db.public.t22;

 database_name | schema_name | table_name | column_name | ordinal_position | column_default | is_nullable |          data_type          | character_maximum_length | numeric_precision | numeric_scale | remarks | sort_key_type | sort_key | dist_key | encoding | collation 
---------------+-------------+------------+-------------+------------------+----------------+-------------+-----------------------------+--------------------------+-------------------+---------------+---------+---------------+----------+----------+----------+-----------
 second_db     | public      | t22        | col1        |                1 |                | YES         | integer                     |                          |                32 |             0 |         | INTERLEAVED   |       -1 |          | mostly8  | 
 second_db     | public      | t22        | col2        |                2 |                | YES         | character varying           |                      100 |                   |               |         | INTERLEAVED   |        2 |          | text255  | default
 second_db     | public      | t22        | col3        |                3 |                | YES         | timestamp without time zone |                          |                   |               |         |               |        0 |          | raw      | 
 second_db     | public      | t22        | col4        |                4 |                | YES         | numeric                     |                          |                10 |             2 |         |               |        0 |          | az64     |
```