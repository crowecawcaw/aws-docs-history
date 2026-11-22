

# Use in-place version upgrades for Apache Flink

With in-place version upgrades for Apache Flink, you retain application traceability against a single ARN across Apache Flink versions. This includes snapshots, logs, metrics, tags, Flink configurations, resource limit increases, VPCs, and more. 

You can perform in-place version upgrades for Apache Flink to upgrade existing applications to a new Flink version in Amazon Managed Service for Apache Flink. To perform this task, you can use the AWS CLI, AWS CloudFormation, AWS SDK, or the AWS Management Console.

**Note**  
You can't use in-place version upgrades for Apache Flink with Amazon Managed Service for Apache Flink Studio.

An application in enhanced snapshot mode uses enhanced snapshots for in-place version upgrades. Enhanced snapshot mode requires Apache Flink version 1.20 or later.

If `SnapshotsEnabled` is `true`, an [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) request on a `RUNNING` application creates a system snapshot. In enhanced snapshot mode, this system snapshot is an enhanced snapshot. In enhanced snapshot mode, the caller also needs `kinesisanalytics:CreateSystemSnapshot` on the application ARN.

In enhanced snapshot mode, `RESTORE_FROM_LATEST_SNAPSHOT` restores the newest `READY` enhanced snapshot that the application created. If no `READY` enhanced snapshot exists, the application starts without state. Managed Service for Apache Flink does not restore an application snapshot (legacy) in this case. For more information, see [System snapshots](snapshots-how-it-works.md#snapshots-how-it-works-system-snapshots) and [Restore from the latest snapshot](snapshots-restore.md#snapshots-restore-restore-from-the-latest-snapshot).

**Topics**
+ [Upgrade applications using in-place version upgrades for Apache Flink](upgrading-applications.md)
+ [Upgrade your application to a new Apache Flink version](upgrading-application-new-version.md)
+ [Roll back application upgrades](rollback.md)
+ [General best practices and recommendations for application upgrades](best-practices-recommendations.md)
+ [Precautions and known issues with application upgrades](precautions.md)
+ [Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md)
+ [State compatibility guide for Flink 2.2 upgrades](state-compatibility.md)