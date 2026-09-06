

# Aurora MySQL database engine updates 2022-09-07 (version 3.02.1) (Deprecated)
<a name="AuroraMySQL.Updates.3021"></a><a name="3.02.1"></a><a name="3.02.1"></a>

 **Version:** 3.02.1 

 Aurora MySQL 3.02.1 is generally available. Aurora MySQL 3.02 versions are compatible with MySQL 8.0.23, Aurora MySQL 2.x versions are compatible with MySQL 5.7, and Aurora MySQL 1.x versions are compatible with MySQL 5.6. 

 For details of new features in Aurora MySQL version 3 and differences between Aurora MySQL version 3 and Aurora MySQL version 2 or community MySQL 8.0, see [ Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.Compare-v2-v3) in the *Amazon Aurora User Guide*. 

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 For information on planning an upgrade to Aurora MySQL version 3, see [ Upgrade planning for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-planning) in the *Amazon Aurora User Guide*. For the upgrade procedure itself, see [ Upgrading to Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-procedure) in the *Amazon Aurora User Guide*. For general information about Aurora MySQL upgrades, see [ Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html) in the *Amazon Aurora User Guide*. 

For troubleshooting information, see [ Troubleshooting upgrade issues with Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html#AuroraMySQL.mysql80-upgrade-troubleshooting). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.3021.Improvements"></a>

Aurora MySQL version 3.02.1 is generally available and generally compatible with community MySQL 8.0.23.

**Fixed security issues and CVEs listed below:**

Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below:
+ [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778)

**Availability improvements:**
+ Fixed an issue which can cause connection failure and high latency when multiple MySQL binary log (binlog) replicas are attached to an Aurora writer node or when there are a large number of concurrent long running queries in conjunction with a surge in new connection requests. 
+  Fixed an issue that causes a database restart when advanced auditing for `CONNECT` events are turned on. 
+  Fixed an issue that can cause a database restart on Aurora MySQL read replica instances when internal temporary tables exhaust the allocated size in memory and mmap files set as a customer-configured or default value. 
+  Fixed an issue that can cause a read replica to repeatedly restart during concurrent DDL operations on stored procedures. 
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).

**General improvements:**
+ Added support for R6i instances.

**Additional Information:**
+ Aurora MySQL version 3.02.1 does not contain support for major version upgrades directly from Aurora MySQL version 2 (compatible with MySQL 5.7). To perform a major version upgrade to this version, first perform a major version upgrade to Aurora MySQL version 3.02.0, then perform an in-place minor version upgrade to Aurora MySQL version 3.02.1.