

# Roll back application upgrades
<a name="rollback"></a>

If you have issues with your application or find inconsistencies in your application code between Flink versions, you can roll back using the AWS CLI, AWS CloudFormation, AWS SDK, or the AWS Management Console. The following examples show what rolling back looks like in different failure scenarios.

## Runtime upgrade succeeded, the application is in `RUNNING` state, but the job is failing and continuously restarting
<a name="succeeded-restarting"></a>

Assume you are trying to upgrade a stateful application named `TestApplication` from Flink 1.15 to Flink 1.18 in US East (N. Virginia). However, the upgraded Flink 1.18 application is failing to start or is constantly restarting, even though the application is in `RUNNING` state. This is a common failure scenario. To avoid further downtime, we recommend that you roll back your application immediately to the previous running version (Flink 1.15), and diagnose the issue later.

To roll back the application to the previous running version, use the [rollback-application](https://docs.aws.amazon.com/cli/latest/reference/kinesisanalyticsv2/rollback-application.html) AWS CLI command or the [RollbackApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RollbackApplication.html) API action. This API action rolls back the changes you've made that resulted in the latest version. Then it restarts your application using the latest successful snapshot. 

In enhanced snapshot mode, Managed Service for Apache Flink restores the newest `READY` enhanced snapshot at or before the application version that the rollback returns to. For more information, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).

We strongly recommend that you take a snapshot with your existing app before you attempt to upgrade. This will help to avoid data loss or having to reprocess data. 

In this failure scenario, CloudFormation will not roll back the application for you. You must update the CloudFormation template to point to the previous runtime and to the previous code to force CloudFormation to update the application. Otherwise, CloudFormation assumes that your application has been updated when it transitions to the `RUNNING` state.

## Rolling back an application that is stuck in `UPDATING`
<a name="stuck-updating"></a>

If your application gets stuck in the `UPDATING` or `AUTOSCALING` state after an upgrade attempt, Amazon Managed Service for Apache Flink offers the [rollback-applications](https://docs.aws.amazon.com/cli/latest/reference/kinesisanalyticsv2/rollback-application.html) AWS CLI command, or the [RollbackApplications](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_RollbackApplication.html) API action that can roll back the application to the version before the stuck `UPDATING` or `AUTOSCALING` state. This API rolls back the changes that you’ve made that caused the application to get stuck in `UPDATING` or `AUTOSCALING` transitive state.

In enhanced snapshot mode, `RollbackApplication` restores from an enhanced snapshot. For an application in the `UPDATING` or `AUTOSCALING` status, Managed Service for Apache Flink uses the newest `READY` enhanced snapshot of the application. If the application has no `READY` enhanced snapshot, the rollback returns `InvalidRequestException`.

The IAM principal that calls `RollbackApplication` needs the `kinesisanalytics:RestoreFromSnapshot` permission on the selected enhanced snapshot. For more information, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).

## Roll back after an upgrade to enhanced snapshot mode
<a name="how-in-place-version-upgrades-rollback-after-opt-in"></a>

After a rollback to the application version before the upgrade to enhanced snapshot mode, the application uses application snapshots (legacy) again. Managed Service for Apache Flink restores the newest `READY` application snapshot (legacy) at or below the application version before the upgrade.
+ The rollback works only if you did not update the application after the upgrade to enhanced snapshot mode.
+ If no `READY` application snapshot (legacy) exists at or below the application version before the upgrade, `RollbackApplication` returns `InvalidRequestException`.
+ After the rollback, the application uses application snapshots (legacy). The application can use the enhanced snapshots that it created after the upgrade only after you upgrade it to enhanced snapshot mode again.

For more information about rollbacks across the boundary of the upgrade to enhanced snapshot mode, see [Roll back after the upgrade](snapshots-upgrade.md#snapshots-upgrade-rollback-behavior).