

# Aurora MySQL database engine updates 2020-03-05 (version 1.22.2) (Deprecated)
<a name="AuroraMySQL.Updates.1222"></a>

**Version:** 1.22.2

Aurora MySQL 1.22.2 is generally available. Aurora MySQL 1.\* versions are compatible with MySQL 5.6 and Aurora MySQL 2.\* versions are compatible with MySQL 5.7.

This engine version is scheduled to be deprecated on February 28, 2023. For more information, see [ Preparing for Amazon Aurora MySQL-Compatible Edition version 1 end of life](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.MySQL56.EOL.html).

 Currently supported Aurora MySQL releases are 1.19.5, 1.19.6, 1.22.\*, 1.23.\*, 2.04.\*, 2.07.\*, 2.08.\*, 2.09.\*, 2.10.\*, 3.01.\* and 3.02.\*. 

 To create a cluster with an older version of Aurora MySQL, please specify the engine version through the RDS Console, the AWS CLI, or the Amazon RDS API. 

**Note**  
 This version is currently not available in the following regions: AWS GovCloud (US-East) [us-gov-east-1], AWS GovCloud (US-West) [us-gov-west-1]. There will be a separate announcement once it is made available.   
 This version is designated as a long-term support (LTS) release. For more information, see [ Aurora MySQL long-term support (LTS) releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Versions.html#AuroraMySQL.Updates.LTS) in the *Amazon Aurora User Guide*. 

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [ Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.1222.Improvements"></a>

 **High priority fixes:** 
+  Fixed an issue of intermittent connection failures after certificate rotation. 
+  Fixed an issue that caused cloning to take longer on some database clusters with high write loads. 
+  Fixed an issue that broke logical replication when the `binlog_checksum` parameter is set to different values on the master and the replica. 
+  Fixed an issue where slow log and general log may not properly rotate on read replicas. 
+  Fixed an issue with ANSI Read Committed Isolation Level behavior. 