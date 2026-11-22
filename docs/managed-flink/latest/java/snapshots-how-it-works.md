

# How enhanced snapshots work

This page explains how enhanced snapshots work in Amazon Managed Service for Apache Flink. Read it before you upgrade an application to enhanced snapshot mode.

**Note**  
Enhanced snapshots aren't available in the AWS Top Secret Cloud Regions or the AWS European Sovereign Cloud at this time.

## Enhanced snapshots as standalone resources
<a name="snapshots-how-it-works-snapshots-as-standalone-resources"></a>

An enhanced snapshot is an Apache Flink savepoint that Managed Service for Apache Flink stores as a standalone AWS resource. Each enhanced snapshot has its own ARN, lifecycle, tags, and IAM permissions.

Your account owns the enhanced snapshot, not the application. The ARN uses the resource type `snapshot`. The ARN does not contain the application name.

The ARN has the following format:

```
arn:{{partition}}:kinesisanalytics:{{region}}:{{account-id}}:snapshot/{{snapshot-name}}
```

The following example shows the ARN of an enhanced snapshot:

```
arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1
```

Each enhanced snapshot name is unique in your account and Region. A name has 1 to 100 characters. Valid characters are letters, digits, underscores (`_`), periods (`.`), and hyphens (`-`).

The following rules apply to name reservation:
+ A name stays reserved in every status, including `FAILED`, until you delete the enhanced snapshot.
+ A create or import request that uses a reserved name returns `ResourceInUseException`.
+ The prefix `SYSTEMSNAPSHOT` is reserved for system snapshots, in any combination of uppercase and lowercase letters. A create or import request with a name that starts with this prefix returns `InvalidArgumentException`.

The following rules apply when you reuse a name:
+ After a delete completes, you can reuse the name for a new enhanced snapshot. The new enhanced snapshot contains none of the state of the deleted snapshot.
+ A new enhanced snapshot with a reused name has the same ARN as the deleted enhanced snapshot. An IAM policy that names that ARN applies to the new enhanced snapshot.
+ The tags of the deleted enhanced snapshot do not carry over to the new enhanced snapshot.
+ For a reused name, `ListSnapshotOperations` returns only the operations of the new enhanced snapshot.
+ A `DeleteSnapshot` request must set `SnapshotCreationTimestamp`. Use the creation time of the enhanced snapshot that you want to delete. If the value does not match, `DeleteSnapshot` returns `InvalidArgumentException`.

You can restore an enhanced snapshot into a different application in the same account and Region. Use this capability for blue/green deployments, A/B tests, and recovery. In a blue/green deployment, you run a new application next to the current application and then move traffic to the new application. For more information, see [Restore an application from an enhanced snapshot](snapshots-restore.md).

Enhanced snapshots require Apache Flink version 1.20 or later. For more information, see [Prerequisites](snapshots-setup.md#snapshots-setup-prerequisites).

Each enhanced snapshot belongs to one Region and one partition. At this time, Managed Service for Apache Flink does not support enhanced snapshot operations across Regions or partitions.

## Snapshot lifecycle
<a name="snapshots-how-it-works-snapshot-lifecycle"></a>

The lifecycle of an enhanced snapshot does not depend on the application that created it. The enhanced snapshot remains after you stop, update, or delete that application.

After you delete an application, its enhanced snapshots remain, including its system snapshots. To remove them, call [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) for each enhanced snapshot.

Managed Service for Apache Flink does not expire or delete enhanced snapshots on a schedule. To manage retention, call [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html). For more information, see [Create and manage enhanced snapshots](snapshots-manage.md).

When you close your AWS account, Managed Service for Apache Flink deletes your enhanced snapshots and your applications.

**Note**  
To restore or export an enhanced snapshot that a customer managed key encrypts, the key policy must have the ARN of the application that created the enhanced snapshot. This rule applies after you delete that application. For more information about key policies, see [Key management in Amazon Managed Service for Apache Flink](key-management-flink.md).

## Snapshot modes
<a name="snapshots-how-it-works-snapshot-mode"></a>

The `SnapshotMode` setting of an application controls which type of snapshot the application uses. An application uses exactly one mode at a time.

`SnapshotMode` has the following values:
+ `APPLICATION_SNAPSHOTS_LEGACY`: The application uses application snapshots (legacy).
+ `ENHANCED_SNAPSHOTS`: The application uses enhanced snapshots.

The default value is `APPLICATION_SNAPSHOTS_LEGACY`.

Managed Service for Apache Flink does not put new applications in enhanced snapshot mode automatically. To use enhanced snapshot mode, set `SnapshotMode` yourself. An application with no stored mode reports `APPLICATION_SNAPSHOTS_LEGACY`.

You set the mode in the following request members:
+ [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html): `ApplicationConfiguration.ApplicationSnapshotConfiguration.SnapshotMode`. For more information, see [Set up enhanced snapshots](snapshots-setup.md).
+ [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html): `ApplicationConfigurationUpdate.ApplicationSnapshotConfigurationUpdate.SnapshotModeUpdate`. For more information, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

To see the mode, call [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html). The response shows the mode in `ApplicationDetail.ApplicationConfigurationDescription.ApplicationSnapshotConfigurationDescription.SnapshotMode`. The following example shows that part of the response:

```json
{
    "ApplicationDetail": {
        "ApplicationConfigurationDescription": {
            "ApplicationSnapshotConfigurationDescription": {
                "SnapshotsEnabled": true,
                "SnapshotMode": "ENHANCED_SNAPSHOTS"
            }
        }
    }
}
```

`SnapshotsEnabled` keeps its existing meaning in enhanced snapshot mode. The setting turns system snapshots on or off. If `SnapshotsEnabled` is `false`, you can still call [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html).

## System snapshots
<a name="snapshots-how-it-works-system-snapshots"></a>

In enhanced snapshot mode, a system snapshot is an enhanced snapshot that Managed Service for Apache Flink creates for you. If `SnapshotsEnabled` is `true`, Managed Service for Apache Flink creates a system snapshot for the following operations:
+ You stop a `RUNNING` application with [`StopApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StopApplication.html). A stop with `Force` set to `true` does not create a system snapshot.
+ You update the application with [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html).
+ For a `RUNNING` application, you add or delete a VPC configuration or a CloudWatch logging option.

The `kinesisanalytics:CreateSystemSnapshot` permission applies only when both of the following are true:
+ The application is in enhanced snapshot mode.
+ `SnapshotsEnabled` is `true`.

In that case, the principal that calls the following API actions needs the `kinesisanalytics:CreateSystemSnapshot` permission on the application ARN:
+ [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html): In any application status.
+ [`StopApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StopApplication.html): Only when the application is `RUNNING`. A `StopApplication` request with `Force` set to `true` does not need the permission.
+ [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html): Only when the application is `RUNNING`. If the request includes `SnapshotModeUpdate` or `SnapshotsEnabledUpdate`, Managed Service for Apache Flink uses those new values to decide whether the permission applies.
+ [`AddApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html): Only when the application is `RUNNING`.
+ [`DeleteApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html): Only when the application is `RUNNING`.
+ [`AddApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html): Only when the application is `RUNNING`.
+ [`DeleteApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html): Only when the application is `RUNNING`.

[`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) and [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) do not check the `kinesisanalytics:CreateSystemSnapshot` permission. For an IAM policy that grants the `kinesisanalytics:CreateSystemSnapshot` permission, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

Start, rollback, and delete operations do not create a system snapshot. `StartApplication` still checks the `kinesisanalytics:CreateSystemSnapshot` permission, as the previous list shows.

A system snapshot name has the following format. The timestamp is the creation time in epoch milliseconds, with 13 digits.

```
SYSTEMSNAPSHOT-{{OPERATION}}-{{application-name}}-{{timestamp-ms}}
```

The following example shows the name of a system snapshot from a stop operation:

```
SYSTEMSNAPSHOT-STOP-MyApplication-1767225600000
```

A system snapshot has the following field values:
+ `SnapshotInitiator`: `SYSTEM`
+ `SnapshotInitiatorOperation`: `SystemCreateSnapshot`

Only the name shows which operation created the system snapshot.

To list your system snapshots, call [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) with `SnapshotInitiator` set to `SYSTEM`. Each call accepts at most one filter. For more information, see [Create and manage enhanced snapshots](snapshots-manage.md).

Managed Service for Apache Flink bills the storage of system snapshots at the same rate as other enhanced snapshots. For more information, see [Billing for enhanced snapshots](#snapshots-how-it-works-billing-for-snapshots).

For each system snapshot that succeeds, [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) returns one operation with the status `SUCCESSFUL`. A failed system snapshot has no snapshot operation.

The [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) response for a system snapshot includes `ApplicationOperationDescription`. To get details of the application operation, call the [`DescribeApplicationOperation` action](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationOperation.html) with the `ApplicationOperationId` and `ApplicationName` values from `ApplicationOperationDescription`.

When `StopApplication`, `UpdateApplication`, or a request that adds or deletes a VPC configuration or a CloudWatch logging option creates a system snapshot, the system snapshot inherits the tags of the application. Managed Service for Apache Flink copies the tags before the system snapshot appears in `ListSnapshots`. If the application has no tags, the system snapshot has no tags. To add more tags to a system snapshot, call [`TagResource`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_TagResource.html) with the ARN of the system snapshot.

## Snapshot statuses
<a name="snapshots-how-it-works-snapshot-statuses"></a>

The `SnapshotStatus` field shows the status of an enhanced snapshot. The following table describes each status.


| Status | Meaning | 
| --- | --- | 
| CREATING | Managed Service for Apache Flink is creating or importing the enhanced snapshot. You cannot restore or export the enhanced snapshot yet. | 
| READY | The enhanced snapshot is complete. You can restore, export, or delete it. | 
| DELETING | Managed Service for Apache Flink is deleting the enhanced snapshot. | 
| FAILED | The create or import failed. The enhanced snapshot keeps its name until you delete it. | 

An enhanced snapshot moves between statuses as follows:
+ **Create or import** – The enhanced snapshot starts in `CREATING`. It then moves to `READY` or `FAILED`.
+ **Delete** – A delete moves a `READY` or `FAILED` enhanced snapshot to `DELETING`. Managed Service for Apache Flink then removes the enhanced snapshot.
+ **Export** – An export does not change the status of the enhanced snapshot. Instead, [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) creates a snapshot operation that tracks the export. To follow the export, check the status of that snapshot operation. A failed export leaves the enhanced snapshot in `READY`. For more information, see [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

No `DELETED` status exists. After a delete completes, [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) returns `ResourceNotFoundException`.

The snapshot operation for a `DeleteSnapshot` request never has the status `FAILED`. For the rules that block a delete request, see [Delete an enhanced snapshot](snapshots-manage.md#snapshots-manage-delete-a-snapshot).

## Asynchronous operations
<a name="snapshots-how-it-works-asynchronous-operations"></a>

The following actions run asynchronously: `CreateSnapshot`, `DeleteSnapshot`, [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html), and [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html). Each action returns a response after Managed Service for Apache Flink accepts the request. Managed Service for Apache Flink then completes the work in the background.

Each response includes a `SnapshotOperationId` and a `SnapshotOperationStatus`. The following table shows the members that each response returns.


| Action | Response members | 
| --- | --- | 
| CreateSnapshot | SnapshotArn, SnapshotStatus, SnapshotOperationId, SnapshotOperationStatus | 
| DeleteSnapshot | SnapshotArn, SnapshotStatus, SnapshotOperationId, SnapshotOperationStatus | 
| ImportSnapshot | SnapshotArn, SnapshotStatus, SnapshotOperationId, SnapshotOperationStatus | 
| ExportSnapshot | SnapshotOperationId, SnapshotOperationStatus | 

The following example shows a `CreateSnapshot` response:

```json
{
    "SnapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
    "SnapshotStatus": "CREATING",
    "SnapshotOperationId": "a1B2c3D4e5F6",
    "SnapshotOperationStatus": "IN_PROGRESS"
}
```

An asynchronous action returns an exception only if Managed Service for Apache Flink rejects the request. If the work fails later, the action does not return an exception. Instead, Managed Service for Apache Flink reports the failure on the snapshot operation. For some actions, Managed Service for Apache Flink also changes the enhanced snapshot status to `FAILED`.

The following table shows where a failure appears for each action.


| Action | Enhanced snapshot status after a failure | Snapshot operation after a failure | 
| --- | --- | --- | 
| [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) | Changes to FAILED | FAILED, with SnapshotOperationFailureDetails | 
| [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) | Changes to FAILED | FAILED, with SnapshotOperationFailureDetails | 
| [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) | Stays READY | FAILED, with SnapshotOperationFailureDetails | 

A `FAILED` enhanced snapshot keeps its name until you delete it.

To check the result of an asynchronous action, call `DescribeSnapshotOperation` with the snapshot name and the `SnapshotOperationId`. For more information, see [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

An import or an export runs until it completes.

## Billing and quotas
<a name="snapshots-how-it-works-billing-and-quotas"></a>

This section describes how Managed Service for Apache Flink bills enhanced snapshots. The section also lists the limits on enhanced snapshot operations that run at the same time.

### Limits on operations in progress
<a name="snapshots-how-it-works-limits-on-operations-in-progress"></a>

Managed Service for Apache Flink limits the number of operations that run at the same time. The limits apply to one application, one enhanced snapshot, or one account in a Region. The following table lists these limits.


| Operation | Limit | Exception for the next request | 
| --- | --- | --- | 
| CreateSnapshot | One enhanced snapshot in CREATING for each application | ResourceInUseException | 
| ExportSnapshot | One export in progress for each enhanced snapshot, for all destinations combined | LimitExceededException | 
| ImportSnapshot and ExportSnapshot | 10 imports and exports combined in progress for each account in each Region | LimitExceededException | 

You can run only one export at a time for each enhanced snapshot, even to different destinations.

If you get one of these exceptions, wait for the operation in progress to finish. Then retry the request.

### Billing for enhanced snapshots
<a name="snapshots-how-it-works-billing-for-snapshots"></a>

Managed Service for Apache Flink bills the storage of enhanced snapshots at the same rate as application snapshots (legacy) of $0.023 per GB-month under durable application backups.

Enhanced snapshot storage appears on your bill under the usage type `{{region}}-DurableApplicationBackups`. For more information about current prices, see [Per second billing in Managed Service for Apache Flink](how-pricing.md).

Managed Service for Apache Flink bills the storage of the following enhanced snapshots:
+ Enhanced snapshots that you create with [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html)
+ Enhanced snapshots that you import with [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html)
+ System snapshots. For the operations that create a system snapshot, see [System snapshots](#snapshots-how-it-works-system-snapshots).

Billing for an enhanced snapshot starts when its status changes to `READY`. Billing stops when its status changes from `READY` to `DELETING`. Managed Service for Apache Flink does not bill an enhanced snapshot in the `CREATING` or `FAILED` status.

Billing for enhanced snapshots differs from billing for application snapshots (legacy) in the following ways:
+ **Imported snapshots** – You pay for the storage of each enhanced snapshot that you import.
+ **Transfers** – Imports and exports have no transfer charge from Managed Service for Apache Flink. Amazon S3 charges apply to the bucket that an import reads or an export writes.

**Note**  
You pay for the storage of each enhanced snapshot until you delete it. This rule applies to system snapshots and after you delete the application.

For more information about deleting enhanced snapshots, see [Delete an enhanced snapshot](snapshots-manage.md#snapshots-manage-delete-a-snapshot).

For more information about current prices, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/).