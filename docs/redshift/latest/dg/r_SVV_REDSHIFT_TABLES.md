Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_REDSHIFT_TABLES

Use SVV_REDSHIFT_TABLES to view a list of all tables that a user has access to. This
set of tables includes the tables on the cluster and the tables from datashares provided
by remote clusters.

SVV_REDSHIFT_TABLES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type    | Description                                                                                    |
| ------------- | ------------ | ---------------------------------------------------------------------------------------------- |
| database_name | varchar(128) | The name of the database where a specified table<br>exists.                                    |
| schema_name   | varchar(128) | The name the schema for the table.                                                             |
| table_name    | varchar(128) | The name of the table.                                                                         |
| table_type    | varchar(128) | The type of table. Possible values are views and<br>tables.                                    |
| table_acl     | varchar(128) | The string that defines the permissions for the<br>specified user or user group for the table. |
| remarks       | varchar(128) | Remarks.                                                                                       |
| table_owner   | varchar(128) | The owner of the table.                                                                        |

## Sample query

The following example returns the output of SVV_REDSHIFT_TABLES.

```
`SELECT *
FROM svv_redshift_tables
WHERE database_name = 'tickit_db' AND TABLE_NAME LIKE 'tickit_%'
ORDER BY database_name,
TABLE_NAME;`

`database_name | schema_name | table_name | table_type | table_acl | remarks | table_owner
--------------+-------------+--------------------------+------------+-----------+---------+-----------
 tickit_db | public | tickit_category_redshift | TABLE | | +
 tickit_db | public | tickit_date_redshift | TABLE | | +
 tickit_db | public | tickit_event_redshift | TABLE | | +
 tickit_db | public | tickit_listing_redshift | TABLE | | +
 tickit_db | public | tickit_sales_redshift | TABLE | | +
 tickit_db | public | tickit_users_redshift | TABLE | | +
 tickit_db | public | tickit_venue_redshift | TABLE | |`
```

If the table_acl value is null, no access privileges have been explicitly granted to the corresponding table.
