# Automatic minor version upgrades for RDS for MySQL

If you specify the following settings when creating or modifying a DB instance, you can have your
DB instance automatically upgraded.

- The **Auto minor version upgrade** setting is enabled.
- The **Backup retention period** setting is greater than 0.
  In the AWS Management Console, these settings are under **Additional configuration**. The
  following image shows the **Auto minor version upgrade** setting.

![The Maintenance section with Enable auto minor version upgrade selected in the Amazon RDS console.](images/amvu.png)
For more information about these settings, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md").

For some RDS for MySQL major versions in some AWS Regions, one minor version is designated by RDS as
the automatic upgrade version. After a minor version has been tested and approved by
Amazon RDS, the minor version upgrade occurs automatically during your maintenance window.
RDS doesn't automatically set newer released minor versions as the automatic
upgrade version. Before RDS designates a newer automatic upgrade version, several
criteria are considered, such as the following:

- Known security issues
- Bugs in the MySQL community version
- Overall fleet stability since the minor version was released
  You can run the following AWS CLI command to determine the current automatic minor
  upgrade target version for a specified MySQL minor version in a specific AWS Region.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine mysql \
--engine-version `minor_version` \
--region `region` \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine mysql ^
--engine-version `minor_version` ^
--region `region` ^
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" ^
--output text
```

For example, the following AWS CLI command determines the automatic minor upgrade target
for MySQL minor version 8.0.11 in the US East (Ohio) AWS Region
(us-east-2).

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine mysql \
--engine-version 8.0.11 \
--region us-east-2 \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output table
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine mysql ^
--engine-version 8.0.11 ^
--region us-east-2 ^
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" ^
--output table
```

Your output is similar to the following.

```
----------------------------------
|    DescribeDBEngineVersions    |
+--------------+-----------------+
|  AutoUpgrade |  EngineVersion  |
+--------------+-----------------+
|  False       |  8.0.15         |
|  False       |  8.0.16         |
|  False       |  8.0.17         |
|  False       |  8.0.19         |
|  False       |  8.0.20         |
|  False       |  8.0.21         |
**| True | 8.0.23 |**
|  False       |  8.0.25         |
+--------------+-----------------+
```

In this example, the `AutoUpgrade` value is `True` for MySQL version 8.0.23. So, the automatic minor upgrade target is
MySQL version 8.0.23, which is highlighted in the output.

A MySQL DB instance is automatically upgraded during your maintenance window if
the following criteria are met:

- The **Auto minor version upgrade** setting is enabled.
- The **Backup retention period** setting is greater than 0.
- The DB instance is running a minor DB engine version that is less than the
  current automatic upgrade minor version.
  For more information, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades").
