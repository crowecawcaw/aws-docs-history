Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVL\_S3LIST

Use the SVL\_S3LIST view to get details about data lake queries at the segment level.

SVL\_S3LIST is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

SVL\_S3LIST only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS\_EXTERNAL\_QUERY\_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name        | Data type        | Description                                                   |
| ------------------ | ---------------- | ------------------------------------------------------------- |
| query              | integer          | The query ID.                                                 |
| segment            | integer          | The segment number. A query consists of multiple<br>segments. |
| node               | integer          | The node number.                                              |
| slice              | integer          | The data slice that a particular segment ran against.         |
| eventtime          | timestamp        | The time in UTC that the event is recorded.                   |
| bucket             | text             | The Amazon S3 bucket name.                                    |
| prefix             | text             | The prefix of the Amazon S3 bucket location.                  |
| recursive          | char(1)          | Whether there is recursive scan for subfolders.               |
| retrieved\_files   | integer          | The number of listed files.                                   |
| max\_file\_size    | bigint           | The maximum file size among listed files.                     |
| avg\_file\_size    | double precision | The average file size among listed files.                     |
| generated\_splits  | integer          | The number of file splits.                                    |
| avg\_split\_length | double precision | The average length of file splits in bytes.                   |
| duration           | bigint           | The duration of file listing, in microseconds.                |

## Sample query

The following example queries SVL\_S3LIST for the last query to run.

```
select *
from svl_s3list
where query = pg_last_query_id()
order by query,segment;
```
