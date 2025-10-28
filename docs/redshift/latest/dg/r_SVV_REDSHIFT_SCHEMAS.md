Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_REDSHIFT_SCHEMAS

Use SVV_REDSHIFT_SCHEMAS to view a list of all schemas that a user has access to. This
set of schemas includes the schemas on the cluster and the schemas from datashares
provided by remote clusters.

SVV_REDSHIFT_SCHEMAS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type    | Description                                                                                  |
| ------------- | ------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------ | ----------- | ---------- | --------------------------------------------------------------------------------------------------------------------- | ------ | --- | ------ | --- | --- |
| database_name | varchar(128) | The name of the database where a specified schema exists.                                    |
| schema_name   | varchar(128) | The namespace or schema name.                                                                |
| schema_owner  | integer      | The internal user ID of the schema owner.                                                    |
| schema_type   | varchar(16)  | The type of the schema. Possible values are shared and local schemas.                        |
| schema_acl    | varchar(128) | The string that defines the permissions for the specified user or user group for the schema. |
| schema_option | varchar(128) | The options of the schema.                                                                   | ## Sample query The following example returns the output of SVV_REDSHIFT_SCHEMAS. ``` SELECT \* FROM svv_redshift_schemas WHERE database_name = 'tickit_db' ORDER BY database_name, SCHEMA_NAME; database_name | schema_name | schema_owner | schema_type | schema_acl | schema_option --------------+--------------------+--------------+-------------+------------+--------------- tickit_db | public | 1   | shared |     | ``` |
