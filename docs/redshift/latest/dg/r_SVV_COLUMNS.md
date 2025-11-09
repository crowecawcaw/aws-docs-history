Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_COLUMNS

Use SVV_COLUMNS to view catalog information about the columns of local and external
tables and views, including [late-binding views](r_CREATE_VIEW.md#r_CREATE_VIEW_late-binding-views "r_CREATE_VIEW.md#r_CREATE_VIEW_late-binding-views").

SVV_COLUMNS is visible to all users by default. To control access to your database's metadata,
enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view
permissions for object metadata by users and roles. For more information, see
[Metadata security](t_metadata_security.md "t_metadata_security.md").

The SVV_COLUMNS view joins table metadata from the [System catalog tables](c_intro_catalog_views.md "c_intro_catalog_views.md") (tables with
a PG prefix) and the [SVV_EXTERNAL_COLUMNS](r_SVV_EXTERNAL_COLUMNS.md "r_SVV_EXTERNAL_COLUMNS.md") system view. The system catalog tables
describe Amazon Redshift database tables. SVV_EXTERNAL_COLUMNS describes external tables that are
used with Amazon Redshift Spectrum.

All users can see all rows from the system catalog tables. Regular users can see
column definitions from the SVV_EXTERNAL_COLUMNS view only for external tables to which
they have been granted access. Although regular users can see table metadata in the
system catalog tables, they can only select data from user-defined tables if they
own the table or have been granted access.

## Table columns

| Column name              | Data type | Description                                                                                                                                          |
| ------------------------ | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| table_catalog            | text      | The name of the catalog where the table<br>is.                                                                                                       |
| table_schema             | text      | The schema name for the table.                                                                                                                       |
| table_name               | text      | The name of the table.                                                                                                                               |
| column_name              | text      | The name of the column.                                                                                                                              |
| ordinal_position         | int       | The position of the column in the table.                                                                                                             |
| column_default           | text      | The default value of the column.                                                                                                                     |
| is_nullable              | text      | A value that indicates whether the column is<br>nullable.                                                                                            |
| data_type                | text      | The data type of the column.                                                                                                                         |
| character_maximum_length | int       | The maximum number of characters in the column.                                                                                                      |
| numeric_precision        | int       | The numeric precision. If the data_type column is numeric,<br>this column returns the number of significant digits in the entire value.              |
| numeric_precision_radix  | int       | The numeric precision radix. If the data_type column is numeric,<br>this column returns the base of the columns numeric_precision and numeric_scale. |
| numeric_scale            | int       | The numeric scale. If the data_type column is numeric,<br>this column returns the number of significant digits in the decimal value.                 |
| datetime_precision       | int       | The datetime precision.                                                                                                                              |
| interval_type            | text      | The interval type.                                                                                                                                   |
| interval_precision       | text      | The interval precision.                                                                                                                              |
| character_set_catalog    | text      | The character set catalog.                                                                                                                           |
| character_set_schema     | text      | The character set schema.                                                                                                                            |
| character_set_name       | text      | The character set name.                                                                                                                              |
| collation_catalog        | text      | The collation catalog.                                                                                                                               |
| collation_schema         | text      | The collation schema.                                                                                                                                |
| collation_name           | text      | The collation name.                                                                                                                                  |
| domain_name              | text      | The domain name.                                                                                                                                     |
| remarks                  | text      | Remarks.                                                                                                                                             |
