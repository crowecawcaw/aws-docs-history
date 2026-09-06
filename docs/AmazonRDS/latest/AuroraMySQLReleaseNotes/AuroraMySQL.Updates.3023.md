

# Aurora MySQL database engine updates 2023-04-17 (version 3.02.3) (Deprecated)
<a name="AuroraMySQL.Updates.3023"></a><a name="3.02.3"></a><a name="3.02.3"></a>

 **Version:** 3.02.3 

 Aurora MySQL 3.02.3 is generally available. Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23, and Aurora MySQL 2.x versions are compatible with MySQL 5.7. 

 For details of the new features in Aurora MySQL version 3, and differences between Aurora MySQL version 3 and Aurora MySQL version 2 or community MySQL 8.0, see [ Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.Compare-v2-v3) in the *Amazon Aurora User Guide*. 

 Currently supported Aurora MySQL releases are 2.07.\*, 2.11.1, 2.11.2, 3.01.\*, 3.02.\*, and 3.03.\*. 

You can perform an in-place upgrade or restore a snapshot from any currently supported Aurora MySQL version 2 cluster into Aurora MySQL 3.02.3.

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For the upgrade procedure itself, see [ Upgrading to Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-procedure) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3023.Improvements"></a>

**Availability improvements:**
+ Fixed an issue which can cause the database instance to restart due to incorrectly accessing invalid memory when a connection is closed immediately after committing a transaction.
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Fixed an issue where unsupported index scan access methods were considered for common table expressions (CTE) while materializing intermediate temporary tables, which can lead to undesired behavior including database restarts or incorrect query results. This issue was fixed by avoiding the use of such unsupported index scan access methods on tables using the TempTable storage engine.
+ Fixed an issue which, in rare cases, can cause an Aurora MySQL reader instance to restart when accessing a table which has large update or Data Definition Language (DDL) operations running concurrently on the Aurora MySQL writer instance.
+ Fixed an issue which, in certain situations, can cause Aurora MySQL reader instances to restart when attempting to read a page which is no longer accessible during a range estimation.
+ Fixed an issue where database instances using binary log replication may experience an increase in CPU utilization and connection failures when multiple binary log replication consumers are attached.
+ Fixed an issue which can cause an Aurora MySQL reader instance to restart while executing a query which utilizes an Aurora parallel query execution plan.