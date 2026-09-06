

# Aurora MySQL database engine updates 2020-11-24 (version 1.23.1) (Deprecated)
<a name="AuroraMySQL.Updates.1231"></a><a name="1231"></a><a name="1.23.1"></a>

**Version:** 1.23.1

Aurora MySQL 1.23.1 is generally available. Aurora MySQL 1.\* versions are compatible with MySQL 5.6 and Aurora MySQL 2.\* versions are compatible with MySQL 5.7.

This engine version is scheduled to be deprecated on February 28, 2023. For more information, see [ Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.MySQL56.EOL.html).

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 To create a cluster with an older version of Aurora MySQL, specify the engine version through the RDS Console, the AWS CLI, or the Amazon RDS API. 

 If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*. 

## Improvements
<a name="AuroraMySQL.Updates.1231.Improvements"></a>

 **Security fixes:** 

 Fixes and other enhancements to fine-tune handling in a managed environment. Additional CVE fixes below: 
+ [CVE-2020-14559](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14559)
+ [CVE-2020-14539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-14539)

 **Incompatible changes:** 

 This version introduces a permission change that affects the behavior of the `mysqldump` command. Users must have the `PROCESS` privilege to access the `INFORMATION_SCHEMA.FILES` table. To run the `mysqldump` command without any changes, grant the `PROCESS` privilege to the database user that the `mysqldump` command connects to. You can also run the `mysqldump` command with the `--no-tablespaces` option. With that option, the `mysqldump `output doesn't include any `CREATE LOGFILE GROUP` or `CREATE TABLESPACE` statements. In that case, the `mysqldump` command doesn't access the `INFORMATION_SCHEMA.FILES` table, and you don't need to grant the `PROCESS` permission. 

 **Availability improvements:** 
+  Fixed an issue that causes an Aurora reader instance in a global database secondary cluster running 1.23.0 to restart repeatedly. 
+  Fixed an issue where a global database secondary Region's replicas might restart when upgraded to release 1.23.0 while the primary Region writer was on an older release version. 
+  Fixed a memory leak in dynamic resizing feature, introduced in Aurora MySQL 1.23.0. 
+  Fixed an issue that might cause server restart during execution of a query using the parallel query feature. 
+  Fixed an issue that might cause a client session to hang when the database engine encounters an error while reading from or writing to the network. 