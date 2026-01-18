Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_AUTOMATIC_OPTIMIZATION

Use SYS_AUTOMATIC_OPTIMIZATION to view details on the tasks that Amazon Redshift runs for
automatic optimization, also known as autonomics. For more information on automatic
optimization, see [Automatic database optimization](c_autonomics.md "c_autonomics.md").

SYS_AUTOMATIC_OPTIMIZATION is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| session_id    | integer        | Process ID executing the task queries. Initially<br>set to 0 when the task is created, this value becomes non-zero only<br>when `event` is set as Started.                                                                                                                                                                                                                                                                                                          |
| database_name | character(128) | Name of the database where the task is<br>executed.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| object_type   | character(30)  | The type of object that the autonomics task<br>operates on. Possible values are the following:<br>• table<br>• mv<br>• table_column_pairs                                                                                                                                                                                                                                                                                                                           |
| object_ids    | character(512) | The identifier of the objects that the autonomics<br>task is operating on. This field can hold more than one object when<br>the task runs on multiple database objects. In this case, the<br>identifiers are separated by commas.                                                                                                                                                                                                                                   |
| task_type     | character(100) | The type of autonomics task run. Possible tasks<br>are as follows:<br>• AutoAlterTableTaskSortkey<br>• AutoAlterTableTaskDistkey<br>• VacuumSort<br>• VacuumDelete<br>• Analyze                                                                                                                                                                                                                                                                                     |
| event         | character(50)  | The type of state transition event for the<br>autonomics task. Possible values are the following:<br>• Queued<br>• Started<br>• Suspended<br>• Completed<br>• Failed                                                                                                                                                                                                                                                                                                |
| event_time    | timestamp      | The time that the state transition<br>occurred.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| status        | character(512) | The execution status of the optimization task.<br>Empty if the task did not try to run.                                                                                                                                                                                                                                                                                                                                                                             |
| compute_type  | character(100) | Compute resource type used by the task. Possible<br>values for provisioned are the following:<br>• primary<br>• primary-scale<br>The value can also be empty on provisioned if the task didn't use any compute.<br>For more information on the different types of compute<br>resource that you can use for autonomics, see [Allocating extra compute resources for automatic database optimization](t_extra-compute-autonomics.md "t_extra-compute-autonomics.md"). |
| task_details  | character(512) | Additional task details if any. This field can be empty.                                                                                                                                                                                                                                                                                                                                                                                                            |

## Usage notes

The compute_type column will be empty for serverless clusters because we do not
differentiate primary or primary-scale compute resources. Serverless cluster compute
resources are measured by Redshift Processing Units (RPUs) usage. For more
information, see [Compute capacity
for Amazon Redshift Serverless](../mgmt/serverless-capacity.md "../mgmt/serverless-capacity.md").

## Examples

The following query displays the automatic optimizations performed on table 155259.

```
`SELECT pid, trim(task_type) as task_type,
 trim(database) as database,
 trim(status) as status,
 trim(event) as event,
 event_time
from SYS_AUTOMATIC_OPTIMIZATION
WHERE object_ids like '%155259%'
AND status = 'Task completed successfully';`

 `task_type | database | status | event | event_time
------------+----------------+-----------------------------+-----------+----------------------------
 VacuumSort | tpcds_100g_oob | Task completed successfully | Completed | 2025-12-22 07:27:15.943018`
```

The following query shows all executed automatic "VacuumSort" optimizations. For
more information about "VacuumSort", see [Automatic table sort](t_Reclaiming_storage_space202.md#automatic-table-sort "t_Reclaiming_storage_space202.md#automatic-table-sort").

```
`SELECT trim(task_type) as task_type,
 trim(database) as database,
 trim(object_type) as object_type,
 trim(object_ids) as object_ids,
 trim(status) as status,
 trim(event) as event,
 event_time
from SYS_AUTOMATIC_OPTIMIZATION
WHERE task_type like '%VacuumSort%'
AND status = 'Task completed successfully';`

`task_type | database | object_type | object_ids | status | event | event_time
------------+----------------+-------------+------------+-----------------------------+-----------+----------------------------
 VacuumSort | tpcds_100g_oob | table | 155301 | Task completed successfully | Completed | 2025-12-22 07:14:00.065391
 VacuumSort | tpcds_100g_oob | table | 155303 | Task completed successfully | Completed | 2025-12-22 07:14:09.158251
 VacuumSort | tpcds_100g_oob | table | 155291 | Task completed successfully | Completed | 2025-12-22 07:17:06.61164
 VacuumSort | tpcds_100g_oob | table | 155293 | Task completed successfully | Completed | 2025-12-22 07:17:37.015069
 VacuumSort | tpcds_100g_oob | table | 155281 | Task completed successfully | Completed | 2025-12-22 07:18:54.903935
 VacuumSort | tpcds_100g_oob | table | 155279 | Task completed successfully | Completed | 2025-12-22 07:20:13.960002
 VacuumSort | tpcds_100g_oob | table | 155271 | Task completed successfully | Completed | 2025-12-22 07:21:26.095549
 VacuumSort | tpcds_100g_oob | table | 155267 | Task completed successfully | Completed | 2025-12-22 07:22:48.119249
 VacuumSort | tpcds_100g_oob | table | 155269 | Task completed successfully | Completed | 2025-12-22 07:24:12.010424
 VacuumSort | tpcds_100g_oob | table | 155263 | Task completed successfully | Completed | 2025-12-22 07:25:35.958388
 VacuumSort | tpcds_100g_oob | table | 155265 | Task completed successfully | Completed | 2025-12-22 07:26:40.580395
 VacuumSort | tpcds_100g_oob | table | 155259 | Task completed successfully | Completed | 2025-12-22 07:27:15.943018
(12 rows)`
```
