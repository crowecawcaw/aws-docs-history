

# Administering your Amazon RDS for Db2 DB instance
<a name="db2-administering-db-instance"></a>

This topic covers the common management tasks that you perform with an Amazon RDS for Db2 DB instance. Some tasks are the same for all Amazon RDS DB instances. Other tasks are specific to RDS for Db2.

The following tasks are common to all RDS databases. There are also tasks specific to RDS for Db2, such as connecting to an RDS for Db2 database with a standard SQL client.


| Task area | Relevant documentation | 
| --- | --- | 
| **Instance classes, storage, and PIOPS**<br />If you are creating a production instance, learn how instance classes, storage types, and Provisioned IOPS work in Amazon RDS.  | [DB instance classes](Concepts.DBInstanceClass.md)<br />[Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage) | 
| **Multi-AZ deployments**<br />A production DB instance should use Multi-AZ deployments. Multi-AZ deployments provide increased availability, data durability, and fault tolerance for DB instances.  | [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) | 
| **Amazon VPC**<br />If your AWS account has a default virtual private cloud (VPC), then your DB instance is automatically created inside the default VPC. If your account doesn't have a default VPC, and you want the DB instance in a VPC, create the VPC and subnet groups before you create the DB instance.  | [Working with a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md) | 
| **Security groups**<br />By default, DB instances use a firewall that prevents access. Make sure that you create a security group with the correct IP addresses and network configuration to access the DB instance. | [Controlling access with security groups](Overview.RDSSecurityGroups.md) | 
| **Parameter groups**<br />Because your RDS for Db2 DB instance requires that you add the `rds.ibm_customer_id` and `rds.ibm_site_id` parameters, create a parameter group before you create the DB instance. If your DB instance requires other specific database parameters, also add them to this parameter group before you create the DB instance. | [Adding IBM IDs to a parameter group for RDS for Db2 DB instances](db2-licensing.md#db2-licensing-options-byol-adding-ids)<br />[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md) | 
| **Option groups**<br />If your DB instance requires specific database options, create an option group before you create the DB instance. | [Options for Amazon RDS for Db2 DB instances](Db2.Options.md) | 
| **Connecting to your DB instance**<br />After creating a security group and associating it to a DB instance, you can connect to the DB instance with any standard SQL client application such as IBM Db2 CLP.  | [Connecting to your Db2 DB instance](USER_ConnectToDb2DBInstance.md) | 
| **Backup and restore**<br />You can configure your DB instance to take automated storage backups, or take manual storage snapshots, and then restore instances from the backups or snapshots.  | [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md) | 
| **Monitoring**<br />You can monitor an RDS for Db2 DB instance with IBM Db2 Data Management Console. <br />You can also monitor an RDS for Db2 DB instance by using CloudWatch Amazon RDS metrics, events, and enhanced monitoring.  | [Connecting to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console](db2-connecting-with-ibm-data-management-console.md)<br />[Viewing metrics in the Amazon RDS console](USER_Monitoring.md)<br />[Viewing Amazon RDS events](USER_ListEvents.md)<br />[Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.OS.md) | 
| **Log files**<br />You can access the log files for your RDS for Db2 DB instance. | [Monitoring Amazon RDS log files](USER_LogAccess.md) | 

**Topics**
+ [Performing common system tasks for Amazon RDS for Db2 DB instances](db2-performing-common-system-tasks-db-instances.md)
+ [Performing common database tasks for Amazon RDS for Db2 DB instances](db2-performing-common-database-tasks-db-instances.md)