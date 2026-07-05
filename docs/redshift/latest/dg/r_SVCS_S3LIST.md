Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVCS\_S3LIST

Use the SVCS\_S3LIST view to get details about Amazon Redshift Spectrum queries at the segment level.
One segment can perform one external table scan.
This view is derived from the SVL\_S3LIST system view but doesn't show slice-level for queries run on a concurrency scaling cluster.

###### Note

System views with the prefix SVCS provide details about queries on both the main and concurrency scaling clusters.
The views are similar to the views with the prefix SVL except that the SVL views provide information only for queries run on the main cluster.

SVCS\_S3LIST is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For information about SVL\_S3LIST, see [SVL\_S3LIST](r_SVL_S3LIST.md "r_SVL_S3LIST.md").

## Table columns

| Column name        | Data type        | Description                                                   |
| ------------------ | ---------------- | ------------------------------------------------------------- |
| query              | integer          | The query ID.                                                 |
| segment            | integer          | The segment number. A query consists of multiple<br>segments. |
| node               | integer          | The node number.                                              |
| eventtime          | timestamp        | The time in UTC that the event is recorded.                   |
| bucket             | char(256)        | The Amazon S3 bucket name.                                    |
| prefix             | char(256)        | The prefix of the Amazon S3 bucket location.                  |
| recursive          | char(1)          | Whether there is recursive scan for subfolders.               |
| retrieved\_files   | integer          | The number of listed files.                                   |
| max\_file\_size    | bigint           | The maximum file size among listed files.                     |
| avg\_file\_size    | double precision | The average file size among listed files.                     |
| generated\_splits  | integer          | The number of file splits.                                    |
| avg\_split\_length | double precision | The average length of file splits in bytes.                   |
| duration           | bigint           | The duration of file listing, in microseconds.                |

## Sample query

The following example queries SVCS\_S3LIST for the last query performed.

```
select *
from svcs_s3list
where query = pg_last_query_id()
order by query,segment;
```
