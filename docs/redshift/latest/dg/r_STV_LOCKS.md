

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STV\_LOCKS
<a name="r_STV_LOCKS"></a>

Use the STV\_LOCKS table to view any current updates on tables in the database.

Amazon Redshift locks tables to prevent two users from updating the same table at the same time. While the STV\_LOCKS table shows all current table updates, query the [STL\_TR\_CONFLICT](r_STL_TR_CONFLICT.md) table to see a log of lock conflicts. Use the [SVV\_TRANSACTIONS](r_SVV_TRANSACTIONS.md) view to identify open transactions and lock contention issues.

STV\_LOCKS is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STV_LOCKS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| table\_id  | bigint  | Table ID for the table acquiring the lock.  | 
| last\_commit  | timestamp  | Timestamp for the last commit in the table.  | 
| last\_update  | timestamp  | Timestamp for the last update for the table.  | 
| lock\_owner  | bigint  | Transaction ID associated with the lock.  | 
| lock\_owner\_pid  | bigint  | Process ID associated with the lock.  | 
| lock\_owner\_start\_ts  | timestamp  | Timestamp for the transaction start time.  | 
| lock\_owner\_end\_ts  | timestamp  | Timestamp for the transaction end time.  | 
| lock\_status  | character (22)  | Status of the process either waiting for or holding a lock.  | 

## Sample query
<a name="r_STV_LOCKS-sample-query"></a>

To view all locks taking place in current transactions, type the following command: 

```
select table_id, last_update, lock_owner, lock_owner_pid from stv_locks;
```

This query returns the following sample output, which displays three locks currently in effect: 

```
 table_id |        last_update         | lock_owner | lock_owner_pid
----------+----------------------------+------------+----------------
100004  | 2008-12-23 10:08:48.882319 |       1043 |           5656
100003  | 2008-12-23 10:08:48.779543 |       1043 |           5656
100140  | 2008-12-23 10:08:48.021576 |       1043 |           5656
(3 rows)
```