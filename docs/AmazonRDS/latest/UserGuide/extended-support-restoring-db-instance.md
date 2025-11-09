# Restoring a DB instance or a Multi-AZ DB cluster with Amazon RDS Extended Support

When you restore a DB instance or a Multi-AZ DB cluster, select **Enable
RDS Extended Support** in the console, or use the Extended Support option in the AWS CLI or the
parameter in the RDS API. When you enroll a DB instance or
Multi-AZ DB cluster in
RDS Extended Support, it is permanently enrolled in RDS Extended Support for the life of the DB instance or Multi-AZ DB cluster.

The default for the RDS Extended Support setting depends on whether you use the console, the AWS CLI,
or the RDS API to restore your database. If you use the console, you don't select
**Enable RDS Extended Support**, and the major engine version you are restoring
is past the RDS end of standard support, then Amazon RDS automatically upgrades
your DB instance to a newer engine version. If you use the AWS CLI or the RDS API and you
don't specify the RDS Extended Support setting, then Amazon RDS defaults to enabling RDS Extended Support. When you
automate by using [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance-return-values:~:text=EngineLifecycleSupport "../../../AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbinstance.md#aws-resource-rds-dbinstance-return-values:~:text=EngineLifecycleSupport") or other services, this default behavior maintains the availability of
your database past the RDS end of standard support date. You can disable RDS Extended Support by using the
AWS CLI or the RDS API.

###### Topics

- [RDS Extended Support
  behavior](#extended-support-restoring-db-instance-behavior "#extended-support-restoring-db-instance-behavior")
- [Considerations
  for RDS Extended Support](#extended-support-restoring-db-instance-considerations "#extended-support-restoring-db-instance-considerations")
- [Restore a DB instance or a Multi-AZ DB cluster with
  RDS Extended Support](#extended-support-restoring-db-instance-restore "#extended-support-restoring-db-instance-restore")

## RDS Extended Support

behavior

The following table summarizes what happens when a major engine version of a DB instance or a Multi-AZ DB cluster that you are restoring has reached the RDS end of
standard support.

| RDS Extended Support status\* | Behavior                                                                                                                                                                   |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enabled                       | Amazon RDS charges you for RDS Extended Support.                                                                                                                           |
| Disabled\*\*                  | After the restore finishes, Amazon RDS automatically upgrades your<br>DB instance or<br>Multi-AZ DB cluster to a newer engine version (in a future<br>maintenance window). |

\* In the RDS console, the RDS Extended Support status appears as Yes or No. In the AWS CLI or
RDS API, the RDS Extended Support status appears as `open-source-rds-extended-support`
or `open-source-rds-extended-support-disabled`.

\*\* This option is only available when restoring a DB instance or a Multi-AZ DB cluster running PostgreSQL 12 and higher or MySQL 8 and
higher.

## Considerations

for RDS Extended Support

Before restoring a DB instance or a
Multi-AZ DB cluster,
consider the following items:

- _After_ the RDS end of standard
  support date has passed, if you want to restore a
  DB instance or a Multi-AZ DB cluster from Amazon S3, you can only do so by using the AWS CLI or
  the RDS API. Use the `--engine-lifecycle-support` option in the
  [restore-db-cluster-from-s3](../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md "../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md") AWS CLI command or the
  `EngineLifecycleSupport` parameter in the [RestoreDBClusterFromS3](../APIReference/API_RestoreDBClusterFromS3.md "../APIReference/API_RestoreDBClusterFromS3.md") RDS API operation.
- If you want to prevent RDS from restoring your databases to
  RDS Extended Support versions, specify
  `open-source-rds-extended-support-disabled` in the AWS CLI or the
  RDS API. By doing so, you will avoid any associated RDS Extended Support charges.

If you specify this setting, Amazon RDS will
automatically upgrade your restored database to a newer, supported major
version. If the upgrade fails pre-upgrade checks, Amazon RDS will safely
roll back to the RDS Extended Support engine version. This database will remain in
RDS Extended Support mode, and Amazon RDS will charge you for RDS Extended Support until
you manually upgrade your database.

For example, if you restore a MySQL 5.7 snapshot without
using RDS Extended Support, Amazon RDS will attempt to automatically upgrade your database to
MySQL 8.0. If this upgrade fails because of an issue that you need to resolve,
Amazon RDS will roll back the database to MySQL 5.7. Amazon RDS will keep the database on
RDS Extended Support until you can fix the issue. For example, an upgrade might fail
because of insufficient storage space. After you fix the issue, you must
initiate the upgrade. After the first attempt to upgrade your database, Amazon RDS
won't attempt to upgrade it again.

- RDS Extended Support is set at the cluster level. Members of a cluster will always have
  the same setting for RDS Extended Support in the RDS console,
  `--engine-lifecycle-support` in the AWS CLI, and
  `EngineLifecycleSupport` in the RDS API.

For more information, see [MySQL versions](MySQL.Concepts.md "MySQL.Concepts.md") and [Release calendars for Amazon RDS for PostgreSQL](../PostgreSQLReleaseNotes/postgresql-release-calendar.md "../PostgreSQLReleaseNotes/postgresql-release-calendar.md").

## Restore a DB instance or a Multi-AZ DB cluster with

RDS Extended Support

You can restore a DB instance or a Multi-AZ DB cluster with an RDS Extended Support version
using the AWS Management Console, the AWS CLI, or the RDS API.

When you restore a DB instance or a
Multi-AZ DB cluster, select **Enable RDS Extended Support** in the
**Engine options** section. If you don't select this
setting and the major engine version that you are restoring is past the RDS
end of standard support, then Amazon RDS automatically
upgrades your DB instance or Multi-AZ DB cluster
to a version under RDS standard support.

The following image shows the **Enable RDS Extended Support**
setting:

![The Enable RDS Extended Support setting in the Engine options section.](images/extended-support-enable.png)
When you run the [restore-db-instance-from-db-snapshot](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md") or [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md") AWS CLI command, select
RDS Extended Support by specifying `open-source-rds-extended-support` for the
`--engine-lifecycle-support` option.

If you want to avoid charges associated with RDS Extended Support, set the
`--engine-lifecycle-support` option to
`open-source-rds-extended-support-disabled`. By default, this
option is set to `open-source-rds-extended-support`.

You can also specify this value using the following AWS CLI commands:

- [restore-db-cluster-from-s3](../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md "../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md")
- [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
- [restore-db-instance-from-s3](../../../cli/latest/reference/rds/restore-db-instance-from-s3.md "../../../cli/latest/reference/rds/restore-db-instance-from-s3.md")
- [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")
  When you use the
  [RestoreDBInstanceFromDBSnapshot](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md") or [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md") Amazon RDS API operation,
  select RDS Extended Support by setting the `EngineLifecycleSupport` parameter
  to `open-source-rds-extended-support`.

If you want to avoid charges associated with RDS Extended Support, set the
`EngineLifecycleSupport` parameter to
`open-source-rds-extended-support-disabled`. By default, this
parameter is set to `open-source-rds-extended-support`.

You can also specify this value using the following RDS API operations:

- [RestoreDBClusterFromS3](../APIReference/API_RestoreDBClusterFromS3.md "../APIReference/API_RestoreDBClusterFromS3.md")
- [RestoreDBClusterToPointInTime](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md")
- [RestoreDBInstanceFromS3](../APIReference/API_RestoreDBInstanceFromS3.md "../APIReference/API_RestoreDBInstanceFromS3.md")
- [RestoreDBInstanceToPointInTime](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")

For more information about restoring a DB instance or a Multi-AZ DB cluster,
follow the instructions for your DB engine in [Restoring to a DB instance](USER_RestoreFromSnapshot.md "USER_RestoreFromSnapshot.md").
