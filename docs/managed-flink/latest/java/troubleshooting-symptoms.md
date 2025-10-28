Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Application issues

This section contains solutions for error conditions that you may encounter with your
Managed Service for Apache Flink application.

###### Topics

- [Application is stuck in a
  transient status](#troubleshooting-rt-stuck "#troubleshooting-rt-stuck")
- [Snapshot creation fails](#troubleshooting-rt-snapshots "#troubleshooting-rt-snapshots")
- [Cannot access resources in a
  VPC](#troubleshooting-rt-vpc "#troubleshooting-rt-vpc")
- [Data is lost when writing to an Amazon S3
  bucket](#troubleshooting-rt-s3 "#troubleshooting-rt-s3")
- [Application is in the
  RUNNING status but isn't processing data](#troubleshooting-rt-processing "#troubleshooting-rt-processing")
- [Snapshot,
  application update, or application stop error:
  InvalidApplicationConfigurationException](#troubleshooting-rt-appconfigexception "#troubleshooting-rt-appconfigexception")
- [java.nio.file.NoSuchFileException:
  /usr/local/openjdk-8/lib/security/cacerts](#troubleshooting-rt-fnf "#troubleshooting-rt-fnf")

## Application is stuck in a

transient status

If your application stays in a transient status (`STARTING`,
`UPDATING`, `STOPPING`, or `AUTOSCALING`), you
can stop your application by using the [StopApplication](../apiv2/API_StopApplication.md "../apiv2/API_StopApplication.md") action with the `Force`
parameter set to `true`. You can't force stop an application in the
`DELETING` status. Alternatively, if the application is in the
`UPDATING` or `AUTOSCALING` status, you can roll it back
to the previous running version. When you roll back an application, it loads state
data from the last successful snapshot. If the application has no snapshots, Managed Service for Apache Flink
rejects the rollback request. For more information about rolling back an
application, see [RollbackApplication](../apiv2/API_RollbackApplication.md "../apiv2/API_RollbackApplication.md") action.

###### Note

Force-stopping your application may lead to data loss or duplication.
To prevent data loss or duplicate processing of data during application restarts,
we recommend you to take frequent snapshots of your application.

Causes
for stuck applications include the following:

- **Application state is too large:** Having an application state that is too large or too persistent can cause the application to become stuck during a checkpoint or snapshot operation. Check your application's `lastCheckpointDuration` and `lastCheckpointSize` metrics for steadily increasing values or abnormally high values.
- **Application code is too large:** Verify that your application JAR file is smaller than 512 MB. JAR files larger than 512 MB are not supported.
- **Application snapshot creation fails:**
  Managed Service for Apache Flink takes a snapshot of the application during an [`UpdateApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.md") or [`StopApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_StopApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_StopApplication.md") request. The service then uses
  this snapshot state and restores the application using the updated
  application configuration to provide _exactly-once_
  processing semantics.If automatic snapshot creation fails, see
  [Snapshot creation fails](#troubleshooting-rt-snapshots "#troubleshooting-rt-snapshots")
  following.
- **Restoring from a snapshot fails:** If you
  remove or change an operator in an application update and attempt to restore
  from a snapshot, the restore will fail by default if the snapshot contains
  state data for the missing operator. In addition, the application will be
  stuck in either the `STOPPED` or `UPDATING` status. To
  change this behavior and allow the restore to succeed, change the
  _AllowNonRestoredState_ parameter of the
  application's [FlinkRunConfiguration](../apiv2/API_FlinkRunConfiguration.md "../apiv2/API_FlinkRunConfiguration.md") to `true`. This will allow the
  resume operation to skip state data that cannot be mapped to the new
  program.
- **Application initialization taking longer:** Managed Service for Apache Flink uses an internal timeout of 5 minutes
  (soft setting) while waiting for a Flink job to start.
  If your job is failing to start within this timeout, you will see a CloudWatch log as follows:

```
Flink job did not start within a total timeout of 5 minutes for application: %s under account: %s
```

If you encounter the above error, it means that your operations defined under Flink job’s `main`
method are taking more than 5 minutes, causing the Flink job creation to time out on the Managed Service for Apache Flink end. We suggest you
check the Flink **JobManager** logs as well as your application code to see if this delay
in the `main` method is expected. If not, you need to take steps to address the issue so it completes in under 5 minutes.

You can check your application status using either the [`ListApplications`](../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md") or the [`DescribeApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md") actions.

## Snapshot creation fails

The Managed Service for Apache Flink service can't take a snapshot under the following circumstances:

- The application exceeded the snapshot limit. The limit for snapshots is 1,000.
  For more information, see [Manage application backups using
  snapshots](how-snapshots.md "how-snapshots.md").
- The application doesn't have permissions to access its source or sink.
- The application code isn't functioning properly.
- The application is experiencing other configuration issues.

If you get an exception while taking a snapshot during an application update or while
stopping the application, set the `SnapshotsEnabled`
property of your application's [`ApplicationSnapshotConfiguration`](../../../managed-service-for-apache-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.md") to `false` and
retry the request.

Snapshots can fail if your application's operators are not properly provisioned. For
information about tuning operator performance, see
[Operator scaling](performance-improving.md#performance-improving-scaling-op "performance-improving.md#performance-improving-scaling-op").

After the application returns to a healthy state, we recommend that you
set the application's `SnapshotsEnabled` property to `true`.

## Cannot access resources in a

VPC

If your application uses a VPC running on Amazon VPC, do the following to verify that your application has access to its resources:

- Check your CloudWatch logs for the following error. This error indicates that
  your application cannot access resources in your VPC:

```
org.apache.kafka.common.errors.TimeoutException: Failed to update metadata after 60000 ms.
```

If you see this error, verify that your route tables are set up correctly,
and that your connectors have the correct connection settings.

For information about setting up and analyzing CloudWatch logs, see [Logging and monitoring in Amazon Managed Service for Apache Flink](monitoring-overview.md "monitoring-overview.md").

## Data is lost when writing to an Amazon S3

bucket

Some data loss might occur when writing output to an Amazon S3 bucket using Apache Flink version 1.6.2.
We recommend using the latest supported version of Apache Flink when using Amazon S3 for output directly. To
write to an Amazon S3 bucket using Apache Flink 1.6.2, we recommend using Firehose. For more information about using Firehose with Managed Service for Apache Flink, see [Firehose sink](earlier.md#get-started-exercise-fh "earlier.md#get-started-exercise-fh").

## Application is in the

RUNNING status but isn't processing data

You can check your application status by using either the [`ListApplications`](../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md "../../../managed-service-for-apache-flink/latest/apiv2/API_ListApplications.md") or the [`DescribeApplication`](../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md "../../../managed-service-for-apache-flink/latest/apiv2/API_DescribeApplication.md") actions. If your application enters the `RUNNING` status but isn't writing data to your sink, you can troubleshoot the issue by adding an Amazon CloudWatch log stream to your application. For more information, see [Work with application CloudWatch logging
options](cloudwatch-logs.md#adding_cloudwatch "cloudwatch-logs.md#adding_cloudwatch"). The log stream contains messages that you can use to troubleshoot application issues.

## Snapshot,

application update, or application stop error:
InvalidApplicationConfigurationException

An error similar to the following might occur during a snapshot operation, or during an operation that creates a snapshot, such as updating or stopping an application:

```
An error occurred (InvalidApplicationConfigurationException) when calling the UpdateApplication operation:

Failed to take snapshot for the application xxxx at this moment. The application is currently experiencing downtime.
Please check the application's CloudWatch metrics or CloudWatch logs for any possible errors and retry the request.
You can also retry the request after disabling the snapshots in the Managed Service for Apache Flink console or by updating
the ApplicationSnapshotConfiguration through the AWS SDK
```

This error occurs when the application is unable to create a snapshot.

If you encounter this error during a snapshot operation or an operation that
creates a snapshot, do the following:

- Disable snapshots for your application. You can do this either in the
  Managed Service for Apache Flink console, or by using the `SnapshotsEnabledUpdate` parameter
  of the [UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action.
- Investigate why snapshots cannot be created. For more information, see
  [Application is stuck in a
  transient status](#troubleshooting-rt-stuck "#troubleshooting-rt-stuck").
- Reenable snapshots when the application returns to a healthy state.

## java.nio.file.NoSuchFileException:

/usr/local/openjdk-8/lib/security/cacerts

The location of the SSL truststore was updated in a previous deployment. Use the following value for the `ssl.truststore.location` parameter instead:

```
/usr/lib/jvm/java-11-amazon-corretto/lib/security/cacerts
```
