Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVCS_S3LOG

Use the SVCS_S3LOG view to get troubleshooting details about Redshift Spectrum queries at the segment level.
One segment can perform one external table scan.
This view is derived from the SVL_S3LOG system view but doesn't show slice-level for queries run on a concurrency scaling cluster.

###### Note

System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.
The views are similar to the views with the prefix SVL except that the SVL views provide information only for queries run on the main cluster.

SVCS_S3LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about SVL_S3LOG, see [SVL_S3LOG](r_SVL_S3LOG.md "r_SVL_S3LOG.md").

## Table columns

| Column name | Data type | Description                                                                                                   |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| pid         | integer   | The process ID.                                                                                               |
| query       | integer   | The query ID.                                                                                                 |
| segment     | integer   | The segment number. A query consists of multiple<br>segments, and each segment consists of one or more steps. |
| step        | integer   | The query step that ran.                                                                                      |
| node        | integer   | The node number.                                                                                              |
| eventtime   | timestamp | The time in UTC that the event is recorded.                                                                   |
| message     | char(512) | The message for the log entry.                                                                                |

## Sample query

The following example queries SVCS_S3LOG for the last query that ran.

```
select *
from svcs_s3log
where query = pg_last_query_id()
order by query,segment;
```
