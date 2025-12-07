# Data

resync settings

The Data resync feature allows you to resync target database with your source
database based on data validation report. For more information, see [AWS DMS data
validation](CHAP_Validating.md "CHAP_Validating.md").

You can add additional parameters for `ResyncSettings` in the
`ReplicationTaskSettings` endpoint that configures the resync
process. For more information, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example") in the [Specifying task settings for AWS Database Migration Service
tasks](CHAP_Tasks.CustomizingTasks.md "CHAP_Tasks.CustomizingTasks.md").

###### Note

`ResyncSchedule` and `MaxResyncTime` parameters are
required if the resync process is enabled and the task has a CDC component. They
are not valid for full-load only tasks.

The Data resync parameter settings and values are as follows:

`**EnableResync**`

Enables Data resync feature when set to `true`. By default,
Data resync is disabled.

**Datatype**: Boolean

**Required**: No

**Default**: `false`

**Validation**: Should not be null if
`ResyncSettings` parameter is present in
`TaskSettings`.

`**ResyncSchedule**`

Time window for the Data resync feature to be in effect. Must be
present in Cron format. For more information, see [Cron expression rules](CHAP_Validating.md#CHAP_DataResync.cron "CHAP_Validating.md#CHAP_DataResync.cron").

**Datatype**: String

**Required**: No

**Validation**:

- Must be present in Cron expression format.
- Should not be null for tasks with CDC that has
  `EnableResync` set to `true`.
- Cannot be set for tasks without CDC component.

`**MaxResyncTime**`

Maximum time limit in minutes for the Data resync feature to be in
effect.

**Datatype**: Integer

**Required**: No

**Validation**:

- Should not be null for tasks with CDC.
- Not required for tasks without CDC.
- Minimum value: `5 minutes`, Maximum value:
  `14400 minutes` (10 days).

`**Validation onlyTaskID**`

Unique ID of the validation task. The validation only task ID is
appended at the end of an ARN. For example:

- Validation only task ARN:
  `arn:aws:dms:us-west-2:123456789012:task:6DG4CLGJ5JSJR67CFD7UDXFY7KV6CYGRICL6KWI`
- Validation only task ID:
  `6DG4CLGJ5JSJR67CFD7UDXFY7KV6CYGRICL6KWI`

**Datatype**: String

**Required**: No

**Validation**: Should not be null for
tasks with Data resync feature enabled and validation disabled.

Example:

```
"ResyncSettings": {
    "EnableResync": true,
    "ResyncSchedule": "30 9 ? * MON-FRI",
    "MaxResyncTime": 400,
    "ValidationTaskId": "JXPP94804DJOEWIJD9348R3049"
},
```
