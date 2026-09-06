

# Amazon RDS for Oracle
<a name="CHAP_Oracle"></a>

Amazon RDS supports DB instances that run the following versions and editions of Oracle Database:
+ Oracle Database 26ai (26.0.0.0)
+ Oracle Database 21c (21.0.0.0)
+ Oracle Database 19c (19.0.0.0)

**Note**  
Oracle Database 11g, Oracle Database 12c, and Oracle Database 18c are legacy versions that are no longer supported in Amazon RDS.  
Oracle is ending support for Oracle Database 21c on July 31, 2027. After this date, Amazon RDS for Oracle will deprecate Oracle Database 21c. To plan your upgrade, see [Preparing for Oracle Database 21c end of support](USER_UpgradeDBInstance.Oracle.21c-end-of-support.md).

Before creating a DB instance, complete the steps in the [Setting up your Amazon RDS environment](CHAP_SettingUp.md) section of this guide. When you create a DB instance using your master account, the account gets DBA privileges, with some limitations. For example, the master user can't perform operations that require SYSDBA privileges, and access to certain Oracle-supplied packages and tables is restricted. For more information, see [RDS for Oracle users and privileges](Oracle.Concepts.Privileges.md). Use this account for administrative tasks such as creating additional database accounts. You can't use SYS, SYSTEM, or other Oracle-supplied administrative accounts. To grant privileges on objects owned by SYS, use the `rdsadmin.rdsadmin_util.grant_sys_object` procedure. For more information, see [How to manage privileges on SYS objects](Oracle.Concepts.Privileges.md#Oracle.Concepts.Privileges.SYS-objects).

You can create the following:
+ DB instances
+ DB snapshots
+ Point-in-time restores
+ Automated backups
+ Manual backups

You can use DB instances running Oracle Database inside a VPC. You can also add features to your DB instance by enabling various options, such as Oracle Spatial or Oracle Statspack. To use an option, you create an option group, add the option to it, and associate the option group with your DB instance. For more information, see [Adding options to Oracle DB instances](Appendix.Oracle.Options.md). Amazon RDS supports Multi-AZ deployments for Oracle as a high-availability, failover solution.

**Important**  
To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. It also restricts access to certain system procedures and tables that need advanced privileges. You can access your database using standard SQL clients such as Oracle SQL\*Plus. However, you can't access the host directly by using Telnet or Secure Shell (SSH).

**Topics**
+ [Overview of Oracle on Amazon RDS](Oracle.Concepts.overview.md)
+ [Connecting to your Oracle DB instance](USER_ConnectToOracleInstance.md)
+ [Securing Oracle DB instance connections](Oracle.Concepts.RestrictedDBAPrivileges.md)
+ [Working with CDBs in RDS for Oracle](oracle-multitenant.md)
+ [Administering your RDS for Oracle DB instance](Appendix.Oracle.CommonDBATasks.md)
+ [Working with storage in RDS for Oracle](User_Oracle_AdditionalStorage.md)
+ [Configuring advanced RDS for Oracle features](CHAP_Oracle.advanced-features.md)
+ [AI features for Oracle](CHAP_Oracle.ai-features.md)
+ [Importing data into Oracle on Amazon RDS](Oracle.Procedural.Importing.md)
+ [Working with read replicas for Amazon RDS for Oracle](oracle-read-replicas.md)
+ [Adding options to Oracle DB instances](Appendix.Oracle.Options.md)
+ [Upgrading the RDS for Oracle DB engine](USER_UpgradeDBInstance.Oracle.md)
+ [Using third-party software with your RDS for Oracle DB instance](Oracle.Resources.md)
+ [Oracle Database engine release notes](USER_Oracle_Releases.md)