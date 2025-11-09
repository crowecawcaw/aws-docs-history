Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_LOCKS

Use the STV_LOCKS table to view any current updates on tables in the database.

Amazon Redshift locks tables to prevent two users from updating the same table at the same
time. While the STV_LOCKS table shows all current table updates, query the [STL_TR_CONFLICT](r_STL_TR_CONFLICT.md "r_STL_TR_CONFLICT.md") table to see a log
of lock conflicts. Use the [SVV_TRANSACTIONS](r_SVV_TRANSACTIONS.md "r_SVV_TRANSACTIONS.md") view to identify open transactions and lock
contention issues.

STV_LOCKS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name         | Data type      | Description                                                    |
| ------------------- | -------------- | -------------------------------------------------------------- |
| table_id            | bigint         | Table ID for the table acquiring the lock.                     |
| last_commit         | timestamp      | Timestamp for the last commit in the table.                    |
| last_update         | timestamp      | Timestamp for the last update for the table.                   |
| lock_owner          | bigint         | Transaction ID associated with the lock.                       |
| lock_owner_pid      | bigint         | Process ID associated with the lock.                           |
| lock_owner_start_ts | timestamp      | Timestamp for the transaction start time.                      |
| lock_owner_end_ts   | timestamp      | Timestamp for the transaction end time.                        |
| lock_status         | character (22) | Status of the process either waiting for or<br>holding a lock. |

## Sample query

To view all locks taking place in current transactions, type the following
command:

```
select table_id, last_update, lock_owner, lock_owner_pid from stv_locks;
```

This query returns the following sample output, which displays three locks
currently in effect:

```
 table_id |        last_update         | lock_owner | lock_owner_pid
----------+----------------------------+------------+----------------
100004  | 2008-12-23 10:08:48.882319 |       1043 |           5656
100003  | 2008-12-23 10:08:48.779543 |       1043 |           5656
100140  | 2008-12-23 10:08:48.021576 |       1043 |           5656
(3 rows)
```
