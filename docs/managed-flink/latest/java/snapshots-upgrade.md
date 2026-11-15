

# Upgrade an existing application to enhanced snapshots
<a name="snapshots-upgrade"></a>

This page describes how to upgrade an existing Amazon Managed Service for Apache Flink application to enhanced snapshot mode. You upgrade with an [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) request. The page lists the changes to make before you upgrade. The page also describes how the upgrade affects your application snapshots (legacy).

## Before you upgrade
<a name="snapshots-upgrade-before-you-upgrade"></a>

Complete the following checklist before you upgrade an application.
+ Make sure that the application uses Apache Flink version 1.20 or later before you send the upgrade request. Managed Service for Apache Flink checks the current runtime of the application, not a `RuntimeEnvironmentUpdate` value in the upgrade request. If the application uses Apache Flink 1.19 or earlier, upgrade the runtime in a separate `UpdateApplication` request first. For more information about runtime upgrades, see [Use in-place version upgrades for Apache Flink](how-in-place-version-upgrades.md).
+ Give the caller the required IAM permissions. The principal that sends the upgrade request needs `kinesisanalytics:UpdateApplication` on the application ARN.

  To upgrade a `RUNNING` application with `SnapshotsEnabled` set to `true`, the caller also needs `kinesisanalytics:CreateSystemSnapshot` on the application ARN. Managed Service for Apache Flink uses the `SnapshotsEnabledUpdate` value of the upgrade request for this check.

  If a restore configuration in the request uses an enhanced snapshot, the caller also needs `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot that the restore uses.

  Give the principals that manage snapshots permission for the enhanced snapshot actions, such as `kinesisanalytics:CreateSnapshot`. For more information about these permissions, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).
+ Keep the existing AWS Key Management Service (AWS KMS) key policy if the application uses a customer managed key. The service execution role needs no changes. For more information about the AWS KMS permissions that [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) callers need, see [Create an enhanced snapshot](snapshots-manage.md#snapshots-manage-create-a-snapshot).
+ Plan for a rollback. Record the current application version ID before you upgrade. [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) can return the application to that version only as long as the upgrade is the most recent update.

  During the upgrade, Managed Service for Apache Flink takes an application snapshot (legacy) of the current version of a running application. This guide calls that snapshot the *boundary capture*. A rollback to the version before the upgrade restores the newest `READY` application snapshot (legacy) at or below that version. If the boundary capture is `READY`, the rollback restores the boundary capture. For more information about rollback behavior across the upgrade boundary, see [Roll back after the upgrade](#snapshots-upgrade-rollback-behavior).
+ Upgrade through the template if CloudFormation manages the application as an `AWS::KinesisAnalyticsV2::Application` resource. For more information about the template change, see [Upgrade with CloudFormation](#snapshots-upgrade-cfn).
+ Plan a cleanup process for enhanced snapshots. For more information about storage charges after the upgrade, see the billing note after this checklist.
+ Update your snapshot tooling. After the upgrade, [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) returns `InvalidApplicationConfigurationException`. Update your scripts and pipelines to call the enhanced snapshot APIs instead. For more information about the API changes, see [Update your tooling](#snapshots-upgrade-update-your-tooling).

**Note**  
After the upgrade, each system snapshot is an enhanced snapshot that remains until you delete it. Managed Service for Apache Flink bills enhanced snapshot storage at the same rate as application snapshots (legacy). For more information about billing for enhanced snapshots, see [Billing for enhanced snapshots](snapshots-how-it-works.md#snapshots-how-it-works-billing-for-snapshots). For current prices, see [Amazon Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/) on the AWS website.

**Note**  
If `SnapshotsEnabled` is `false` when you upgrade, Managed Service for Apache Flink takes no boundary capture. For the upgrade restart, Managed Service for Apache Flink then uses the newest `READY` snapshot that already exists, either an application snapshot (legacy) or an enhanced snapshot. That snapshot contains the state from when Managed Service for Apache Flink took it, not the current state. If the application has no such snapshot, Managed Service for Apache Flink starts the application without state. To keep the current state, set `SnapshotsEnabledUpdate` to `true` in the upgrade request.

## Upgrade with `UpdateApplication`
<a name="snapshots-upgrade-opt-in-with-updateapplication"></a>

An application that doesn't use enhanced snapshot mode uses *application snapshot (legacy) mode* (`APPLICATION_SNAPSHOTS_LEGACY`).

**Note**  
The upgrade is one-way. After the upgrade, no `UpdateApplication` request can return the application to application snapshot (legacy) mode.  
If you set `SnapshotModeUpdate` to `APPLICATION_SNAPSHOTS_LEGACY` on an upgraded application, `UpdateApplication` returns `InvalidArgumentException`.  
To return to application snapshot (legacy) mode, roll back to the application version before the upgrade. The rollback works only as long as the upgrade is the most recent update. For more information about the rollback path, see [Roll back after the upgrade](#snapshots-upgrade-rollback-behavior).

To upgrade, set `SnapshotModeUpdate` to `ENHANCED_SNAPSHOTS`. This member is in `ApplicationConfigurationUpdate.ApplicationSnapshotConfigurationUpdate`. Also send `SnapshotsEnabledUpdate`. The API requires it even when you change only the mode.

You can upgrade an application in the `READY` or `RUNNING` status.

**Note**  
For an application in the `READY` status, the upgrade takes effect at once. Managed Service for Apache Flink takes no snapshot of the application.  
The next `StartApplication` request with `RESTORE_FROM_LATEST_SNAPSHOT` finds no enhanced snapshot. Managed Service for Apache Flink then starts the application without state. After the upgrade, you can't restore an application snapshot (legacy) by name.  
To keep the application state, upgrade the application while its status is `RUNNING`.

**To prepare an upgrade request**

1. Note the `ApplicationVersionId` value in the output of the AWS CLI `describe-application` command.

1. Confirm that `ApplicationSnapshotConfigurationDescription.SnapshotsEnabled` is `true` in the same output. If the value is `false`, read the `SnapshotsEnabled` note in [Before you upgrade](#snapshots-upgrade-before-you-upgrade).

1. Save the following JSON request as `upgrade.json` in a text editor.

   ```
   {
     "ApplicationName": "MyApplication",
     "CurrentApplicationVersionId": 3,
     "ApplicationConfigurationUpdate": {
       "ApplicationSnapshotConfigurationUpdate": {
         "SnapshotsEnabledUpdate": true,
         "SnapshotModeUpdate": "ENHANCED_SNAPSHOTS"
       }
     }
   }
   ```

   Replace `MyApplication` with the name of your application.

1. Set `CurrentApplicationVersionId` in `upgrade.json` to the version ID from step 1.

**To send an upgrade request**

1. Run the following AWS CLI command at a command prompt to send the request.

   ```
   PROMPT> aws kinesisanalyticsv2 update-application --cli-input-json file://upgrade.json
   ```

   For a `RUNNING` application, the response contains the `ApplicationDetail` and an `OperationId`. For a `READY` application, the response contains no `OperationId`.

1. Run the following AWS CLI command for a `RUNNING` application until the operation status is `SUCCESSFUL` or `FAILED`. The command calls [`DescribeApplicationOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationOperation.html) with the `OperationId`. For a `READY` application, skip this step.

   ```
   PROMPT> aws kinesisanalyticsv2 describe-application-operation --application-name MyApplication --operation-id {{operation-id}}
   ```

1. Confirm that `ApplicationSnapshotConfigurationDescription.SnapshotMode` is `ENHANCED_SNAPSHOTS` in the output of the AWS CLI `describe-application` command. The application now uses enhanced snapshot mode.

### What happens during the upgrade
<a name="snapshots-upgrade-what-happens-during-opt-in"></a>

For a `RUNNING` application, Managed Service for Apache Flink performs the following steps.

1. Managed Service for Apache Flink checks the caller permissions before it records the change. If the check fails, the call returns `AccessDeniedException` and the application doesn't change.

1. Managed Service for Apache Flink records the mode change and returns HTTP 200 with an `OperationId`. The remaining steps run asynchronously.

1. Managed Service for Apache Flink takes an application snapshot (legacy) of the current application version. This snapshot is the boundary capture. Managed Service for Apache Flink skips this step if `SnapshotsEnabled` is `false`.

1. Managed Service for Apache Flink restarts the application in enhanced snapshot mode from the boundary capture. Without a boundary capture, Managed Service for Apache Flink uses the newest `READY` snapshot, either an application snapshot (legacy) or an enhanced snapshot. If none exists, Managed Service for Apache Flink starts the application without state.

Managed Service for Apache Flink doesn't copy or convert snapshot data. Your existing application snapshots (legacy) stay as they are.

After Managed Service for Apache Flink restarts the application in enhanced snapshot mode, every new snapshot of the application is an enhanced snapshot. The application has no enhanced snapshot until you call `CreateSnapshot` or Managed Service for Apache Flink takes a system snapshot.

For an application in the `READY` status, Managed Service for Apache Flink records the mode change at once. Managed Service for Apache Flink takes no snapshot of the application. The response contains no `OperationId`. The next `StartApplication` request with `RESTORE_FROM_LATEST_SNAPSHOT` finds no enhanced snapshot. Managed Service for Apache Flink then starts the application without state.

A restore configuration in the upgrade request applies only to a `RUNNING` application. For an application in any other status, the request returns `InvalidArgumentException`.

## Upgrade with CloudFormation
<a name="snapshots-upgrade-cfn"></a>

For an application that CloudFormation manages as an `AWS::KinesisAnalyticsV2::Application` resource, set `SnapshotMode` in `ApplicationConfiguration.ApplicationSnapshotConfiguration`.

**To upgrade a stack-managed application**

1. In the template, set `SnapshotMode` to `ENHANCED_SNAPSHOTS`. Keep `SnapshotsEnabled` set to `true`.

   ```
   ApplicationConfiguration:
     ApplicationSnapshotConfiguration:
       SnapshotsEnabled: true
       SnapshotMode: ENHANCED_SNAPSHOTS
   ```

1. In CloudFormation, update the stack. CloudFormation sends the upgrade request to Managed Service for Apache Flink only when `SnapshotMode` in the template differs from the mode of the application.

The following rules apply after the upgrade:
+ If you change `SnapshotMode` in the template from `ENHANCED_SNAPSHOTS` to `APPLICATION_SNAPSHOTS_LEGACY`, the stack update fails with an `InvalidRequest` error. CloudFormation makes no change to the application.
+ If you upgrade the application with the API, a stack update that doesn't change `SnapshotMode` keeps enhanced snapshot mode.
+ A stack rollback doesn't return the application to application snapshots (legacy). If the rollback template restores from a snapshot by `SnapshotName`, CloudFormation restores from the latest snapshot instead.
+ To restore from an enhanced snapshot, set `SnapshotArn` in `RunConfiguration.ApplicationRestoreConfiguration`. Specify `SnapshotName` or `SnapshotArn`, not both.
+ The role that CloudFormation uses to update the stack needs `kinesisanalytics:RestoreFromSnapshot` and `kinesisanalytics:CreateSystemSnapshot`. For more information about these permissions, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

## Errors during the upgrade
<a name="snapshots-upgrade-opt-in-behavior"></a>

The upgrade is one-way. For more information about the one-way rule, see [Upgrade with `UpdateApplication`](#snapshots-upgrade-opt-in-with-updateapplication). For more information about the rollback path, see [Roll back after the upgrade](#snapshots-upgrade-rollback-behavior).

A repeated upgrade request for an application in enhanced snapshot mode creates a new application version. For a `RUNNING` application, the request runs an update that takes a system snapshot.

The following table lists the errors that an upgrade request can return.


| Exception | Cause | 
| --- | --- | 
| InvalidArgumentException | The application uses Apache Flink 1.19 or earlier, or a runtime other than Apache Flink. | 
| InvalidArgumentException | The request sets an upgraded application back to APPLICATION\_SNAPSHOTS\_LEGACY. | 
| InvalidApplicationConfigurationException | The request restores from an application snapshot (legacy) by SnapshotName. | 
| UnsupportedOperationException | Enhanced snapshots aren't available for your account in the Region of the request. | 
| AccessDeniedException | The caller lacks a required permission, such as kinesisanalytics:CreateSystemSnapshot. The application doesn't change. | 
| ConcurrentModificationException | CurrentApplicationVersionId or ConditionalToken doesn't match the current application. | 
| InvalidArgumentException | The request includes a restore configuration, and the application isn't RUNNING. | 

## Existing application snapshots after the upgrade
<a name="snapshots-upgrade-existing-application-snapshots-after-opt-in"></a>

The upgrade doesn't delete or change your existing application snapshots (legacy). The upgraded application can use them only in the ways that the following lists describe.

After the upgrade, you can do the following with application snapshots (legacy):
+ Roll back to the application version before the upgrade. The rollback restores the newest `READY` application snapshot (legacy) at or below that version. If the boundary capture is `READY`, the rollback restores the boundary capture. After the rollback, the application uses application snapshots (legacy) again.
+ Call [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) to list the existing application snapshots (legacy) of the application. The [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) API returns only enhanced snapshots. Neither API returns both snapshot types.
+ Call [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html) to describe an existing application snapshot (legacy).
+ Call [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) to delete an existing application snapshot (legacy).

After the upgrade, you can't do the following with application snapshots (legacy):
+ Create an application snapshot (legacy). [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) returns `InvalidApplicationConfigurationException`. The error message tells you to use `CreateSnapshot` instead.
+ Restore an application snapshot (legacy) by name. A restore with `RESTORE_FROM_CUSTOM_SNAPSHOT` and `SnapshotName` returns `InvalidApplicationConfigurationException`.
+ Export an application snapshot (legacy).

### Restore from the latest snapshot after the upgrade
<a name="snapshots-upgrade-restore-from-latest-after-opt-in"></a>

In enhanced snapshot mode, `RESTORE_FROM_LATEST_SNAPSHOT` uses the newest `READY` enhanced snapshot of the application. For the selection rules, see [Restore from the latest snapshot](snapshots-restore.md#snapshots-restore-restore-from-the-latest-snapshot). Managed Service for Apache Flink doesn't fall back to an application snapshot (legacy).

**Note**  
If the application has no enhanced snapshot yet, `RESTORE_FROM_LATEST_SNAPSHOT` starts the application without state. The application loses the state from before the upgrade.  
To prevent this data loss, create an enhanced snapshot right after the upgrade. Wait until its status is `READY` before you stop or restart the application.

## Roll back after the upgrade
<a name="snapshots-upgrade-rollback-behavior"></a>

Only a rollback to the version before the upgrade returns an application to application snapshot (legacy) mode.

To roll back manually, call `RollbackApplication` to return to the version before the upgrade.
+ The application returns to application snapshot (legacy) mode. Managed Service for Apache Flink restores the newest `READY` application snapshot (legacy) at or below the version before the upgrade. If the boundary capture is `READY`, Managed Service for Apache Flink restores the boundary capture.
+ The rollback works only as long as the upgrade is the most recent update of the application.
+ Managed Service for Apache Flink keeps the enhanced snapshots that the application created after the upgrade. The application can use them again only after another upgrade.

For more information about application rollbacks, see [Roll back application upgrades](rollback.md).

To turn on system rollbacks for an existing application, set `ApplicationConfigurationUpdate.ApplicationSystemRollbackConfigurationUpdate.RollbackEnabledUpdate` to `true`. For more information about system rollbacks, see [Enable system rollbacks for your Managed Service for Apache Flink application](how-system-rollbacks.md).

If system rollbacks are on and the upgrade fails, Managed Service for Apache Flink rolls back the application. The upgrade operation status is `FAILED`. Managed Service for Apache Flink returns the application to the `RUNNING` status. The application returns to the version before the upgrade, in application snapshot (legacy) mode. Managed Service for Apache Flink restores the newest `READY` application snapshot (legacy) at or below that version.

**Note**  
If system rollbacks are off and the upgrade fails, the operation status is `FAILED`. The application stays in the `READY` status. The value of `SnapshotMode` stays `ENHANCED_SNAPSHOTS`. The next restore with `RESTORE_FROM_LATEST_SNAPSHOT` starts the application without state. To keep the state, don't start the application with `RESTORE_FROM_LATEST_SNAPSHOT`. Call `RollbackApplication` to return to the version before the upgrade.

### Upgrade without losing state
<a name="snapshots-upgrade-recommended-upgrade-procedure"></a>

Use the following procedures to upgrade an application without loss of state.

**To upgrade and verify the application**

1. Complete the checklist in [Before you upgrade](#snapshots-upgrade-before-you-upgrade).

1. Send the upgrade request. For more information about the request, see [Upgrade with `UpdateApplication`](#snapshots-upgrade-opt-in-with-updateapplication).

1. Wait until the `UpdateApplication` operation status is `SUCCESSFUL`.

1. Wait until the application status is `RUNNING`.

**To create a snapshot and update tooling**

1. Run the following AWS CLI command at a command prompt to create an enhanced snapshot with [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html).

   ```
   PROMPT> aws kinesisanalyticsv2 create-snapshot --application-name MyApplication --snapshot-name MyApplication-snapshot-1
   ```

   Managed Service for Apache Flink starts to create the enhanced snapshot. Its status is `CREATING`.

1. Run the following AWS CLI command until `SnapshotStatus` is `READY`. The command calls [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html).

   ```
   PROMPT> aws kinesisanalyticsv2 describe-snapshot --snapshot-name MyApplication-snapshot-1
   ```

   If the status is `FAILED`, read [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

1. Update your scripts, pipelines, and IAM policies to use the enhanced snapshot APIs.

1. Remove the calls to legacy snapshot APIs from your tooling.

## Update your tooling
<a name="snapshots-upgrade-update-your-tooling"></a>

After the upgrade, change each legacy snapshot API call in your tooling to its enhanced snapshot equivalent. The following table maps each legacy API to the enhanced snapshot API and lists the differences.


| Legacy API | Enhanced snapshot API | Differences | 
| --- | --- | --- | 
| [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) | [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) | Takes ApplicationName and SnapshotName, plus optional SnapshotDescription and Tags. Snapshot names are unique in the account and Region. The call runs asynchronously. The response contains SnapshotArn and SnapshotOperationId. The application must be RUNNING. | 
| [`DescribeApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplicationSnapshot.html) | [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) | Takes SnapshotName only, with no ApplicationName. Returns SnapshotInfoDetails. The SnapshotSourceDescription field names the source application. | 
| [`ListApplicationSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListApplicationSnapshots.html) | [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html) | Lists enhanced snapshots for the whole account. To list the snapshots of one application, use the SourceApplicationName filter. Each ListSnapshots call accepts no more than one filter. Limit accepts up to 50. Results come newest first. | 
| [`DeleteApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationSnapshot.html) | [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html) | Takes SnapshotName and SnapshotCreationTimestamp, with no ApplicationName. Copy the timestamp from DescribeSnapshot. The call runs asynchronously. | 
| [`ApplicationRestoreConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html).SnapshotName | [`ApplicationRestoreConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ApplicationRestoreConfiguration.html).SnapshotArn | Use RESTORE\_FROM\_CUSTOM\_SNAPSHOT with SnapshotArn on StartApplication or UpdateApplication. Set either SnapshotName or SnapshotArn, not both. The caller needs kinesisanalytics:RestoreFromSnapshot on the enhanced snapshot that the restore uses. | 
| None | [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html), [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) | Track the progress and failures of asynchronous snapshot calls with the SnapshotOperationId. | 

For more information about requests and responses, see [Enhanced snapshot API examples](snapshots-api-examples.md).