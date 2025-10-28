Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ALL_COLUMNS

Use SVV_ALL_COLUMNS to view a union of columns from Amazon Redshift tables as shown in SVV_REDSHIFT_COLUMNS and the
consolidated list of all external columns from all external tables. For information
about Amazon Redshift columns, see [SVV_REDSHIFT_COLUMNS](r_SVV_REDSHIFT_COLUMNS.md "r_SVV_REDSHIFT_COLUMNS.md").

SVV_ALL_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type     | Description                                                                            |
| ------------------------ | ------------- | -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- | ----------- | ---------------- | -------------- | ----------- | --------- | ------------------------ | ----------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------------------- | ------- | --- | --- | --- | ------- | --- | --- | --- | --------- | ------ | --------------------- | ---------- | --- | --- | --- | ------- | --- | --- | --- | --------- | ------ | --------------------- | ------ | --- | --- | --- | -------- | --- | --- | --- | --------- | ------ | --------------------- | ------- | --- | --- | --- | ------- | --- | --- | --- | --------- | ------ | --------------------- | ------ | --- | --- | --- | ------- | --- | --- | --- | --- |
| database_name            | varchar(128)  | The name of the database.                                                              |
| schema_name              | varchar(128)  | The name of the schema.                                                                |
| table_name               | varchar(128)  | The name of the table.                                                                 |
| column_name              | varchar(128)  | The name of the column.                                                                |
| ordinal_position         | integer       | The position of the column in the table.                                               |
| column_default           | varchar(4000) | The default value of the column.                                                       |
| is_nullable              | varchar(3)    | A value that indicates whether the column is nullable. Possible values are yes and no. |
| data_type                | varchar(128)  | The data type of the column.                                                           |
| character_maximum_length | integer       | The maximum number of characters in the column.                                        |
| numeric_precision        | integer       | The numeric precision.                                                                 |
| numeric_scale            | integer       | The numeric scale.                                                                     |
| remarks                  | varchar(256)  | Remarks.                                                                               | ## Sample queries The following example returns the output of SVV_ALL_COLUMNS. ``` SELECT \* FROM svv_all_columns WHERE database_name = 'tickit_db' AND TABLE_NAME = 'tickit_sales_redshift' ORDER BY COLUMN_NAME, SCHEMA_NAME LIMIT 5; database_name | schema_name | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | numeric_precision | numeric_scale | remarks --------------+-------------+-----------------------+-------------+------------------+----------------+-------------+-----------+--------------------------+-------------------+---------------+--------- tickit_db | public | tickit_sales_redshift | buyerid | 4   |     | NO  | integer |     | 32  | 0   | tickit_db | public | tickit_sales_redshift | commission | 9   |     | YES | numeric |     | 8   | 2   | tickit_db | public | tickit_sales_redshift | dateid | 7   |     | NO  | smallint |     | 16  | 0   | tickit_db | public | tickit_sales_redshift | eventid | 5   |     | NO  | integer |     | 32  | 0   | tickit_db | public | tickit_sales_redshift | listid | 2   |     | NO  | integer |     | 32  | 0   | ``` |
