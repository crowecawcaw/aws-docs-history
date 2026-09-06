

# Manage application backups using snapshots
<a name="how-snapshots"></a>

A *snapshot* is the Managed Service for Apache Flink implementation of an Apache Flink *Savepoint*. A snapshot is a user- or service-triggered, created, and managed backup of the application state. For information about Apache Flink Savepoints, see [Savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/) in the Apache Flink Documentation. Using snapshots, you can restart an application from a particular snapshot of the application state.

**Note**  
We recommend that your application create a snapshot several times a day to restart properly with correct state data. The correct frequency for your snapshots depends on your application's business logic. Taking frequent snapshots lets you recover more recent data, but increases cost and requires more system resources.

In Managed Service for Apache Flink, you manage snapshots using the following API actions:
+ [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationSnapshot.html)
+ [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationSnapshot.html)
+ [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplicationSnapshot.html)
+ [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html)

For the per-application limit on the number of snapshots, see [Managed Service for Apache Flink and Studio notebook quota](limits.md). If your application reaches the limit on snapshots, then manually creating a snapshot fails with a `LimitExceededException`. 

Managed Service for Apache Flink never deletes snapshots. You must manually delete your snapshots using the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action.

To load a saved snapshot of application state when starting an application, use the [`ApplicationRestoreConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html) parameter of the [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html) or [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action.

**Topics**
+ [Manage automatic snapshot creation](#how-fault-snapshot-update)
+ [Restore from a snapshot that contains incompatible state data](#how-fault-snapshot-restore)
+ [Review snapshot API examples](#how-fault-snapshot-examples)

## Manage automatic snapshot creation
<a name="how-fault-snapshot-update"></a>

If `SnapshotsEnabled` is set to `true` in the [ ApplicationSnapshotConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.html) for the application, Managed Service for Apache Flink automatically creates and uses snapshots when the application is updated, scaled, or stopped to provide exactly-once processing semantics.

**Note**  
Setting `ApplicationSnapshotConfiguration::SnapshotsEnabled` to `false` will lead to data loss during application updates.

**Note**  
Managed Service for Apache Flink triggers intermediate savepoints during snapshot creation. For Flink version 1.15 or greater, intermediate savepoints no longer commit any side effects. See [Triggering savepoints](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#triggering-savepoints).

Automatically created snapshots have the following qualities:
+ The snapshot is managed by the service, but you can see the snapshot using the [ ListApplicationSnapshots](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplicationSnapshots.html) action. Automatically created snapshots count against your snapshot limit.
+ If your application exceeds the snapshot limit, manually created snapshots will fail, but the Managed Service for Apache Flink service will still successfully create snapshots when the application is updated, scaled, or stopped. You must manually delete snapshots using the [ DeleteApplicationSnapshot](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action before creating more snapshots manually.

## Restore from a snapshot that contains incompatible state data
<a name="how-fault-snapshot-restore"></a>

Because snapshots contain information about operators, restoring state data from a snapshot for an operator that has changed since the previous application version may have unexpected results. An application will fault if it attempts to restore state data from a snapshot that does not correspond to the current operator. The faulted application will be stuck in either the `STOPPING` or `UPDATING` state. 

To allow an application to restore from a snapshot that contains incompatible state data, set the `AllowNonRestoredState` parameter of the [FlinkRunConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkRunConfiguration.html) to `true` using the [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) action.

You will see the following behavior when an application is restored from an obsolete snapshot:
+ **Operator added:** If a new operator is added, the savepoint has no state data for the new operator. No fault will occur, and it is not necessary to set `AllowNonRestoredState`.
+ **Operator deleted:** If an existing operator is deleted, the savepoint has state data for the missing operator. A fault will occur unless `AllowNonRestoredState` is set to `true`.
+ **Operator modified:** If compatible changes are made, such as changing a parameter's type to a compatible type, the application can restore from the obsolete snapshot. For more information about restoring from snapshots, see [Savepoints](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/) in the Apache Flink Documentation. An application that uses Apache Flink version 1.8 or later can possibly be restored from a snapshot with a different schema. An application that uses Apache Flink version 1.6 cannot be restored. For two-phase-commit sinks, we recommend using system snapshot (SwS) instead of user-created snapshot (CreateApplicationSnapshot).

  For Flink, Managed Service for Apache Flink triggers intermediate savepoints during snapshot creation. For Flink 1.15 onward, intermediate savepoints no longer commit any side effects. See [Triggering Savepoints](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/state/savepoints/#triggering-savepoints).

If you need to resume an application that is incompatible with existing savepoint data, we recommend that you skip restoring from the snapshot by setting the `ApplicationRestoreType` parameter of the [StartApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StartApplication.html) action to `SKIP_RESTORE_FROM_SNAPSHOT`.

For more information about how Apache Flink deals with incompatible state data, see [State Schema Evolution](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/schema_evolution/) in the *Apache Flink Documentation*.

## Review snapshot API examples
<a name="how-fault-snapshot-examples"></a>

This section includes example requests for API actions for using snapshots with an application. For information about how to use a JSON file for input for an API action, see [Managed Service for Apache Flink API example code](api-examples.md).

### Enable snapshots for an application
<a name="how-fault-savepoint-examples-enable"></a>

The following example request for the [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action enables snapshots for an application:

```
{
   "ApplicationName": "MyApplication",
   "CurrentApplicationVersionId": 1,
   "ApplicationConfigurationUpdate": { 
      "ApplicationSnapshotConfigurationUpdate": { 
         "SnapshotsEnabledUpdate": "true"
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

### List snapshots for an application
<a name="how-fault-snapshot-examples-list"></a>

The following example request for the [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) action lists the first 50 snapshots for the current application state:

```
{
   "ApplicationName": "MyApplication",
   "Limit": 50
}
```

### List details for an application snapshot
<a name="how-fault-snapshot-examples-describe"></a>

The following example request for the [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html) action lists details for a specific application snapshot:

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyCustomSnapshot"
}
```

### Delete a snapshot
<a name="how-fault-snapshot-examples-delete"></a>

The following example request for the [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) action deletes a previously saved snapshot. You can get the `SnapshotCreationTimestamp` value using either [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) or [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html):

```
{
   "ApplicationName": "MyApplication",
   "SnapshotName": "MyCustomSnapshot",
   "SnapshotCreationTimestamp": 12345678901.0,
}
```

### Restart an application using a named snapshot
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

### Restart an application using the most recent snapshot
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

### Restart an application using no snapshot
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