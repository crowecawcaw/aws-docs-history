Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_SCHEMA\_QUOTA\_STATE

Displays the quota and the current disk usage for each schema.

Regular users can see information for schemas for which they have USAGE permission. Superusers can see information for all schemas in the current database.

SVV\_SCHEMA\_QUOTA\_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name      | Data type        | Description                                                                                    |
| ---------------- | ---------------- | ---------------------------------------------------------------------------------------------- |
| schema\_id       | integer          | The namespace or schema ID.                                                                    |
| schema\_name     | character (128)  | The namespace or schema name.                                                                  |
| schema\_owner    | integer          | The internal user ID of the schema owner.                                                      |
| quota            | integer          | The amount of disk space (in MB) that the schema<br>can use.                                   |
| disk\_usage      | integer          | The disk space (in MB) that is currently used by<br>the schema.                                |
| disk\_usage\_pct | double precision | The disk space percentage that is currently used<br>by the schema out of the configured quota. |

## Sample query

The following example displays the quota and the current disk usage for the schema.

```
SELECT TRIM(SCHEMA_NAME) "schema_name", QUOTA, disk_usage, disk_usage_pct FROM svv_schema_quota_state
WHERE SCHEMA_NAME = 'sales_schema';
schema_name   | quota | disk_usage | disk_usage_pct
--------------+-------+------------+----------------
sales_schema  | 2048  | 30         | 1.46
(1 row)


```
