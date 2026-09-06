

# Aurora MySQL database engine updates 2026-03-09 (version 2.12.6, compatible with MySQL 5.7.44) - RDS Extended Support version
<a name="AuroraMySQL.Updates.2126"></a><a name="2126"></a><a name="2.12.6"></a>

 **Version:** 2.12.6 

 Aurora MySQL 2.12.6 is generally available. Aurora MySQL 2.12 versions are compatible up to MySQL 5.7.44. For more information on community changes, see [Changes in MySQL 5.7.44 (2022-10-11, General Availability)](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-44.html). 

 Currently supported Aurora MySQL releases are 2.11.\*, 2.12.\*, 3.04.\*, 3.08.\*, 3.09.\*, 3.10.\*, 3.11.\*, and 3.12.\*. 

 You can upgrade an existing Aurora MySQL 2.\* database cluster to Aurora MySQL 2.12.6. You can also restore a snapshot from any currently supported Aurora MySQL release into Aurora MySQL 2.12.6. 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

**Note**  
For information on how to upgrade your Aurora MySQL database cluster, see [ Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.2126.Improvements"></a>

 **Security fixes:** 
+  Fixed an issue which can cause some SQL statements to not get logged in the audit log. 

 **Medium CVEs:** 
+  [CVE-2025-53054](https://www.cve.org/CVERecord?id=CVE-2025-53054) 
+  [CVE-2025-53053](https://www.cve.org/CVERecord?id=CVE-2025-53053) 
+  [CVE-2025-53044](https://www.cve.org/CVERecord?id=CVE-2025-53044) 
+  [CVE-2025-53045](https://www.cve.org/CVERecord?id=CVE-2025-53045) 
+  [CVE-2025-53062](https://www.cve.org/CVERecord?id=CVE-2025-53062) 
+  [CVE-2025-53069](https://www.cve.org/CVERecord?id=CVE-2025-53069) 
+  [CVE-2025-53040](https://www.cve.org/CVERecord?id=CVE-2025-53040) 
+  [CVE-2025-53042](https://www.cve.org/CVERecord?id=CVE-2025-53042) 
+  [CVE-2025-50082](https://www.cve.org/CVERecord?id=CVE-2025-50082) 
+  [CVE-2025-50085](https://www.cve.org/CVERecord?id=CVE-2025-50085) 
+  [CVE-2025-53023](https://www.cve.org/CVERecord?id=CVE-2025-53023) 
+  [CVE-2025-50087](https://www.cve.org/CVERecord?id=CVE-2025-50087) 
+  [CVE-2025-50099](https://www.cve.org/CVERecord?id=CVE-2025-50099) 
+  [CVE-2025-50079](https://www.cve.org/CVERecord?id=CVE-2025-50079) 
+  [CVE-2025-50092](https://www.cve.org/CVERecord?id=CVE-2025-50092) 
+  [CVE-2025-50102](https://www.cve.org/CVERecord?id=CVE-2025-50102) 
+  [CVE-2025-50083](https://www.cve.org/CVERecord?id=CVE-2025-50083) 
+  [CVE-2025-50096](https://www.cve.org/CVERecord?id=CVE-2025-50096) 
+  [CVE-2025-50091](https://www.cve.org/CVERecord?id=CVE-2025-50091) 
+  [CVE-2025-50084](https://www.cve.org/CVERecord?id=CVE-2025-50084) 
+  [CVE-2025-50101](https://www.cve.org/CVERecord?id=CVE-2025-50101) 
+  [CVE-2025-50077](https://www.cve.org/CVERecord?id=CVE-2025-50077) 
+  [CVE-2025-50088](https://www.cve.org/CVERecord?id=CVE-2025-50088) 
+  [CVE-2025-50080](https://www.cve.org/CVERecord?id=CVE-2025-50080) 
+  [CVE-2025-50097](https://www.cve.org/CVERecord?id=CVE-2025-50097) 
+  [CVE-2025-50094](https://www.cve.org/CVERecord?id=CVE-2025-50094) 
+  [CVE-2025-50093](https://www.cve.org/CVERecord?id=CVE-2025-50093) 
+  [CVE-2025-50086](https://www.cve.org/CVERecord?id=CVE-2025-50086) 
+  [CVE-2025-50078](https://www.cve.org/CVERecord?id=CVE-2025-50078) 
+  [CVE-2025-21501](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21501) 
+  [CVE-2025-21500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21500) 
+  [CVE-2025-21543](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21543) 
+  [CVE-2025-21540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21540) 
+  [CVE-2025-21491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21491) 
+  [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490) 
+  [CVE-2025-21559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21559) 
+  [CVE-2025-21555](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21555) 
+  [CVE-2025-21497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21497) 
+  [CVE-2025-21519](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21519) 
+  [CVE-2025-21529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21529) 
+  [CVE-2025-21505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21505) 
+  [CVE-2025-21531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21531) 
+  [CVE-2025-21523](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21523) 
+  [CVE-2025-21503](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21503) 
+  [CVE-2025-21522](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21522) 
+  [CVE-2025-21518](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21518) 
+  [CVE-2025-21577](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21577) 
+  [CVE-2025-30682](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30682) 
+  [CVE-2025-30687](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30687) 
+  [CVE-2025-30688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30688) 
+  [CVE-2025-21574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21574) 
+  [CVE-2025-21575](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21575) 
+  [CVE-2025-30693](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30693) 
+  [CVE-2025-30695](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30695) 
+  [CVE-2025-30715](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30715) 
+  [CVE-2025-21584](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21584) 
+  [CVE-2025-21580](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21580) 
+  [CVE-2025-21581](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21581) 
+  [CVE-2025-21585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21585) 
+  [CVE-2025-30689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30689) 
+  [CVE-2025-21579](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21579) 
+  [CVE-2025-30696](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30696) 
+  [CVE-2025-30705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30705) 
+  [CVE-2025-30683](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30683) 
+  [CVE-2025-30684](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30684) 
+  [CVE-2025-30685](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30685) 
+  [CVE-2025-30699](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30699) 
+  [CVE-2025-30704](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30704) 
+  [CVE-2025-30721](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30721) 

 **Low CVEs:** 
+  [CVE-2025-50104](https://www.cve.org/CVERecord?id=CVE-2025-50104) 
+  [CVE-2025-50098](https://www.cve.org/CVERecord?id=CVE-2025-50098) 
+  [CVE-2025-50100](https://www.cve.org/CVERecord?id=CVE-2025-50100) 
+  [CVE-2025-21520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21520) 
+  [CVE-2025-21546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21546) 
+  [CVE-2025-30703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30703) 
+  [CVE-2025-30681](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30681) 