# AWS DMS data resync

AWS Database Migration Service (AWS DMS) Data resync automatically fixes data inconsistencies identified
through data validation between your source and target databases. This feature works as
part of your existing DMS migration tasks, ensuring proper updates occur based on your
task configurations, connection settings, table mappings, and transformations.

Data resync feature operates by reading validation failures from a control table on
the target database and executing appropriate fix-up operations. When a mismatch is
detected, the current data is retrived from the source using the primary key stored in
the failure record, and it is applied to the target while respecting any configured
transformations. For more information, see [awsdms_validation_failures_v2 control table](CHAP_Validating.md#CHAP_DataResync.Troubleshooting.v2table "CHAP_Validating.md#CHAP_DataResync.Troubleshooting.v2table").

The behavior varies depending on your migration type. For full-load-only tasks, Data
resync runs once after the initial load and validation complete. For tasks with change
data capture (CDC), Data resync operates according to a configured schedule, temporarily
pausing replication and validation while fixes are applied.

During CDC resync operations:

- Replication and validation pause temporarily.
- Data resync processes existing validation failures.
- Normal replication and validation resume.
- The process repeats based on your configured schedule.
  Data resync automatically tracks the status of each fix-up operation and provides
  detailed metrics through table statistics.

**Prerequisites**:

The Data resync feature needs following prerequisites:

- You must have AWS DMS engine version 3.6.1 or later.
- You must configure schedule and timing duration settings for tasks
  that have ongoing replication. Full load only tasks do not require
  these settings.

## Limitations

The Data resync feature has following limitations:

- Data resync only supports Oracle and SQL Server as source database.
- Data resync supports PostgreSQL and Amazon Aurora PostgreSQL compatible
  engine as target database.
- All the tables in your source and target database must have primary keys.
  Validation does not support tables without a primary key or a unique key.
  Any tables that do not have a valid primary or unique key are suspended from
  validation and no validation failures are reported.
- When running Full-load-only tasks, data validation must be enabled.
- Data resync cannot be enabled for Validation only task as they do not
  replicate any data. You can enable resync on the parent replication task by
  providing the Validation only `taskID`. For more information, see
  [Validation only tasks](CHAP_Validating.md#CHAP_Validating.ValidationOnly "CHAP_Validating.md#CHAP_Validating.ValidationOnly").
- If the Validation only task has a `ControlSchema` parameter
  setting configured in the task settings, then the replication task must also
  have the same parameter configuration for Data resync to find the correct
  validation failures.
- You are required to configure schedule and timing duration settings for
  CDC tasks.
- During the resync window, Data resync can have an impact on the
  replication latency in DMS.

For more information regarding troubleshooting validations in AWS DMS during Data
resync, see the [Troubleshooting](CHAP_Validating.md#CHAP_Validating.Troubleshooting "CHAP_Validating.md#CHAP_Validating.Troubleshooting") section under [AWS DMS data
validation](CHAP_Validating.md "CHAP_Validating.md").

## Scheduling and timing

For tasks with CDC, you must configure when and how long Data resync operates.
This helps prevent impact to your normal replication operations. You specify:

- A schedule using cron format to define when resync operations can
  occur.
- A maximum duration to ensure resync operations don't extend into peak
  usage periods.

It is recommended to schedule resync operations during off-peak hours or to a
period where there minimal to no changes on the source database.

###### Note

The scheduled time includes waiting for the target apply stream to be empty,
as Data resync and normal replication cannot run simultaneously.

## Use cases

The data resync feature enables users to reconcile data inconsistencies between
source and target systems. It identifies mismatched records and synchronizes them to
maintain data consistency across distributed environments. The following use cases
demonstrate common scenarios where the data resync feature resolves data consistency
challenges:

**Scenario 1: Full load task - run resync using the
same DMS task**

In your existing DMS full-load migration task, you can do the
following:

- Enable validation: `Validation with data migration =
true`.
- Enable resync: `Data resync = true`

**Scenario 2: Full load and CDC, CDC only task - run
resync using the same DMS task**

In your existing DMS CDC migration task, you can do the
following:

- Enable validation: `Validation with data migration =
true`.
- Enable resync: `Data resync = true`
- Specify resync schedule: `"ResyncSchedule": "0 0,2,4,6 \*
- \*"`.
- Specify resync time: `MaxResyncTime": 60`

**Scenario 3: Full load and CDC or CDC only task for
replication and resync, in combination with a validation only
task**

To perform validation only operation in another DMS task when using
resync, you can do the following:

- Create a validation only DMS CDC task.

###### Note

You must note down and specify the ID of this task during
Data resync.

- In your primary CDC task, disable validation: `Data
validation = false`.
- Enable resync: `Data resync = true`
- Specify resync schedule: `"ResyncSchedule": "0 0,2,4,6 \*
- \*"`.
- Specify resync time: `MaxResyncTime": 60`.
- Specify the ID of the validation only DMS CDC task. Validation
  only task ID is appended at the end of ARN. Example ARN:
  `arn:aws:dms:us-west-2:123456789012:task:6DG4CLGJ5JSJR67CFD7UDXFY7KV6CYGRICL6KWI`
  and Example validation only task ID:
  `6DG4CLGJ5JSJR67CFD7UDXFY7KV6CYGRICL6KWI`.

## Best practices

You can leverage the Data resync feature in AWS Database Migration Service to improve durability of
your replication tasks and attain consistency. Some of the best practices to use the
Data resync feature are:

- As part of the Data resync, records that have mismatches are fixed by
  fetching it from the source and applying it on the target database. If the
  source database is updated during the resync window, resync reads the latest
  record value and applies it on the target. This can cause CDC apply events
  to fail and introduce temporary inconsistencies on the target database . To
  avoid this, you must schedule the resync window during off-business hours or
  periods where the changes on the source database are zero or minimal.
- Set the resync window during periods of minimal source database activity
  and within your acceptable target latency threshold. Small resync intervals
  can cause unprocessed validation mismatches to accumulate, while large
  windows may increase replication latency when many validation failures
  occur. Monitor validation failure and resync rates to determine optimal
  resync windows during source inactivity periods. Some examples for setting
  up the resync windows are:
  - Multiple short window configuration:

  ```
  "ResyncSchedule": "0 0,2,4,6 * * *",
  "MaxResyncTime": 60
  ```

  - Single daily window configuration:

  ```
  "ResyncSchedule": "0 0 * * *",
  "MaxResyncTime": 360
  ```

- Monitoring replication latency in DMS during resync windows and adjust
  schedule accordingly to mitigate large spikes.
- You can review resync results through table stastics or by querying the
  `awsdms_validation_failures_v2` table on the target
  databadse. For more information, see [Monitoring replication tasks using Amazon
  CloudWatch](CHAP_Monitoring.md#CHAP_Monitoring.CloudWatch "CHAP_Monitoring.md#CHAP_Monitoring.CloudWatch").
- When the task is in an ongoing replication phase, avoid initiating a
  reload for individual tables during the resync window.
- Best practices for a CDC replication task:
  - All the tables in your database complete loading process.
  - Mismatches are identified in the on going validation
    process.
  - As per the resync scheduled window, the replication task pauses
    for a brief period.
  - Data resync fixes the issues idenfified during the validation
    process.
  - The replication process resumes and repeats as per the
    schedule.

## Data resync configuration and

examples

**Data resync settings
configuration**:

You can configure resync for your replication task in DMS. Below is an
example of Data resync settings configuration in your task:

```
"ResyncSettings": {
    "EnableResync": true,
    "ResyncSchedule": "0 0,2,4,6 * * *",  // Run at 12AM, 2AM, 4AM, and 6AM daily
    "MaxResyncTime": 60,                  // Run for maximum of 60 minutes, or 1 hour
    "ValidationTaskId": "TASK-ID-IF-NEEDED" //Optional, used only if validation is performed as a separate Validation only task
}
```

**Examples of common resync scheduling
patterns**:

- `0 0 * * *`: Run once everyday at midnight.
- `0 0,12 * * *`: Run twice every day at midnight and
  noon.
- `0 0,2,4,6, * * *`: Run every two hours between midnight and 6
  am.
- `0 1 * * 1`: Run every week on Mondays at 1 am.

###### Note

You must specifiy a number for each day starting 0 to 6. For more information,
see [Cron expressions rules](#CHAP_DataResync.cron "#CHAP_DataResync.cron").

**Monitoring resync operations**:

You can monitor the resync operation through table statistics. Here is
an example output:

```
{
    "TableStatistics": {
        ...
        "ValidationFailedRecords": 1000,
        ...
        "ResyncRowsAttempted": 1000,
        "ResyncRowsSucceeded": 995,
        "ResyncRowsFailed": 5,
        "ResyncProgress": 99.5, // ratio of ResyncRowsSucceeded/ValidationFailedRecords
        "ResyncState": "Last resync at: 2024-03-14T06:00:00Z"
    }
}
```

To configure the Data resync feature in AWS DMS, you can review various resync
parameters and their respective configuration settings. For more information, see
[Data
resync settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").
For more information regarding data resync logging settings, see [Logging task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md").

## Validation and troubleshooting

**Validation**:

When data valudation is enabled, AWS DMS creates a validation failures
table in your target database with the following structure:

```
CREATE TABLE awsdms_validation_failures_v2 (
    "RESYNC_ID" bigint NOT NULL,
    "TASK_NAME" varchar(128) NOT NULL,
    "TABLE_OWNER" varchar(128) NOT NULL,
    "TABLE_NAME" varchar(128) NOT NULL,
    "FAILURE_TIME" timestamp NOT NULL,
    "KEY_TYPE" varchar(128) NOT NULL,
    "KEY" varchar(7800) NOT NULL,
    "FAILURE_TYPE" varchar(128) NOT NULL,
    "DETAILS" varchar(7000) NOT NULL,
    "RESYNC_RESULT" varchar(128) NULL,
    "RESYNC_TIME" timestamp NULL,
    "RESYNC_ACTION" varchar(128) NULL
);
```

You can write a query to this table to understand the data mismatches
that are found and how are they resolved.

When validation is enabled, AWS DMS creates a validation failures table in your
target database. If you have any issues you can query the
`awsdms_control.awsdms_validation_failures_v2` table to understand
the data mismatches that are found and how are they resolved. For more information,
see [Troubleshooting](CHAP_Validating.md#CHAP_Validating.Troubleshooting "CHAP_Validating.md#CHAP_Validating.Troubleshooting") section in [AWS DMS Data
validation](CHAP_Validating.md "CHAP_Validating.md").

**Common workflow**:

During validation in data resync the standard workflow is as
follows:

**Full Load Only tasks**:

1. All the tables in your database complete loading
   process.
2. Mismatches are identified in the on going validation
   process.
3. Data resync fixes the issues idenfified during the validation
   process.
4. Validation process validates the rectification.
5. Migration task is completed successfully.

**CDC tasks**:

1. All the tables in your database complete loading
   process.
2. Mismatches are identified in the on going validation
   process.
3. As per the resync scheduled window, the replication task
   pauses for a brief period.
4. Data resync fixes the issues idenfified during the validation
   process.
5. The replication process resumes and repeats as per the
   schedule.

Any modification done to the task such as stoping the replication task during the
resync operation or reloading and revalidating tables can impact the task's behavior
and outcome. Some of the known behavior changes are as follows:

**When you stop the replication task while resync operation is
in progress**:

- The resync operation does not automatically resume. You must restart it
  again.
- Future resync operations occur as per the configured schedule.
- Any incomplete fixes are attempted in the next resync schedule
  window.

**When you reload a table in your database**:

- The resync operation skips any table undergoing reload.
- The previous validation failures for a table that was reloaded are
  ignored.
- New validation begins after the reload action completes.

**When you revalidate a table in your
database**:

- All the statiscs for your resync operation are reset.
- The previous validation failures for a table that was revalidated are
  ignored.

###### Note

When upgrading or moving a task to DMS version 3.6.1 and above, any failures
in the `awsdms_control.awsdms_validation_failures_v1` table are not
resynced. Only failures in the `awsdms_validation_failures_v2` table
are resynced. To resync failures in
`awsdms_control.awsdms_validation_failures_v2` table, you must
reload the task, reload one or more tables in the task, or re-validate one or
more tables. For more information, see the following links:

- To reload a task, see [`StartReplicationTask` API reference](../APIReference/API_StartReplicationTask.md "../APIReference/API_StartReplicationTask.md").
- To reload one or more tables in a task, see [`reload-tables`](../../../cli/latest/reference/dms/reload-tables.md "../../../cli/latest/reference/dms/reload-tables.md") in the _AWS CLI command reference_
  documentation.
- To re-validate one or more tables, see the `validate-only`
  option in the [`reload-tables`](../../../cli/latest/reference/dms/reload-tables.md "../../../cli/latest/reference/dms/reload-tables.md") section in the _AWS CLI command reference_
  documentation.
  .

## Cron expression rules

To configure Data resync operations during a replication task in AWS DMS you can use
cron expressions rules. These rules allow you customise resync time windows and
schedule them as per your business needs. You can use various parameters such as
minutes, hours, days, months, and days of the week. The cron expression rules for
each parameters are:

**Minutes**:

- Minute range from 0 to 59.
- You can use (`-`), `or`/`and`
  to specify the range. Maximum 10 items separated by a comma
  (`,`).
- **Examples**:
  - `2-5` equals to
    `2,3,5,5`.
  - `1-2,3-4,5,7-10` is a valid range.
  - `1,2,3,4,5,6,7,8,9,10` is a valid
    range.
  - `1,2,3,4,5,6,7,8,9,10,11` is not a valid
    range. The resync operation skips after the 10th range
    item.

- You can use (`*`). Example: `*` equals
  to `0-59`.
- You can use (`/`) only in combination with
  (`-`) or (`*`).

**Examples**:

    + `2-7/2` equals to
     `2,4,6`.
    + `*/15` equals to
     `0,15,30,45`.

**Hours**:

Same as "**Minutes**" but the valid range
is from `0` to `23`.

**Days**:

- Same as "**Minutes**" but the
  valid range is from `1` to `31`.
- Use of `L` is supported in resync configuration. It
  is intepretted as last day of the month. You must not use it in
  combination with another syntax.

**Months**:

Same as "**Minutes**" but the valid range
is from `1` to `12`.

**Days of week**:

- Same as "**Minutes**" but the
  valid range is from `0` to `6`.
- You cannot add a string value for the name of the week.
