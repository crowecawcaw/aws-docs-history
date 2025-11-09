Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_S3LOG

Use the SVL_S3LOG view to get details about Amazon Redshift Spectrum queries at the segment and
node slice level.

SVL_S3LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

SVL_S3LOG only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type | Description                                                                                                   |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| pid         | integer   | The process ID.                                                                                               |
| query       | integer   | The query ID.                                                                                                 |
| segment     | integer   | The segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps. |
| step        | integer   | The query step that ran.                                                                                      |
| node        | integer   | The node number.                                                                                              |
| slice       | integer   | The data slice that a particular segment ran<br>against.                                                      |
| eventtime   | timestamp | Time in UTC that the step started<br>executing.                                                               |
| message     | text      | Message for the log entry.                                                                                    |

## Sample query

The following example queries SVL_S3LOG for the last query that ran.

```
select *
from svl_s3log
where query = pg_last_query_id()
order by query,segment,slice;
```
