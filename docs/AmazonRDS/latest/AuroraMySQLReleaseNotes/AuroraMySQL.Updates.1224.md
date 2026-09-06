

# Aurora MySQL database engine updates 2021-03-04 (version 1.22.4) (Deprecated)
<a name="AuroraMySQL.Updates.1224"></a><a name="1224"></a><a name="1.22.4"></a>

**Version:** 1.22.4

Aurora MySQL 1.22.4 is generally available. Aurora MySQL 1.\* versions are compatible with MySQL 5.6 and Aurora MySQL 2.\* versions are compatible with MySQL 5.7.

This engine version is scheduled to be deprecated on February 28, 2023. For more information, see [ Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.MySQL56.EOL.html).

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 To create a cluster with an older version of Aurora MySQL, specify the engine version through the RDS Console, the AWS CLI, or the Amazon RDS API. 

**Note**  <a name="lts_notice_1224"></a>
 This version is designated as a long-term support (LTS) release. For more information, see [ Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Versions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*. 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.1224.Improvements"></a>

 **Security fixes:** 

 Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below: 
+ [CVE-2020-14867](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14867)
+ [CVE-2020-14812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14812)
+ [CVE-2020-14793](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14793)
+ [CVE-2020-14769](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14769)
+ [CVE-2020-14765](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14765)
+ [CVE-2020-14672](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14672)
+ [CVE-2020-1971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-1971)

 **Availability improvements:** 
+  Fixed an issue that could trigger a database restart or failover during a `kill session` command. If you encounter this issue, contact AWS support to enable this fix on your instance. 
+  Improved binary logging to reduce crash recovery time and commit latency when large transactions are involved. 
+  Fixed an issue that caused a binlog replica to stop with an `HA_ERR_KEY_NOT_FOUND` error. 