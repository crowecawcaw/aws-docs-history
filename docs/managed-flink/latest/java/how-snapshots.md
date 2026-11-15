

# Manage application backups using snapshots
<a name="how-snapshots"></a>

A *snapshot* is a backup of the state of a Managed Service for Apache Flink application. Each snapshot is an Apache Flink savepoint. For more information, see [Savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/) in the Apache Flink Documentation.

Restore an application from a snapshot to resume processing from the saved state.

**Note**  
We recommend that your application create a snapshot several times a day to restart properly with correct state data. The correct frequency for your snapshots depends on your application's business logic. Taking frequent snapshots lets you recover more recent data, but increases cost and requires more system resources.

Managed Service for Apache Flink supports two types of snapshots:
+ **Enhanced snapshots** – An enhanced snapshot is an AWS resource with its own Amazon Resource Name (ARN). The enhanced snapshot exists independently of the application that created it.

  You can restore an enhanced snapshot into any application in enhanced snapshot mode in the same account and Region. For the conditions, see [Restore an application from an enhanced snapshot](snapshots-restore.md).

  You can also export an enhanced snapshot to Amazon S3 and import one from Amazon S3.

  Enhanced snapshots require Apache Flink version 1.20 or later.
+ **Application snapshots (legacy)** – An application snapshot belongs to the application that created it. Only that application can restore from it.

An application uses one type of snapshot at a time. New applications use application snapshots by default. To use enhanced snapshots, create the application in *enhanced snapshot mode*, or upgrade an existing application to enhanced snapshot mode.

**Note**  
After you upgrade to enhanced snapshot mode, the application stays in enhanced snapshot mode. To restore an application snapshot (legacy), roll back to the version before the upgrade. You can roll back only if you have not updated the application since the upgrade. For more information about rollbacks, see [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior).

Use the following topics to work with enhanced snapshots:
+ [How enhanced snapshots work](snapshots-how-it-works.md): Learn how enhanced snapshots, enhanced snapshot mode, and system snapshots work.
+ [Set up enhanced snapshots](snapshots-setup.md): Create an application that uses enhanced snapshots.
+ [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md): Upgrade an existing application to enhanced snapshot mode.
+ [Create and manage enhanced snapshots](snapshots-manage.md): Create, describe, list, and delete enhanced snapshots.
+ [Restore an application from an enhanced snapshot](snapshots-restore.md): Start or update an application from an enhanced snapshot.
+ [Import and export enhanced snapshots](snapshots-import-export.md): Move enhanced snapshots between Managed Service for Apache Flink and Amazon S3.
+ [Monitor enhanced snapshot operations](snapshots-monitor-operations.md): Track the status of asynchronous enhanced snapshot operations.
+ [Enhanced snapshot API examples](snapshots-api-examples.md): Review example requests for the enhanced snapshot API actions.

## Application snapshots (legacy)
<a name="how-snapshots-legacy"></a>

You manage application snapshots with the following API actions:
+ [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationSnapshot.html)
+ [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationSnapshot.html)
+ [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationSnapshot.html)
+ [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html)

After the upgrade to enhanced snapshot mode, these rules apply to the application snapshots (legacy) of the application:
+ `ListApplicationSnapshots`, `DescribeApplicationSnapshot`, and `DeleteApplicationSnapshot` work for the existing application snapshots.
+ `CreateApplicationSnapshot` returns `InvalidApplicationConfigurationException`. Use [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) instead.

For the quota on application snapshots (legacy), see [Managed Service for Apache Flink and Studio notebook quota](limits.md). If your application reaches the limit on snapshots, then manually creating a snapshot fails with a `LimitExceededException`. 

While the application exists, Managed Service for Apache Flink does not delete its application snapshots (legacy). To delete one, use the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action. When you delete the application, Managed Service for Apache Flink also deletes its application snapshots (legacy). `DeleteApplication` does not delete enhanced snapshots.

To load a saved snapshot of application state when starting an application, use the [`ApplicationRestoreConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html) parameter of the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) or [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action.

## System snapshots
<a name="how-fault-snapshot-update"></a>

A *system snapshot* is a snapshot that Managed Service for Apache Flink creates when you update or stop the application. Depending on the snapshot type, other application actions also create a system snapshot, as this section lists. The application uses the system snapshot to keep exactly-once processing.

To turn on system snapshots for either snapshot type, set `SnapshotsEnabled` to `true` in the [`ApplicationSnapshotConfiguration`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.html) for the application.

The operations that create a system snapshot depend on whether the application uses enhanced snapshot mode or application snapshots (legacy):
+ **Enhanced snapshot mode** – Managed Service for Apache Flink creates a system snapshot when you update or stop a `RUNNING` application. Managed Service for Apache Flink also creates one when you add or delete the Amazon VPC settings of a `RUNNING` application. The same applies when you add or delete a CloudWatch logging option. A stop with `Force` set to `true` does not create a system snapshot. For the Amazon VPC settings, see [Configure Managed Service for Apache Flink to access resources in an Amazon VPC](vpc.md).
+ **Application snapshots (legacy)** – Managed Service for Apache Flink creates a system snapshot when you update, scale, or stop the application.

**Note**  
If you set `SnapshotsEnabled` to `false`, an application update discards the application state data.

**Note**  
Managed Service for Apache Flink triggers intermediate savepoints during snapshot creation. For Flink version 1.15 or greater, intermediate savepoints no longer commit any side effects. See [Triggering savepoints](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#triggering-savepoints).

In enhanced snapshot mode, system snapshots have the following properties:
+ Each system snapshot is an enhanced snapshot with its own ARN.
+ Managed Service for Apache Flink names each system snapshot `SYSTEMSNAPSHOT-{{OPERATION}}-{{ApplicationName}}-{{Timestamp}}`. The timestamp is the creation time in milliseconds since the Unix epoch.
+ To list system snapshots, call [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) with `SnapshotInitiator` set to `SYSTEM`.

For application snapshots (legacy), system snapshots have the following properties:
+ Managed Service for Apache Flink manages the system snapshot. To see the system snapshot, use the [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html) action. System snapshots count against your snapshot limit.
+ If your application reaches the snapshot limit, the snapshots that you create fail. Managed Service for Apache Flink still creates system snapshots when you update, scale, or stop the application.

  To create more snapshots, first delete snapshots with the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action.

## Restore from a snapshot that contains incompatible state data
<a name="how-fault-snapshot-restore"></a>

A snapshot contains state data for each operator. If an operator changed after the previous application version, a restore of its state data can have unexpected results. An application faults if it restores state data that does not match the current operator. The faulted application stays in the `STARTING` or `UPDATING` status.

The guidance in this section applies to enhanced snapshots and to application snapshots (legacy). The [`ApplicationRestoreConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html) parameter identifies each type differently:
+ To restore from an enhanced snapshot, set `SnapshotArn`.
+ To restore from an application snapshot (legacy), set `SnapshotName`. The examples on this page use this form.

For more information, see [Restore an application from an enhanced snapshot](snapshots-restore.md).

You can restore an application from an enhanced snapshot that a different application created. Before you restore, confirm that the snapshot state is compatible with the operators in the target application. The target application must be in the same account and Region as the enhanced snapshot. For the other conditions, see [Restore to a different application](snapshots-restore.md#snapshots-restore-restore-to-a-different-application).

To restore from a snapshot that contains incompatible state data, set `AllowNonRestoredState` to `true`. Set this parameter of the [`FlinkRunConfiguration`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkRunConfiguration.html) object with the [`UpdateApplication`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) action.

A restore from a snapshot that an earlier application version created has the following results:
+ **Operator added** – The savepoint has no state data for the new operator. The application does not fault, even if `AllowNonRestoredState` is `false`.
+ **Operator deleted** – The savepoint has state data for the deleted operator. The application faults unless `AllowNonRestoredState` is `true`.
+ **Operator modified** – If you make a compatible change to an operator, the application can restore from the snapshot. An example is a change of a parameter type to a compatible type. For more information about restoring from snapshots, see [Savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/) in the Apache Flink Documentation. An application that uses Apache Flink version 1.8 or later might restore from a snapshot with a different schema. An application that uses Apache Flink version 1.6 cannot restore from such a snapshot. For two-phase-commit sinks, we recommend system snapshots instead of snapshots that you create with `CreateApplicationSnapshot` or `CreateSnapshot`.

  For Flink, Managed Service for Apache Flink triggers intermediate savepoints during snapshot creation. For Flink 1.15 onward, intermediate savepoints no longer commit any side effects. See [Triggering Savepoints](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#triggering-savepoints).

To resume an application that is incompatible with the existing savepoint data, we recommend that you skip the restore. Set the `ApplicationRestoreType` parameter of the [`StartApplication`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html) action to `SKIP_RESTORE_FROM_SNAPSHOT`.

For more information about how Apache Flink deals with incompatible state data, see [State Schema Evolution](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/schema_evolution/) in the *Apache Flink Documentation*.

## Review snapshot API examples
<a name="how-fault-snapshot-examples"></a>

Each example in this section shows the request for application snapshots (legacy). Where the API differs, the example also shows the equivalent request for an enhanced snapshot. For more enhanced snapshot examples and their responses, see [Enhanced snapshot API examples](snapshots-api-examples.md).

This section includes example requests for API actions for using snapshots with an application. For information about how to use a JSON file for input for an API action, see [Managed Service for Apache Flink API example code](api-examples.md).

### Enable system snapshots
<a name="how-fault-savepoint-examples-enable"></a>

The following example request for the [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action enables snapshots for an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 1,
   "ApplicationConfigurationUpdate": { 
      "ApplicationSnapshotConfigurationUpdate": { 
         "SnapshotsEnabledUpdate": true
       }
    }
}
```

`SnapshotsEnabledUpdate` turns on system snapshots for the application. The same `ApplicationSnapshotConfigurationUpdate` object also accepts `SnapshotModeUpdate`. To upgrade to enhanced snapshot mode, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

The following example request upgrades the application to enhanced snapshot mode. The request sets `SnapshotModeUpdate` and `SnapshotsEnabledUpdate` together. For the limits on a rollback to application snapshots (legacy), see [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior).

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 1,
   "ApplicationConfigurationUpdate": {
      "ApplicationSnapshotConfigurationUpdate": {
         "SnapshotsEnabledUpdate": true,
         "SnapshotModeUpdate": "ENHANCED_SNAPSHOTS"
      }
   }
}
```

### Create a snapshot
<a name="how-fault-savepoint-examples-create"></a>

The following example request for the [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) action creates a snapshot of the current application state:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyCustomSnapshot"
}
```

For an application in enhanced snapshot mode, use the [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) action. The following example request creates an enhanced snapshot of a running application:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotDescription": "Before code update"
}
```

### List snapshots
<a name="how-fault-snapshot-examples-list"></a>

The following example request for the [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) action lists the first 50 snapshots for the current application state:

```
{
   "ApplicationName": "MyApplication",
   "Limit": 50
}
```

For enhanced snapshots, use the [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) action. The following example request lists the first 50 enhanced snapshots in the account and Region. To list the enhanced snapshots of one application, add the optional `SourceApplicationName` filter.

```
{
   "Limit": 50
}
```

### Describe a snapshot
<a name="how-fault-snapshot-examples-describe"></a>

The following example request for the [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html) action lists details for a specific application snapshot:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyCustomSnapshot"
}
```

For an enhanced snapshot, use the [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) action. The request identifies the enhanced snapshot by name only, because the name is unique in the account and Region:

```
{
   "SnapshotName": "MyApplication-snapshot-1"
}
```

### Delete a snapshot
<a name="how-fault-snapshot-examples-delete"></a>

The following example request for the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action deletes a previously saved snapshot. You can get the `SnapshotCreationTimestamp` value using either [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) or [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html):

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyCustomSnapshot",
   "SnapshotCreationTimestamp": 12345678901.0
}
```

For an enhanced snapshot, use the [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) action. Copy the `SnapshotCreationTimestamp` value from the `DescribeSnapshot` response:

```
{
   "SnapshotName": "MyApplication-snapshot-1",
   "SnapshotCreationTimestamp": 1767225600
}
```

### Restart an application from a specific snapshot
<a name="how-fault-snapshot-examples-load-custom"></a>

The following example request for the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) action starts the application using the saved state from a specific snapshot:

```
{
   "ApplicationName": "MyApplication",
   "RunConfiguration": { 
      "ApplicationRestoreConfiguration": { 
         "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
         "SnapshotName": "MyCustomSnapshot"
      }
   }
}
```

For an application in enhanced snapshot mode, identify the enhanced snapshot with `SnapshotArn`, not `SnapshotName`. The caller needs `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot. For more information, see [Restore an application from an enhanced snapshot](snapshots-restore.md).

```
{
   "ApplicationName": "MyApplication",
   "RunConfiguration": {
      "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
         "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
      }
   }
}
```

### Restart an application from the latest snapshot
<a name="how-fault-snapshot-examples-load-recent"></a>

The following example request for the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) action starts the application using the most recent snapshot:

```
{
   "ApplicationName": "MyApplication",
   "RunConfiguration": { 
      "ApplicationRestoreConfiguration": { 
         "ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"
      }
   }
}
```

The same request works in enhanced snapshot mode. In that mode, Managed Service for Apache Flink restores the newest enhanced snapshot in the `READY` status that the application created. For more information, see [Restore from the latest snapshot](snapshots-restore.md#snapshots-restore-restore-from-the-latest-snapshot).

### Restart an application without a snapshot
<a name="how-fault-snapshot-examples-load-none"></a>

The following example request for the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) action starts the application without loading application state, even if a snapshot is present:

```
{
   "ApplicationName": "MyApplication",
   "RunConfiguration": { 
      "ApplicationRestoreConfiguration": { 
         "ApplicationRestoreType": "SKIP_RESTORE_FROM_SNAPSHOT"
      }
   }
}
```

The same request works in enhanced snapshot mode.