Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_SCHEMA_QUOTA_VIOLATIONS

Records the occurrence, transaction ID, and other useful information when a schema
quota is exceeded. This system table is a translation of [STL_SCHEMA_QUOTA_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md "r_STL_SCHEMA_QUOTA_VIOLATIONS.md").

r_SYS_SCHEMA_QUOTA_VIOLATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type                   | Description                                                  |
| -------------- | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ----- | ---------- | ---------------------------------------------------------------------------------------- | ------------ | ---- | ---- | -------------------------------------- |
| owner_id       | integer                     | The ID of the schema owner.                                  |
| user_id        | integer                     | The ID of the user who generated the entry.                  |
| transaction_id | bigint                      | The transaction ID associated with the statement.            |
| session_id     | integer                     | The process ID associated with the statement.                |
| schema_id      | integer                     | The namespace or schema ID.                                  |
| schema_name    | character (128)             | The namespace or schema name.                                |
| quota          | integer                     | The amount of disk space (in MB) that the schema can use.    |
| disk_usage     | integer                     | The disk space (in MB) that is currently used by the schema. |
| record_time    | timestamp without time zone | The time when the violation occurred.                        | ## Sample queries The following query shows the result of a quota violation: `SELECT user_id, TRIM(schema_name) "schema_name", quota, disk_usage, record_time FROM sys_schema_quota_violations WHERE SCHEMA_NAME = 'sales_schema' ORDER BY timestamp DESC;` This query returns the following sample output for the specified schema: ``` user_id | schema_name | quota | disk_usage | record_time -------+--------------+-------+------------+---------------------------- 104 | sales_schema | 2048 | 2798 | 2020-04-20 20:09:25.494723 (1 row) ``` |
