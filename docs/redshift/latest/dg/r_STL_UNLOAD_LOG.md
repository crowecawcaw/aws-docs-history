Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_UNLOAD_LOG

Records the details for an unload operation.

STL_UNLOAD_LOG records one row for each file created by an UNLOAD statement. For
example, if an UNLOAD creates 12 files, STL_UNLOAD_LOG will contain 12 corresponding
rows.

STL_UNLOAD_LOG is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_UNLOAD_LOG only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_UNLOAD_HISTORY](SYS_UNLOAD_HISTORY.md "SYS_UNLOAD_HISTORY.md") and
[SYS_UNLOAD_DETAIL](SYS_UNLOAD_DETAIL.md "SYS_UNLOAD_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name   | Data type       | Description                                                   |
| ------------- | --------------- | ------------------------------------------------------------- |
| userid        | integer         | ID of the user who generated the entry.                       |
| query         | integer         | The query ID.                                                 |
| slice         | integer         | Number that identifies the slice where the query was running. |
| pid           | integer         | Process ID associated with the query<br>statement.            |
| path          | character(1280) | The complete Amazon S3 object path for the<br>file.           |
| start_time    | timestamp       | Start time for the transaction.                               |
| end_time      | timestamp       | End time for the transaction.                                 |
| line_count    | bigint          | Number of lines (rows) unloaded to the<br>file.               |
| transfer_size | bigint          | Number of bytes transferred.                                  |
| file_format   | character(10)   | Format of unloaded file.                                      |

## Sample query

To get a list of the files that were written to Amazon S3 by an UNLOAD command, you can
call an Amazon S3 list operation after the UNLOAD completes. You can also query STL_UNLOAD_LOG.

The following query returns the pathname for files that were created by an UNLOAD
for the last query completed:

```
select query, substring(path,0,40) as path
from stl_unload_log
where query = pg_last_query_id()
order by path;
```

This command returns the following sample output:

```

 query |             path
-------+--------------------------------------
  2320 | s3://amzn-s3-demo-bucket/venue0000_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0001_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0002_part_00
  2320 | s3://amzn-s3-demo-bucket/venue0003_part_00
(4 rows)

```
