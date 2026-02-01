Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_LOAD_ERROR_DETAIL

Use SYS_LOAD_ERROR_DETAIL to view details of COPY command errors. Each row represents
a COPY command. It contains both running and finished COPY commands.

SYS_LOAD_ERROR_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type      | Description                                                                                                                                                                                                 |
| -------------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id        | integer        | The identifier of the user who submitted the<br>copy.                                                                                                                                                       |
| query_id       | bigint         | The query identifier of the copy.                                                                                                                                                                           |
| transaction_id | bigint         | The transaction identifier.                                                                                                                                                                                 |
| session_id     | integer        | The process identifier of the process running the<br>copy.                                                                                                                                                  |
| database_name  | character(64)  | The name of the database the user was connected to<br>when the copy was issued.                                                                                                                             |
| table_id       | integer        | The table identifier.                                                                                                                                                                                       |
| start_time     | timestamp      | The time (UTC) when the copy began.                                                                                                                                                                         |
| file_name      | character(256) | The complete path to the input file to<br>load.                                                                                                                                                             |
| line_number    | bigint         | The line number in the load file with the error.<br>When you load a JSON file, the line number of the last line of the<br>JSON object with the error.                                                       |
| column_name    | character(127) | The field with the error.                                                                                                                                                                                   |
| column_type    | character(10)  | The data type of the field with the error.                                                                                                                                                                  |
| column_length  | character(10)  | The column length, if applicable. This field is<br>populated when the data type has a limit length. For example, for a<br>column with a data type of "character(3)", this column contains the<br>value "3." |
| position       | integer        | The position of the error in the field.                                                                                                                                                                     |
| error_code     | integer        | The error code.                                                                                                                                                                                             |
| error_message  | character(512) | The explanation of the error.                                                                                                                                                                               |

## Sample queries

The following query shows the load error details of copy command for specific
query.

```
SELECT query_id,
       table_id,
       start_time,
       trim(file_name) AS file_name,
       trim(column_name) AS column_name,
       trim(column_type) AS column_type,
       trim(error_message) AS error_message
FROM sys_load_error_detail
WHERE query_id = 762949
ORDER BY start_time
LIMIT 10;
```

Sample output.

```
 query_id | table_id |         start_time         |               file_name                  | column_name | column_type |                 error_message
----------+----------+----------------------------+------------------------------------------+-------------+-------------+------------------------------------------------
   762949 |   137885 | 2022-02-15 22:14:46.759151 | s3://load-test/copyfail/wrong_format_000 | id          | int4        | Invalid digit, Value 'a', Pos 0, Type: Integer
   762949 |   137885 | 2022-02-15 22:14:46.759151 | s3://load-test/copyfail/wrong_format_001 | id          | int4        | Invalid digit, Value 'a', Pos 0, Type: Integer
```
