Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_EXTERNAL\_COLUMNS

Use SVV\_EXTERNAL\_COLUMNS to view details for columns in external tables. Use
SVV\_EXTERNAL\_COLUMNS also for cross-database queries to view details on all columns from
the table on unconnected databases that users have access to.

SVV\_EXTERNAL\_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW COLUMNS](r_SHOW_COLUMNS.md "r_SHOW_COLUMNS.md") command for column discovery. SHOW COLUMNS works consistently across
local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name              | Data type | Description                                                                                                                             |
| ------------------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| redshift\_database\_name | text      | The name of the local Amazon Redshift database.                                                                                         |
| schemaname               | text      | The name of the Amazon Redshift external schema for the<br>external table.                                                              |
| tablename                | text      | The name of the external table.                                                                                                         |
| columnname               | text      | The name of the column.                                                                                                                 |
| external\_type           | text      | The data type of the column.                                                                                                            |
| columnnum                | integer   | The external column number, starting from<br>1.                                                                                         |
| part\_key                | integer   | If the column is a partition key, the order of the<br>key. If the column isn't a partition, the value is<br>`0`.                        |
| is\_nullable             | text      | Defines whether a column is nullable or not. Some<br>values are `true`, `false`, or " " empty<br>string that represents no information. |
