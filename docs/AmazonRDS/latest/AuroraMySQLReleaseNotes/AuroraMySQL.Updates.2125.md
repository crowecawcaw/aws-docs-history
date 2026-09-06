

# Aurora MySQL database engine updates 2025-04-09 (version 2.12.5, compatible with MySQL 5.7.44) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2125"></a><a name="2125"></a><a name="2.12.5"></a>

 **Version:** 2.12.5

Aurora MySQL 2.12.5 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.44. For more information on community changes, see [Changes in MySQL 5.7.44 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html). 

Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.04.\*, 3.05.\*, 3.06.\*, 3.07.\*, and 3.08\*.

You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.5. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.5.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2124.Improvements"></a>

 **Fixed security issues and CVEs:** 

This release includes all community CVE fixes up to and including MySQL 5.7.44. The following CVE fixes are included:
+  [CVE-2025-21543](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21543) 
+  [CVE-2025-21500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21500) 
+  [CVE-2025-21491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21491) 
+  [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490) 
+  [CVE-2025-21540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21540) 
+  [CVE-2025-21559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21559) 
+  [CVE-2025-21555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21555) 
+  [CVE-2025-21497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21497) 
+  [CVE-2025-21520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21520) 
+  [CVE-2025-21501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21501) 
+  [CVE-2024-37371](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37371) 
+  [CVE-2024-11053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11053) 
+  [CVE-2024-21201](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21201) 
+  [CVE-2024-21241](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21241) 
+  [CVE-2024-21230](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21230) 
+  [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487) 

 **Availability improvements:** 
+ Fixed an issue on the replica where a network interruption may not correctly re-establish connection with the writer.