# Upgrading to Flink 2.2: Complete guide

This guide provides step-by-step instructions for upgrading your Amazon Managed Service for Apache Flink
application from Flink 1.x to Flink 2.2. This is a major version upgrade with breaking
changes that require careful planning and testing.

###### Major version upgrade is uni-directional

The Upgrade operation can move your application from Flink 1.x to 2.2 with state
preservation, but you cannot move back from 2.2 to 1.x with 2.2 state. If your
application becomes unhealthy after upgrading, use the Rollback API to return to the
1.x version with your original 1.x state from the latest snapshot.

## Prerequisites

Before beginning your upgrade:

- Review [Breaking changes and deprecations](flink-2-2.md#flink-2-2-breaking-changes "flink-2-2.md#flink-2-2-breaking-changes")
- Review [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md "state-compatibility.md")
- Ensure you have a non-production environment for testing
- Document your current application configuration and dependencies

## Understanding your migration paths

Your upgrade experience depends on your application's compatibility with Flink 2.2.
Understanding these paths helps you prepare appropriately and set realistic
expectations.

**Path 1: Compatible binary and application state**

**What to expect:**

- Invoke the Upgrade operation
- Complete the migration to 2.2 with the application status
  transitioning: `RUNNING` → `UPDATING` →
  `RUNNING`
- Preserve all application state without data loss or
  reprocessing
- Same experience as minor version migrations

Best for: Stateless applications or applications using compatible serialization
(Avro, compatible Protobuf schemas, POJOs without collections)

**Path 2: Binary incompatibilities**

**What to expect:**

- Invoke the Upgrade operation
- Operation fails and surfaces the binary incompatibility through
  Operations API and logs
- With auto-rollback enabled: Applications automatically roll back
  within minutes without your intervention
- With auto-rollback disabled: Applications remain in running state
  without data processing; you manually roll back to older
  version
- Once the binary is fixed, use the [UpdateApplication API](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") for an experience
  similar to Path 1

Best for: Applications using removed APIs that are detected during Flink job
startup

**Path 3: Incompatible application state**

**What to expect:**

- Invoke the Upgrade operation
- Migration appears to succeed initially
- Applications enter restart loops within seconds as state restoration
  fails
- Detect failures through CloudWatch Metrics showing continuous
  restarts
- Manually invoke the Rollback operation
- Return to production within minutes after initiating
  rollback
- Review
  [State migration](state-compatibility.md#state-compat-migration "state-compatibility.md#state-compat-migration") for your application

Best for: Applications with state serialization incompatibilities (POJOs with
collections, certain Kryo-serialized state)

###### Note

It is highly recommended to create a replica of your production application and test
each of the following phases of the upgrade on the replica before following the same
steps for your production application.

## Phase 1: Preparation

**Update application code**

Update your application code to be compatible with Flink 2.2:

- **Update Flink dependencies** to version
  2.2.1 in your `pom.xml` or
  `build.gradle`
- **Update connector dependencies** to Flink
  2.2-compatible versions (see
  [Connector availability](flink-2-2.md#flink-2-2-connectors "flink-2-2.md#flink-2-2-connectors"))
- **Remove deprecated API usage**:

  - Replace DataSet API with DataStream API or Table
    API/SQL
  - Replace legacy `SourceFunction`/`SinkFunction`
    with FLIP-27 Source and FLIP-143 Sink APIs
  - Replace Scala API usage with Java API

- **Update to Java 17**

**Upload updated application code**

- Build your application JAR with Flink 2.2 dependencies
- Upload to Amazon S3 with a **different file
  name** than your current JAR (for example,
  `my-app-flink-2.2.jar`)
- Note the S3 bucket and key for use in the upgrade step

## Phase 2: Enable auto-rollback

Auto-rollback allows Amazon Managed Service for Apache Flink to automatically revert to the previous version
if the upgrade fails.

**Check auto-rollback status**

_AWS Management Console:_

1. Navigate to your application
2. Choose **Configuration**
3. Under **Application settings**, verify
   **System rollback** is enabled

_AWS CLI:_

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

If automatic snapshots are enabled for your application you can skip this step, otherwise take a snapshot of your application to save the state of your application before upgrading.

**Take snapshot from running application**

_AWS Management Console:_

1. Navigate to your application
2. Choose **Snapshots**
3. Choose **Create snapshot**
4. Enter a snapshot name (for example,
   `pre-flink-2.2-upgrade`)
5. Choose **Create**

_AWS CLI:_

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

Wait until `SnapshotStatus` is `READY` before
proceeding.

## Phase 4: Upgrade application

You can upgrade your Flink application by using the [`UpdateApplication`](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action.

You can call the `UpdateApplication` API in multiple ways:

- **Use the AWS Management Console.**

  - Go to your app page on the AWS Management Console.
  - Choose **Configure**.
  - Select the new runtime and the snapshot that you want to start
    from, also known as restore configuration. Use the latest setting as the
    restore configuration to start the app from the latest snapshot. Point
    to the new upgraded application JAR/zip on Amazon S3.

- **Use the AWS CLI**
  [`update-application`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html")
  action.
- **Use CloudFormation.**

  - Update the `RuntimeEnvironment` field. Previously,
    CloudFormation deleted the application and created a new one, causing your
    snapshots and other app history to be lost. Now CloudFormation updates your
    `RuntimeEnvironment` in place and does not delete your
    application.

- **Use the AWS SDK.**

  - Consult the SDK documentation for the programming language of
    your choice. See [`UpdateApplication`](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md").

You can perform the upgrade while the application is in `RUNNING` state
or while the application is stopped in `READY` state. Amazon Managed Service for Apache Flink
validates the compatibility between the original runtime version and the target runtime
version. This compatibility check runs when you perform `UpdateApplication`
while in `RUNNING` state or at the next
`StartApplication` if you upgrade while in `READY`
state.

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

**Compatibility check**

- Use the Operations API to check the status of the upgrade. If there
  are binary incompatibilities or issues with job startup, the upgrade operation
  will fail with logs.
- If the Upgrade Operation has succeeded but the application is stuck in
  restart loops, this means the state is incompatible with the new Flink version
  or there is a problem with the updated code. Review
  [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md "state-compatibility.md") on how to identify state
  incompatibility issues.

**Monitor application health**

_Application state:_

- Application status should transition: `RUNNING` →
  `UPDATING` → `RUNNING`
- Check the runtime of the application. If it is 2.2, the upgrade
  operation was successful.
- If your application is in `RUNNING` but still on the older
  runtime, auto-rollback kicked in. Operations API will show operation as
  `FAILED`. Check logs to find the exception for
  failure.

In addition, monitor these metrics in CloudWatch:

_Restart metric:_

- `numRestarts`: Monitor for unexpected restarts — the
  upgrade is successful if `numRestarts` is zero and
  `uptime` or `runningTime` is
  increasing.

_Checkpoint metrics:_

- `lastCheckpointDuration`: Should be similar to pre-upgrade
  values
- `numberOfFailedCheckpoints`: Should remain at
  0

## Phase 6: Validate application behavior

After the application is running on Flink 2.2:

**Functional validation**

- Verify data is being read from sources
- Verify data is being written to sinks
- Verify business logic produces expected results
- Compare output with pre-upgrade baseline

**Performance validation**

- Monitor latency metrics (end-to-end processing time)
- Monitor throughput metrics (records per second)
- Monitor checkpoint duration and size
- Monitor memory and CPU utilization

**Run for 24+ hours**

Allow the application to run for at least 24 hours in production to ensure:

- No memory leaks
- Stable checkpoint behavior
- No unexpected restarts
- Consistent throughput

## Phase 7: Rollback procedures

If the upgrade fails or the application is running but unhealthy, roll back to the
previous version.

**Automatic rollback**

If auto-rollback is enabled and the upgrade fails during startup, Amazon Managed Service for Apache Flink
automatically reverts to the previous version.

**Manual rollback**

If the application is running but unhealthy, use the
`RollbackApplication` API:

_AWS Management Console:_

1. Navigate to your application
2. Choose **Actions** →
   **Roll back**
3. Confirm the rollback

_AWS CLI:_

```
aws kinesisanalyticsv2 rollback-application \
    --application-name MyApplication \
    --current-application-version-id <version-id>
```

**What happens during rollback:**

- Application stops
- Runtime reverts to previous Flink version
- Application code reverts to previous JAR
- Application restarts from the last successful snapshot taken
  **before** the upgrade

###### Important

- You cannot restore a Flink 2.2 snapshot on Flink
  1.x
- Rollback uses the snapshot taken before the
  upgrade
- Always take a snapshot before upgrading (Phase

3.

## Next steps

For questions or issues during upgrade, see the [Troubleshoot Managed Service for Apache Flink](troubleshooting.md "troubleshooting.md") or contact AWS Support.
