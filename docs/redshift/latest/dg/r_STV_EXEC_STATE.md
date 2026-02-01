Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_EXEC_STATE

Use the STV_EXEC_STATE table to find out information about queries and query steps
that are actively running on compute nodes.

This information is usually used only to troubleshoot engineering issues. The views
SVV_QUERY_STATE and SVL_QUERY_SUMMARY extract their information from
STV_EXEC_STATE.

STV_EXEC_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name     | Data type | Description                                                                                                                                                                                                                                                                                        |
| --------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid          | integer   | ID of user who generated entry.                                                                                                                                                                                                                                                                    |
| query           | integer   | Query ID. Can be used to join various other system<br>tables and views.                                                                                                                                                                                                                            |
| slice           | integer   | Node slice where the step completed.                                                                                                                                                                                                                                                               |
| segment         | integer   | Segment of the query that ran. A query<br>segment is a series of steps.                                                                                                                                                                                                                            |
| step            | integer   | Step of the query segment that completed. A step is<br>the smallest unit that a query performs.                                                                                                                                                                                                    |
| starttime       | timestamp | Time that the step ran.                                                                                                                                                                                                                                                                            |
| currenttime     | timestamp | Current time.                                                                                                                                                                                                                                                                                      |
| tasknum         | integer   | Query task process that is assigned to complete<br>the step.                                                                                                                                                                                                                                       |
| rows            | bigint    | Number of rows processed.                                                                                                                                                                                                                                                                          |
| bytes           | bigint    | Number of bytes processed.                                                                                                                                                                                                                                                                         |
| label           | char(256) | Step label, which consists of a query step name<br>and, when applicable, table ID and table name (for example,<br>`scan tbl=100448 name =user`). Three-digit table IDs<br>usually refer to scans of transient tables. When you see<br>`tbl=0`, it usually refers to a scan of a constant<br>value. |
| is_diskbased    | char(1)   | Whether this step of the query was completed as a<br>disk-based operation: true (`t`) or false<br>(`f`). Only certain steps, such as hash,<br>sort, and aggregate steps, can go to disk. Many types of steps are<br>always completed in memory.                                                    |
| workmem         | bigint    | Number of bytes of working memory assigned to the<br>step.                                                                                                                                                                                                                                         |
| num_parts       | integer   | Number of partitions a hash table is divided into<br>during a hash step.<br>A positive number in this column does not imply that the hash step<br>ran as a disk-based operation. Check the value in the<br>IS_DISKBASED column to see if the hash step was disk-based.                             |
| is_rrscan       | char(1)   | If true (`t`), indicates that<br>range-restricted scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                                            |
| is_delayed_scan | char(1)   | If true (`t`), indicates that<br>delayed scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                                                     |

## Sample queries

Rather than querying STV_EXEC_STATE directly, Amazon Redshift recommends querying
SVL_QUERY_SUMMARY or SVV_QUERY_STATE to obtain the information in STV_EXEC_STATE in
a more user-friendly format. See the [SVL_QUERY_SUMMARY](r_SVL_QUERY_SUMMARY.md "r_SVL_QUERY_SUMMARY.md") or [SVV_QUERY_STATE](r_SVV_QUERY_STATE.md "r_SVV_QUERY_STATE.md") table documentation for more details.
