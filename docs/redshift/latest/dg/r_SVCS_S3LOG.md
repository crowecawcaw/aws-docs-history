

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVCS\_S3LOG
<a name="r_SVCS_S3LOG"></a>

Use the SVCS\_S3LOG view to get troubleshooting details about data lake queries at the segment level. One segment can perform one external table scan. This view is derived from the SVL\_S3LOG system view but doesn't show slice-level for queries run on a concurrency scaling cluster. 

**Note**  
System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters. The views are similar to the views with the prefix SVL except that the SVL views provide information only for queries run on the main cluster.

SVCS\_S3LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For information about SVL\_S3LOG, see [SVL\_S3LOG](r_SVL_S3LOG.md).

## Table columns
<a name="r_SVCS_S3LOG-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| pid | integer | The process ID. | 
| query | integer | The query ID. | 
| segment | integer | The segment number. A query consists of multiple segments, and each segment consists of one or more steps.  | 
| step | integer | The query step that ran.  | 
| node | integer | The node number. | 
| eventtime | timestamp | The time in UTC that the event is recorded. | 
| message | char(512) | The message for the log entry. | 

## Sample query
<a name="r_SVCS_S3LOG-sample-query"></a>

The following example queries SVCS\_S3LOG for the last query that ran.

```
select * 
from svcs_s3log 
where query = pg_last_query_id() 
order by query,segment;
```