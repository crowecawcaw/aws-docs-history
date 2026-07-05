Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STV\_DB\_ISOLATION\_LEVEL

STV\_DB\_ISOLATION\_LEVEL displays the current isolation level for databases. For more
information about isolation levels, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

STV\_DB\_ISOLATION\_LEVEL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name      | Data type      | Description                                                                                           |
| ---------------- | -------------- | ----------------------------------------------------------------------------------------------------- |
| db\_name         | character(128) | The database name.                                                                                    |
| isolation\_level | character(20)  | The isolation level of the database. Possible values include `Serializable` and `Snapshot Isolation`. |
