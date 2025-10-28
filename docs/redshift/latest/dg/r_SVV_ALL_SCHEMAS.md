Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ALL_SCHEMAS

Use SVV_ALL_SCHEMAS to view a union of Amazon Redshift schemas as shown in SVV_REDSHIFT_SCHEMAS and the
consolidated list of all external schemas from all databases. For more information about Amazon Redshift schemas, see [SVV_REDSHIFT_SCHEMAS](r_SVV_REDSHIFT_SCHEMAS.md "r_SVV_REDSHIFT_SCHEMAS.md").

SVV_ALL_SCHEMAS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type    | Description                                                                                                             |
| --------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------ | ----------- | ---------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------ | --- | ------ | --- | --- | --- |
| database_name   | varchar(128) | The name of the database where the schema exists.                                                                       |
| schema_name     | varchar(128) | The name of the schema.                                                                                                 |
| schema_owner    | integer      | The user ID of the schema owner. For information about user IDs, see [PG_USER_INFO](pg_user_info.md "pg_user_info.md"). |
| schema_type     | varchar(128) | The type of the schema. Possible values are external, local, and shared schemas.                                        |
| schema_acl      | varchar(128) | The string that defines the permissions for the specified user or user group for the schema.                            |
| source_database | varchar(128) | The name of the source database for external schema.                                                                    |
| schema_option   | varchar(256) | The options of the schema. This is an external schema attribute.                                                        | ## Sample query The following example returns the output of SVV_ALL_SCHEMAS. ``` SELECT \* FROM svv_all_schemas WHERE database_name = 'tickit_db' ORDER BY database_name, SCHEMA_NAME; database_name | schema_name | schema_owner | schema_type | schema_acl | source_database | schema_option ---------------+--------------------+--------------+-------------+------------+-----------------+--------------- tickit_db | public | 1   | shared |     |     | ``` |
