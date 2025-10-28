Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_RESTORE_ALTER_TABLE_PROGRESS

Use SVL_RESTORE_ALTER_TABLE_PROGRESS to monitor the migration progress
of each table in the cluster during a classic resize to RA3 nodes.
It captures the historic throughput of data migration during the resize
operation. For more information about classic resize to RA3 nodes, go to
[Classic resize](../mgmt/managing-cluster-operations.md#classic-resize-faster "../mgmt/managing-cluster-operations.md#classic-resize-faster").

SVL_RESTORE_ALTER_TABLE_PROGRESS is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_RESTORE_LOG](SYS_RESTORE_LOG.md "SYS_RESTORE_LOG.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

###### Note

Rows with a progress of `100.00%` or `ABORTED`
are deleted after 7 days. Rows for tables dropped during or after a classic
resize can still appear in SVL_RESTORE_ALTER_TABLE_PROGRESS.

## Table columns

| Column name | Data type | Description                                                                                                                                                                                                                                                        |
| ----------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------- | ---------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------- | ------- | ---------------------------------------------------------------- | ----- | ---------------------------------------------------- | ------- | ---------------------------------------------------------------- | ------- | ---------------------------------------------------------------- | ------- | -------------------------------------- |
| tbl         | integer   | The ID of the table.                                                                                                                                                                                                                                               |
| progress    | char(32)  | The status of redistribution progress of the table. Possible values are percentages from `0.00%` to `100.00%` and the message `ABORTED`. `ABORTED` means that the redistribution was stopped without finishing, with the reason explained in the `message` column. |
| message     | char(256) | The message associated with the redistribution progress of the table.                                                                                                                                                                                              | ## Sample query The following query returns running and queued queries. ```select * from svl_restore_alter_table_progress;`tbl | progress | message --------+----------+----------------------------------------------------------- 105614 | ABORTED | Abort:Table no longer contains the prior dist key column. 105610 | ABORTED | Abort:Table no longer contains the prior dist key column. 105594 | 0.00% | Table waiting for alter diststyle conversion. 105602 | ABORTED | Abort:Table no longer contains the prior dist key column. 105606 | ABORTED | Abort:Table no longer contains the prior dist key column. 105598 | 100.00% | Restored to distkey successfully.` ``` |
