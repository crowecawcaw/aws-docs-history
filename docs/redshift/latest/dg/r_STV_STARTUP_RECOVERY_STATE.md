Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_STARTUP_RECOVERY_STATE

Records the state of tables that are temporarily locked during cluster restart
operations. Amazon Redshift places a temporary lock on tables while they are being processed to
resolve stale transactions following a cluster restart.

STV_STARTUP_RECOVERY_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name | Data type      | Description  |
| ----------- | -------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------ | ------ | ---------------- | ------ | ----------- | ------ | --------------- | ------ | --------------------- |
| db_id       | integer        | Database ID. |
| table_id    | integer        | Table ID.    |
| table_name  | character(137) | Table name.  | ## Sample queries To monitor which tables are temporarily locked, run the following query after a cluster restart. ``` select \* from STV_STARTUP_RECOVERY_STATE; db_id | tbl_id | table_name --------+--------+------------ 100044 | 100058 | lineorder 100044 | 100068 | part 100044 | 100072 | customer 100044 | 100192 | supplier (4 rows) ``` |
