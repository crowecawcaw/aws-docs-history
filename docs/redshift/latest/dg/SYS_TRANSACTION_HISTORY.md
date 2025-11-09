Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_TRANSACTION_HISTORY

Use SYS_TRANSACTION_HISTORY to see details of a transaction when tracking a
query.

SYS_TRANSACTION_HISTORY is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type | Description                                                                                                |
| ---------------------- | --------- | ---------------------------------------------------------------------------------------------------------- |
| user_id                | integer   | ID of the user who generated the entry.                                                                    |
| transaction_id         | bigint    | The ID of the transaction.                                                                                 |
| isolation_level        | text      | The isolation level of the transaction. Possible<br>values are `Serializable` and `Snapshot<br>Isolation`. |
| status                 | text      | The status of the transaction. Possible statuses<br>are `committed` and `rolledback`.                      |
| transaction_start_time | timestamp | The start time of the transaction.                                                                         |
| commit_start_time      | timestamp | The start time of the commit.                                                                              |
| commit_end_time        | timestamp | The end time of the commit.                                                                                |
| blocks_committed       | bigint    | The number of blocks that had to be written as<br>part of this commit.                                     |
| undo_transaction_id    | bigint    | The ID of the undo transaction if any transactions<br>have been undone. Otherwise, this value is -1.       |

## Sample queries

```
select * from sys_transaction_history order by transaction_start_time desc;

 user_id | transaction_id | isolation_level |   status   |   transaction_start_time   |     commit_start_time      |      commit_end_time       | blocks_committed | undo_transaction_id
---------+----------------+-----------------+------------+----------------------------+----------------------------+----------------------------+------------------+---------------------
     100 |           1310 | Serializable    | committed  | 2023-08-27 21:03:11.822205 | 2023-08-28 21:03:11.825287 | 2023-08-28 21:03:11.854883 |               17 |                  -1
     101 |           1345 | Serializable    | committed  | 2023-08-27 21:03:12.000278 | 2023-08-28 21:03:12.003736 | 2023-08-28 21:03:12.030061 |               17 |                  -1
     102 |           1367 | Serializable    | committed  | 2023-08-27 21:03:12.1532   | 2023-08-28 21:03:12.156124 | 2023-08-28 21:03:12.186468 |               17 |                  -1
     100 |           1370 | Serializable    | committed  | 2023-08-27 21:03:12.199316 | 2023-08-28 21:03:12.204854 | 2023-08-28 21:03:12.238186 |               24 |                  -1
     100 |           1408 | Serializable    | committed  | 2023-08-27 21:03:53.891107 | 2023-08-28 21:03:53.894825 | 2023-08-28 21:03:53.927465 |               17 |                  -1
     100 |           1409 | Serializable    | rolledback | 2023-08-27 21:03:53.936431 | 2000-01-01 00:00:00        | 2023-08-28 21:04:08.712532 |                0 |                1409
     101 |           1415 | Serializable    | committed  | 2023-08-27 21:04:24.283188 | 2023-08-28 21:04:24.289196 | 2023-08-28 21:04:24.374318 |               25 |                  -1
     101 |           1416 | Serializable    | committed  | 2023-08-27 21:04:24.38818  | 2023-08-28 21:04:24.391688 | 2023-08-28 21:04:24.415135 |               17 |                  -1
     100 |           1417 | Serializable    | rolledback | 2023-08-27 21:04:24.424252 | 2000-01-01 00:00:00        | 2023-08-28 21:04:28.354826 |                0 |                1417
     101 |           1418 | Serializable    | rolledback | 2023-08-27 21:04:24.425195 | 2000-01-01 00:00:00        | 2023-08-28 21:04:28.680355 |                0 |                1418
     100 |           1420 | Serializable    | committed  | 2023-08-27 21:04:28.697607 | 2023-08-28 21:04:28.702374 | 2023-08-28 21:04:28.735541 |               23 |                  -1
     101 |           1421 | Serializable    | committed  | 2023-08-27 21:04:28.744854 | 2023-08-28 21:04:28.749344 | 2023-08-28 21:04:28.779029 |               23 |                  -1
     101 |           1423 | Serializable    | committed  | 2023-08-27 21:04:28.78942  | 2023-08-28 21:04:28.791556 | 2023-08-28 21:04:28.817485 |               16 |                  -1
     100 |           1430 | Serializable    | committed  | 2023-08-27 21:04:28.917788 | 2023-08-28 21:04:28.919993 | 2023-08-28 21:04:28.944812 |               16 |                  -1
     102 |           1494 | Serializable    | committed  | 2023-08-27 21:04:37.029058 | 2023-08-28 21:04:37.033137 | 2023-08-28 21:04:37.062001 |               16 |                  -1

```
