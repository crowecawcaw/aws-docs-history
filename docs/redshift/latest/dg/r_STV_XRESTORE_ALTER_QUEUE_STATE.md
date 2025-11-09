Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_XRESTORE_ALTER_QUEUE_STATE

Use STV_XRESTORE_ALTER_QUEUE_STATE to monitor the migration progress of each
table during a classic resize. This is specifically applicable when the
target node type is RA3. For more information about classic resize to RA3 nodes, go to
[Classic resize](../mgmt/managing-cluster-operations.md#classic-resize-faster "../mgmt/managing-cluster-operations.md#classic-resize-faster").

STV_XRESTORE_ALTER_QUEUE_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_RESTORE_STATE](SYS_RESTORE_STATE.md "SYS_RESTORE_STATE.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type | Description                                                                                                                                                                                                                             |
| ----------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer   | The ID of the user who initiated the resize.                                                                                                                                                                                            |
| db_id       | integer   | The ID of the database.                                                                                                                                                                                                                 |
| schema      | char(128) | The name of the schema.                                                                                                                                                                                                                 |
| table_name  | char(128) | The name of the table.                                                                                                                                                                                                                  |
| tbl         | integer   | The ID of the table.                                                                                                                                                                                                                    |
| status      | char(64)  | The status of the migration progress of the table. Possible values are as follows.<br>• `Waiting`: Waiting for redistribution to start<br>• `Applying`: Currently redistributing<br>• `Finished`: Finished redistributing               |
| task_type   | integer   | The redistribution type for the table. Possible values are as follows.<br>• `1`: KEY<br>• `2`: EVEN<br>For more information about distribution styles,<br>see [Distribution styles](c_choosing_dist_sort.md "c_choosing_dist_sort.md"). |

## Sample query

The following query shows the number of tables in a database that are
waiting to be resized, are currently being resized, and are finished resizing.

```
select db_id, status, count(*)
from stv_xrestore_alter_queue_state
group by 1,2 order by 3 desc

`db_id | status | count
-------+------------+------
694325 | Waiting | 323
694325 | Finished | 60
694325 | Applying | 1`
```
