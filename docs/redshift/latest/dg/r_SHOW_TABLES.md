

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SHOW TABLES
<a name="r_SHOW_TABLES"></a>

Shows a list of tables in a schema, along with some table attributes.

Each output row consists of database name, schema name, table name, table type, table ACL, remarks, table owner, last altered time, last modified time, dist\_style, and table sub-type. For more information about these attributes, see [SVV\_ALL\_TABLES](r_SVV_ALL_TABLES.md).

The modification and alteration timestamps can lag behind the table updates at a fixed interval of approximately 5 minutes.

If more than 10,000 tables would result from the SHOW TABLES command, then an error is returned.

## Required permissions
<a name="r_SHOW_TABLES-privileges"></a>

To view a table in an Amazon Redshift schema, the current user must satisfy one of the following criteria:
+ Be a superuser.
+ Be the owner of the table.
+ Granted USAGE privilege on the parent schema and granted SELECT privilege on the table or granted SELECT privilege on any column in the table.

## Syntax
<a name="r_SHOW_TABLES-synopsis"></a>

```
SHOW TABLES FROM SCHEMA database_name.schema_name [LIKE 'filter_pattern'] [LIMIT row_limit ]
```

## Parameters
<a name="r_SHOW_TABLES-parameters"></a>

 *database\_name*   
The name of the database that contains the tables to list.   
To show tables in an AWS Glue Data Catalog, specify (`awsdatacatalog`) as the database name, and make sure the system configuration `data_catalog_auto_mount` is set to `true`. For more information, see [ALTER SYSTEM](r_ALTER_SYSTEM.md).

 *schema\_name*   
The name of the schema that contains the tables to list.   
To show AWS Glue Data Catalog tables, provide the AWS Glue database name as the schema name.

 *filter\_pattern*   
A valid UTF-8 character expression with a pattern to match table names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/redshift/latest/dg/r_SHOW_TABLES.html)
If *filter\_pattern* does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator. 

 *row\_limit*   
The maximum number of rows to return. The *row\_limit* can be 0–10,000. 

## Examples
<a name="r_SHOW_TABLES-examples"></a>

```
SHOW TABLES FROM SCHEMA s1;

 database_name | schema_name |    table_name     | table_type |              table_acl              | remarks | owner |     last_altered_time      |     last_modified_time     | dist_style |   table_subtype   
---------------+-------------+-------------------+------------+-------------------------------------+---------+-------+----------------------------+----------------------------+------------+-------------------
 dev           | s1          | late_binding_view | VIEW       | alice=arwdRxtDPA/alice~bob=d/alice  |         | alice |                            |                            |            | LATE BINDING VIEW
 dev           | s1          | manual_mv         | VIEW       | alice=arwdRxtDPA/alice~bob=P/alice  |         | alice |                            |                            |            | MATERIALIZED VIEW
 dev           | s1          | regular_view      | VIEW       | alice=arwdRxtDPA/alice~bob=r/alice  |         | alice |                            |                            |            | REGULAR VIEW
 dev           | s1          | test_table        | TABLE      | alice=arwdRxtDPA/alice~bob=rw/alice |         | alice | 2025-11-18 15:52:00.010452 | 2025-11-18 15:44:34.856073 | AUTO (ALL) | REGULAR TABLE
```

```
SHOW TABLES FROM SCHEMA dev.s1 LIKE '%view' LIMIT 1;

 database_name | schema_name |    table_name     | table_type |              table_acl               | remarks | owner | last_altered_time | last_modified_time | dist_style |   table_subtype   
---------------+-------------+-------------------+------------+--------------------------------------+---------+-------+-------------------+--------------------+------------+-------------------
 dev           | s1          | late_binding_view | VIEW       | {alice=arwdRxtDPA/alice,bob=d/alice} |         | alice |                   |                    |            | LATE BINDING VIEW
```