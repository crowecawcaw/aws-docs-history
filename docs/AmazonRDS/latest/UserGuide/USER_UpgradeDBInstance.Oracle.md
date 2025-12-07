# Overview of RDS for Oracle engine upgrades

Before upgrading your RDS for Oracle DB instance, familiarize yourself with the following
concepts.

###### Topics

- [Major and minor version upgrades](#USER_UpgradeDBInstance.Oracle.Overview.versions "#USER_UpgradeDBInstance.Oracle.Overview.versions")
- [Support dates and mandatory
  upgrades for RDS for Oracle](#Aurora.VersionPolicy.MajorVersionLifetime "#Aurora.VersionPolicy.MajorVersionLifetime")
- [Oracle engine version management](#Oracle.Concepts.Patching "#Oracle.Concepts.Patching")
- [Automatic snapshots during engine
  upgrades](#USER_UpgradeDBInstance.Oracle.Overview.snapshots "#USER_UpgradeDBInstance.Oracle.Overview.snapshots")
- [Oracle upgrades in a Multi-AZ deployment](#USER_UpgradeDBInstance.Oracle.Overview.multi-az "#USER_UpgradeDBInstance.Oracle.Overview.multi-az")
- [Oracle upgrades of read replicas](#USER_UpgradeDBInstance.Oracle.Overview.read-replicas "#USER_UpgradeDBInstance.Oracle.Overview.read-replicas")

## Major and minor version upgrades

Major versions are major releases of Oracle Database that occur every 1-2 years.
Oracle Database 19c and Oracle Database 21c are major releases.

Every quarter, RDS for Oracle releases new minor engine versions for every supported major
engine. A Release Update (RU) engine version incorporates bug fixes from Oracle by
including the RU patches for the specified quarter. For example,
21.0.0.0.ru-2024-10.rur-2024-10.r1 is a minor version of Oracle Database 21c that
incorporates the October 2024 RU.

A Spatial Patch Bundle (SPB) engine version contains RU patches and patches specific
to Oracle Spatial. For example, 19.0.0.0.ru-2025-01.spb-1.r1 is a minor engine version
that contains the RU patches in engine version 19.0.0.0.ru-2025-01.rur-2025-01.r1 plus
Spatial patches. Typically, RDS for Oracle releases SPBs 2–3 weeks after the
corresponding RU. For an explanation of the differences between RUs and SPBs, see [Release Updates (RUs) and Spatial Patch Bundles
(SPBs)](USER_UpgradeDBInstance.Oracle.md#RUs-and-SPBs "USER_UpgradeDBInstance.Oracle.md#RUs-and-SPBs"). For information about
supported RUs and SPBs, see [Release notes for Amazon Relational Database Service (Amazon RDS) for
Oracle](../OracleReleaseNotes.md "../OracleReleaseNotes.md").

RDS for Oracle supports the following upgrades to a DB instance.

| Upgrade type  | Application compatibility                                                                                 | Upgrade methods     | Sample upgrade path                                                              |
| ------------- | --------------------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------- |
| Major version | A major version upgrade can introduce changes that aren't compatible<br>with existing applications.       | Manual only         | From Oracle Database 19c to Oracle Database 21c                                  |
| Minor version | A minor version upgrade includes only changes that are<br>backward-compatible with existing applications. | Automatic or manual | From 21.0.0.0.ru-2023-07.rur-2022-07.r1 to<br>21.0.0.0.ru-2023-10.rur-2022-10.r1 |

###### Important

When you upgrade your DB engine, an outage occurs. The duration of the outage depends
on your engine version and DB instance size.

Make sure that you thoroughly test any upgrade to verify that your applications
work correctly before applying the upgrade to your production databases. For more
information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.md "USER_UpgradeDBInstance.Oracle.md").

## Support dates and mandatory

upgrades for RDS for Oracle

Database versions of RDS for Oracle have expected support dates. When a major or minor
version of an RDS for Oracle DB engine nears its end-of-support date, RDS begins mandatory
upgrades, also known as _forced upgrades_. RDS publishes the
following information:

- A recommendation for you to begin manually upgrading instances on deprecated
  versions to supported versions
- A date after which you can no longer create instances on the unsupported
  versions
- A date on which RDS begins to upgrade your instances to supported versions
  automatically during maintenance windows
- A date on which RDS begins to upgrade your instances to supported versions
  automatically outside of maintenance windows

###### Important

Forced upgrades can have unexpected consequences for CloudFormation stacks. If you rely on
RDS to upgrade your DB instances automatically, you might encounter issues with
CloudFormation.

This section contains the following topics:

###### Topics

- [Support dates for major releases of
  RDS for Oracle](#oracle-major-support-dates "#oracle-major-support-dates")
- [Support dates for minor versions of
  RDS for Oracle](#oracle-minor-support-dates "#oracle-minor-support-dates")

### Support dates for major releases of

RDS for Oracle

RDS for Oracle major versions remain available at least until the end of support date
for the corresponding Oracle Database release version. You can use the following
dates to plan your testing and upgrade cycles. These dates represent the earliest
date that an upgrade to a newer version might be required. If Amazon extends
support for an RDS for Oracle version for longer than originally stated, we plan to update
this table to reflect the later date.

###### Note

You can view the major versions of your Oracle databases by running the [describe-db-major-engine-versions](../../../cli/latest/reference/rds/describe-db-major-engine-versions.md "../../../cli/latest/reference/rds/describe-db-major-engine-versions.md") AWS CLI command or by using the
[DescribeDBMajorEngineVersions](../APIReference/API_DescribeDBMajorEngineVersions.md "../APIReference/API_DescribeDBMajorEngineVersions.md") RDS API operation.

| Oracle Database major release version | Expected date for upgrading to a newer version                                                                                                                                                                                      |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oracle Database 19c                   | December 31, 2029 with BYOL Premier Support (fees waived for<br>Extended Support)<br>December 31, 2032 with BYOL Extended Support (extra cost) or<br>an Unlimited License Agreement<br>December 31, 2029 with License Included (LI) |
| Oracle Database 21c                   | July 31, 2027 (not available for Extended Support)                                                                                                                                                                                  |

RDS notifies you at least 12 months before you need to upgrade to a newer major
version. The notification describes the upgrade process, including the timing of
important milestones, the effect on your DB instances, and recommended actions. We
recommend that you thoroughly test your applications with new RDS for Oracle versions
before you upgrade your database to a major version.

After this advance notification period, an automatic upgrade to the subsequent
major version might be applied to any RDS for Oracle DB instance still running the older
version. If so, the upgrade is started during scheduled maintenance windows.

For more information, see [Release Schedule of Current Database Releases](https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html "https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html") in My Oracle
Support.

### Support dates for minor versions of

RDS for Oracle

In some cases, we end support for minor versions of major releases in RDS for Oracle.
RDS notifies you at least 12 months before you need to upgrade to a newer minor
version. The notification describes the upgrade process, including the timing of
important milestones, the effect on the DB instances running the deprecated minor version,
and recommended actions. We recommend that you thoroughly test your applications
with new RDS for Oracle versions before you upgrade your database to a new minor
version.

For more information about deprecated and desupported minor versions, see [Release notes for
Amazon Relational Database Service (Amazon RDS) for Oracle](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md").

## Oracle engine version management

With DB engine version management, you control when and how the database engine is patched and upgraded. You get the flexibility to
maintain compatibility with database engine patch versions. You can also test new patch versions of RDS for Oracle to ensure they work with your
application before deploying them in production. In addition, you upgrade the versions on your own terms and timelines.

###### Note

Amazon RDS periodically aggregates official Oracle database patches using an Amazon RDS-specific DB engine
version. To see a list of which Oracle patches are contained in an Amazon RDS Oracle-specific engine version,
go to [_Amazon RDS for Oracle Release Notes_](../OracleReleaseNotes/Welcome.md "../OracleReleaseNotes/Welcome.md").

## Automatic snapshots during engine

upgrades

During upgrades of an Oracle DB instance, snapshots offer protection against upgrade issues. If the backup
retention period for your DB instance is greater than 0, Amazon RDS takes the following DB snapshots during the
upgrade:

1. A snapshot of the DB instance before any upgrade changes have been made. If the upgrade fails, you
   can restore this snapshot to create a DB instance running the old version.
2. A snapshot of the DB instance after the upgrade completes.

###### Note

To change your backup retention period, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

After an upgrade, you can't revert to the previous engine version. However, you can create a new Oracle DB
instance by restoring the pre-upgrade snapshot.

## Oracle upgrades in a Multi-AZ deployment

If your DB instance is in a Multi-AZ deployment, Amazon RDS upgrades both the
primary and standby replicas. If no operating system updates are required, the
primary and standby upgrades occur simultaneously. The instances are not available
until the upgrade completes.

If operating system updates are required in a Multi-AZ deployment, Amazon RDS applies the
updates when you request the database upgrade. Amazon RDS performs the following
steps:

1. Updates the operating system on the current standby DB instance.
2. Fails over the primary DB instance to the standby DB instance.
3. Upgrades the database version on the new primary DB instance, which was formerly the
   standby instance. The primary database is unavailable during the upgrade.
4. Updates the operating system on the new standby DB instance, which was formerly the
   primary DB instance.
5. Upgrades the database version on the new standby DB instance.
6. Fails over the new primary DB instance back to the original primary DB instance, and the
   new standby DB instance back to the original standby DB instance. Thus, Amazon RDS returns the
   replication configuration to its original state.

## Oracle upgrades of read replicas

The Oracle DB engine version of the source DB instance and all of its read replicas must be the same.
Amazon RDS performs the upgrade in the following stages:

1. Upgrades the source DB instance. The read replicas are available during
   this stage.
2. Upgrades the read replicas in parallel, regardless of the replica
   maintenance windows. The source DB is available during this stage.

For major version upgrades of cross-Region read replicas, Amazon RDS performs
additional actions:

- Generates an option group for the target version automatically
- Copies all options and option settings from the original option group to
  the new option group
- Associates the upgraded cross-Region read replica with the new option
  group
