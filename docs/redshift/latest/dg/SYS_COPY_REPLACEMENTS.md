

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_COPY\_REPLACEMENTS
<a name="SYS_COPY_REPLACEMENTS"></a>

Displays a log that records when invalid UTF-8 characters were replaced by the [COPY](r_COPY.md) command with the ACCEPTINVCHARS option. A log entry is added to SYS\_COPY\_REPLACEMENTS for each of the first 100 rows on each node slice that required at least one replacement. 

You can use this view to see information about serverless workgroups and provisioned clusters.

SYS\_COPY\_REPLACEMENTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_COPY_REPLACEMENTS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | ID of the user who generated the query. | 
| query\_id | bigint | The query ID. The column used to join other system tables and views. | 
| table\_id | integer | The table ID. | 
| file\_name | character(256) | The complete path to the input file for the COPY command. | 
| column\_name | character(127) | The first field that contains an invalid UTF-8 character. | 
| line\_number | bigint | The line number in the input data file that containes an invalid UTF-8 character. -1 indicates that the line number is not available, such as when copying from a columnar data file. | 
| raw\_line | character(1024) | The raw load data that contains an invalid UTF-8 character. | 

## Sample queries
<a name="SYS_COPY_REPLACEMENTS-sample-queries"></a>

The following example returns replacements for the most recent COPY operation.

```
select query_idp, table_id, file_name, line_number, colname
from sys_copy_replacements
where query = pg_last_copy_id();


 query_id | table_id |   file_name                                           | line_number | column_name
 ---------+----------+-------------------------------------------------------+-------------+--------
    96    |    26    | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt             |         123 | city
    96    |    26    | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt             |         456 | city
    96    |    26    | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt             |         789 | city
    96    |    26    | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt             |         012 | city
    96    |    26    | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt             |         119 | city
...
```