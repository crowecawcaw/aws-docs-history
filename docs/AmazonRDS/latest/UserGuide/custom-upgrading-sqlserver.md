# Upgrading an Amazon RDS Custom for SQL Server DB instance

You can upgrade an Amazon RDS Custom for SQL Server DB instance by modifying it to use a new DB engine version.
For general information about upgrading DB instances, see
[Upgrading a DB instance engine version](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

###### Topics

- [Overview of upgrades in RDS Custom for SQL Server](#custom-upgrading-sqlserver.Overview "#custom-upgrading-sqlserver.Overview")
- [Upgrading major and minor engine version](#custom-upgrading-sqlserver.Upgrade "#custom-upgrading-sqlserver.Upgrade")
- [Database compatibility level](#custom-upgrading-sqlserver.Major.Compatibility "#custom-upgrading-sqlserver.Major.Compatibility")

## Overview of upgrades in RDS Custom for SQL Server

Amazon RDS Custom for SQL Server supports major and minor version upgrades. Minor version upgrades can include security patches, bug fixes, and engine improvements.
Microsoft releases these updates as cumulative updates (CUs). Major version upgrades introduce new features and engine changes between versions,
like upgrading from SQL Server 2019 to 2022. You can apply both upgrades immediately or during scheduled maintenance windows.
To prevent potential backward compatibility issues, we recommend testing your applications in a non-production environment before upgrading.

RDS Custom for SQL Server allows you to upgrade an RDS Provided Engine Version (RPEV) or a Custom Engine Version (CEV).

- RDS-provided engine versions (RPEV) contain up-to-date operating system (OS) patches and SQL Server cumulative updates (CU).
- For a custom engine version (CEV), you must follow a two-step process. First,
  create a new CEV with your target SQL Server version, see [Preparing to create a CEV for RDS Custom for SQL Server](custom-cev-sqlserver.md "custom-cev-sqlserver.md"). This target version must
  be equal to or newer than your current version. Once the new CEV is created,
  modify your database instance to use this new version. For more information, see
  [Performing a minor version upgrade for Amazon RDS Custom for SQL Server
  CEV with Multi-AZ](https://aws.amazon.com/blogs/database/performing-a-minor-version-upgrade-for-amazon-rds-custom-for-sql-server-cev-with-multi-az/ "https://aws.amazon.com/blogs/database/performing-a-minor-version-upgrade-for-amazon-rds-custom-for-sql-server-cev-with-multi-az/").

Do not apply SQL Server cumulative updates in-place to your running RDS Custom instance.
Once you create a CEV with a specific SQL Server version (for example, SQL Server 2022 CU16),
applying a newer cumulative update directly to the instance takes it out of the support perimeter
and reports error `SP-S3006`. To patch an existing SQL Server instance using a CEV, create a new CEV
that includes the desired cumulative update, then modify your existing instance to switch to the new CEV.

If you upgrade an RDS Custom for SQL Server DB instance in a Multi-AZ deployment, RDS Custom for SQL Server performs rolling upgrades for your instance.
This approach minimizes downtime by upgrading one instance at a time.
RDS performs the following actions to perform rolling upgrades:

1. Upgrade the standby DB instance.
2. Failover to the upgraded standby DB instance, making it the new primary DB instance.
3. Upgrade the new standby DB instance.

The DB instance downtime for Multi-AZ deployments is the time it takes for the failover.

The following limitations apply when upgrading an RDS Custom for SQL Server DB instance:

- Custom DB option and parameter groups aren't supported.
- Any additional storage volumes that you attach to your RDS Custom for SQL Server DB instance are not attached after the upgrade.
- For CEVs, in-place application of SQL Server cumulative updates is not supported and results in the instance being taken out of the support perimeter.

## Upgrading major and minor engine version

Both major and minor engine version upgrades are irreversible and must always be done
to a newer version. To identify available target versions, use the AWS Management Console and choose
from the available versions when modifying your DB instance. Alternatively, use the [`describe-db-engine-versions`](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") CLI command or [DescribeDBEngineVersions](../APIReference/API_DescribeDBEngineVersions.md "../APIReference/API_DescribeDBEngineVersions.md") RDS API command.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
    --engine custom-sqlserver-se \
    --engine-version `15.00.4322.2.v1` \
    --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" \
    --output table

```

For Windows:

```
aws rds describe-db-engine-versions ^
    --engine custom-sqlserver-se ^
    --engine-version `15.00.4322.2.v1` ^
    --query "DBEngineVersions[*].ValidUpgradeTarget[*].{EngineVersion:EngineVersion}" ^
    --output table
```

The output shows the available target engine versions:

```
--------------------------
|DescribeDBEngineVersions|
+------------------------+
|      EngineVersion     |
+------------------------+
|  15.00.4410.1.v1       |
|  15.00.4415.2.v1       |
|  15.00.4430.1.v1       |
|  16.00.4165.4.v1       |
|  16.00.4175.1.v1       |
|  16.00.4185.3.v1       |
+------------------------+
```

After identifying your target version, use the AWS Management Console and follow the instructions in
[Modifying an RDS Custom for SQL Server DB instance](custom-managing.md "custom-managing.md"). Alternatively, use
[`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") CLI command or
[ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") RDS API command.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `DB_INSTANCE_IDENTIFIER` \
    --engine-version `ENGINE_VERSION` \
    --allow-major-version-upgrade \
    --region `Region` \
    --no-apply-immediately
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `DB_INSTANCE_IDENTIFIER` ^
    --engine-version `ENGINE_VERSION` ^
    --allow-major-version-upgrade ^
    --region `Region` ^
    --no-apply-immediately
```

###### Note

You must include the `--allow-major-version-upgrade` parameter to perform major version upgrades.

## Database compatibility level

You can use Microsoft SQL Server database compatibility levels
to adjust some database behaviors to mimic previous versions of SQL Server.
For more information, see [Compatibility level](https://msdn.microsoft.com/en-us/library/bb510680.aspx "https://msdn.microsoft.com/en-us/library/bb510680.aspx")
in the Microsoft documentation.

When you upgrade your DB instance,
all existing databases remain at their original compatibility level.
For example, if you upgrade from SQL Server 2019 to SQL Server 2022,
all existing databases have a compatibility level of 150.
Any new database created after the upgrade have compatibility level 160.

You can change the compatibility level of a database
by using the ALTER DATABASE command.
For example, to change a database named `customeracct`
to be compatible with SQL Server 2022,
issue the following command:

```
ALTER DATABASE customeracct SET COMPATIBILITY_LEVEL = 160
```
