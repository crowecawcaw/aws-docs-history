Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_EXTERNAL_DATABASES

Use SVV_EXTERNAL_DATABASES to view details for external databases.

SVV_EXTERNAL_DATABASES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name  | Data type | Description                                                                                                            |
| ------------ | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| eskind       | integer   | The type of the external catalog for the database;<br>`1` indicates a data catalog,<br>`2` indicates a Hive metastore. |
| esoptions    | text      | Details of the catalog where the database<br>resides.                                                                  |
| databasename | text      | The name of the database in the external<br>catalog.                                                                   |
| location     | text      | The location of the database.                                                                                          |
| parameters   | text      | Database parameters.                                                                                                   |
