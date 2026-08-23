# Applying database version upgrades

RDS for SQL Server Developer Edition supports both minor and major version upgrades using Custom Engine Versions (CEVs). Upgrading requires creating a new CEV with the latest Cumulative Update (CU) and applying it to your instance. Database version upgrades for SQL Server Developer Edition involve the following steps:

## Understanding major and minor versions

A major version represents a full release of Microsoft SQL Server. Each major version introduces new features, significant changes in functionality or performance characteristics, and engine-level changes that might not be backward-compatible with existing applications.

The following table shows the major versions:

| SQL Server release                           | Example engine version |
| -------------------------------------------- | ---------------------- |
| SQL Server 2025 Enterprise Developer Edition | 17.00.4045.5           |
| SQL Server 2025 Standard Developer Edition   | 17.00.4045.5           |
| SQL Server 2022 Developer Edition            | 16.00.4215.2           |
| SQL Server 2019 Developer Edition            | 15.00.4455.2           |

## Minor versions (cumulative updates)

A minor version represents a Cumulative Update (CU) released by Microsoft within a given major version. Minor version upgrades include security patches, bug fixes, and engine improvements.

For example, within SQL Server 2022 (major version 16.00), the following are minor versions:

- 16.00.4255.1 (CU25)
- 16.00.4215.2 (CU21)

Before performing a version upgrade, review the following resources to understand potential impacts and best practices:

- [Considerations for upgrading the SQL Server DB engine](USER_UpgradeDBInstance.SQLServer.Considerations.md "USER_UpgradeDBInstance.SQLServer.Considerations.md") – Covers compatibility levels, deprecated features, collation changes, linked servers, and other factors that might affect your workloads after an upgrade.
- [Testing an upgrade](USER_UpgradeDBInstance.SQLServer.UpgradeTesting.md "USER_UpgradeDBInstance.SQLServer.UpgradeTesting.md") – Describes how to test a major version upgrade on a snapshot restore before applying it to your production instance, helping you identify issues without impacting live workloads.

## Verify current engine version and identify target version

Use the `describe-db-engine-versions` AWS CLI command to view supported versions and determine valid upgrade targets for your current engine version. This helps you distinguish between major and minor upgrade paths before applying changes. Identify the target database engine version from Amazon RDS supported versions. For information about what SQL Server versions are available on Amazon RDS, see [Working with SQL Server Developer Edition on RDS for SQL Server](sqlserver-dev-edition.md "sqlserver-dev-edition.md").

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

- `IsMajorVersionUpgrade: False` indicates a minor version upgrade
- `IsMajorVersionUpgrade: True` indicates a major version upgrade

## Create a new custom engine version

Obtain and upload the required installation media (ISO and CU), then create a new CEV. For detailed instructions on creating a CEV, see [Creating a Custom Engine Version for RDS for SQL Server Developer Edition](sqlserver-dev-edition.creating-cev.md "sqlserver-dev-edition.creating-cev.md").

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

### Using the AWS CLI

Apply the version upgrade using the Amazon RDS [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the new CEV:

```
aws rds modify-db-instance \
--db-instance-identifier <instance-id> \
--engine-version <new-cev-version> \
--allow-major-version-upgrade ## required only for major version upgrades \
--no-apply-immediately ## use --apply-immediately for immediate update
```

###### Note

`--no-apply-immediately` (the default) to apply the changes during the next maintenance window.

###### Important

The `--allow-major-version-upgrade` parameter is required for major version upgrades.

### Using the AWS Management Console

To upgrade the engine version of a DB instance using the Console:

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to upgrade.
3. Choose **Modify**. The Modify DB Instance page appears.
4. For **DB engine version**, choose the new target version (your new CEV) from the dropdown list.
5. Choose **Continue** and review the summary of modifications.
6. Choose when to apply the changes:

   - Select **Apply immediately** to start the upgrade now.
   - Select **Apply during the next scheduled maintenance window** to apply the changes during the next scheduled maintenance window.

7. Choose **Modify DB Instance** to save your changes.
