Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STV\_XRESTORE\_ALTER\_QUEUE\_STATE

Use STV\_XRESTORE\_ALTER\_QUEUE\_STATE to monitor the migration progress of each
table during a classic resize. This is specifically applicable when the
target node type is RG or RA3. For more information about classic resize to RG or RA3 nodes, go to
[Classic resize](../mgmt/managing-cluster-operations.md#classic-resize-faster "../mgmt/managing-cluster-operations.md#classic-resize-faster").

STV\_XRESTORE\_ALTER\_QUEUE\_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_RESTORE\_STATE](SYS_RESTORE_STATE.md "SYS_RESTORE_STATE.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type | Description                                                                                                                                                                                                                             |
| ----------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer   | The ID of the user who initiated the resize.                                                                                                                                                                                            |
| db\_id      | integer   | The ID of the database.                                                                                                                                                                                                                 |
| schema      | char(128) | The name of the schema.                                                                                                                                                                                                                 |
| table\_name | char(128) | The name of the table.                                                                                                                                                                                                                  |
| tbl         | integer   | The ID of the table.                                                                                                                                                                                                                    |
| status      | char(64)  | The status of the migration progress of the table. Possible values are as follows.<br>• `Waiting`: Waiting for redistribution to start<br>• `Applying`: Currently redistributing<br>• `Finished`: Finished redistributing               |
| task\_type  | integer   | The redistribution type for the table. Possible values are as follows.<br>• `1`: KEY<br>• `2`: EVEN<br>For more information about distribution styles,<br>see [Distribution styles](c_choosing_dist_sort.md "c_choosing_dist_sort.md"). |

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
