Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ALL_TABLES

Use SVV_ALL_TABLES to view a union of Amazon Redshift tables as shown in SVV_REDSHIFT_TABLES and the consolidated list of all external tables from all external
schemas. For information about Amazon Redshift tables, see [SVV_REDSHIFT_TABLES](r_SVV_REDSHIFT_TABLES.md "r_SVV_REDSHIFT_TABLES.md").

SVV_ALL_TABLES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type    | Description                                                                                           |
| ------------- | ------------ | ----------------------------------------------------------------------------------------------------- |
| database_name | varchar(128) | The name of the database where the table exists.                                                      |
| schema_name   | varchar(128) | The schema name for the table.                                                                        |
| table_name    | varchar(128) | The name of the table.                                                                                |
| table_acl     | varchar(128) | The string that defines the permission for the<br>specified user or user group for the table.         |
| table_type    | varchar(128) | The type of the table. Possible values are views,<br>base tables, external tables, and shared tables. |
| remarks       | varchar(256) | Remarks.                                                                                              |

## Sample queries

The following example returns the output of SVV_ALL_TABLES.

```
`SELECT *
FROM svv_all_tables
WHERE database_name = 'tickit_db'
ORDER BY TABLE_NAME,
 SCHEMA_NAME
LIMIT 5;`

 `database_name | schema_name | table_name | table_type | table_acl | remarks
---------------+-------------+--------------------------+------------+-----------+---------
 tickit_db | public | tickit_category_redshift | TABLE | |
 tickit_db | public | tickit_date_redshift | TABLE | |
 tickit_db | public | tickit_event_redshift | TABLE | |
 tickit_db | public | tickit_listing_redshift | TABLE | |
 tickit_db | public | tickit_sales_redshift | TABLE | |`
```

If the table_acl value is null, no access privileges have been explicitly granted to the corresponding table.
