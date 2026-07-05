Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STL\_COMMIT\_STATS

Provides metrics related to commit performance, including the timing of the various
stages of commit and the number of blocks committed. Query STL\_COMMIT\_STATS to determine
what portion of a transaction was spent on commit and how much queuing is
occurring.

STL\_COMMIT\_STATS is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_TRANSACTION\_HISTORY](SYS_TRANSACTION_HISTORY.md "SYS_TRANSACTION_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name      | Data type | Description                                                                        |
| ---------------- | --------- | ---------------------------------------------------------------------------------- |
| xid              | bigint    | Transaction id being committed.                                                    |
| node             | integer   | Node number. `-1` is the leader<br>node.                                           |
| startqueue       | timestamp | Start of queueing for commit.                                                      |
| startwork        | timestamp | Start of commit.                                                                   |
| endflush         | timestamp | End of dirty block flush phase.                                                    |
| endstage         | timestamp | End of metadata staging phase.                                                     |
| endlocal         | timestamp | End of local commit phase.                                                         |
| startglobal      | timestamp | Start of global phase.                                                             |
| endtime          | timestamp | End of the commit.                                                                 |
| queuelen         | bigint    | Number of transactions that were ahead of this<br>transaction in the commit queue. |
| permblocks       | bigint    | Number of existing permanent blocks at the time of<br>this commit.                 |
| newblocks        | bigint    | Number of new permanent blocks at the time of this<br>commit.                      |
| dirtyblocks      | bigint    | Number of blocks that had to be written as part of<br>this commit.                 |
| headers          | bigint    | Number of block headers that had to be written as<br>part of this commit.          |
| numxids          | integer   | The number of active DML transactions.                                             |
| oldestxid        | bigint    | The XID of the oldest active DML<br>transaction.                                   |
| extwritelatency  | bigint    | This information is for internal use only.                                         |
| metadatawritten  | int       | This information is for internal use only.                                         |
| tombstonedblocks | _bigint_  | This information is for internal use only.                                         |
| tossedblocks     | bigint    | This information is for internal use only.                                         |
| batched\_by      | bigint    | This information is for internal use only.                                         |

## Sample query

```
select node, datediff(ms,startqueue,startwork) as queue_time,
datediff(ms, startwork, endtime) as commit_time, queuelen
from stl_commit_stats
where xid = 2574
order by node;

node | queue_time   | commit_time | queuelen
-----+--------------+-------------+---------
  -1 |            0 |         617 |        0
   0 | 444950725641 |         616 |        0
   1 | 444950725636 |         616 |        0
```
