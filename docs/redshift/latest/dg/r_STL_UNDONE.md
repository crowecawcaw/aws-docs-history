Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STL\_UNDONE

Displays information about transactions that have been undone.

STL\_UNDONE is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_TRANSACTION\_HISTORY](SYS_TRANSACTION_HISTORY.md "SYS_TRANSACTION_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name      | Data type | Description                                                    |
| ---------------- | --------- | -------------------------------------------------------------- |
| userid           | integer   | ID of the user who generated the entry.                        |
| xact\_id         | bigint    | ID for the undo transaction.                                   |
| xact\_id\_undone | bigint    | ID for the transaction that was undone.                        |
| undo\_start\_ts  | timestamp | Start time for the undo transaction.                           |
| undo\_end\_ts    | timestamp | End time for the undo transaction.                             |
| table\_id        | bigint    | ID for the table that was affected by the undo<br>transaction. |

## Sample query

To view a concise log of all undone transactions, type the following command:

```
select xact_id, xact_id_undone, table_id from stl_undone;
```

This command returns the following sample output:

```
 xact_id | xact_id_undone | table_id
---------+----------------+----------
1344 |           1344 |   100192
1326 |           1326 |   100192
1551 |           1551 |   100192
(3 rows)
```
