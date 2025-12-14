# Specifying task settings

for AWS Database Migration Service tasks

Each task has settings that you can configure according to the needs of your
database migration. You create these settings in a JSON file or, with some settings,
you can specify the settings using the AWS DMS console. For information about how to use a task configuration file to set task settings, see [Task settings example](#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "#CHAP_Tasks.CustomizingTasks.TaskSettings.Example").

There are several main types of task settings, as listed following.

###### Topics

- [Task settings example](#CHAP_Tasks.CustomizingTasks.TaskSettings.Example "#CHAP_Tasks.CustomizingTasks.TaskSettings.Example")
- [Target
  metadata task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Full-load
  task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Time Travel task
  settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Logging task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Control
  table task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Stream
  buffer task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Change processing tuning settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Data
  validation task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Data
  resync settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Task
  settings for change processing DDL handling](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Character substitution task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Before
  image task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Error
  handling task settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")
- [Saving task
  settings](CHAP_Tasks.CustomizingTasks.TaskSettings.md "CHAP_Tasks.CustomizingTasks.TaskSettings.md")

| Task settings                                                                                                                                                                                                                                                                                                 | Relevant documentation                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Creating a task assessment report**<br>You can create a task assessment report that shows any<br>unsupported data types that could cause problems during<br>migration. You can run this report on your task before running<br>the task to find out potential issues.                                        | [Enabling and working with premigration<br>assessments for a task](CHAP_Tasks.md "CHAP_Tasks.md")                                                                                                                                                                                                                                                                                                    |
| **Creating a task**<br>When you create a task, you specify the source, target, and<br>replication instance, along with any migration settings.                                                                                                                                                                | [Creating a task](CHAP_Tasks.md "CHAP_Tasks.md")                                                                                                                                                                                                                                                                                                                                                     |
| **Creating an ongoing replication task**<br>You can set up a task to provide continuous replication<br>between the source and target.                                                                                                                                                                         | [Creating tasks for ongoing replication using<br>AWS DMS](CHAP_Task.md "CHAP_Task.md")                                                                                                                                                                                                                                                                                                               |
| **Applying task settings**<br>Each task has settings that you can configure according to the<br>needs of your database migration. You create these settings in a<br>JSON file or, with some settings, you can specify the settings<br>using the AWS DMS console.                                              | Specifying task settings<br>for AWS Database Migration Service tasks                                                                                                                                                                                                                                                                                                                                 |
| **Data validation**<br>Use data validation to have AWS DMS compare the data on your<br>target data store with the data from your source data<br>store.                                                                                                                                                        | [AWS DMS data validation](CHAP_Validating.md "CHAP_Validating.md")                                                                                                                                                                                                                                                                                                                                   |
| **Modifying a task**<br>When a task is stopped, you can modify the settings for the<br>task.                                                                                                                                                                                                                  | [Modifying a task](CHAP_Tasks.md "CHAP_Tasks.md")                                                                                                                                                                                                                                                                                                                                                    |
| **Reloading tables during a task**<br>You can reload a table during a task if an error occurs during<br>the task.                                                                                                                                                                                             | [Reloading tables during a task](CHAP_Tasks.md "CHAP_Tasks.md")                                                                                                                                                                                                                                                                                                                                      |
| **Using table mapping**<br>Table mapping uses several types of rules to specify task<br>settings for the data source, source schema, data, and any<br>transformations that should occur during the task.                                                                                                      | Selection Rules<br>[Selection rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")<br>Transformation Rules<br>[Transformation rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md") |
| **Applying filters**<br>You can use source filters to limit the number and type of<br>records transferred from your source to your target. For<br>example, you can specify that only employees with a location of<br>headquarters are moved to the target database. You apply filters<br>on a column of data. | [Using source filters](CHAP_Tasks.CustomizingTasks.md "CHAP_Tasks.CustomizingTasks.md")                                                                                                                                                                                                                                                                                                              |
| **Monitoring a task**<br>There are several ways to get information on the performance<br>of a task and the tables used by the task.                                                                                                                                                                           | [Monitoring AWS DMS tasks](CHAP_Monitoring.md "CHAP_Monitoring.md")                                                                                                                                                                                                                                                                                                                                  |
| **Managing task logs**<br>You can view and delete task logs using the AWS DMS API or<br>AWS CLI.                                                                                                                                                                                                              | [Viewing and managing AWS DMS task logs](CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs "CHAP_Monitoring.md#CHAP_Monitoring.ManagingLogs")                                                                                                                                                                                                                                                          |

## Task settings example

You can use either the AWS Management Console or the AWS CLI to create a replication task. If you
use the AWS CLI, you set task settings by creating a JSON file, then specifying the
file:// URI of the JSON file as the [ReplicationTaskSettings](../APIReference/API_CreateReplicationTask.md#DMS-CreateReplicationTask-request-ReplicationTaskSettings "../APIReference/API_CreateReplicationTask.md#DMS-CreateReplicationTask-request-ReplicationTaskSettings") parameter of the [CreateReplicationTask](../APIReference/API_CreateReplicationTask.md "../APIReference/API_CreateReplicationTask.md") operation.

The following example shows how to use the AWS CLI to call the
`CreateReplicationTask` operation:

```
aws dms create-replication-task \
--replication-task-identifier MyTask \
--source-endpoint-arn arn:aws:dms:us-west-2:123456789012:endpoint:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABC \
--target-endpoint-arn arn:aws:dms:us-west-2:123456789012:endpoint:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABC \
--replication-instance-arn arn:aws:dms:us-west-2:123456789012:rep:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890ABC \
--migration-type cdc \
--table-mappings file://tablemappings.json \
--replication-task-settings file://settings.json


```

The preceding example uses a table mapping file called `tablemappings.json`. For table
mapping examples, see [Using table mapping to
specify task settings](CHAP_Tasks.CustomizingTasks.md "CHAP_Tasks.CustomizingTasks.md").

A task settings JSON file can look like the following.

```

{
  "TargetMetadata": {
    "TargetSchema": "",
    "SupportLobs": true,
    "FullLobMode": false,
    "LobChunkSize": 64,
    "LimitedSizeLobMode": true,
    "LobMaxSize": 32,
    "InlineLobMaxSize": 0,
    "LoadMaxFileSize": 0,
    "ParallelLoadThreads": 0,
    "ParallelLoadBufferSize":0,
    "ParallelLoadQueuesPerThread": 1,
    "ParallelApplyThreads": 0,
    "ParallelApplyBufferSize": 100,
    "ParallelApplyQueuesPerThread": 1,
    "BatchApplyEnabled": false,
    "TaskRecoveryTableEnabled": false
  },
  "FullLoadSettings": {
    "TargetTablePrepMode": "DO_NOTHING",
    "CreatePkAfterFullLoad": false,
    "StopTaskCachedChangesApplied": false,
    "StopTaskCachedChangesNotApplied": false,
    "MaxFullLoadSubTasks": 8,
    "TransactionConsistencyTimeout": 600,
    "CommitRate": 10000
  },
    "TTSettings" : {
    "EnableTT" : true,
    "TTS3Settings": {
        "EncryptionMode": "SSE_KMS",
        "ServerSideEncryptionKmsKeyId": "arn:aws:kms:us-west-2:112233445566:key/myKMSKey",
        "ServiceAccessRoleArn": "arn:aws:iam::112233445566:role/dms-tt-s3-access-role",
        "BucketName": "myttbucket",
        "BucketFolder": "myttfolder",
        "EnableDeletingFromS3OnTaskDelete": false
      },
    "TTRecordSettings": {
        "EnableRawData" : true,
        "OperationsToLog": "DELETE,UPDATE",
        "MaxRecordSize": 64
      }
  },
  "Logging": {
    "EnableLogging": false
  },
  "ControlTablesSettings": {
    "ControlSchema":"",
    "HistoryTimeslotInMinutes":5,
    "HistoryTableEnabled": false,
    "SuspendedTablesTableEnabled": false,
    "StatusTableEnabled": false
  },
  "StreamBufferSettings": {
    "StreamBufferCount": 3,
    "StreamBufferSizeInMB": 8
  },
  "ChangeProcessingTuning": {
    "BatchApplyPreserveTransaction": true,
    "BatchApplyTimeoutMin": 1,
    "BatchApplyTimeoutMax": 30,
    "BatchApplyMemoryLimit": 500,
    "BatchSplitSize": 0,
    "MinTransactionSize": 1000,
    "CommitTimeout": 1,
    "MemoryLimitTotal": 1024,
    "MemoryKeepTime": 60,
    "StatementCacheSize": 50
  },
  "ChangeProcessingDdlHandlingPolicy": {
    "HandleSourceTableDropped": true,
    "HandleSourceTableTruncated": true,
    "HandleSourceTableAltered": true
  },
  "LoopbackPreventionSettings": {
    "EnableLoopbackPrevention": true,
    "SourceSchema": "LOOP-DATA",
    "TargetSchema": "loop-data"
  },

  "CharacterSetSettings": {
    "CharacterReplacements": [ {
        "SourceCharacterCodePoint": 35,
        "TargetCharacterCodePoint": 52
      }, {
        "SourceCharacterCodePoint": 37,
        "TargetCharacterCodePoint": 103
      }
    ],
    "CharacterSetSupport": {
      "CharacterSet": "UTF16_PlatformEndian",
      "ReplaceWithCharacterCodePoint": 0
    }
  },
  "BeforeImageSettings": {
    "EnableBeforeImage": false,
    "FieldName": "",
    "ColumnFilter": "pk-only"
  },
  "ErrorBehavior": {
    "DataErrorPolicy": "LOG_ERROR",
    "DataTruncationErrorPolicy":"LOG_ERROR",
    "DataMaskingErrorPolicy": "STOP_TASK",
    "DataErrorEscalationPolicy":"SUSPEND_TABLE",
    "DataErrorEscalationCount": 50,
    "TableErrorPolicy":"SUSPEND_TABLE",
    "TableErrorEscalationPolicy":"STOP_TASK",
    "TableErrorEscalationCount": 50,
    "RecoverableErrorCount": 0,
    "RecoverableErrorInterval": 5,
    "RecoverableErrorThrottling": true,
    "RecoverableErrorThrottlingMax": 1800,
    "ApplyErrorDeletePolicy":"IGNORE_RECORD",
    "ApplyErrorInsertPolicy":"LOG_ERROR",
    "ApplyErrorUpdatePolicy":"LOG_ERROR",
    "ApplyErrorEscalationPolicy":"LOG_ERROR",
    "ApplyErrorEscalationCount": 0,
    "FullLoadIgnoreConflicts": true
  },
  "ValidationSettings": {
    "EnableValidation": false,
    "ValidationMode": "ROW_LEVEL",
    "ThreadCount": 5,
    "PartitionSize": 10000,
    "FailureMaxCount": 1000,
    "RecordFailureDelayInMinutes": 5,
    "RecordSuspendDelayInMinutes": 30,
    "MaxKeyColumnSize": 8096,
    "TableFailureMaxCount": 10000,
    "ValidationOnly": false,
    "HandleCollationDiff": false,
    "RecordFailureDelayLimitInMinutes": 1,
    "SkipLobColumns": false,
    "ValidationPartialLobSize": 0,
    "ValidationQueryCdcDelaySeconds": 0
  }
}

```
