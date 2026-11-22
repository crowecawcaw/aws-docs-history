

# Restore an application from an enhanced snapshot

This page describes how to start or update an Amazon Managed Service for Apache Flink application from an enhanced snapshot. It also describes how to start an application without state, how to roll back, and how to fix restore errors.

## Restore from a specific snapshot
<a name="snapshots-restore-restore-by-snapshot-arn"></a>

To restore from a specific enhanced snapshot, set the `ApplicationRestoreConfiguration` object in one of these requests:
+ [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html): `RunConfiguration.ApplicationRestoreConfiguration`.
+ [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html): `RunConfigurationUpdate.ApplicationRestoreConfiguration`.

In `ApplicationRestoreConfiguration`, set these members:
+ `ApplicationRestoreType`: `RESTORE_FROM_CUSTOM_SNAPSHOT`. Enhanced snapshots use the same restore type as application snapshots (legacy).
+ `SnapshotArn`: the ARN of the enhanced snapshot.

With `RESTORE_FROM_CUSTOM_SNAPSHOT`, set exactly one of `SnapshotName` or `SnapshotArn`:
+ `SnapshotName`: Identifies an application snapshot (legacy). Use it only for an application that does not use enhanced snapshot mode.
+ `SnapshotArn`: Identifies an enhanced snapshot. Use it only for an application in enhanced snapshot mode.

A request with both members, or with neither member, returns `InvalidArgumentException`.

Before you restore, make sure that these conditions are true:
+ The application uses enhanced snapshot mode.
+ The enhanced snapshot is in the `READY` status.
+ The enhanced snapshot is in the same account and Region as the application.
+ The Apache Flink runtime of the enhanced snapshot is compatible with the runtime of the application. If the runtimes are not compatible, the request returns `InvalidArgumentException`. Managed Service for Apache Flink does not check the runtime for an imported snapshot. If you restore an imported snapshot to an application that uses an older Apache Flink version than the application that created the snapshot, the restore can lose or corrupt application data.
+ For an enhanced snapshot that a customer managed key encrypts, the caller has `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on that key. For more information, see [KMS key permissions](key-management-flink.md#kms-key-permissions).
+ For `UpdateApplication`, the application is `RUNNING`. If the application is in any other status, the `UpdateApplication` request returns `InvalidArgumentException`.

The caller needs these IAM permissions:
+ `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot that the restore uses. IAM denies this action by default, also for enhanced snapshots of the same application.
+ `kinesisanalytics:StartApplication` or `kinesisanalytics:UpdateApplication` on the application ARN.
+ `kinesisanalytics:CreateSystemSnapshot` on the application ARN, if `SnapshotsEnabled` is `true`. For more information, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots).

For a `StartApplication` request, Managed Service for Apache Flink checks the caller's `RestoreFromSnapshot` permission in any application status. For an `UpdateApplication` request, Managed Service for Apache Flink checks this permission only when the application is `RUNNING`.

**To start an application from an enhanced snapshot**

1. Call [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) or [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html). In the response, copy the `SnapshotArn` value of an enhanced snapshot in the `READY` status.

1. Send a `StartApplication` request for your application with the snapshot ARN. If the request fails, see [Troubleshoot restore errors](#snapshots-restore-errors) for the cause and the fix.

   ```json
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

   To send the same request, run the following AWS CLI command:

   ```bash
   PROMPT> aws kinesisanalyticsv2 start-application \
       --application-name MyApplication \
       --run-configuration '{"ApplicationRestoreConfiguration": {"ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT", "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"}}'
   ```

1. Save the `OperationId` value from the response. For an example response, see [Start an application from an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-startapplication).

1. Call [`DescribeApplicationOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationOperation.html) with the `OperationId` value. Repeat the call until the operation completes.

**To update a running application from an enhanced snapshot**

1. Call [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) for your application. In the response, copy the `ApplicationVersionId` value.

1. Send an `UpdateApplication` request for your application. Set `CurrentApplicationVersionId` to the value from the previous step.

   ```json
   {
     "ApplicationName": "MyApplication",
     "CurrentApplicationVersionId": 3,
     "RunConfigurationUpdate": {
       "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
         "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
       }
     }
   }
   ```

   To send the same request, run the following AWS CLI command:

   ```bash
   PROMPT> aws kinesisanalyticsv2 update-application \
       --application-name MyApplication \
       --current-application-version-id 3 \
       --run-configuration-update '{"ApplicationRestoreConfiguration": {"ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT", "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"}}'
   ```

1. Call `DescribeApplicationOperation` with the `OperationId` value from the response. Repeat the call until the operation completes.

## Restore from the latest snapshot
<a name="snapshots-restore-restore-from-the-latest-snapshot"></a>

In enhanced snapshot mode, `RESTORE_FROM_LATEST_SNAPSHOT` restores from the newest enhanced snapshot in the `READY` status. Managed Service for Apache Flink considers the enhanced snapshots that you create and system snapshots alike.

`RESTORE_FROM_LATEST_SNAPSHOT` selects only enhanced snapshots that the same application created. The selection never includes an enhanced snapshot that you imported or that another application created. To restore from one of those enhanced snapshots, use `RESTORE_FROM_CUSTOM_SNAPSHOT` with `SnapshotArn`.

If the application has no enhanced snapshot in the `READY` status, the application starts without state. Managed Service for Apache Flink does not fall back to an application snapshot (legacy).

Right after the upgrade to enhanced snapshot mode, an application has no enhanced snapshot. Before you restart the application, see [Restore from the latest snapshot after the upgrade](snapshots-upgrade.md#snapshots-upgrade-restore-from-latest-after-opt-in).

For `RESTORE_FROM_LATEST_SNAPSHOT`, Managed Service for Apache Flink checks `kinesisanalytics:RestoreFromSnapshot` as follows:
+ `StartApplication`: Managed Service for Apache Flink checks the permission on the selected enhanced snapshot.
+ `UpdateApplication`, `AddApplicationVpcConfiguration`, `DeleteApplicationVpcConfiguration`, `AddApplicationCloudWatchLoggingOption`, and `DeleteApplicationCloudWatchLoggingOption` for a `RUNNING` application: If `SnapshotsEnabled` is `true`, Managed Service for Apache Flink does not check the permission. The application restores from the system snapshot that the request creates. If `SnapshotsEnabled` is `false`, Managed Service for Apache Flink checks the permission on the selected enhanced snapshot. It also checks the permission on an enhanced snapshot of the application in the `CREATING` status, if one exists.
+ `RollbackApplication`: Managed Service for Apache Flink checks the permission on the enhanced snapshot that the rollback selects. For more information, see [Roll back an application](#snapshots-restore-rollback).

A `CreateSnapshot` request can be in progress when you send one of these requests with `SnapshotsEnabled` set to `false`. If that enhanced snapshot becomes `READY` first, the application can restore from it. Scope the `RestoreFromSnapshot` permission to cover both the enhanced snapshot in the `CREATING` status and the newest `READY` enhanced snapshot. These rules apply to the `Resource` element:
+ To cover system snapshots, add `arn:aws:kinesisanalytics:{{region}}:{{account-id}}:snapshot/SYSTEMSNAPSHOT-*` to the `Resource` element of the policy. This pattern matches the system snapshots of every application in the account.
+ To cover the enhanced snapshots that you create, add their ARNs or an ARN name pattern to the `Resource` element.

The following example request starts an application from the latest enhanced snapshot.

```json
{
  "ApplicationName": "MyApplication",
  "RunConfiguration": {
    "ApplicationRestoreConfiguration": {
      "ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"
    }
  }
}
```

To send the same request, run the following AWS CLI command:

```bash
PROMPT> aws kinesisanalyticsv2 start-application \
    --application-name MyApplication \
    --run-configuration '{"ApplicationRestoreConfiguration": {"ApplicationRestoreType": "RESTORE_FROM_LATEST_SNAPSHOT"}}'
```

## Restore to a different application
<a name="snapshots-restore-restore-to-a-different-application"></a>

An enhanced snapshot belongs to the account, not to the application that created it. You can restore an enhanced snapshot into a different application in the same account and Region. Use cases include blue/green deployments, A/B tests, and recovery.

These limits apply:
+ You can restore only from an enhanced snapshot that your account owns.
+ You can restore only from an enhanced snapshot in the same Region as the target application.

The caller needs `kinesisanalytics:RestoreFromSnapshot` on the snapshot ARN and `kinesisanalytics:StartApplication` on the target application.

The target application can have `SnapshotsEnabled` set to `true`. In that case, the caller also needs `kinesisanalytics:CreateSystemSnapshot` on the target application. Without this action, the request returns `AccessDeniedException`. The following example policy allows the caller to start `MyApplication2` from `MyApplication-snapshot-1`.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kinesisanalytics:StartApplication",
        "kinesisanalytics:CreateSystemSnapshot"
      ],
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication2"
    },
    {
      "Effect": "Allow",
      "Action": "kinesisanalytics:RestoreFromSnapshot",
      "Resource": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
    }
  ]
}
```

**Customer managed keys** – The target application can use a different key than the enhanced snapshot. The restore uses the key that encrypts the enhanced snapshot.

The caller needs `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey` on that key. Without these permissions, the restore returns `AccessDeniedException`.

When you restore an enhanced snapshot, the key policy must allow two ARNs for both `kms:EncryptionContext:aws:kinesisanalytics:arn` and `aws:SourceArn`:
+ The ARN of the application that restores the enhanced snapshot.
+ The source ARN of the enhanced snapshot. For an enhanced snapshot that an application created, this is the ARN of that application. For an imported snapshot, this is the snapshot ARN.

When an application restores its own enhanced snapshot, the two ARNs are the same.

The source ARN allows only reads of the enhanced snapshot. Managed Service for Apache Flink encrypts new savepoints of the application with the ARN of the restoring application as the encryption context.

Keep the source application ARN in the key policy after you delete the source application. Without that ARN, you cannot restore its enhanced snapshots that the key encrypts. For more information about key management, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md).

The target application must be able to read the state in the enhanced snapshot. The Flink operator IDs (UIDs) of the target application must match the UIDs of the source application. For more information about restores with matching UIDs, see [Restore from a snapshot that contains incompatible state data](how-snapshots.md#how-fault-snapshot-restore).

**To start a different application from an enhanced snapshot**

1. Call `DescribeSnapshot` for the source snapshot. Confirm that `SnapshotStatus` is `READY`, and copy the `SnapshotArn` value.

1. Send a `StartApplication` request for the target application with the snapshot ARN.

   ```json
   {
     "ApplicationName": "MyApplication2",
     "RunConfiguration": {
       "ApplicationRestoreConfiguration": {
         "ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT",
         "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
       }
     }
   }
   ```

   To send the same request, run the following AWS CLI command:

   ```bash
   PROMPT> aws kinesisanalyticsv2 start-application \
       --application-name MyApplication2 \
       --run-configuration '{"ApplicationRestoreConfiguration": {"ApplicationRestoreType": "RESTORE_FROM_CUSTOM_SNAPSHOT", "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"}}'
   ```

## Start without restoring a snapshot
<a name="snapshots-restore-skip-restore"></a>

To start an application without state, set `ApplicationRestoreType` to `SKIP_RESTORE_FROM_SNAPSHOT`. With this value, Managed Service for Apache Flink does not check `kinesisanalytics:RestoreFromSnapshot`.

```json
{
  "ApplicationName": "MyApplication",
  "RunConfiguration": {
    "ApplicationRestoreConfiguration": {
      "ApplicationRestoreType": "SKIP_RESTORE_FROM_SNAPSHOT"
    }
  }
}
```

To send the same request, run the following AWS CLI command:

```bash
PROMPT> aws kinesisanalyticsv2 start-application \
    --application-name MyApplication \
    --run-configuration '{"ApplicationRestoreConfiguration": {"ApplicationRestoreType": "SKIP_RESTORE_FROM_SNAPSHOT"}}'
```

## Roll back an application
<a name="snapshots-restore-rollback"></a>

In enhanced snapshot mode, [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) restores from an enhanced snapshot of the application. The selection depends on the application status:
+ `RUNNING`: Managed Service for Apache Flink selects the newest `READY` enhanced snapshot with an `ApplicationVersionId` that is less than or equal to the `ApplicationVersionUpdatedFrom` value of the application.
+ `UPDATING` or `AUTOSCALING`: Managed Service for Apache Flink selects the newest `READY` enhanced snapshot.

If no enhanced snapshot meets the condition, the rollback fails with `InvalidRequestException`. Managed Service for Apache Flink does not fall back to a start without state.

The caller needs these IAM permissions:
+ `kinesisanalytics:RollbackApplication` on the application ARN.
+ `kinesisanalytics:RestoreFromSnapshot` on the snapshot that Managed Service for Apache Flink selects. If IAM denies this action, the `AccessDeniedException` message includes the ARN of the selected snapshot.

You cannot name the selected snapshot ARN in a policy, because each new snapshot can become the selected snapshot. To limit `RestoreFromSnapshot`, we recommend an `aws:ResourceTag` condition. A snapshot name prefix with a wildcard in the resource ARN also works.

A rollback fails if you deleted every snapshot that meets the conditions. Keep at least one `READY` enhanced snapshot from each application version that you want to roll back to.

A rollback to the version before the upgrade returns the application to application snapshots (legacy). Managed Service for Apache Flink restores the newest `READY` application snapshot (legacy) at or below that version. For more information about rollbacks across the upgrade, see [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior).

**To roll back an application**

1. Call `DescribeApplication` for your application. In the response, copy the `ApplicationVersionId` value.

1. Send a `RollbackApplication` request for your application. Set `CurrentApplicationVersionId` to the value from the previous step.

   ```json
   { "ApplicationName": "MyApplication", "CurrentApplicationVersionId": 4 }
   ```

   To send the same request, run the following AWS CLI command:

   ```bash
   PROMPT> aws kinesisanalyticsv2 rollback-application \
       --application-name MyApplication \
       --current-application-version-id 4
   ```

1. Call `DescribeApplicationOperation` with the `OperationId` value from the response. Repeat the call until the operation completes.

## Troubleshoot restore errors
<a name="snapshots-restore-errors"></a>

The following table lists the causes of restore errors from an enhanced snapshot, the exception that `StartApplication`, `UpdateApplication`, or `RollbackApplication` returns, and the fix.


| Cause | Exception | Fix | 
| --- | --- | --- | 
| The application does not use enhanced snapshot mode, and the request sets SnapshotArn. | InvalidApplicationConfigurationException | Upgrade the application to enhanced snapshot mode, or use SnapshotName with an application snapshot (legacy). | 
| The application uses enhanced snapshot mode, and the request sets SnapshotName. | InvalidApplicationConfigurationException | Use SnapshotArn with an enhanced snapshot. | 
| With RESTORE\_FROM\_CUSTOM\_SNAPSHOT, the request sets both SnapshotName and SnapshotArn, or neither. | InvalidArgumentException | Set exactly one of the two members. | 
| An UpdateApplication request has a restore configuration, and the application is not RUNNING. | InvalidArgumentException | Use StartApplication with the restore configuration. | 
| The application uses enhanced snapshot mode, and a StartApplication or UpdateApplication request sets SnapshotArn. Enhanced snapshots are not available for your account in the Region of the request. | UnsupportedOperationException | Contact AWS Support. | 
| The Apache Flink runtime of the enhanced snapshot is not compatible with the runtime of the application. Managed Service for Apache Flink does not check the runtime for an imported snapshot. | InvalidArgumentException | Restore from an enhanced snapshot with a compatible runtime. | 
| No enhanced snapshot with this ARN exists in the account and Region. | ResourceNotFoundException | Check the ARN with ListSnapshots. | 
| The enhanced snapshot is not in the READY status. | ResourceInUseException | Wait until the enhanced snapshot is READY, or choose a different enhanced snapshot. | 
| The enhanced snapshot uses a customer managed key, and the caller does not have kms:DescribeKey, kms:Decrypt, or kms:GenerateDataKey on that key. | AccessDeniedException | Grant these permissions on the key that encrypts the enhanced snapshot. | 
| The caller does not have kinesisanalytics:RestoreFromSnapshot on the enhanced snapshot. For a rollback, the message includes the ARN of the selected snapshot. | AccessDeniedException | Grant RestoreFromSnapshot on the snapshot ARN. | 
| SnapshotsEnabled is true, and the caller does not have kinesisanalytics:CreateSystemSnapshot on the application. | AccessDeniedException | Grant CreateSystemSnapshot on the application ARN. | 
| RollbackApplication found no enhanced snapshot that meets the selection rule. For more information about the selection rule, see [Roll back an application](#snapshots-restore-rollback). | InvalidRequestException | Restore from a specific enhanced snapshot with RESTORE\_FROM\_CUSTOM\_SNAPSHOT. | 