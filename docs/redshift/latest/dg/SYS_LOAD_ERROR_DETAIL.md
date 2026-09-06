

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_LOAD\_ERROR\_DETAIL
<a name="SYS_LOAD_ERROR_DETAIL"></a>

Use SYS\_LOAD\_ERROR\_DETAIL to view details of COPY command errors. Each row represents a COPY command. It contains both running and finished COPY commands.

SYS\_LOAD\_ERROR\_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_LOAD_ERROR_DETAIL-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The identifier of the user who submitted the copy. | 
| query\_id | bigint | The query identifier of the copy. | 
| transaction\_id | bigint | The transaction identifier. | 
| session\_id | integer | The process identifier of the process running the copy. | 
| database\_name | character(64) | The name of the database the user was connected to when the copy was issued. | 
| table\_id | integer | The table identifier. | 
| start\_time | timestamp | The time (UTC) when the copy began. | 
| file\_name | character(256) | The complete path to the input file to load. | 
| line\_number | bigint | The line number in the load file with the error. When you load a JSON file, the line number of the last line of the JSON object with the error. | 
| column\_name | character(127) | The field with the error. | 
| column\_type | character(10) | The data type of the field with the error. | 
| column\_length | character(10) | The column length, if applicable. This field is populated when the data type has a limit length. For example, for a column with a data type of "character(3)", this column contains the value "3." | 
| position | integer | The position of the error in the field. | 
| error\_code | integer | The error code. | 
| error\_message | character(512) | The explanation of the error. | 

## Sample queries
<a name="SYS_LOAD_ERROR_DETAIL-sample-queries"></a>

The following query shows the load error details of copy command for specific query.

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