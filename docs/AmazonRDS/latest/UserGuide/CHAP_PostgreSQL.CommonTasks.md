

# Common management tasks for Amazon RDS for PostgreSQL
<a name="CHAP_PostgreSQL.CommonTasks"></a>

The following are the common management tasks you perform with an Amazon RDS for PostgreSQL DB instance, with links to relevant documentation for each task.


| Task area | Relevant documentation | 
| --- | --- | 
| **Setting up Amazon RDS for first-time use**<br />Before you can create your DB instance, make sure to complete a few prerequisites. For example, DB instances are created by default with a firewall that prevents access to it. So you need to create a security group with the correct IP addresses and network configuration to access the DB instance.  | [Setting up your Amazon RDS environment](CHAP_SettingUp.md) | 
| **Understanding Amazon RDS DB instances**<br />If you are creating a DB instance for production purposes, you should understand how instance classes, storage types, and Provisioned IOPS work in Amazon RDS.  | [DB instance classes](Concepts.DBInstanceClass.md)<br />[Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage)<br />[Provisioned IOPS SSD storage](CHAP_Storage.md#USER_PIOPS) | 
| **Finding available PostgreSQL versions**<br />Amazon RDS supports several versions of PostgreSQL.  | [Available PostgreSQL database versions](PostgreSQL.Concepts.General.DBVersions.md) | 
| **Setting up high availability and failover support**<br />A production DB instance should use Multi-AZ deployments. Multi-AZ deployments provide increased availability, data durability, and fault tolerance for DB instances.  | [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) | 
| **Understanding the Amazon Virtual Private Cloud (VPC) network**<br />If your AWS account has a default VPC, then your DB instance is automatically created inside the default VPC. In some cases, your account might not have a default VPC, and you might want the DB instance in a VPC. In these cases, create the VPC and subnet groups before you create the DB instance. <br /> | [Working with a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md) | 
| **Importing data into Amazon RDS PostgreSQL**<br />You can use several different tools to import data into your PostgreSQL DB instance on Amazon RDS.  | [Importing data into PostgreSQL on Amazon RDS](PostgreSQL.Procedural.Importing.md) | 
| **Setting up read-only read replicas (primary and standbys)**<br />RDS for PostgreSQL supports read replicas in both the same AWS Region and in a different AWS Region from the primary instance. | [Working with DB instance read replicas](USER_ReadRepl.md)<br />[Working with read replicas for Amazon RDS for PostgreSQL](USER_PostgreSQL.Replication.ReadReplicas.md)<br />[Creating a read replica in a different AWS Region](USER_ReadRepl.XRgn.md) | 
| **Understanding security groups**<br />By default, DB instances are created with a firewall that prevents access to them. To provide access through that firewall, you edit the inbound rules for the VPC security group associated with the VPC hosting the DB instance.  | [Controlling access with security groups](Overview.RDSSecurityGroups.md) | 
| **Setting up parameter groups and features**<br />To change the default parameters for your DB instance, create a custom DB parameter group and change settings to that. If you do this before creating your DB instance, you can choose your custom DB parameter group when you create the instance.  | [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md) | 
| **Connecting to your PostgreSQL DB instance**<br />After creating a security group and associating it to a DB instance, you can connect to the DB instance using any standard SQL client application such as `psql` or `pgAdmin`. | [Connecting to a DB instance running the PostgreSQL database engine](USER_ConnectToPostgreSQLInstance.md)<br />[Using SSL with a PostgreSQL DB instance](PostgreSQL.Concepts.General.SSL.md) | 
| **Backing up and restoring your DB instance**<br />You can configure your DB instance to take automated backups, or take manual snapshots, and then restore instances from the backups or snapshots.  | [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md) | 
| **Monitoring the activity and performance of your DB instance**<br />You can monitor a PostgreSQL DB instance by using CloudWatch Amazon RDS metrics, events, and enhanced monitoring.  | [Viewing metrics in the Amazon RDS console](USER_Monitoring.md)<br />[Viewing Amazon RDS events](USER_ListEvents.md) | 
| **Upgrading the PostgreSQL database version**<br />You can do both major and minor version upgrades for your PostgreSQL DB instance.  | [Upgrades of the RDS for PostgreSQL DB engine](USER_UpgradeDBInstance.PostgreSQL.md)<br />[Choosing a major version for an RDS for PostgreSQL upgrade](USER_UpgradeDBInstance.PostgreSQL.MajorVersion.md) | 
| **Working with log files**<br />You can access the log files for your PostgreSQL DB instance.  | [ RDS for PostgreSQL database log files](USER_LogAccess.Concepts.PostgreSQL.md) | 
| **Understanding the best practices for PostgreSQL DB instances**<br />Find some of the best practices for working with PostgreSQL on Amazon RDS.  | [Best practices for working with PostgreSQL](CHAP_BestPractices.md#CHAP_BestPractices.PostgreSQL) | 

Following is a list of other sections in this guide that can help you understand and use important features of RDS for PostgreSQL: 
+  [Understanding PostgreSQL roles and permissions](Appendix.PostgreSQL.CommonDBATasks.Roles.md) 
+  [Controlling user access to the PostgreSQL database](Appendix.PostgreSQL.CommonDBATasks.Access.md) 
+  [Working with parameters on your RDS for PostgreSQL DB instance](Appendix.PostgreSQL.CommonDBATasks.Parameters.md) 
+  [Understanding logging mechanisms supported by RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.Auditing) 
+  [Working with PostgreSQL autovacuum on Amazon RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md) 
+  [Using a custom DNS server for outbound network access](Appendix.PostgreSQL.CommonDBATasks.CustomDNS.md) 