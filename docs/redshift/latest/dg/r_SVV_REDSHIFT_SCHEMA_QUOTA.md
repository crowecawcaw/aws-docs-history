Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_REDSHIFT_SCHEMA_QUOTA

Displays the quota and the current disk usage for each schema in a database.

SVV_REDSHIFT_SCHEMA_QUOTA is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

This view is available when querying provisioned clusters or Redshift Serverless workgroups.

## Table columns

| Column name   | Data type      | Description                                                     |
| ------------- | -------------- | --------------------------------------------------------------- |
| database_name | character(128) | The database that contains the schema.                          |
| schema_name   | character(128) | The name of the schema.                                         |
| schema_owner  | integer        | The internal user ID of the schema owner.                       |
| quota         | integer        | The amount of disk space (in MB) that the schema<br>can use.    |
| disk_usage    | integer        | The disk space (in MB) that is currently used by<br>the schema. |

## Sample query

The following example displays the quota and the current disk usage for the schema named `sales_schema`.

```
`SELECT TRIM(SCHEMA_NAME) "schema_name", QUOTA, disk_usage FROM svv_redshift_schema_quota
WHERE SCHEMA_NAME = 'sales_schema';`

`schema_name | quota | disk_usage
--------------+-------+------------
sales_schema | 2048 | 30`
```
