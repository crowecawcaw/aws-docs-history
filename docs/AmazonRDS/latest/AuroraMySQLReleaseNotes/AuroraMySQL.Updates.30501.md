

# Aurora MySQL database engine updates 2023-10-30 (version 3.05.0.1) (Deprecated)
<a name="AuroraMySQL.Updates.30501"></a><a name="30501"></a><a name="3.05.0.1"></a>

 **Version:** 3.05.0.1 

 Aurora MySQL 3.05.0.1 is generally available in the following regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), AWS GovCloud (US-East), and AWS GovCloud (US-West). This is an early, security fix–only release. These fixes will be deployed more broadly across all Regions with the next patch release, 3.05.1. Aurora MySQL 3.05 versions are compatible with MySQL 8.0.32. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/). 

 Currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, 3.04.\*, and 3.05.\*. 

 You can upgrade an existing Aurora MySQL 3.\* database cluster to Aurora MySQL 3.05.0.1. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 3.05.0.1. 

 If you upgrade an Aurora MySQL global database to version 3.05.\*, you must upgrade your primary and secondary DB clusters to the exact same version, including the patch level. For more information on upgrading the minor version of an Aurora global database, see [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html#aurora-global-database-upgrade.minor). 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.30501.Improvements"></a>

**Fixed security issues and CVEs listed below:**

This release includes all community CVEs fixes up to and including MySQL 8.0.32.
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)