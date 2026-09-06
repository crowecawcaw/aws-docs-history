

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVL\_S3LOG
<a name="r_SVL_S3LOG"></a>

Use the SVL\_S3LOG view to get details about data lake queries at the segment and node slice level.

SVL\_S3LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

**Note**  
SVL\_S3LOG only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters or on serverless namespaces. To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view [SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md) . The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns
<a name="r_SVL_S3LOG-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| pid | integer | The process ID. | 
| query | integer | The query ID. | 
| segment | integer | The segment number. A query consists of multiple segments, and each segment consists of one or more steps.  | 
| step | integer | The query step that ran.  | 
| node | integer | The node number. | 
| slice | integer | The data slice that a particular segment ran against. | 
| eventtime | timestamp | Time in UTC that the step started executing. | 
| message | text | Message for the log entry. | 

## Sample query
<a name="r_SVL_S3LOG-sample-query"></a>

The following example queries SVL\_S3LOG for the last query that ran.

```
select * 
from svl_s3log 
where query = pg_last_query_id() 
order by query,segment,slice;
```