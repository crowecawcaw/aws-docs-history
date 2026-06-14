# Control table task settings

Control tables provide information about an AWS DMS task. They also provide
useful statistics that you can use to plan and manage both the current migration
task and future tasks. You can apply these task settings in a JSON file or by
choosing **Advanced Settings** on the **Create
task** page in the AWS DMS console. The Apply Exceptions table
(`dmslogs.awsdms_apply_exceptions`) is always created on database targets.
For information about how to use a task configuration file to set task settings, see [Task settings example](CHAP_Tasks.CustomizingTasks.TaskSettings.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.TaskSettings.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

AWS DMS only creates control tables only during Full Load + CDC or CDC-only tasks,
and not during Full Load Only tasks.

For full load and CDC (Migrate existing data and replicate ongoing changes)
and CDC only (Replicate data changes only) tasks, you can also create
additional tables, including the following:

- **Replication Status
  (dmslogs.awsdms_status)** – This table provides
  details about the current task. These include task status, amount of
  memory consumed by the task, and the number of changes not yet applied
  to the target. This table also gives the position in the source database
  where AWS DMS is currently reading. Also, it indicates if the task is in
  the full load phase or change data capture (CDC).
- **Suspended Tables
  (dmslogs.awsdms_suspended_tables)** – This table
  provides a list of suspended tables as well as the reason they were
  suspended.
- **Replication History
  (dmslogs.awsdms_history)** – This table provides
  information about replication history. This information includes the
  number and volume of records processed during the task, latency at the
  end of a CDC task, and other statistics.
  The Apply Exceptions table (`dmslogs.awsdms_apply_exceptions`)
  contains the following parameters.

| Column      | Type      | Description                                                                |
| ----------- | --------- | -------------------------------------------------------------------------- |
| TASK_NAME   | nvchar    | The Resource ID of the AWS DMS task. Resource ID can be found in task ARN. |
| TABLE_OWNER | nvchar    | The table owner.                                                           |
| TABLE_NAME  | nvchar    | The table name.                                                            |
| ERROR_TIME  | timestamp | The time the exception (error) occurred.                                   |
| STATEMENT   | nvchar    | The statement that was being run when the error<br>occurred.               |
| ERROR       | nvchar    | The error name and description.                                            |

The Replication Status table (`dmslogs.awsdms_status`) contains the
current status of the task and the target database. It has the following
settings.

| Column                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SERVER_NAME                   | nvchar    | The name of the machine where the replication task is<br>running.                                                                                                                                                                                                                                                                                                                       |
| TASK_NAME                     | nvchar    | The Resource ID of the AWS DMS task. Resource ID can be found in task ARN.                                                                                                                                                                                                                                                                                                              |
| TASK_STATUS                   | varchar   | One of the following values:<br>• FULL LOAD<br>• CHANGE PROCESSING (CDC)<br>• NOT RUNNING<br>Task status is set to FULL LOAD as long as there is at<br>least one table in full load. After all tables have been<br>loaded, the task status changes to CHANGE PROCESSING if CDC<br>is enabled. The task is set to NOT RUNNING before you start the task,<br>or after the task completes. |
| STATUS_TIME                   | timestamp | The timestamp of the task status.                                                                                                                                                                                                                                                                                                                                                       |
| PENDING_CHANGES               | int       | The number of change records that were committed in the source database<br>and cached in the memory and disk of your replication instance.                                                                                                                                                                                                                                              |
| DISK_SWAP_SIZE                | int       | The amount of disk space used by old or offloaded<br>transactions.                                                                                                                                                                                                                                                                                                                      |
| TASK_MEMORY                   | int       | Current memory used, in MB.                                                                                                                                                                                                                                                                                                                                                             |
| SOURCE_CURRENT<br>\_POSITION  | varchar   | The position in the source database that AWS DMS is<br>currently reading from.                                                                                                                                                                                                                                                                                                          |
| SOURCE_CURRENT<br>\_TIMESTAMP | timestamp | The timestamp in the source database that AWS DMS is<br>currently reading from.                                                                                                                                                                                                                                                                                                         |
| SOURCE_TAIL<br>\_POSITION     | varchar   | The position of the oldest start transaction that isn't<br>committed. This value is the newest position that you can<br>revert to without losing any changes.                                                                                                                                                                                                                           |
| SOURCE_TAIL<br>\_TIMESTAMP    | timestamp | The timestamp of the oldest start transaction that isn't<br>committed. This value is the newest timestamp that you can<br>revert to without losing any changes.                                                                                                                                                                                                                         |
| SOURCE_TIMESTAMP<br>\_APPLIED | timestamp | The timestamp of the last transaction commit. In a bulk<br>apply process, this value is the timestamp for the commit of<br>the last transaction in the batch.                                                                                                                                                                                                                           |

The Suspended table (`dmslogs.awsdms_suspended_tables`) contains the following parameters.

| Column            | Type      | Description                                                    |
| ----------------- | --------- | -------------------------------------------------------------- |
| SERVER_NAME       | nvchar    | The name of the machine where the replication task is running. |
| TASK_NAME         | nvchar    | The name of the AWS DMS task                                   |
| TABLE_OWNER       | nvchar    | The table owner.                                               |
| TABLE_NAME        | nvchar    | The table name.                                                |
| SUSPEND_REASON    | nvchar    | Reason for suspension.                                         |
| SUSPEND_TIMESTAMP | timestamp | The time the suspension occurred.                              |

The Replication History table (`dmslogs.awsdms_history`) contains
the following parameters.

| Column            | Type      | Description                                                                                                                                                                     |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SERVER_NAME       | nvchar    | The name of the machine where the replication task is<br>running.                                                                                                               |
| TASK_NAME         | nvchar    | The Resource ID of the AWS DMS task. Resource ID can be found in task ARN.                                                                                                      |
| TIMESLOT_TYPE     | varchar   | One of the following values:<br>• FULL LOAD<br>• CHANGE PROCESSING (CDC)<br>If the task is running both full load and CDC, two history<br>records are written to the time slot. |
| TIMESLOT          | timestamp | The ending timestamp of the time slot.                                                                                                                                          |
| TIMESLOT_DURATION | int       | The duration of the time slot, in minutes.                                                                                                                                      |
| TIMESLOT_LATENCY  | int       | The target latency at the end of the time slot, in<br>seconds. This value only applies to CDC time slots.                                                                       |
| RECORDS           | int       | The number of records processed during the time<br>slot.                                                                                                                        |
| TIMESLOT_VOLUME   | int       | The volume of data processed in MB.                                                                                                                                             |

The Validation Failure table (`awsdms_validation_failures_v1`) contains all the data
validation failures for a task. For more information see,
[Data Validation Troubleshooting](CHAP_Validating.md#CHAP_Validating.Troubleshooting "CHAP_Validating.md#CHAP_Validating.Troubleshooting").

Additional control table settings include the following:

- `HistoryTimeslotInMinutes` – Use this option to
  indicate the length of each time slot in the Replication History table.
  The default is 5 minutes.
- `ControlSchema` – Use this option to indicate the
  database schema name for the control tables for the AWS DMS target. If you
  don't enter any information for this option, then the tables are
  copied to the default location in the database as listed following:

  - PostgreSQL, Public
  - Oracle, the target schema
  - Microsoft SQL Server, dbo in the target database
  - MySQL, awsdms_control
  - MariaDB, awsdms_control
  - Amazon Redshift, Public
  - DynamoDB, created as individual tables in the database
  - IBM Db2 LUW, awsdms_control
