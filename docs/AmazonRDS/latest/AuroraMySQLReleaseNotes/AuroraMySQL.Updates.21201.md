

# Aurora MySQL database engine updates 2023-10-25 (version 2.12.0.1, compatible with MySQL 5.7.40) - RDS Extended Support version (Beta)
<a name="AuroraMySQL.Updates.21201"></a><a name="21201"></a><a name="2.12.0.1"></a>

**Version:** 2.12.0.1

Aurora MySQL 2.12.0.1 is generally available in the following regions: US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), AWS GovCloud (US-East), and AWS GovCloud (US-West). This is an early, security fix–only release. These fixes will be deployed more broadly across all Regions with the next patch release, 2.12.1. Aurora MySQL 2.12 versions are compatible with MySQL 5.7.40.

Currently supported Aurora MySQL releases are 2.07.\*, 2.11.\*, 2.12.\*, 3.01.\*, 3.02.\*, 3.03.\*, and 3.04.\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.0.1. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.0.1.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.21201.Improvements"></a>

**Fixed security issues and CVEs listed below:**

This release includes all community CVEs fixes up to and including MySQL 5.7.40.
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)

**Availability improvements:**
+ Fast insert isn't enabled in this Aurora MySQL version, due to an issue that can cause inconsistencies when running queries such as `INSERT INTO`, `SELECT`, and `FROM`. For more information on the fast insert optimization, see [Amazon Aurora MySQL performance enhancements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html#Aurora.AuroraMySQL.Performance).