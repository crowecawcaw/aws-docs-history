# Error

handling task settings

You can set the error handling behavior of your replication task using the
following settings. For information about how to use a task configuration file to set task settings, see [Task settings example](CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "CHAP_Tasks.CustomizingTasks.md#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

- `DataErrorPolicy` – Determines the action AWS DMS
  takes when there is an error related to data processing at the record
  level. Some examples of data processing errors include conversion
  errors, errors in transformation, and bad data. The default is
  `LOG_ERROR`.
  - `IGNORE_RECORD` – The task continues and the
    data for that record is ignored. The error counter for the
    `DataErrorEscalationCount` property is
    incremented. Thus, if you set a limit on errors for a table,
    this error counts toward that limit.
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `DataTruncationErrorPolicy` – Determines the action
  AWS DMS takes when data is truncated. The default is
  `LOG_ERROR`.
  - `IGNORE_RECORD` – The task continues and the
    data for that record is ignored. The error counter for the
    `DataErrorEscalationCount` property is
    incremented. Thus, if you set a limit on errors for a table,
    this error counts toward that limit.
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `DataErrorEscalationPolicy` – Determines the action
  AWS DMS takes when the maximum number of errors (set in the
  `DataErrorEscalationCount` parameter) is reached. The
  default is `SUSPEND_TABLE`.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `DataErrorEscalationCount` – Sets the maximum number
  of errors that can occur to the data for a specific record. When this
  number is reached, the data for the table that contains the error record
  is handled according to the policy set in the
  `DataErrorEscalationPolicy`. The default is 0.
- `EventErrorPolicy` – Determines the action AWS DMS
  takes when an error occurs while sending a task-related event.
  Its possible values are
  - `IGNORE` – The task continues and any
    data associated with that event is ignored.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `TableErrorPolicy` – Determines the action
  AWS DMS takes when an error occurs when processing data or metadata
  for a specific table. This error only applies to general table data and
  isn't an error that relates to a specific record. The default is
  `SUSPEND_TABLE`.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `TableErrorEscalationPolicy` – Determines the action
  AWS DMS takes when the maximum number of errors (set using the
  `TableErrorEscalationCount` parameter). The default and
  only user setting is `STOP_TASK`, where the task is stopped
  and manual intervention is required.
- `TableErrorEscalationCount` – The maximum number of
  errors that can occur to the general data or metadata for a specific
  table. When this number is reached, the data for the table is handled
  according to the policy set in the
  `TableErrorEscalationPolicy`. The default is 0.
- `RecoverableErrorCount` – The maximum number of
  attempts made to restart a task when an environmental error occurs. After
  the system attempts to restart the task the designated number of times, the
  task is stopped and manual intervention is required. The default value is
  -1.

When you set this value to -1, the number of retries that DMS attempts
varies based on the returned error type as follows:

    + **Running state, recoverable error**: If a recoverable error such
     as a lost connection or a target apply fail occurs, DMS retries the
     task nine times.
    + **Starting state, recoverable error**: DMS retries
     the task six times.
    + **Running state, fatal error handled by DMS**:
     DMS retries the task six times.
    + **Running state, fatal error not handled by DMS**:
     DMS does not retry the task.
    + **Other than above**: AWS DMS retries
     the task indefinitely.

Set this value to 0 to never attempt to restart a
task.

We recommend that you set `RecoverableErrorCount` and
`RecoverableErrorInterval` to values such that there are sufficient
retries at sufficient intervals for your DMS task to recover properly. If
a fatal error occurs, DMS stops making restart attempts in most scenarios.

- `RecoverableErrorInterval` – The number of seconds
  that AWS DMS waits between attempts to restart a task. The default is

5.

- `RecoverableErrorThrottling` – When enabled, the
  interval between attempts to restart a task is increased in a series based on the
  value of `RecoverableErrorInterval`. For example, if `RecoverableErrorInterval`
  is set to 5 seconds, then the next retry will happen after 10 seconds, then 20,
  then 40 seconds and so on. The default is `true`.
- `RecoverableErrorThrottlingMax` – The maximum number
  of seconds that AWS DMS waits between attempts to restart a task if
  `RecoverableErrorThrottling` is enabled. The default is

1800.

- `RecoverableErrorStopRetryAfterThrottlingMax`– Default
  value is set to `true`, and DMS stops resuming the task after the
  maximum number of seconds that AWS DMS waits between recovery attempts is
  reached, per `RecoverableErrorStopRetryAfterThrottlingMax`. When
  set to `false`, DMS keeps resuming the task after the maximum
  number of seconds that AWS DMS waits between recovery attempts is reached, per
  `RecoverableErrorStopRetryAfterThrottlingMax` until
  `RecoverableErrorCount` is reached.
- `ApplyErrorDeletePolicy` – Determines what action
  AWS DMS takes when there is a conflict with a DELETE operation. The
  default is `IGNORE_RECORD`. Possible values are the
  following:
  - `IGNORE_RECORD` – The task continues and the
    data for that record is ignored. The error counter for the
    `ApplyErrorEscalationCount` property is
    incremented. Thus, if you set a limit on errors for a table,
    this error counts toward that limit.
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `ApplyErrorInsertPolicy` – Determines what action
  AWS DMS takes when there is a conflict with an INSERT operation. The
  default is `LOG_ERROR`. Possible values are the
  following:
  - `IGNORE_RECORD` – The task continues and the
    data for that record is ignored. The error counter for the
    `ApplyErrorEscalationCount` property is
    incremented. Thus, if you set a limit on errors for a table,
    this error counts toward that limit.
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.
  - `INSERT_RECORD` – If there is an existing
    target record with the same primary key as the inserted source
    record, the target record is updated.

  ###### Note

      - **In Transactional Apply
       mode**: In this process, the system first
       attempts to insert the record. If the insert fails due
       to a primary key conflict, it deletes the existing
       record and then inserts the new one.
      - **In Batch Apply mode**:
       The process removes all existing records in the target
       batch before inserting the complete set of new records,
       ensuring a clean replacement of data.

- `ApplyErrorUpdatePolicy` – Determines what action
  AWS DMS takes when there is a missing data conflict with an UPDATE operation.
  The default is `LOG_ERROR`.
  Possible values are the following:
  - `IGNORE_RECORD` – The task continues and the
    data for that record is ignored. The error counter for the
    `ApplyErrorEscalationCount` property is
    incremented. Thus, if you set a limit on errors for a table,
    this error counts toward that limit.
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.
  - `UPDATE_RECORD` – If the target record is
    missing, the missing target record is inserted into the target
    table. AWS DMS completely disables LOB column support for the task.
    Selecting this option requires full supplemental logging
    to be enabled for all the source table columns when Oracle is
    the source database.

  ###### Note

      - **In Transactional Apply
       mode**: In this process, the system first
       attempts to update the record. If the update fails due
       to a missing record on target, it run a delete for the
       failed record and then inserts the new one. This process
       requires full supplemental logging for Oracle source
       databases and DMS disables LOB column support for this
       task.
      - **In Batch Apply mode**:
       The process removes all existing records in the target
       batch before inserting the complete set of new records,
       ensuring a clean replacement of data.

- `ApplyErrorEscalationPolicy` – Determines what
  action AWS DMS takes when the maximum number of errors (set using the
  `ApplyErrorEscalationCount` parameter) is reached. The default is LOG_ERROR:
  - `LOG_ERROR` – The task continues and the
    error is written to the task log.
  - `SUSPEND_TABLE` – The task continues but
    data from the table with the error record is moved into an error
    state and the data isn't replicated.
  - `STOP_TASK` – The task stops and manual
    intervention is required.

- `ApplyErrorEscalationCount` – This option sets the
  maximum number of APPLY conflicts that can occur for a specific table
  during a change process operation. When this number is reached, the
  table data is handled according to the policy set in the
  `ApplyErrorEscalationPolicy` parameter. The default is 0.
- `ApplyErrorFailOnTruncationDdl` – Set this option to
  `true` to cause the task to fail when a truncation is
  performed on any of the tracked tables during CDC.
  The
  default is `false`.

This approach doesn't work with PostgreSQL version 11.x or lower,
or any other source endpoint that doesn't replicate DDL table truncation.

- `FailOnNoTablesCaptured` – Set this option to
  `true` to cause a task to fail when the table mappings
  defined for a task find no tables when the task starts. The default is
  `true`.
- `FailOnTransactionConsistencyBreached` – This option
  applies to tasks using Oracle as a source with CDC. The default is false. Set it to
  `true` to cause a task to fail when a transaction is open
  for more time than the specified timeout and can be dropped.

When a CDC task starts with Oracle, AWS DMS waits for a limited time for
the oldest open transaction to close before starting CDC. If the oldest
open transaction doesn't close until the timeout is reached, then
in most cases AWS DMS starts CDC, ignoring that transaction. If this
option is set to `true`, the task fails.

- `FullLoadIgnoreConflicts` – Set this option to
  `true` to have AWS DMS ignore "zero rows affected" and
  "duplicates" errors when applying cached events. If set to
  `false`, AWS DMS reports all errors instead of ignoring
  them. The default is `true`.
- `DataMaskingErrorPolicy` – Determines the action AWS DMS takes when the data masking is failed due to incompatible data type or any other reason.
  The follwing are available options:

      + `STOP_TASK` (Default) – The task stops and manual intervention is required.
      + `IGNORE_RECORD` – The task continues and the data for that record is ignored.
      + `LOG_ERROR` – The task continues and the error is written to the task log. Unmasked data will be loaded in target table.
      + `SUSPEND_TABLE` – The task continues but data from the table with the error record is moved into an error state and the data isn't replicated.

  Note that _table load errors_ in Redshift as a target are reported
  in `STL_LOAD_ERRORS`. For more information, see
  [STL_LOAD_ERRORS](../../../redshift/latest/dg/r_STL_LOAD_ERRORS.md "../../../redshift/latest/dg/r_STL_LOAD_ERRORS.md")
  in the _Amazon Redshift Database Developer Guide_.
