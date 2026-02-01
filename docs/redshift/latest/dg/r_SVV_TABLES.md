Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_TABLES

Use SVV_TABLES to view tables in local and external catalogs.

SVV_TABLES is visible to all users by default. To control access to your database's metadata,
enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view
permissions for object metadata by users and roles. For more information, see
[Metadata security](t_metadata_security.md "t_metadata_security.md").

## Table columns

| Column name   | Data type | Description                                                                        |
| ------------- | --------- | ---------------------------------------------------------------------------------- |
| table_catalog | text      | The name of the catalog where the table<br>exists.                                 |
| table_schema  | text      | The name the schema for the table.                                                 |
| table_name    | text      | The name of the table.                                                             |
| table_type    | text      | The type of table. Possible values are views,<br>external tables, and base tables. |
| remarks       | text      | Remarks.                                                                           |
