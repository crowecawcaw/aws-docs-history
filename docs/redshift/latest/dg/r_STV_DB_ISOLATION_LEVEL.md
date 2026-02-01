Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_DB_ISOLATION_LEVEL

STV_DB_ISOLATION_LEVEL displays the current isolation level for databases. For more
information about isolation levels, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

STV_DB_ISOLATION_LEVEL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type      | Description                                                                                           |
| --------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| db_name         | character(128) | The database name.                                                                                    |
| isolation_level | character(20)  | The isolation level of the database. Possible values include `Serializable` and `Snapshot Isolation`. |
