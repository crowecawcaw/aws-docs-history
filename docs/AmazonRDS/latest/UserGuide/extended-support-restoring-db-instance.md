

# Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support
<a name="extended-support-restoring-db-instance"></a>

When you restore a DB instance or a Multi-AZ DB cluster, select **Enable RDS Extended Support** in the console, or use the Extended Support option in the AWS CLI or the parameter in the RDS API. When you enroll a DB instance or Multi-AZ DB cluster in RDS Extended Support, it is permanently enrolled in RDS Extended Support for the life of the DB instance or Multi-AZ DB cluster. 

The default for the RDS Extended Support setting depends on whether you use the console, the AWS CLI, or the RDS API to restore your database. If you use the console, you don't select **Enable RDS Extended Support**, and the major engine version you are restoring is past the RDS end of standard support, then Amazon RDS automatically upgrades your DB instance to a newer engine version. If you use the AWS CLI or the RDS API and you don't specify the RDS Extended Support setting, then Amazon RDS defaults to enabling RDS Extended Support. When you automate by using [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.html#aws-resource-rds-dbinstance-return-values:~:text=EngineLifecycleSupport) or other services, this default behavior maintains the availability of your database past the RDS end of standard support date. You can disable RDS Extended Support by using the AWS CLI or the RDS API.

**Topics**
+ [RDS Extended Support behavior](#extended-support-restoring-db-instance-behavior)
+ [Considerations for RDS Extended Support](#extended-support-restoring-db-instance-considerations)
+ [Restore a DB instance or a Multi-AZ DB cluster with RDS Extended Support](#extended-support-restoring-db-instance-restore)

## RDS Extended Support behavior
<a name="extended-support-restoring-db-instance-behavior"></a>

The following table summarizes what happens when a major engine version of a DB instance or a Multi-AZ DB cluster that you are restoring has reached the RDS end of standard support. 


| RDS Extended Support status\* | Behavior | 
| --- | --- | 
| Enabled | Amazon RDS charges you for RDS Extended Support. | 
| Disabled\*\* | After the restore finishes, Amazon RDS automatically upgrades your DB instance or Multi-AZ DB cluster to a newer engine version (in a future maintenance window). | 

\* In the RDS console, the RDS Extended Support status appears as Yes or No. In the AWS CLI or RDS API, the RDS Extended Support status appears as `open-source-rds-extended-support` or `open-source-rds-extended-support-disabled`.

\*\* This option is only available when restoring a DB instance or a Multi-AZ DB cluster running PostgreSQL 12 and higher or MySQL 8 and higher.

## Considerations for RDS Extended Support
<a name="extended-support-restoring-db-instance-considerations"></a>

Before restoring a DB instance or a Multi-AZ DB cluster, consider the following items:
+ *After* the RDS end of standard support date has passed, if you want to restore a DB instance or a Multi-AZ DB cluster from Amazon S3, you can only do so by using the AWS CLI or the RDS API. Use the `--engine-lifecycle-support` option in the [restore-db-cluster-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-s3.html) AWS CLI command or the `EngineLifecycleSupport` parameter in the [RestoreDBClusterFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromS3.html) RDS API operation. 
+ If you want to prevent RDS from restoring your databases to RDS Extended Support versions, specify `open-source-rds-extended-support-disabled` in the AWS CLI or the RDS API. By doing so, you will avoid any associated RDS Extended Support charges. 

  If you specify this setting, Amazon RDS will automatically upgrade your restored database to a newer, supported major version. If the upgrade fails pre-upgrade checks, Amazon RDS will safely roll back to the RDS Extended Support engine version. This database will remain in RDS Extended Support mode, and Amazon RDS will charge you for RDS Extended Support until you manually upgrade your database.

  For example, if you restore a MySQL 5.7 snapshot without using RDS Extended Support, Amazon RDS will attempt to automatically upgrade your database to MySQL 8.0. If this upgrade fails because of an issue that you need to resolve, Amazon RDS will roll back the database to MySQL 5.7. Amazon RDS will keep the database on RDS Extended Support until you can fix the issue. For example, an upgrade might fail because of insufficient storage space. After you fix the issue, you must initiate the upgrade. After the first attempt to upgrade your database, Amazon RDS won't attempt to upgrade it again.
+ RDS Extended Support is set at the cluster level. Members of a cluster will always have the same setting for RDS Extended Support in the RDS console, `--engine-lifecycle-support` in the AWS CLI, and `EngineLifecycleSupport` in the RDS API.

For more information, see [MySQL versions](MySQL.Concepts.VersionMgmt.md) and [Release calendars for Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/PostgreSQLReleaseNotes/postgresql-release-calendar.html).

## Restore a DB instance or a Multi-AZ DB cluster with RDS Extended Support
<a name="extended-support-restoring-db-instance-restore"></a>

You can restore a DB instance or a Multi-AZ DB cluster with an RDS Extended Support version using the AWS Management Console, the AWS CLI, or the RDS API. 

### Console
<a name="extended-support-restoring-db-instance-restore-console"></a>

When you restore a DB instance or a Multi-AZ DB cluster, select **Enable RDS Extended Support** in the **Engine options** section. If you don't select this setting and the major engine version that you are restoring is past the RDS end of standard support, then Amazon RDS automatically upgrades your DB instance or Multi-AZ DB cluster to a version under RDS standard support.

The following image shows the **Enable RDS Extended Support** setting:

![The Enable RDS Extended Support setting in the Engine options section.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/extended-support-enable.png)


### AWS CLI
<a name="extended-support-restoring-db-instance-restore-cli"></a>

When you run the [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html) or [restore-db-cluster-from-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-snapshot.html) AWS CLI command, select RDS Extended Support by specifying `open-source-rds-extended-support` for the `--engine-lifecycle-support` option. 

If you want to avoid charges associated with RDS Extended Support, set the `--engine-lifecycle-support` option to `open-source-rds-extended-support-disabled`. By default, this option is set to `open-source-rds-extended-support`.

You can also specify this value using the following AWS CLI commands:
+ [restore-db-cluster-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-s3.html)
+ [restore-db-cluster-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-to-point-in-time.html)
+ [restore-db-instance-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-s3.html)
+ [restore-db-instance-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html)

### RDS API
<a name="extended-support-restoring-db-instance-restore-api"></a>

When you use the [RestoreDBInstanceFromDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html) or [RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.html) Amazon RDS API operation, select RDS Extended Support by setting the `EngineLifecycleSupport` parameter to `open-source-rds-extended-support`. 

If you want to avoid charges associated with RDS Extended Support, set the `EngineLifecycleSupport` parameter to `open-source-rds-extended-support-disabled`. By default, this parameter is set to `open-source-rds-extended-support`.

You can also specify this value using the following RDS API operations:
+ [RestoreDBClusterFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromS3.html)
+ [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html)
+ [RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html)
+ [RestoreDBInstanceToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html)

For more information about restoring a DB instance or a Multi-AZ DB cluster, follow the instructions for your DB engine in [Restoring to a DB instance](USER_RestoreFromSnapshot.md).