Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_QUERY\_STATE

Use SVV\_QUERY\_STATE to view information about the runtime of currently running
queries.

The SVV\_QUERY\_STATE view contains a data subset of the STV\_EXEC\_STATE table.

SVV\_QUERY\_STATE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_QUERY\_DETAIL](SYS_QUERY_DETAIL.md "SYS_QUERY_DETAIL.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

###### Note

This view is only available when querying provisioned clusters.

## Table columns

| Column name       | Data type        | Description                                                                                                                                                                                                                                                              |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| userid            | integer          | ID of user who generated entry.                                                                                                                                                                                                                                          |
| query             | integer          | Query ID. Can be used to join various other system<br>tables and views.                                                                                                                                                                                                  |
| seg               | integer          | Number of the query segment that is running. A<br>query consists of multiple segments, and each segment consists of<br>one or more steps. Query segments can run in parallel. Each segment<br>runs in a single process.                                                  |
| step              | integer          | Number of the query step that is running. A step<br>is the smallest unit of query runtime. Each step represents a<br>discrete unit of work, such as scanning a table, returning results,<br>or sorting data.                                                             |
| maxtime           | interval         | Maximum amount of time (in microseconds) for this<br>step to run.                                                                                                                                                                                                        |
| avgtime           | interval         | Average time (in microseconds) for this step to<br>run.                                                                                                                                                                                                                  |
| rows              | bigint           | Number of rows produced by the step that is<br>running.                                                                                                                                                                                                                  |
| bytes             | bigint           | Number of bytes produced by the step that is<br>running.                                                                                                                                                                                                                 |
| cpu               | bigint           | For internal use.                                                                                                                                                                                                                                                        |
| memory            | bigint           | For internal use.                                                                                                                                                                                                                                                        |
| rate\_row         | double precision | Rows-per-second rate since the query started,<br>computed by summing the rows and dividing by the number of seconds<br>from when the query started to the current time.                                                                                                  |
| rate\_byte        | double precision | Bytes-per-second rate since the query started,<br>computed by summing the bytes and dividing by the number of seconds<br>from when the query started to the current time.                                                                                                |
| label             | character(25)    | Query label: a name for the step, such as<br>`scan` or `sort`.                                                                                                                                                                                                           |
| is\_diskbased     | character(1)     | Whether this step of the query is running as a<br>disk-based operation: true (`t`) or false<br>(`f`). Only certain steps, such as hash,<br>sort, and aggregate steps, can go to disk. Many types of steps are<br>always performed in memory.                             |
| workmem           | bigint           | Amount of working memory (in bytes) assigned to<br>the query step.                                                                                                                                                                                                       |
| num\_parts        | integer          | Number of partitions a hash table is divided into<br>during a hash step.<br>A positive number in this column does not imply that the hash step<br>runs as a disk-based operation. Check the value in the<br>IS\_DISKBASED column to see if the hash step was disk-based. |
| is\_rrscan        | character(1)     | If true (`t`), indicates that<br>range-restricted scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                  |
| is\_delayed\_scan | character(1)     | If true (`t`), indicates that<br>delayed scan was used on the step. Default is false<br>(`f`).                                                                                                                                                                           |

## Sample queries

**Determining the processing time of a query by step**

The following query shows how long each step of the query with query ID 279 took
to run and how many data rows Amazon Redshift processed:

```
select query, seg, step, maxtime, avgtime, rows, label
from svv_query_state
where query = 279
order by query, seg, step;
```

This query retrieves the processing information about query 279, as shown in the
following sample output:

```
query |   seg   | step | maxtime | avgtime |  rows   | label
------+---------+------+---------+---------+---------+-------------------
  279 |       3 |    0 | 1658054 | 1645711 | 1405360 | scan
  279 |       3 |    1 | 1658072 | 1645809 |       0 | project
  279 |       3 |    2 | 1658074 | 1645812 | 1405434 | insert
  279 |       3 |    3 | 1658080 | 1645816 | 1405437 | distribute
  279 |       4 |    0 | 1677443 | 1666189 | 1268431 | scan
  279 |       4 |    1 | 1677446 | 1666192 | 1268434 | insert
  279 |       4 |    2 | 1677451 | 1666195 |       0 | aggr
(7 rows)
```

**Determining if any active queries are currently running on
disk**

The following query shows if any active queries are currently running on disk:

```
select query, label, is_diskbased from svv_query_state
where is_diskbased = 't';
```

This sample output shows any active queries currently running on disk:

```
 query | label        | is_diskbased
-------+--------------+--------------
1025   | hash tbl=142 |      t
(1 row)
```
