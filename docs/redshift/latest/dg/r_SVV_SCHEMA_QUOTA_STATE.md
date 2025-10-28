Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_SCHEMA_QUOTA_STATE

Displays the quota and the current disk usage for each schema.

Regular users can see information for schemas for which they have USAGE permission. Superusers can see information for all schemas in the current database.

SVV_SCHEMA_QUOTA_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name    | Data type        | Description                                                                                 |
| -------------- | ---------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ---------- | -------------------------------------------------------------------------------- | ---- | --- | ---------------- |
| schema_id      | integer          | The namespace or schema ID.                                                                 |
| schema_name    | character (128)  | The namespace or schema name.                                                               |
| schema_owner   | integer          | The internal user ID of the schema owner.                                                   |
| quota          | integer          | The amount of disk space (in MB) that the schema can use.                                   |
| disk_usage     | integer          | The disk space (in MB) that is currently used by the schema.                                |
| disk_usage_pct | double precision | The disk space percentage that is currently used by the schema out of the configured quota. | ## Sample query The following example displays the quota and the current disk usage for the schema. ``` SELECT TRIM(SCHEMA_NAME) "schema_name", QUOTA, disk_usage, disk_usage_pct FROM svv_schema_quota_state WHERE SCHEMA_NAME = 'sales_schema'; schema_name | quota | disk_usage | disk_usage_pct --------------+-------+------------+---------------- sales_schema | 2048 | 30  | 1.46 (1 row) ``` |
