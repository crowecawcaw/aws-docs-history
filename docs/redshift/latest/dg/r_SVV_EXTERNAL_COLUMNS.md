Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_EXTERNAL_COLUMNS

Use SVV_EXTERNAL_COLUMNS to view details for columns in external tables. Use
SVV_EXTERNAL_COLUMNS also for cross-database queries to view details on all columns from
the table on unconnected databases that users have access to.

SVV_EXTERNAL_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type | Description                                                                                                                       |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------- |
| redshift_database_name | text      | The name of the local Amazon Redshift database.                                                                                   |
| schemaname             | text      | The name of the Amazon Redshift external schema for the external table.                                                           |
| tablename              | text      | The name of the external table.                                                                                                   |
| columnname             | text      | The name of the column.                                                                                                           |
| external_type          | text      | The data type of the column.                                                                                                      |
| columnnum              | integer   | The external column number, starting from 1.                                                                                      |
| part_key               | integer   | If the column is a partition key, the order of the key. If the column isn't a partition, the value is `0`.                        |
| is_nullable            | text      | Defines whether a column is nullable or not. Some values are `true`, `false`, or " " empty string that represents no information. |
