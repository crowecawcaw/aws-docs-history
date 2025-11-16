# Automatic minor

version upgrades for RDS for PostgreSQL

If you enable the **Auto minor version upgrade** option when
creating or modifying a DB instance or Multi-AZ DB cluster, you can have your database
automatically upgraded.

For each RDS for PostgreSQL major version, one minor version is designated by
RDS as the automatic upgrade version. After a minor version has been tested
and approved by Amazon RDS, the minor version upgrade occurs automatically during
your maintenance window. RDS doesn't automatically set newer released
minor versions as the automatic upgrade version. Before RDS designates a
newer automatic upgrade version, several criteria are considered, such as
the following:

- Known security issues
- Bugs in the PostgreSQL community version
- Overall fleet stability since the minor version was
  released
  You can use the following AWS CLI command to determine the current automatic
  minor upgrade target version for a specified PostgreSQL minor version in a
  specific AWS Region.

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine postgres \
--engine-version `minor-version` \
--region `region` \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output text
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine postgres ^
--engine-version `minor-version` ^
--region `region` ^
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" ^
--output text
```

For example, the following AWS CLI command determines the automatic minor
upgrade target for PostgreSQL minor version 16.1 in the US East (Ohio)
AWS Region (us-east-2).

For Linux, macOS, or Unix:

```
aws rds describe-db-engine-versions \
--engine postgres \
--engine-version 16.1 \
--region us-east-2 \
--query "DBEngineVersions[*].ValidUpgradeTarget[*].{AutoUpgrade:AutoUpgrade,EngineVersion:EngineVersion}" \
--output table
```

For Windows:

```
aws rds describe-db-engine-versions ^
--engine postgres ^
--engine-version 16.1 ^
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
|  False       |  16.2           |
**| True | 16.3 |**
|  False       |  16.4           |
|  False       |  16.5           |
|  False       |  16.6           |
|  False       |  17.1           |
|  False       |  17.2           |
+--------------+-----------------+
```

In this example, the `AutoUpgrade` value is `True` for
PostgreSQL version 16.3. So, the automatic minor upgrade target is
PostgreSQL version 16.3, which is highlighted in the output.

A PostgreSQL database is automatically upgraded during your maintenance window
if the following criteria are met:

- The database has the **Auto minor version
  upgrade** option enabled.
- The database is running a minor DB engine version that is less
  than the current automatic upgrade minor version.
  For more information, see [Automatically upgrading the minor engine version](USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades "USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.AutoMinorVersionUpgrades").

###### Note

A PostgreSQL upgrade doesn't upgrade PostgreSQL extensions. To
upgrade extensions, see [Upgrading PostgreSQL extensions in RDS for PostgreSQL databases](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").
