

# Applying database version upgrades
<a name="sqlserver-dev-edition.db-version-upgrade"></a>

RDS for SQL Server Developer Edition supports both minor and major version upgrades using Custom Engine Versions (CEVs). Upgrading requires creating a new CEV with the latest Cumulative Update (CU) and applying it to your instance. Database version upgrades for SQL Server Developer Edition involve the following steps:

## Understanding major and minor versions
<a name="sqlserver-dev-edition.db-version-upgrade.major-minor"></a>

A major version represents a full release of Microsoft SQL Server. Each major version introduces new features, significant changes in functionality or performance characteristics, and engine-level changes that might not be backward-compatible with existing applications.

The following table shows the major versions:


| SQL Server release | Example engine version | 
| --- | --- | 
| SQL Server 2025 Enterprise Developer Edition | 17.00.4045.5 | 
| SQL Server 2025 Standard Developer Edition | 17.00.4045.5 | 
| SQL Server 2022 Developer Edition | 16.00.4215.2 | 
| SQL Server 2019 Developer Edition | 15.00.4455.2 | 

## Minor versions (cumulative updates)
<a name="sqlserver-dev-edition.db-version-upgrade.minor-versions"></a>

A minor version represents a Cumulative Update (CU) released by Microsoft within a given major version. Minor version upgrades include security patches, bug fixes, and engine improvements.

For example, within SQL Server 2022 (major version 16.00), the following are minor versions:
+ 16.00.4255.1 (CU25)
+ 16.00.4215.2 (CU21)

Before performing a version upgrade, review the following resources to understand potential impacts and best practices:
+ [Considerations for upgrading the SQL Server DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.Considerations.html) – Covers compatibility levels, deprecated features, collation changes, linked servers, and other factors that might affect your workloads after an upgrade.
+ [Testing an upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.UpgradeTesting.html) – Describes how to test a major version upgrade on a snapshot restore before applying it to your production instance, helping you identify issues without impacting live workloads.

## Verify current engine version and identify target version
<a name="sqlserver-dev-edition.db-version-upgrade.verify"></a>

Use the `describe-db-engine-versions` AWS CLI command to view supported versions and determine valid upgrade targets for your current engine version. This helps you distinguish between major and minor upgrade paths before applying changes. Identify the target database engine version from Amazon RDS supported versions. For information about what SQL Server versions are available on Amazon RDS, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md).

```
aws rds describe-db-engine-versions \
  --engine sqlserver-dev-ee \
  --engine-version "16.00.4215.2.my-cev" \
  --query "DBEngineVersions[0].ValidUpgradeTarget[*].{EngineVersion:EngineVersion,IsMajorVersionUpgrade:IsMajorVersionUpgrade}" \
  --output table
```

```
---------------------------------------------------------
|              DescribeDBEngineVersions                  |
+----------------------------+--------------------------+
|       EngineVersion        |  IsMajorVersionUpgrade   |
+----------------------------+--------------------------+
|  16.00.4255.1.my-target-cev|  False                   |
|  17.00.4055.5.my-target-cev|  True                    |
+----------------------------+--------------------------+
```

In this output:
+ `IsMajorVersionUpgrade: False` indicates a minor version upgrade
+ `IsMajorVersionUpgrade: True` indicates a major version upgrade

## Create a new custom engine version
<a name="sqlserver-dev-edition.db-version-upgrade.create-cev"></a>

Obtain and upload the required installation media (ISO and CU), then create a new CEV. For detailed instructions on creating a CEV, see [Creating a Custom Engine Version for RDS for SQL Server Developer Edition](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.creating-cev.html).

Run `describe-db-engine-versions` to confirm valid upgrade paths for your CEV:

```
aws rds describe-db-engine-versions \
  --engine sqlserver-dev-ee \
  --engine-version "16.00.4215.2.my-cev" \
  --query "DBEngineVersions[0].ValidUpgradeTarget[*].{EngineVersion:EngineVersion,IsMajorVersionUpgrade:IsMajorVersionUpgrade}" \
  --output table
```

Example output:

```
---------------------------------------------------------
|              DescribeDBEngineVersions                  |
+----------------------------+--------------------------+
|       EngineVersion        |  IsMajorVersionUpgrade   |
+----------------------------+--------------------------+
|  17.00.4055.5.my-target-cev|  True                    |
+----------------------------+--------------------------+
```

## Apply the version upgrade
<a name="sqlserver-dev-edition.db-version-upgrade.apply"></a>

### Using the AWS CLI
<a name="sqlserver-dev-edition.db-version-upgrade.apply.cli"></a>

Apply the version upgrade using the Amazon RDS [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command with the new CEV:

```
aws rds modify-db-instance \
--db-instance-identifier <instance-id> \
--engine-version <new-cev-version> \
--allow-major-version-upgrade ## required only for major version upgrades \
--no-apply-immediately ## use --apply-immediately for immediate update
```

**Note**  
`--no-apply-immediately` (the default) to apply the changes during the next maintenance window.

**Important**  
The `--allow-major-version-upgrade` parameter is required for major version upgrades.

### Using the AWS Management Console
<a name="sqlserver-dev-edition.db-version-upgrade.apply.console"></a>

To upgrade the engine version of a DB instance using the Console:

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to upgrade.

1. Choose **Modify**. The Modify DB Instance page appears.

1. For **DB engine version**, choose the new target version (your new CEV) from the dropdown list.

1. Choose **Continue** and review the summary of modifications.

1. Choose when to apply the changes: 
   + Select **Apply immediately** to start the upgrade now.
   + Select **Apply during the next scheduled maintenance window** to apply the changes during the next scheduled maintenance window.

1. Choose **Modify DB Instance** to save your changes.