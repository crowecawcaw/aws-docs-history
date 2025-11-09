Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVCS_S3LIST

Use the SVCS_S3LIST view to get details about Amazon Redshift Spectrum queries at the segment level.
One segment can perform one external table scan.
This view is derived from the SVL_S3LIST system view but doesn't show slice-level for queries run on a concurrency scaling cluster.

###### Note

System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.
The views are similar to the views with the prefix SVL except that the SVL views provide information only for queries run on the main cluster.

SVCS_S3LIST is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about SVL_S3LIST, see [SVL_S3LIST](r_SVL_S3LIST.md "r_SVL_S3LIST.md").

## Table columns

| Column name      | Data type        | Description                                                   |
| ---------------- | ---------------- | ------------------------------------------------------------- |
| query            | integer          | The query ID.                                                 |
| segment          | integer          | The segment number. A query consists of multiple<br>segments. |
| node             | integer          | The node number.                                              |
| eventtime        | timestamp        | The time in UTC that the event is recorded.                   |
| bucket           | char(256)        | The Amazon S3 bucket name.                                    |
| prefix           | char(256)        | The prefix of the Amazon S3 bucket location.                  |
| recursive        | char(1)          | Whether there is recursive scan for subfolders.               |
| retrieved_files  | integer          | The number of listed files.                                   |
| max_file_size    | bigint           | The maximum file size among listed files.                     |
| avg_file_size    | double precision | The average file size among listed files.                     |
| generated_splits | integer          | The number of file splits.                                    |
| avg_split_length | double precision | The average length of file splits in bytes.                   |
| duration         | bigint           | The duration of file listing, in microseconds.                |

## Sample query

The following example queries SVCS_S3LIST for the last query performed.

```
select *
from svcs_s3list
where query = pg_last_query_id()
order by query,segment;
```
