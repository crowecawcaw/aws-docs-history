

# Application issues
<a name="troubleshooting-symptoms"></a>

This section contains solutions for error conditions that you may encounter with your Managed Service for Apache Flink application.

**Topics**
+ [Application is stuck in a transient status](#troubleshooting-rt-stuck)
+ [Snapshot creation fails](#troubleshooting-rt-snapshots)
+ [Cannot access resources in a VPC](#troubleshooting-rt-vpc)
+ [Data is lost when writing to an Amazon S3 bucket](#troubleshooting-rt-s3)
+ [Application is in the RUNNING status but isn't processing data](#troubleshooting-rt-processing)
+ [Snapshot, application update, or application stop error: InvalidApplicationConfigurationException](#troubleshooting-rt-appconfigexception)
+ [Upgrade to enhanced snapshot mode fails](#troubleshooting-rt-opt-in)
+ [Restore from an enhanced snapshot fails](#troubleshooting-rt-restore-enhanced)
+ [Import or export of an enhanced snapshot fails](#troubleshooting-rt-import-export)
+ [Import fails with a checksum error](#troubleshooting-rt-import-checksum)
+ [`DeleteSnapshot` fails](#troubleshooting-rt-delete-snapshot)
+ [java.nio.file.NoSuchFileException: /usr/local/openjdk-8/lib/security/cacerts](#troubleshooting-rt-fnf)

## Application is stuck in a transient status
<a name="troubleshooting-rt-stuck"></a>

If your application stays in a transient status (`STARTING`, `UPDATING`, `STOPPING`, or `AUTOSCALING`), you can stop your application by using the [StopApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_StopApplication.html) action with the `Force` parameter set to `true`. You can't force stop an application in the `DELETING` status. Alternatively, if the application is in the `UPDATING` or `AUTOSCALING` status, you can roll it back to the previous running version. When you roll back an application, it loads state data from the last successful snapshot. If the application has no snapshots, Managed Service for Apache Flink rejects the rollback request. For more information about rolling back an application, see [RollbackApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RollbackApplication.html) action.

In enhanced snapshot mode, a rollback from the `UPDATING` or `AUTOSCALING` status restores the newest `READY` enhanced snapshot of the application. If the application has no `READY` enhanced snapshot, the rollback fails with `InvalidRequestException`. For more information, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).

**Note**  
Force-stopping your application may lead to data loss or duplication. To prevent data loss or duplicate processing of data during application restarts, we recommend you to take frequent snapshots of your application.

**Upgrade to enhanced snapshot mode:** To upgrade a running application, you send an [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) request with `SnapshotModeUpdate` set to `ENHANCED_SNAPSHOTS`. The request must also include `SnapshotsEnabledUpdate`, even when you change only the mode. The application status is `UPDATING` until the upgrade completes. To track the upgrade, call [`DescribeApplicationOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationOperation.html) with the `OperationId` from the response. For an application in the `READY` status, the upgrade takes effect at once. The status stays `READY`. The response has no `OperationId`. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

Causes for stuck applications include the following:
+ **Application state is too large:** Having an application state that is too large or too persistent can cause the application to become stuck during a checkpoint or snapshot operation. Check your application's `lastCheckpointDuration` and `lastCheckpointSize` metrics for steadily increasing values or abnormally high values.
+ **Application code is too large:** Verify that your application JAR file is smaller than 512 MB. JAR files larger than 512 MB are not supported.
+ **Application snapshot creation fails:** Managed Service for Apache Flink takes a system snapshot of the application during an [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) or [`StopApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StopApplication.html) request. A system snapshot is a snapshot that Managed Service for Apache Flink creates for you. In enhanced snapshot mode, each system snapshot is an enhanced snapshot. With application snapshots (legacy), each system snapshot is an application snapshot (legacy). The service then uses this system snapshot and restores the application using the updated application configuration to provide *exactly-once* processing semantics. In enhanced snapshot mode, Managed Service for Apache Flink also takes a system snapshot when you add or delete a Amazon VPC configuration or a CloudWatch logging option. For more information, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots). If automatic snapshot creation fails, see [Snapshot creation fails](#troubleshooting-rt-snapshots) following.
+ **Restoring from a snapshot fails:** If you remove or change an operator in an application update and attempt to restore from a snapshot, the restore will fail by default if the snapshot contains state data for the missing operator. In addition, the application will be stuck in either the `STARTING` or `UPDATING` status. To change this behavior and allow the restore to succeed, change the `AllowNonRestoredState` parameter of the application's [`FlinkRunConfiguration`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_FlinkRunConfiguration.html) to `true`. With this setting, the restore skips state data that Apache Flink cannot map to the new program.
+ **Application initialization taking longer:** Managed Service for Apache Flink uses an internal timeout of 5 minutes (soft setting) while waiting for a Flink job to start. If your job is failing to start within this timeout, you will see a CloudWatch log as follows:

  ```
  Flink job did not start within a total timeout of 5 minutes for application: %s under account: %s
  ```

   If you encounter the above error, it means that your operations defined under Flink job’s `main` method are taking more than 5 minutes, causing the Flink job creation to time out on the Managed Service for Apache Flink end. We suggest you check the Flink **JobManager** logs as well as your application code to see if this delay in the `main` method is expected. If not, you need to take steps to address the issue so it completes in under 5 minutes. 

You can check your application status using either the [`ListApplications`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplications.html) or the [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) actions.

## Snapshot creation fails
<a name="troubleshooting-rt-snapshots"></a>

The Managed Service for Apache Flink service can't take a snapshot under the following circumstances:
+ The application reached its snapshot quota. For more information, see [Manage application backups using snapshots](how-snapshots.md).
+ The application doesn't have permissions to access its source or sink.
+ The application code isn't functioning properly.
+ The application is experiencing other configuration issues.

If you get an exception while taking a snapshot during an application update or while stopping the application, set the `SnapshotsEnabled` property of your application's [`ApplicationSnapshotConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.html) to `false` and retry the request. 

Snapshots can fail if your application's operators are not properly provisioned. For information about tuning operator performance, see [Operator scaling](performance-improving.md#performance-improving-scaling-op).

After the application returns to a healthy state, we recommend that you set the application's `SnapshotsEnabled` property to `true`.

**Enhanced snapshots:** A [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) call returns before Managed Service for Apache Flink captures the state. If the capture fails later, the enhanced snapshot status changes to `FAILED`. To find the cause, call [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) with the snapshot name and the `SnapshotOperationId` from the `CreateSnapshot` response. Then read `SnapshotOperationFailureDetails.ErrorInfo.ErrorCode`. The following table lists the values.


| `ErrorCode` | Cause and fix | 
| --- | --- | 
| ApplicationStateCaptureFailed | The Apache Flink job did not complete the savepoint. If logging is enabled, check the CloudWatch logs of the application. Then retry the request. | 
| ApplicationStateCaptureTimedOut | The savepoint timed out. If logging is enabled, check the CloudWatch logs of the application for slow or blocked operators. Then retry the request. | 
| KMSAccessDenied | The key policy of the application key does not allow Managed Service for Apache Flink to use the key. Update the key policy, then retry the request. | 

If the operation status is `CANCELLED`, the response has no `ErrorCode`. Retry the request after the application is `RUNNING` and no other application operation is in progress.

For more information, see [Failure reasons](snapshots-monitor-operations.md#snapshots-monitor-operations-failure-reasons). For the exceptions that `CreateSnapshot` returns, see [Troubleshoot snapshot API errors](snapshots-manage.md#snapshots-manage-errors).

## Cannot access resources in a VPC
<a name="troubleshooting-rt-vpc"></a>

If your application uses a VPC running on Amazon VPC, do the following to verify that your application has access to its resources:
+ Check your CloudWatch logs for the following error. This error indicates that your application cannot access resources in your VPC:

  ```
  org.apache.kafka.common.errors.TimeoutException: Failed to update metadata after 60000 ms.
  ```

  If you see this error, verify that your route tables are set up correctly, and that your connectors have the correct connection settings.

  For information about setting up and analyzing CloudWatch logs, see [Logging and monitoring in Amazon Managed Service for Apache Flink](monitoring-overview.md).

## Data is lost when writing to an Amazon S3 bucket
<a name="troubleshooting-rt-s3"></a>

Some data loss might occur when writing output to an Amazon S3 bucket using Apache Flink version 1.6.2. We recommend using the latest supported version of Apache Flink when using Amazon S3 for output directly. To write to an Amazon S3 bucket using Apache Flink 1.6.2, we recommend using Firehose. For more information about using Firehose with Managed Service for Apache Flink, see [Firehose sink](earlier.md#get-started-exercise-fh).

## Application is in the RUNNING status but isn't processing data
<a name="troubleshooting-rt-processing"></a>

You can check your application status by using either the [`ListApplications`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplications.html) or the [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) actions. If your application enters the `RUNNING` status but isn't writing data to your sink, you can troubleshoot the issue by adding an Amazon CloudWatch log stream to your application. For more information, see [Work with application CloudWatch logging options](cloudwatch-logs.md#adding_cloudwatch). The log stream contains messages that you can use to troubleshoot application issues.

## Snapshot, application update, or application stop error: InvalidApplicationConfigurationException
<a name="troubleshooting-rt-appconfigexception"></a>

An error similar to the following might occur during a snapshot operation, or during an operation that creates a snapshot, such as updating or stopping an application:

```
An error occurred (InvalidApplicationConfigurationException) when calling the UpdateApplication operation: 

Failed to take snapshot for the application xxxx at this moment. The application is currently experiencing downtime. 
Please check the application's CloudWatch metrics or CloudWatch logs for any possible errors and retry the request. 
You can also retry the request after disabling the snapshots in the Managed Service for Apache Flink console or by updating 
the ApplicationSnapshotConfiguration through the AWS SDK
```

This error occurs when the application is unable to create a snapshot. 

If you encounter this error during a snapshot operation or an operation that creates a snapshot, do the following:
+ Disable snapshots for your application. You can do this either in the Managed Service for Apache Flink console, or by using the `SnapshotsEnabledUpdate` parameter of the [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) action.
+ Investigate why snapshots cannot be created. For more information, see [Application is stuck in a transient status](#troubleshooting-rt-stuck).
+ Reenable snapshots when the application returns to a healthy state.

**Enhanced snapshot mode:** Managed Service for Apache Flink also returns `InvalidApplicationConfigurationException` when a request uses a snapshot type that does not match the `SnapshotMode` value of the application. The following table lists these causes.


| Cause | Fix | 
| --- | --- | 
| A request to upgrade to enhanced snapshot mode restores from an application snapshot (legacy) by SnapshotName. | Remove the restore configuration from the request. | 
| The application uses enhanced snapshot mode, and a restore request sets SnapshotName. | Set SnapshotArn to the ARN of an enhanced snapshot. | 
| The application does not use enhanced snapshot mode, and a restore request sets SnapshotArn. | Upgrade the application to enhanced snapshot mode, or use SnapshotName with an application snapshot (legacy). | 
| The application uses enhanced snapshot mode, and the request calls CreateApplicationSnapshot. | Call CreateSnapshot instead. | 

For more information, see [Errors during the upgrade](snapshots-upgrade.md#snapshots-upgrade-opt-in-behavior) and [Troubleshoot restore errors](snapshots-restore.md#snapshots-restore-errors).

## Upgrade to enhanced snapshot mode fails
<a name="troubleshooting-rt-opt-in"></a>

An upgrade request can fail in two ways. Managed Service for Apache Flink can reject the request, or the upgrade operation can fail after Managed Service for Apache Flink accepts the request.

**Rejected request:** The application does not change. The following table lists the common causes.


| Exception | Cause | Fix | 
| --- | --- | --- | 
| InvalidArgumentException | The application uses Apache Flink 1.19 or earlier, or a runtime other than Apache Flink. | Upgrade the application to Apache Flink 1.20 or later in a separate request. Then upgrade to enhanced snapshot mode. | 
| InvalidArgumentException | The request includes a restore configuration, and the application is not RUNNING. | Remove the restore configuration. | 
| InvalidArgumentException | The request sets SnapshotModeUpdate to APPLICATION\_SNAPSHOTS\_LEGACY for an application in enhanced snapshot mode. | You cannot reverse the upgrade with UpdateApplication. To return to application snapshots (legacy), roll back to the application version before the upgrade. For more information, see [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior). | 
| AccessDeniedException | The caller lacks a required permission, such as kinesisanalytics:CreateSystemSnapshot. | Grant the caller the permission on the application ARN. | 
| ConcurrentModificationException | CurrentApplicationVersionId or ConditionalToken does not match the current application. | Call DescribeApplication, and then send the request with the current version ID. | 
| UnsupportedOperationException | Enhanced snapshots are not available for your account in the Region of the request. | Contact AWS Support. | 

**Failed upgrade operation:** The operation status is `FAILED`. The result depends on the system rollback setting of the application:
+ System rollbacks turned on: Managed Service for Apache Flink returns the application to the `RUNNING` status on the version before the upgrade. The application no longer uses enhanced snapshot mode.
+ System rollbacks turned off: The application stays in the `READY` status. `SnapshotMode` stays `ENHANCED_SNAPSHOTS`. To keep the state, call [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) to return to the version before the upgrade.

**Note**  
After a failed upgrade with system rollbacks turned off, do not start the application with `RESTORE_FROM_LATEST_SNAPSHOT`. The application has no enhanced snapshot, so the application starts without state.

For more information, see [Errors during the upgrade](snapshots-upgrade.md#snapshots-upgrade-opt-in-behavior) and [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior).

## Restore from an enhanced snapshot fails
<a name="troubleshooting-rt-restore-enhanced"></a>

A `StartApplication`, `UpdateApplication`, or `RollbackApplication` request that restores from an enhanced snapshot can return the errors in the following table.


| Exception | Cause | Fix | 
| --- | --- | --- | 
| ResourceInUseException | The enhanced snapshot is not in the READY status. | Wait until the enhanced snapshot is READY, or choose a different enhanced snapshot. | 
| ResourceNotFoundException | No enhanced snapshot with this ARN exists in the account and Region. | Check the ARN with ListSnapshots. | 
| InvalidArgumentException | With RESTORE\_FROM\_CUSTOM\_SNAPSHOT, the request sets both SnapshotName and SnapshotArn, or neither. | Set exactly one of the two members. | 
| InvalidArgumentException | An UpdateApplication request has a restore configuration, and the application is not RUNNING. | Use StartApplication with the restore configuration. | 
| AccessDeniedException | The caller lacks a required permission. The missing permission can be one of the following: kinesisanalytics:RestoreFromSnapshot on the enhanced snapshot, kinesisanalytics:CreateSystemSnapshot on the application, or kms:Decrypt on the AWS KMS key of the enhanced snapshot. | Grant the caller the missing permission. | 
| InvalidRequestException | RollbackApplication found no enhanced snapshot that meets the selection rule. For more information, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback). | Restore from a specific enhanced snapshot with RESTORE\_FROM\_CUSTOM\_SNAPSHOT. | 

A restore can also fail if the Apache Flink operator IDs (UIDs) of the application do not match the enhanced snapshot. For more information, see [Restore to a different application](snapshots-restore.md#snapshots-restore-restore-to-a-different-application).

For the full list of errors, see [Troubleshoot restore errors](snapshots-restore.md#snapshots-restore-errors).

## Import or export of an enhanced snapshot fails
<a name="troubleshooting-rt-import-export"></a>

An [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) or [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) request can fail in two ways:
+ **Rejected request:** The call returns an exception. For the exceptions and their fixes, see [Troubleshoot import and export errors](snapshots-import-export.md#snapshots-import-export-troubleshoot).
+ **Failed operation:** The snapshot operation status changes to `FAILED`. Call `DescribeSnapshotOperation`, and read `SnapshotOperationFailureDetails.ErrorInfo.ErrorCode`. For each `ErrorCode` value and its fix, see [Failure reasons](snapshots-monitor-operations.md#snapshots-monitor-operations-failure-reasons).

A failed import leaves the enhanced snapshot in the `FAILED` status. To import again with the same name, first delete the failed enhanced snapshot. A failed export leaves the enhanced snapshot in the `READY` status. You can call `ExportSnapshot` again.

## Import fails with a checksum error
<a name="troubleshooting-rt-import-checksum"></a>

An import operation fails with the `MissingObjectChecksum` error code if a source object has no full-object checksum. Every source object needs an Amazon S3 full-object checksum that uses the CRC64NVME algorithm.

To fix the error, upload each source object again with a full-object CRC64NVME checksum. Then delete the failed enhanced snapshot, and import again. Files that `ExportSnapshot` writes already have this checksum. For more information, see [Import an enhanced snapshot from Amazon S3](snapshots-import-export.md#snapshots-import-export-import-a-snapshot-from-amazon-s3).

## `DeleteSnapshot` fails
<a name="troubleshooting-rt-delete-snapshot"></a>

[`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) returns `ResourceInUseException` when the enhanced snapshot is not in the `READY` or `FAILED` status. For example, an imported enhanced snapshot is `CREATING` until the import completes.

Wait until the enhanced snapshot is `READY` or `FAILED`, and then send the request again. If an operation such as an export uses the enhanced snapshot, Managed Service for Apache Flink accepts the delete and waits for that operation to finish.

Managed Service for Apache Flink does not protect an enhanced snapshot that an application uses. A running application does not block the delete. A restore configuration that names the enhanced snapshot also does not block the delete. After the delete, a later restore or rollback cannot use the enhanced snapshot.

For more information, see [Delete a snapshot while an operation uses it](snapshots-manage.md#snapshots-manage-delete-protection-for-snapshots-in-use).

## java.nio.file.NoSuchFileException: /usr/local/openjdk-8/lib/security/cacerts
<a name="troubleshooting-rt-fnf"></a>

The location of the SSL truststore was updated in a previous deployment. Use the following value for the `ssl.truststore.location` parameter instead:

```
/usr/lib/jvm/java-11-amazon-corretto/lib/security/cacerts
```