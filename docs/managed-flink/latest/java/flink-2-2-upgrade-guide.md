

# Upgrading to Flink 2.2: Complete guide
<a name="flink-2-2-upgrade-guide"></a>

This guide provides step-by-step instructions for upgrading your Amazon Managed Service for Apache Flink application from Flink 1.x to Flink 2.2. This is a major version upgrade with breaking changes that require careful planning and testing.

**Major version upgrade is uni-directional**  
The Upgrade operation can move your application from Flink 1.x to 2.2 with state preservation, but you cannot move back from 2.2 to 1.x with 2.2 state. If your application becomes unhealthy after upgrading, use the Rollback API to return to the 1.x version with your original 1.x state from the latest snapshot.

## Prerequisites
<a name="upgrade-guide-prerequisites"></a>

Before beginning your upgrade:
+ Review [Breaking changes and deprecations](flink-2-2.md#flink-2-2-breaking-changes)
+ Review [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md)
+ Ensure you have a non-production environment for testing
+ Document your current application configuration and dependencies
+ (Optional) Upgrade to enhanced snapshot mode. To upgrade, set `SnapshotModeUpdate` to `ENHANCED_SNAPSHOTS` in an `UpdateApplication` request. Otherwise, your application continues to use application snapshots (legacy). The application must already use Apache Flink 1.20 or later when you send this request. Managed Service for Apache Flink checks the current runtime, not the `RuntimeEnvironmentUpdate` value. If the application uses Apache Flink 1.19 or earlier, upgrade the runtime in a separate `UpdateApplication` request first. After the upgrade to enhanced snapshot mode, the application stays in that mode. For more information about the upgrade to enhanced snapshot mode, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

## Understanding your migration paths
<a name="upgrade-guide-migration-paths"></a>

Your upgrade experience depends on your application's compatibility with Flink 2.2. Understanding these paths helps you prepare appropriately and set realistic expectations.

**Path 1: Compatible binary and application state**

**What to expect:**
+ Invoke the Upgrade operation
+ Complete the migration to 2.2 with the application status transitioning: `RUNNING` → `UPDATING` → `RUNNING`
+ Preserve all application state without data loss or reprocessing
+ Same experience as minor version migrations

Best for: Stateless applications or applications using compatible serialization (Avro, compatible Protobuf schemas, POJOs without collections)

**Path 2: Binary incompatibilities**

**What to expect:**
+ Invoke the Upgrade operation
+ Operation fails and surfaces the binary incompatibility through Operations API and logs
+ With auto-rollback enabled: Applications automatically roll back within minutes without your intervention
+ With auto-rollback disabled: Applications remain in running state without data processing; you manually roll back to older version
+ Once the binary is fixed, use the [UpdateApplication API](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) for an experience similar to Path 1

Best for: Applications using removed APIs that are detected during Flink job startup

**Path 3: Incompatible application state**

**What to expect:**
+ Invoke the Upgrade operation
+ Migration appears to succeed initially
+ Applications enter restart loops within seconds as state restoration fails
+ Detect failures through CloudWatch Metrics showing continuous restarts
+ Manually invoke the Rollback operation
+ Return to production within minutes after initiating rollback
+ Review [State migration](state-compatibility.md#state-compat-migration) for your application

Best for: Applications with state serialization incompatibilities (POJOs with collections, certain Kryo-serialized state)

**Note**  
It is highly recommended to create a replica of your production application and test each of the following phases of the upgrade on the replica before following the same steps for your production application.

## Phase 1: Preparation
<a name="upgrade-guide-phase-1"></a>

**Update application code**

Update your application code to be compatible with Flink 2.2:
+ **Update Flink dependencies** to version 2.2.1 in your `pom.xml` or `build.gradle`
+ **Update connector dependencies** to Flink 2.2-compatible versions (see [Connector availability](flink-2-2.md#flink-2-2-connectors))
+ **Remove deprecated API usage**:
  + Replace DataSet API with DataStream API or Table API/SQL
  + Replace legacy `SourceFunction`/`SinkFunction` with FLIP-27 Source and FLIP-143 Sink APIs
  + Replace Scala API usage with Java API
+ **Update to Java 17**

**Upload updated application code**
+ Build your application JAR with Flink 2.2 dependencies
+ Upload to Amazon S3 with a **different file name** than your current JAR (for example, `my-app-flink-2.2.jar`)
+ Note the S3 bucket and key for use in the upgrade step

## Phase 2: Enable auto-rollback
<a name="upgrade-guide-phase-2"></a>

Auto-rollback allows Amazon Managed Service for Apache Flink to automatically revert to the previous version if the upgrade fails.

**Check auto-rollback status**

*AWS Management Console:*

1. Navigate to your application

1. Choose **Configuration**

1. Under **Application settings**, verify **System rollback** is enabled

*AWS CLI:*

```
aws kinesisanalyticsv2 describe-application \
    --application-name MyApplication \
    --query 'ApplicationDetail.ApplicationConfigurationDescription.ApplicationSystemRollbackConfigurationDescription.RollbackEnabled'
```

**Enable auto-rollback (if not enabled)**

```
aws kinesisanalyticsv2 update-application \
    --application-name MyApplication \
    --current-application-version-id <version-id> \
    --application-configuration-update '{
        "ApplicationSystemRollbackConfigurationUpdate": {
            "RollbackEnabledUpdate": true
        }
    }'
```

## Phase 3: Take snapshot (optional)
<a name="upgrade-guide-phase-3"></a>

If automatic snapshots are enabled for your application you can skip this step, otherwise take a snapshot of your application to save the state of your application before upgrading.

**Take snapshot from running application**

*AWS Management Console:*

1. Navigate to your application

1. Choose **Snapshots**

1. Choose **Create snapshot**

1. Enter a snapshot name (for example, `pre-flink-2.2-upgrade`)

1. Choose **Create**

*AWS CLI:*

```
aws kinesisanalyticsv2 create-application-snapshot \
    --application-name MyApplication \
    --snapshot-name pre-flink-2.2-upgrade
```

**Verify snapshot creation**

```
aws kinesisanalyticsv2 describe-application-snapshot \
    --application-name MyApplication \
    --snapshot-name pre-flink-2.2-upgrade
```

Wait until `SnapshotStatus` is `READY` before proceeding.

**Take an enhanced snapshot (enhanced snapshot mode)**

The previous commands create an application snapshot (legacy). For an application in enhanced snapshot mode, `CreateApplicationSnapshot` returns `InvalidApplicationConfigurationException`. Call [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) instead. Run the following AWS CLI command for Amazon Managed Service for Apache Flink. Replace `MyApplication` with the name of your application, and `pre-flink-2.2-upgrade` with a name for the enhanced snapshot.

```
PROMPT> aws kinesisanalyticsv2 create-snapshot \
    --application-name MyApplication \
    --snapshot-name pre-flink-2.2-upgrade
```

Run the following AWS CLI command, which calls [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html), until `SnapshotStatus` is `READY`. Copy the `SnapshotArn` value. You need the ARN to restore the application from this enhanced snapshot.

```
PROMPT> aws kinesisanalyticsv2 describe-snapshot \
    --snapshot-name pre-flink-2.2-upgrade
```

For more information about enhanced snapshot creation, see [Create an enhanced snapshot](snapshots-manage.md#snapshots-manage-create-a-snapshot).

## Phase 4: Upgrade application
<a name="upgrade-guide-phase-4"></a>

You can upgrade your Flink application by using the [`UpdateApplication`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) action.

You can call the `UpdateApplication` API in multiple ways:
+ **Use the AWS Management Console.**
  + Go to your app page on the AWS Management Console.
  + Choose **Configure**.
  + Select the new runtime and the snapshot that you want to start from, also known as restore configuration. Use the latest setting as the restore configuration to start the app from the latest snapshot. Point to the new upgraded application JAR/zip on Amazon S3.
+ **Use the AWS CLI** [`update-application`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html) action.
+ **Use CloudFormation.**
  + Update the `RuntimeEnvironment` field. Previously, CloudFormation deleted the application and created a new one, causing your snapshots and other app history to be lost. Now CloudFormation updates your `RuntimeEnvironment` in place and does not delete your application.
+ **Use the AWS SDK.**
  + Consult the SDK documentation for the programming language of your choice. See [`UpdateApplication`](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html).

You can perform the upgrade while the application is in `RUNNING` state or while the application is stopped in `READY` state. Amazon Managed Service for Apache Flink validates the compatibility between the original runtime version and the target runtime version. This compatibility check runs when you perform `UpdateApplication` while in `RUNNING` state or at the next `StartApplication` if you upgrade while in `READY` state.

In enhanced snapshot mode, the upgrade needs extra permissions:
+ For an upgrade from the `RUNNING` state, Managed Service for Apache Flink creates a system snapshot if `SnapshotsEnabled` in the application snapshot configuration is `true`. The caller of `UpdateApplication` needs `kinesisanalytics:CreateSystemSnapshot` on the application.
+ For an upgrade from the `READY` state, the caller of `StartApplication` needs `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot that the start restores from.

For more information, see [IAM permissions](snapshots-setup.md#snapshots-setup-iam-permissions).

**Upgrade from RUNNING state**

```
aws kinesisanalyticsv2 update-application \
    --application-name MyApplication \
    --current-application-version-id <version-id> \
    --runtime-environment-update FLINK-2_2 \
    --application-configuration-update '{
        "ApplicationCodeConfigurationUpdate": {
            "CodeContentUpdate": {
                "S3ContentLocationUpdate": {
                    "FileKeyUpdate": "my-app-flink-2.2.jar"
                }
            }
        }
    }'
```

**Upgrade from READY state**

```
aws kinesisanalyticsv2 update-application \
    --application-name MyApplication \
    --current-application-version-id <version-id> \
    --runtime-environment-update FLINK-2_2 \
    --application-configuration-update '{
        "ApplicationCodeConfigurationUpdate": {
            "CodeContentUpdate": {
                "S3ContentLocationUpdate": {
                    "FileKeyUpdate": "my-app-flink-2.2.jar"
                }
            }
        }
    }'
```

## Phase 5: Monitor upgrade
<a name="upgrade-guide-phase-5"></a>

**Compatibility check**
+ Use the Operations API to check the status of the upgrade. If there are binary incompatibilities or issues with job startup, the upgrade operation will fail with logs.
+ If the Upgrade Operation has succeeded but the application is stuck in restart loops, this means the state is incompatible with the new Flink version or there is a problem with the updated code. Review [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md) on how to identify state incompatibility issues.

**Monitor application health**

*Application state:*
+ Application status should transition: `RUNNING` → `UPDATING` → `RUNNING`
+ Check the runtime of the application. If it is 2.2, the upgrade operation was successful.
+ If your application is in `RUNNING` but still on the older runtime, auto-rollback kicked in. Operations API will show operation as `FAILED`. Check logs to find the exception for failure.

In addition, monitor these metrics in CloudWatch:

*Restart metric:*
+ `numRestarts`: Monitor for unexpected restarts — the upgrade is successful if `numRestarts` is zero and `uptime` or `runningTime` is increasing.

*Checkpoint metrics:*
+ `lastCheckpointDuration`: Should be similar to pre-upgrade values
+ `numberOfFailedCheckpoints`: Should remain at 0

## Phase 6: Validate application behavior
<a name="upgrade-guide-phase-6"></a>

After the application is running on Flink 2.2:

**Functional validation**
+ Verify data is being read from sources
+ Verify data is being written to sinks
+ Verify business logic produces expected results
+ Compare output with pre-upgrade baseline

**Performance validation**
+ Monitor latency metrics (end-to-end processing time)
+ Monitor throughput metrics (records per second)
+ Monitor checkpoint duration and size
+ Monitor memory and CPU utilization

**Run for 24\+ hours**

Allow the application to run for at least 24 hours in production to ensure:
+ No memory leaks
+ Stable checkpoint behavior
+ No unexpected restarts
+ Consistent throughput

## Phase 7: Rollback procedures
<a name="upgrade-guide-phase-7"></a>

If the upgrade fails or the application is running but unhealthy, roll back to the previous version.

**Automatic rollback**

If auto-rollback is enabled and the upgrade fails during startup, Amazon Managed Service for Apache Flink automatically reverts to the previous version.

**Manual rollback**

If the application is running but unhealthy, use the `RollbackApplication` API:

*AWS Management Console:*

1. Navigate to your application

1. Choose **Actions** → **Roll back**

1. Confirm the rollback

*AWS CLI:*

```
aws kinesisanalyticsv2 rollback-application \
    --application-name MyApplication \
    --current-application-version-id <version-id>
```

**What happens during rollback:**
+ Application stops
+ Runtime reverts to previous Flink version
+ Application code reverts to previous JAR
+ Application restarts from the last successful snapshot taken **before** the upgrade

**Important**  
You cannot restore a Flink 2.2 snapshot on Flink 1.x
Rollback uses the snapshot taken before the upgrade
Always take a snapshot before upgrading (Phase 3)

**Rollback in enhanced snapshot mode**

In enhanced snapshot mode, `RollbackApplication` restores from an enhanced snapshot. For a `RUNNING` application, Managed Service for Apache Flink selects the newest `READY` enhanced snapshot from the pre-upgrade application version or an earlier version.
+ Keep a `READY` enhanced snapshot from the version before the upgrade or an earlier version, so that `RollbackApplication` can succeed. Without one, `RollbackApplication` returns `InvalidRequestException`.
+ The IAM principal that calls `RollbackApplication` needs the `kinesisanalytics:RestoreFromSnapshot` permission on the selected enhanced snapshot.
+ Keep the enhanced snapshot from Phase 3 until you finish the validation in Phase 6. A rollback cannot use a deleted enhanced snapshot.

For more information about rollbacks in enhanced snapshot mode, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).

## Next steps
<a name="upgrade-guide-next-steps"></a>

For questions or issues during upgrade, see the [Troubleshoot Managed Service for Apache Flink](troubleshooting.md) or contact AWS Support.