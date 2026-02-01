Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_RESTORE_STATE

Use SYS_RESTORE_STATE to monitor the migration progress of each table during a classic
resize. This is specifically applicable when the target node type is RA3. For more
information about classic resize to RA3 nodes, see [Classic
resize](../mgmt/managing-cluster-operations.md#classic-resize-faster "../mgmt/managing-cluster-operations.md#classic-resize-faster").

SYS_RESTORE_STATE is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type | Description                                                                                                                                                                                                                      |
| ------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id                  | integer   | The identifier of the user who submitted the<br>query.                                                                                                                                                                           |
| database_name            | char(64)  | The name of the database of the table.                                                                                                                                                                                           |
| schema_id                | integer   | The schema ID of the table.                                                                                                                                                                                                      |
| table_id                 | integer   | The ID of the table.                                                                                                                                                                                                             |
| table_name               | char(128) | The name of the table.                                                                                                                                                                                                           |
| redistribution_status    | char(128) | The status of redistribution progress of the<br>table. Possible values are `Completed`, `In<br>progress`, and `Pending`.                                                                                                         |
| percentage_redistributed | float     | The percentage of the redistribution progress of<br>the table. Possible values are from 0 to 100%. For example, a value<br>of 25 indicates that 25% of the data is redistributed.                                                |
| redistribution_type      | char(32)  | The redistribution type for the table. Either KEY<br>conversion or an EVEN rebalancing task. For more information about<br>distribution styles, see [Distribution<br>styles](c_choosing_dist_sort.md "c_choosing_dist_sort.md"). |

## Sample queries

The following query returns records for running and queued queries.

```
SELECT * FROM sys_restore_state;
```

Sample output.

```
 userid | database_name | schema_id | table_id |   table_name   | redistribution_status | precentage_redistributed |   redistribution_type
--------+---------------+-----------+----------+----------------+-----------------------+--------------------------+-------------------------
    1   |     test1     |   124865  |  124878  | customer_key_4 |         Pending       |      0                   |  Rebalance Disteven Table
    1   |      dev      |   124865  |  124874  | customer_key_3 |         Pending       |      0                   |  Rebalance Disteven Table
    1   |      dev      |   124865  |  124870  | customer_key_2 |        Completed      |     100                  |  Rebalance Disteven Table
    1   |      dev      |   124865  |  124866  | customer_key_1 |       In progress     |     13.52                |  Restore Distkey Table
```

The following gives you the data-processing status.

```
SELECT
    redistribution_status, ROUND(SUM(block_count) / 1024.0, 2) AS total_size_gb
FROM sys_restore_state sys inner join stv_tbl_perm stv
    on sys.table_id = stv.id
GROUP BY sys.redistribution_status;
```

Sample output.

```
 redistribution_status | total_size_gb
-----------------------+---------------
 Completed             |          0.07
 Pending               |          0.71
 In progress           |          0.20
(3 rows)
```
