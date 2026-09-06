

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_REPLACEMENTS
<a name="r_STL_REPLACEMENTS"></a>

Displays a log that records when invalid UTF-8 characters were replaced by the [COPY](r_COPY.md) command with the ACCEPTINVCHARS option. A log entry is added to STL\_REPLACEMENTS for each of the first 100 rows on each node slice that required at least one replacement. 

STL\_REPLACEMENTS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
STL\_NESTLOOP only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_COPY\_REPLACEMENTS](SYS_COPY_REPLACEMENTS.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_STL_REPLACEMENTS-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| query  | integer | Query ID. The query column can be used to join other system tables and views. | 
| slice | integer | Node slice number where the replacement occurred. | 
| tbl | integer | Table ID. | 
| starttime | timestamp | Start time in UTC for the COPY command. | 
| session | integer | Session ID for the session performing the COPY command. | 
| filename | character(256) | Complete path to the input file for the COPY command. | 
| line\_number | bigint | Line number in the input data file that contained an invalid UTF-8 character. A -1 indicates that the line number is not available, such as, when copying from a columnar data file. | 
| colname | character(127) | First field that contained an invalid UTF-8 character. | 
| raw\_line | character(1024) | Raw load data that contained an invalid UTF-8 character. | 
| user\_query\_id  | bigint  | The query identifier of the user-submitted query, as recorded in the query\_id column of [SYS\_COPY\_REPLACEMENTS](SYS_COPY_REPLACEMENTS.md).  | 

## Sample queries
<a name="r_STL_REPLACEMENTS-sample-queries"></a>

The following example returns replacements for the most recent COPY operation. 

```
select query, session, filename, line_number, colname
from stl_replacements
where query = pg_last_copy_id();

 query | session |   filename                                  | line_number | colname
 ------+---------+---------------------------------------------+-------------+--------
    96 |    6314 | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt   |         251 | city
    96 |    6314 | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt   |         317 | city
    96 |    6314 | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt   |         569 | city
    96 |    6314 | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt   |         623 | city
    96 |    6314 | s3://DOC-EXAMPLE-BUCKET/allusers_pipe.txt   |         694 | city
...
```