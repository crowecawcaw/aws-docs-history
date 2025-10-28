Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_INTEGRATION_TABLE_MAPPING

SVV_INTEGRATION_TABLE_MAPPING displays the mapping of source database, schema, table, column, and data type to the target when the identifier value of those fields are different.

###### Note

This view is only populated for the following types of zero-ETL integrations:

- AWS Glue third-party applications to Amazon SageMaker Lakehouse
- Amazon DynamoDB to Amazon SageMaker Lakehouse
  For more information, see
  [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md")
  in the _AWS Glue Developer Guide_.

The transformation of identifier values from source to target follow the following rules:

- An upper case letter is converted to lower case.
- A character that is not a lowercase letter, a digit, or underscore (\_) is converted to an underscore (\_).
- If there is a conflict with a existing identifier value, then an Universally Unique Identifier (UUID) is appended to the new identifier.
- If the source identifier value is an Amazon Redshift keyword, then the suffix `_redshift` is appended to the new identifier.
  After transformation, a character must be a lowercase letter, a digit, or underscore (\_) and match the regex pattern `[a-z0-9_]`.
  The following examples demonstrate the conversion rules:

| Source             | Target             | Notes                                                                              |
| ------------------ | ------------------ | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------- | ------------------ | ------------------ | ----------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | -------- | -------- | ------- | ------- |
| foo                | foo                | No transformation                                                                  |
| Bar                | bar                |                                                                                    |
| fooBar             | foobar             |                                                                                    |
| foo1               | foo1               | No transformation                                                                  |
| foo_1              | foo_1              | No transformation                                                                  |
| Bar@1              | bar_1              |                                                                                    |
| foo_bar@           | foo_bar\_          |                                                                                    |
| case               | case_redshift      |                                                                                    | SVV_INTEGRATION_TABLE_MAPPING is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data"). For information about zero-ETL integrations, see [Zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md") in the _Amazon Redshift Management Guide_. ## Table columns |
| Column name        | Data type          | Description                                                                        |
| ---                | ---                | ---                                                                                |
| integration_id     | character(128)     | The identifier associated with the integration.                                    |
| source_database    | character(128)     | The name of the database in the source.                                            |
| target_database    | character(128)     | The database in Amazon Redshift that receives the integration data.                |
| source_schema_name | character(128)     | The name of the schema in the source.                                              |
| target_schema_name | character(128)     | The schema in Amazon Redshift that receives the integration data.                  |
| source_table_name  | character(128)     | The name of the table in the source.                                               |
| target_table_name  | character(128)     | The table in Amazon Redshift that receives the integration data.                   |
| source_column_name | character(128)     | The name of the column in the source.                                              |
| target_column_name | character(128)     | The column in Amazon Redshift that receives the integration data.                  |
| source_data_type   | character(128)     | The data type of the column in the source.                                         |
| target_data_type   | character(128)     | The data type of the column in Amazon Redshift that receives the integration data. | ## Sample queries The following SQL command displays mapping of metadata values from source to target. ``` `select \* from svv_integration_table_mapping;` `integration_id                                                                                                                                                                                                                                                                                                                           | source_database                                                                    | target_database | source_schema_name | target_schema_name | source_table_name | target_table_name | ---------------------------------------+-----------------+-----------------+---------------------+--------------------+---------------------------------------+ 99108e72-1cfd-414f-8cc0-0216acefac77 | mydatabase | mydatabase | myschema | myschema | Mytable | mytable |
| source_column_name | target_column_name | source_data_type                                                                   | target_data_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | +--------------------+--------------------+-------------------+------------------+ |
| Mycolumnname       | mycolumnname       | Mydatatype                                                                         | mydatatype                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | ` ```                                                                              |
