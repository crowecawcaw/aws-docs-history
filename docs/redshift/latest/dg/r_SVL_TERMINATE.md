Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVL\_TERMINATE

Records the time when a user cancels or terminates a process.

SELECT PG\_TERMINATE\_BACKEND(_pid_),
SELECT PG\_CANCEL\_BACKEND(_pid_), and
CANCEL _pid_ creates a log entry in SVL\_TERMINATE.

SVL\_TERMINATE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type | Description                                             |
| ----------- | --------- | ------------------------------------------------------- |
| pid         | integer   | The process ID of the canceled or terminated process.   |
| eventtime   | timestamp | The time when the process is canceled or terminated.    |
| userid      | integer   | The user ID of the user running the<br>command.         |
| type        | string    | The type of termination. It can be CANCEL or TERMINATE. |

The following command shows the latest cancelled query.

```
select * from svl_terminate order by eventtime desc limit 1;
 pid  |         eventtime          | userid |  type
------+----------------------------+--------+--------
 8324 | 2020-03-24 09:42:07.298937 |      1 | CANCEL
(1 row)
```
