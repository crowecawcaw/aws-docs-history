Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_TRANSACTIONS

Records information about transactions that currently hold locks on tables in the
database. Use the SVV_TRANSACTIONS view to identify open transactions and lock
contention issues. For more information about locks, see [Managing concurrent write operations](c_Concurrent_writes.md "c_Concurrent_writes.md") and [LOCK](r_LOCK.md "r_LOCK.md").

SVV_TRANSACTIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name          | Data type | Description                                                                                                                                                                       |
| -------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| txn_owner            | text      | Name of the owner of the transaction.                                                                                                                                             |
| txn_db               | text      | Name of the database associated with the<br>transaction.                                                                                                                          |
| xid                  | bigint    | Transaction ID.                                                                                                                                                                   |
| pid                  | integer   | Process ID associated with the lock.                                                                                                                                              |
| txn_start            | timestamp | Start time of the transaction.                                                                                                                                                    |
| lock_mode            | text      | Name of the lock mode held or requested by this<br>process. If `lock_mode` is `ExclusiveLock` and<br>`granted` is true (`t`), then this<br>transaction ID is an open transaction. |
| lockable_object_type | text      | Type of object requesting or holding the lock,<br>either `relation` if it is a table or<br>`transactionid` if it is a transaction.                                                |
| relation             | integer   | Table ID for the table (relation) acquiring the<br>lock. This value is NULL if `lockable_object_type` is<br>`transactionid`.                                                      |
| granted              | boolean   | Value that indicates whether that the lock has<br>been granted (`t`) or is pending (`f`)<br>.                                                                                     |

## Sample queries

The following command shows all active transactions and the locks requested by
each transaction.

```
select * from svv_transactions;

 txn_                                                                                 lockable_
 owner | txn_db |  xid   |  pid  |         txn_start          |      lock_mode      | object_type    | relation | granted
-------+--------+--------+-------+----------------------------+---------------------+----------------+----------+---------
 root  | dev    | 438484 | 22223 | 2016-03-02 18:42:18.862254 | AccessShareLock     | relation       |   100068 | t
 root  | dev    | 438484 | 22223 | 2016-03-02 18:42:18.862254 | ExclusiveLock       | transactionid  |          | t
 root  | tickit | 438490 | 22277 | 2016-03-02 18:42:48.084037 | AccessShareLock     | relation       |    50860 | t
 root  | tickit | 438490 | 22277 | 2016-03-02 18:42:48.084037 | AccessShareLock     | relation       |    52310 | t
 root  | tickit | 438490 | 22277 | 2016-03-02 18:42:48.084037 | ExclusiveLock       | transactionid  |          | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | AccessExclusiveLock | relation       |   100068 | f
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | RowExclusiveLock    | relation       |    16688 | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | AccessShareLock     | relation       |   100064 | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | AccessExclusiveLock | relation       |   100166 | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | AccessExclusiveLock | relation       |   100171 | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | AccessExclusiveLock | relation       |   100190 | t
 root  | dev    | 438505 | 22378 | 2016-03-02 18:43:27.611292 | ExclusiveLock       | transactionid  |          | t
(12 rows)

(12 rows)
```
