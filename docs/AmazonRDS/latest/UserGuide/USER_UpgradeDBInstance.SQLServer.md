

# Upgrades of the Microsoft SQL Server DB engine
<a name="USER_UpgradeDBInstance.SQLServer"></a>

When Amazon RDS supports a new version of a database engine, you can upgrade your DB instances to the new version. There are two kinds of upgrades for SQL Server DB instances: major version upgrades and minor version upgrades. 

*Major version upgrades* can contain database changes that are not backward-compatible with existing applications. As a result, you must *manually* perform major version upgrades of your DB instances. You can initiate a major version upgrade by modifying your DB instance. However, before you perform a major version upgrade, we recommend that you test the upgrade by following the steps described in [Testing an RDS for SQL Server upgrade](USER_UpgradeDBInstance.SQLServer.UpgradeTesting.md). 

*Minor version upgrades* contain only changes that are backward-compatible with existing applications. You can upgrade the minor version for your DB instance in two ways:
+ *Manually* – Modify your DB instance to initiate the upgrade
+ *Automatically* – Enable automatic minor version upgrades for your DB instance

When you enable automatic minor version upgrades, RDS for SQL Server automatically upgrades your database instance during scheduled maintenance windows when critical security updates are available in a newer minor version.

For minor engine versions after `16.00.4120.1`, `15.00.4365.2`, `14.00.3465.1`, `13.00.6435.1`, the following security protocols are disabled by default:
+ `rds.tls10` (TLS 1.0 protocol)
+ `rds.tls11` (TLS 1.1 protocol)
+ `rds.rc4` (RC4 cipher)
+ `rds.curve25519` (Curve25519 encryption)
+ `rds.3des168` (Triple DES encryption)

For earlier engine versions, Amazon RDS enables these security protocols by default.

```
...

"ValidUpgradeTarget": [
    {
        "Engine": "sqlserver-se",
        "EngineVersion": "14.00.3281.6.v1",
        "Description": "SQL Server 2017 14.00.3281.6.v1",
        "AutoUpgrade": false,
        "IsMajorVersionUpgrade": false
    }
...
```

For more information about performing upgrades, see [Upgrading a SQL Server DB instance](#USER_UpgradeDBInstance.SQLServer.Upgrading). For information about what SQL Server versions are available on Amazon RDS, see [Amazon RDS for Microsoft SQL Server](CHAP_SQLServer.md).

Amazon RDS also supports upgrade rollout policy to manage automatic minor version upgrades across multiple database resources and AWS accounts. For more information, see [Using AWS Organizations upgrade rollout policy for automatic minor version upgrades](RDS.Maintenance.AMVU.UpgradeRollout.md).

**Topics**
+ [Major version upgrades for RDS for SQL Server](USER_UpgradeDBInstance.SQLServer.Major.md)
+ [Considerations for SQL Server upgrades](USER_UpgradeDBInstance.SQLServer.Considerations.md)
+ [Testing an RDS for SQL Server upgrade](USER_UpgradeDBInstance.SQLServer.UpgradeTesting.md)
+ [Upgrading a SQL Server DB instance](#USER_UpgradeDBInstance.SQLServer.Upgrading)
+ [Upgrading deprecated DB instances before support ends](#USER_UpgradeDBInstance.SQLServer.DeprecatedVersions)

## Upgrading a SQL Server DB instance
<a name="USER_UpgradeDBInstance.SQLServer.Upgrading"></a>

For information about manually or automatically upgrading a SQL Server DB instance, see the following:
+ [Upgrading a DB instance engine version](USER_UpgradeDBInstance.Upgrading.md)
+ [Best practices for upgrading SQL Server 2008 R2 to SQL Server 2016 on Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/best-practices-for-upgrading-sql-server-2008-r2-to-sql-server-2016-on-amazon-rds-for-sql-server/)

**Important**  
If you have any snapshots that are encrypted using AWS KMS, we recommend that you initiate an upgrade before support ends. 

## Upgrading deprecated DB instances before support ends
<a name="USER_UpgradeDBInstance.SQLServer.DeprecatedVersions"></a>

After a major version is deprecated, you can't install it on new DB instances. RDS will try to automatically upgrade all existing DB instances. 

If you need to restore a deprecated DB instance, you can do point-in-time recovery (PITR) or restore a snapshot. Doing this gives you temporary access a DB instance that uses the version that is being deprecated. However, after a major version is fully deprecated, these DB instances will also be automatically upgraded to a supported version. 