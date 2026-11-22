

# Set up enhanced snapshots

This page describes how to create a new Amazon Managed Service for Apache Flink application in enhanced snapshot mode. It covers the prerequisites, the AWS Identity and Access Management (IAM) permissions, and the steps to create your first enhanced snapshot.

## Prerequisites
<a name="snapshots-setup-prerequisites"></a>

Before you create an application in enhanced snapshot mode, check the following requirements.

**Apache Flink version**  
The application must use Apache Flink version 1.20 or later.

**Region**  
Enhanced snapshots are available in the AWS Regions where Managed Service for Apache Flink operates, except the AWS Top Secret Cloud Regions and the AWS European Sovereign Cloud. Enhanced snapshots aren't available in the AWS Top Secret Cloud Regions or the AWS European Sovereign Cloud at this time. If a request returns `UnsupportedOperationException`, enhanced snapshots aren't available for your account in the Region of the request.

The Apache Flink version range includes every `RuntimeEnvironment` value from `FLINK-1_20` on.

For Apache Flink 1.19 or earlier, a `CreateApplication` or `UpdateApplication` request that sets `SnapshotMode` to `ENHANCED_SNAPSHOTS` returns `InvalidArgumentException`. For an application on Apache Flink 1.19 or earlier, [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) returns `InvalidApplicationConfigurationException`.

New applications do not use enhanced snapshot mode by default. To use enhanced snapshot mode, set `SnapshotMode` to `ENHANCED_SNAPSHOTS` in your [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) request. To upgrade an existing application to enhanced snapshot mode, see [Upgrade an existing application to enhanced snapshots](snapshots-upgrade.md).

## IAM permissions
<a name="snapshots-setup-iam-permissions"></a>

Enhanced snapshots add new AWS Identity and Access Management (IAM) actions. Managed Service for Apache Flink checks these actions on the principal that calls each enhanced snapshot API.

**Caller permissions**  
The caller needs the enhanced snapshot action for each API that it calls. Examples are `kinesisanalytics:CreateSnapshot` and `kinesisanalytics:DescribeSnapshot`.

**`RestoreFromSnapshot`**  
A restore in enhanced snapshot mode needs `kinesisanalytics:RestoreFromSnapshot` on the enhanced snapshot that the restore uses.  
Managed Service for Apache Flink denies the restore by default, even for a snapshot that your own application created.  
Managed Service for Apache Flink checks this action in the following cases:  
+ [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html), in any application status.
+ [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html), for a `RUNNING` application only.
+ [`AddApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html) and [`DeleteApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html), for a `RUNNING` application only.
+ [`AddApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html) and [`DeleteApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html), for a `RUNNING` application only.
+ [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html), for a `RUNNING`, `UPDATING`, or `AUTOSCALING` application. For the snapshot that a rollback uses, see [Roll back an application](snapshots-restore.md#snapshots-restore-rollback).
Managed Service for Apache Flink does not check this action when `ApplicationRestoreType` is `SKIP_RESTORE_FROM_SNAPSHOT`. For `RESTORE_FROM_LATEST_SNAPSHOT` with `SnapshotsEnabled` set to `true`, Managed Service for Apache Flink also skips the check. This second rule applies to the following APIs:  
+ `UpdateApplication`
+ `AddApplicationVpcConfiguration` and `DeleteApplicationVpcConfiguration`
+ `AddApplicationCloudWatchLoggingOption` and `DeleteApplicationCloudWatchLoggingOption`
With `SnapshotsEnabled` set to `false`, these APIs also check an enhanced snapshot of the application in the `CREATING` status. For more information, see [Restore from the latest snapshot](snapshots-restore.md#snapshots-restore-restore-from-the-latest-snapshot).

**`CreateSystemSnapshot`**  
For an application in enhanced snapshot mode with `SnapshotsEnabled` set to `true`, the following APIs need `kinesisanalytics:CreateSystemSnapshot` on the application ARN:  
+ [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html), in any application status.
+ [`StopApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StopApplication.html), for a `RUNNING` application. A `StopApplication` request with `Force` set to `true` does not need the action.
+ [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html), for a `RUNNING` application. The request needs the action if it sets or keeps enhanced snapshot mode. The request also needs the action if `SnapshotsEnabled` is `true` after the update.
+ [`AddApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationVpcConfiguration.html), for a `RUNNING` application.
+ [`DeleteApplicationVpcConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationVpcConfiguration.html), for a `RUNNING` application.
+ [`AddApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html), for a `RUNNING` application.
+ [`DeleteApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html), for a `RUNNING` application.
[`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) and [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) do not check this action. For more information about system snapshots, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots).

**Service execution role**  
Enhanced snapshots need no changes to the service execution role.

**Customer managed keys and AWS KMS**  
Keep your existing key policy for an application that uses a customer managed key. That key policy already grants access to the service principals `kinesisanalytics.amazonaws.com` and `infrastructure.kinesisanalytics.amazonaws.com`. The caller of [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) also needs `kms:Decrypt` and `kms:GenerateDataKey` on the key.  
If the caller lacks one of these two AWS KMS permissions on the customer managed key, `CreateSnapshot` returns `AccessDeniedException`. Managed Service for Apache Flink does not run this check for an AWS owned key.

For example caller policies, see [Identity-based policy examples for enhanced snapshots](security-iam-snapshots.md#security-iam-snapshots-examples). When you write a caller policy, apply the following rules:
+ To restore from system snapshots, allow `kinesisanalytics:RestoreFromSnapshot` on `snapshot/SYSTEMSNAPSHOT-*`. This pattern matches the system snapshots of every application in the account.
+ Use `"*"` as the resource for `kinesisanalytics:ListSnapshots`, even if you call `ListSnapshots` with `SourceApplicationName`.
+ Add a AWS KMS statement only if the application uses a customer managed key.

For the full list of actions, resources, and condition keys, see [How Amazon Managed Service for Apache Flink works with IAM](security_iam_service-with-iam.md). For more policy examples, see [Identity-based policy examples for Amazon Managed Service for Apache Flink](security_iam_id-based-policy-examples.md).

## Create an application in enhanced snapshot mode
<a name="snapshots-setup-create-an-application-in-snapshot-mode"></a>

To create an application in enhanced snapshot mode, set `SnapshotMode` to `ENHANCED_SNAPSHOTS` in the `CreateApplication` request. The member is `ApplicationConfiguration.ApplicationSnapshotConfiguration.SnapshotMode`.
+ `SnapshotsEnabled` stays mandatory in `ApplicationSnapshotConfiguration`.
+ If you omit `SnapshotMode`, the application uses `APPLICATION_SNAPSHOTS_LEGACY`.
+ If you set `SnapshotMode` to `ENHANCED_SNAPSHOTS` on Apache Flink 1.19 or earlier, `CreateApplication` returns `InvalidArgumentException`.

  `CreateApplication` also returns `InvalidArgumentException` if you set `ENHANCED_SNAPSHOTS` for a runtime other than Apache Flink, such as `SQL-1_0`.
+ `CreateApplication` takes no snapshot.

**To create an application in enhanced snapshot mode**

1. Open a terminal where the AWS Command Line Interface (AWS CLI) is installed and configured.

1. Save the following JSON request as `create-application.json`.

   ```json
   {
     "ApplicationName": "MyApplication",
     "RuntimeEnvironment": "FLINK-1_20",
     "ServiceExecutionRole": "arn:aws:iam::111122223333:role/MyApplicationServiceRole",
     "ApplicationConfiguration": {
       "ApplicationCodeConfiguration": {
         "CodeContent": {
           "S3ContentLocation": {
             "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
             "FileKey": "my-flink-app.jar"
           }
         },
         "CodeContentType": "ZIPFILE"
       },
       "ApplicationSnapshotConfiguration": {
         "SnapshotsEnabled": true,
         "SnapshotMode": "ENHANCED_SNAPSHOTS"
       }
     }
   }
   ```

1. Replace the role ARN, bucket ARN, and file key in `create-application.json` with your own values.

1. Run the following AWS CLI command in the terminal to send the request.

   ```bash
   PROMPT> aws kinesisanalyticsv2 create-application --cli-input-json file://create-application.json
   ```

1. Run the following AWS CLI command in the terminal to describe the application.

   ```bash
   PROMPT> aws kinesisanalyticsv2 describe-application --application-name MyApplication
   ```

1. Confirm that `ApplicationDetail.ApplicationConfigurationDescription.ApplicationSnapshotConfigurationDescription.SnapshotMode` is `ENHANCED_SNAPSHOTS` in the [`DescribeApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.html) response.

   ```json
   {
     "ApplicationSnapshotConfigurationDescription": {
       "SnapshotsEnabled": true,
       "SnapshotMode": "ENHANCED_SNAPSHOTS"
     }
   }
   ```

### Create your first enhanced snapshot
<a name="snapshots-setup-create-your-first-enhanced-snapshot"></a>

After the application reaches the `RUNNING` status, create an enhanced snapshot with [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html). Managed Service for Apache Flink creates the enhanced snapshot asynchronously.

**To create your first enhanced snapshot**

1. Run the following AWS CLI command in the terminal to start the application with [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html).

   ```bash
   PROMPT> aws kinesisanalyticsv2 start-application --application-name MyApplication
   ```

1. Run the AWS CLI `describe-application` command in the terminal until `ApplicationStatus` is `RUNNING`.

1. Send a JSON `CreateSnapshot` request with the application name and a snapshot name. The snapshot name must be unique in the account and Region.

   ```json
   {
     "ApplicationName": "MyApplication",
     "SnapshotName": "MyApplication-snapshot-1"
   }
   ```

   Run the following AWS CLI command to send the same request:

   ```bash
   PROMPT> aws kinesisanalyticsv2 create-snapshot \
       --application-name MyApplication \
       --snapshot-name MyApplication-snapshot-1
   ```

   Replace `MyApplication` with the name of your application. Replace `MyApplication-snapshot-1` with a name for the enhanced snapshot.

   If the request fails, check the exception. `AccessDeniedException` means that the caller lacks `kinesisanalytics:CreateSnapshot` or a required AWS KMS permission. `InvalidArgumentException` means that the snapshot name breaks the name rules. For all errors, see [Troubleshoot snapshot API errors](snapshots-manage.md#snapshots-manage-errors).

   Creating the enhanced snapshot can take several minutes. In the response, `SnapshotStatus` is `CREATING`. Note the `SnapshotOperationId` value. You use it if the enhanced snapshot fails. For the full response, see [Create an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-createsnapshot).

**To verify your first enhanced snapshot**

1. Call [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html) in the terminal with the snapshot name. Repeat the call until `SnapshotStatus` is `READY` or `FAILED`. This process might take several minutes.

   ```bash
   PROMPT> aws kinesisanalyticsv2 describe-snapshot --snapshot-name MyApplication-snapshot-1
   ```

   The status is in `SnapshotInfoDetails.SnapshotStatus`. For the full response, see [Describe an enhanced snapshot](snapshots-api-examples.md#snapshots-api-examples-describesnapshot).

1. Call [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) if `SnapshotStatus` is `FAILED`. Use the `SnapshotOperationId` from the `CreateSnapshot` response. The following example shell script checks the status and prints the failure details:

   ```bash
   PROMPT> STATUS=$(aws kinesisanalyticsv2 describe-snapshot \
       --snapshot-name MyApplication-snapshot-1 \
       --query 'SnapshotInfoDetails.SnapshotStatus' \
       --output text)
   PROMPT> if [ "$STATUS" = "FAILED" ]; then
       aws kinesisanalyticsv2 describe-snapshot-operation --snapshot-name MyApplication-snapshot-1 \
           --snapshot-operation-id a1B2c3D4e5F6 \
           --query 'SnapshotOperationInfoDetails.SnapshotOperationFailureDetails'
   fi
   ```

   In this example, replace `a1B2c3D4e5F6` with your `SnapshotOperationId` value. For more information about snapshot operations, see [Monitor enhanced snapshot operations](snapshots-monitor-operations.md).

For the errors that `CreateSnapshot` returns, see [Troubleshoot snapshot API errors](snapshots-manage.md#snapshots-manage-errors).

The legacy [`CreateApplicationSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplicationSnapshot.html) API returns `InvalidApplicationConfigurationException` for an application in enhanced snapshot mode.

Wait until the enhanced snapshot status is `READY` before you call `UpdateApplication`.