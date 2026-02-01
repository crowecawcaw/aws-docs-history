Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_TR_CONFLICT

Displays information to identify and resolve transaction conflicts with database
tables.

A transaction conflict occurs when two or more users are querying and modifying data
rows from tables such that their transactions cannot be serialized. The transaction that
runs a statement that would break serializability is stopped and rolled back. Every
time a transaction conflict occurs, Amazon Redshift writes a data row to the STL_TR_CONFLICT system
table containing details about the canceled transaction. For more information, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

STL_TR_CONFLICT is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_TRANSACTION_HISTORY](SYS_TRANSACTION_HISTORY.md "SYS_TRANSACTION_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name   | Data type | Description                                                      |
| ------------- | --------- | ---------------------------------------------------------------- |
| xact_id       | bigint    | Transaction ID for the rolled back transaction.                  |
| process_id    | bigint    | Process associated with the transaction that was<br>rolled back. |
| xact_start_ts | timestamp | Timestamp (UTC) when the transaction started.                    |
| abort_time    | timestamp | Timestamp (UTC) when the transaction was stopped.                |
| table_id      | bigint    | Table ID for the table where the conflict<br>occurred.           |

## Sample query

To return information about conflicts that involved a particular table, run a
query that specifies the table ID:

```
select * from stl_tr_conflict where table_id=100234
order by xact_start_ts;

xact_id|process_|      xact_start_ts       |        abort_time        |table_
       |id      |                          |                          |id
-------+--------+--------------------------+--------------------------+------
  1876 |  8551  |2010-03-30 09:19:15.852326|2010-03-30 09:20:17.582499|100234
  1928 | 15034  |2010-03-30 13:20:00.636045|2010-03-30 13:20:47.766817|100234
  1991 | 23753  |2010-04-01 13:05:01.220059|2010-04-01 13:06:06.94098 |100234
  2002 | 23679  |2010-04-01 13:17:05.173473|2010-04-01 13:18:27.898655|100234
(4 rows)
```

You can get the table ID from the DETAIL section of the error message for
serializability violations (error 1023).
