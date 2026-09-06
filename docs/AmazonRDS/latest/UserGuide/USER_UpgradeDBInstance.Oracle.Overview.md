

# Overview of RDS for Oracle engine upgrades
<a name="USER_UpgradeDBInstance.Oracle.Overview"></a>

Before upgrading your RDS for Oracle DB instance, familiarize yourself with the following concepts.

**Topics**
+ [Major and minor version upgrades](#USER_UpgradeDBInstance.Oracle.Overview.versions)
+ [Support dates and mandatory upgrades for RDS for Oracle](#Aurora.VersionPolicy.MajorVersionLifetime)
+ [Oracle engine version management](#Oracle.Concepts.Patching)
+ [Pre-upgrade checklist](#USER_UpgradeDBInstance.Oracle.Overview.pre-upgrade-checklist)
+ [Automatic snapshots during engine upgrades](#USER_UpgradeDBInstance.Oracle.Overview.snapshots)
+ [Oracle upgrades in a Multi-AZ deployment](#USER_UpgradeDBInstance.Oracle.Overview.multi-az)
+ [Oracle upgrades of read replicas](#USER_UpgradeDBInstance.Oracle.Overview.read-replicas)
+ [Post-upgrade validation](#USER_UpgradeDBInstance.Oracle.Overview.post-upgrade-validation)

## Major and minor version upgrades
<a name="USER_UpgradeDBInstance.Oracle.Overview.versions"></a>

Major versions are major releases of Oracle Database that occur every 1-2 years. Oracle Database 19c, Oracle Database 21c, and Oracle Database 26ai are major releases. 

Every quarter, RDS for Oracle releases new minor engine versions for every supported major engine. A Release Update (RU) engine version incorporates bug fixes from Oracle by including the RU patches for the specified quarter. For example, 21.0.0.0.ru-2024-10.rur-2024-10.r1 is a minor version of Oracle Database 21c that incorporates the October 2024 RU.

A Supplemental Patch Bundle (SPB) engine version is an RU engine version that includes additional database patches recommended by Oracle for specific use cases, such as Oracle Spatial, Oracle Data Pump, and Oracle GoldenGate. For example, 19.0.0.0.ru-2026-04.spb-1.r1 is a minor engine version that contains the RU patches in engine version 19.0.0.0.ru-2026-04.rur-2026-04.r1 plus supplemental patches. Typically, RDS for Oracle releases SPBs 2–3 weeks after the corresponding RU. For an explanation of the differences between RUs and SPBs, see [Release Updates (RUs) and Supplemental Patch Bundles (SPBs)](USER_UpgradeDBInstance.Oracle.Minor.md#RUs-and-SPBs). For information about supported RUs and SPBs, see [Release notes for Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/OracleReleaseNotes).

RDS for Oracle supports the following upgrades to a DB instance.


| Upgrade type | Application compatibility | Upgrade methods | Sample upgrade path | 
| --- | --- | --- | --- | 
| Major version | A major version upgrade can introduce changes that aren't compatible with existing applications. | Manual only | From Oracle Database 19c to Oracle Database 26ai | 
| Minor version | A minor version upgrade includes only changes that are backward-compatible with existing applications. | Automatic or manual | From 21.0.0.0.ru-2023-07.rur-2022-07.r1 to 21.0.0.0.ru-2023-10.rur-2022-10.r1 | 

**Important**  
When you upgrade your DB engine, an outage occurs. The duration of the outage depends on your engine version and DB instance size.   
Make sure that you thoroughly test any upgrade to verify that your applications work correctly before applying the upgrade to your production databases. For more information, see [Testing an Oracle DB upgrade](USER_UpgradeDBInstance.Oracle.UpgradeTesting.md).

## Support dates and mandatory upgrades for RDS for Oracle
<a name="Aurora.VersionPolicy.MajorVersionLifetime"></a>

Database versions of RDS for Oracle have expected support dates. When a major or minor version of an RDS for Oracle DB engine nears its end-of-support date, RDS begins mandatory upgrades, also known as *forced upgrades*. RDS publishes the following information:
+ A recommendation for you to begin manually upgrading instances on deprecated versions to supported versions
+ A date after which you can no longer create instances on the unsupported versions
+ A date on which RDS begins to upgrade your instances to supported versions automatically during maintenance windows
+ A date on which RDS begins to upgrade your instances to supported versions automatically outside of maintenance windows

**Important**  
Forced upgrades can have unexpected consequences for CloudFormation stacks. If you rely on RDS to upgrade your DB instances automatically, you might encounter issues with CloudFormation.

This section contains the following topics:

**Topics**
+ [Support dates for major releases of RDS for Oracle](#oracle-major-support-dates)
+ [Support dates for minor versions of RDS for Oracle](#oracle-minor-support-dates)

### Support dates for major releases of RDS for Oracle
<a name="oracle-major-support-dates"></a>

RDS for Oracle major versions remain available at least until the end of support date for the corresponding Oracle Database release version. You can use the following dates to plan your testing and upgrade cycles. These dates represent the earliest date that an upgrade to a newer version might be required. If Amazon extends support for an RDS for Oracle version for longer than originally stated, we plan to update this table to reflect the later date. 

**Note**  
You can view the major versions of your Oracle databases by running the [describe-db-major-engine-versions](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-major-engine-versions.html) AWS CLI command or by using the [DescribeDBMajorEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBMajorEngineVersions.html) RDS API operation.

**Note**  
Oracle Database 26ai is available only in Enterprise Edition.


| Oracle Database major release version  | Expected date for upgrading to a newer version | 
| --- | --- | 
| Oracle Database 19c | December 31, 2029 with BYOL Premier Support (fees waived for Extended Support)<br />December 31, 2032 with BYOL Extended Support (extra cost) or an Unlimited License Agreement<br />December 31, 2029 with License Included (LI) | 
| Oracle Database 21c | July 31, 2027 (not available for Extended Support) | 
| Oracle Database 26ai | December 31, 2031 with BYOL Premier Support<br />To be announced, with BYOL Extended Support (extra cost) | 

RDS notifies you at least 12 months before you need to upgrade to a newer major version. The notification describes the upgrade process, including the timing of important milestones, the effect on your DB instances, and recommended actions. We recommend that you thoroughly test your applications with new RDS for Oracle versions before you upgrade your database to a major version.

After this advance notification period, an automatic upgrade to the subsequent major version might be applied to any RDS for Oracle DB instance still running the older version. If so, the upgrade is started during scheduled maintenance windows. 

For more information, see [ Release Schedule of Current Database Releases](https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html) in My Oracle Support.

### Support dates for minor versions of RDS for Oracle
<a name="oracle-minor-support-dates"></a>

In some cases, we end support for minor versions of major releases in RDS for Oracle. RDS notifies you at least 6 months before you need to upgrade to a newer minor version. The notification describes the upgrade process, including the timing of important milestones, the effect on the DB instances running the deprecated minor version, and recommended actions. We recommend that you thoroughly test your applications with new RDS for Oracle versions before you upgrade your database to a new minor version.

For more information about deprecated and desupported minor versions, see [Release notes for Amazon Relational Database Service (Amazon RDS) for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/OracleReleaseNotes/Welcome.html).

## Oracle engine version management
<a name="Oracle.Concepts.Patching"></a>

With DB engine version management, you control when and how the database engine is patched and upgraded. You get the flexibility to maintain compatibility with database engine patch versions. You can also test new patch versions of RDS for Oracle to ensure they work with your application before deploying them in production. In addition, you upgrade the versions on your own terms and timelines.

**Note**  
Amazon RDS periodically aggregates official Oracle database patches using an Amazon RDS-specific DB engine version. To see a list of which Oracle patches are contained in an Amazon RDS Oracle-specific engine version, go to [*Amazon RDS for Oracle Release Notes*](https://docs.aws.amazon.com/AmazonRDS/latest/OracleReleaseNotes/Welcome.html).

## Pre-upgrade checklist
<a name="USER_UpgradeDBInstance.Oracle.Overview.pre-upgrade-checklist"></a>

Before you perform a major version upgrade of your RDS for Oracle DB instance, complete the following preparation steps:
+ Verify that your applications are compatible with the target Oracle Database version. Test your application code, queries, and stored procedures against the target version.
+ Check for deprecated initialization parameters in the target version. Remove or replace any parameters that are no longer supported.
+ Verify that your option group is compatible with the target version. Some options require updates or have different settings for different major versions. To list the options available for a target version, run the [describe-option-group-options](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-option-group-options.html) AWS CLI command, for example:

  ```
  aws rds describe-option-group-options --engine-name oracle-ee --major-engine-version 21
  ```
+ Verify that your parameter group is compatible with the target version. Some parameters have different valid ranges or default values in newer versions.
+ Confirm that the backup retention period for your DB instance is greater than 0. This ensures that Amazon RDS takes an automatic pre-upgrade snapshot that you can use for recovery.
+ Plan for read replica upgrades. Amazon RDS upgrades read replicas automatically after the source DB instance upgrade completes. Factor the additional downtime for replicas into your maintenance window planning.

## Automatic snapshots during engine upgrades
<a name="USER_UpgradeDBInstance.Oracle.Overview.snapshots"></a>

During upgrades of an Oracle DB instance, snapshots offer protection against upgrade issues. If the backup retention period for your DB instance is greater than 0, Amazon RDS takes the following DB snapshots during the upgrade:

1. A snapshot of the DB instance before any upgrade changes have been made. If the upgrade fails, you can restore this snapshot to create a DB instance running the old version.

1. A snapshot of the DB instance after the upgrade completes.

**Note**  
To change your backup retention period, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 

After an upgrade, you can't revert to the previous engine version. However, you can create a new Oracle DB instance by restoring the pre-upgrade snapshot.

To recover from a failed or problematic upgrade, restore the automatic pre-upgrade snapshot using the [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html) AWS CLI command. Note that the restored DB instance has a new endpoint. Update your application connection strings to point to the new DB instance endpoint after the restore completes.

## Oracle upgrades in a Multi-AZ deployment
<a name="USER_UpgradeDBInstance.Oracle.Overview.multi-az"></a>

If your DB instance is in a Multi-AZ deployment, Amazon RDS upgrades both the primary and standby replicas. If no operating system updates are required, the primary and standby upgrades occur simultaneously. The instances are not available until the upgrade completes.

If operating system updates are required in a Multi-AZ deployment, Amazon RDS applies the updates when you request the database upgrade. Amazon RDS performs the following steps:

1. Updates the operating system on the current standby DB instance.

1. Fails over the primary DB instance to the standby DB instance.

1. Upgrades the database version on the new primary DB instance, which was formerly the standby instance. The primary database is unavailable during the upgrade.

1. Updates the operating system on the new standby DB instance, which was formerly the primary DB instance.

1. Upgrades the database version on the new standby DB instance.

1. Fails over the new primary DB instance back to the original primary DB instance, and the new standby DB instance back to the original standby DB instance. Thus, Amazon RDS returns the replication configuration to its original state.

## Oracle upgrades of read replicas
<a name="USER_UpgradeDBInstance.Oracle.Overview.read-replicas"></a>

The Oracle DB engine version of the source DB instance and all of its read replicas must be the same. Amazon RDS performs the upgrade in the following stages:

1. Upgrades the source DB instance. The read replicas are available during this stage.

1. Upgrades the read replicas in parallel, regardless of the replica maintenance windows. The source DB is available during this stage.

For major version upgrades of cross-Region read replicas, Amazon RDS performs additional actions:
+ Generates an option group for the target version automatically
+ Copies all options and option settings from the original option group to the new option group
+ Associates the upgraded cross-Region read replica with the new option group

## Post-upgrade validation
<a name="USER_UpgradeDBInstance.Oracle.Overview.post-upgrade-validation"></a>

After the upgrade completes, verify the new version and check for invalid objects:

```
SELECT VERSION_FULL FROM V$INSTANCE;

SELECT COMP_NAME, VERSION, STATUS FROM DBA_REGISTRY;

SELECT OWNER, OBJECT_NAME, OBJECT_TYPE FROM DBA_OBJECTS WHERE STATUS = 'INVALID' ORDER BY OWNER, OBJECT_TYPE;
```

If the last query returns invalid objects that you own, recompile them by running the following procedure as the master user, substituting your schema name:

```
EXEC DBMS_UTILITY.COMPILE_SCHEMA(schema => '{{schema_name}}');
```

If a component in `DBA_REGISTRY` shows a status other than `VALID`, or if Oracle-supplied objects (owned by `SYS` or `SYSTEM`) remain invalid after the upgrade, contact AWS Support.