

# Administering your RDS for Oracle DB instance
<a name="Appendix.Oracle.CommonDBATasks"></a>

Following are the common management tasks that you perform with an RDS for Oracle DB instance. Some tasks are the same for all RDS DB instances. Other tasks are specific to RDS for Oracle.

The following tasks are common to all RDS databases, but Oracle Database has special considerations. For example, you connect to an Oracle database using the Oracle clients SQL\*Plus and SQL Developer.



| Task area | Relevant documentation | 
| --- | --- | 
| **Instance classes, storage, and PIOPS**<br />If you are creating a production instance, learn how instance classes, storage types, and Provisioned IOPS work in Amazon RDS.  | [RDS for Oracle DB instance classes](Oracle.Concepts.InstanceClasses.md)<br />[Amazon RDS storage types](CHAP_Storage.md#Concepts.Storage) | 
| **Multi-AZ deployments**<br />A production DB instance should use Multi-AZ deployments. Multi-AZ deployments provide increased availability, data durability, and fault tolerance for DB instances.  | [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) | 
| **Amazon VPC**<br />If your AWS account has a default virtual private cloud (VPC), then your DB instance is automatically created inside the default VPC. If your account doesn't have a default VPC, and you want the DB instance in a VPC, create the VPC and subnet groups before you create the instance.  | [Working with a DB instance in a VPC](USER_VPC.WorkingWithRDSInstanceinaVPC.md) | 
| **Security groups**<br />By default, DB instances use a firewall that prevents access. Make sure that you create a security group with the correct IP addresses and network configuration to access the DB instance. | [Controlling access with security groups](Overview.RDSSecurityGroups.md) | 
| **Parameter groups**<br />If your DB instance is going to require specific database parameters, create a parameter group before you create the DB instance.  | [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md) | 
| **Option groups**<br />If your DB instance requires specific database options, create an option group before you create the DB instance.  | [Adding options to Oracle DB instances](Appendix.Oracle.Options.md) | 
| **Connecting to your DB instance**<br />After creating a security group and associating it to a DB instance, you can connect to the DB instance using any standard SQL client application such as Oracle SQL\*Plus.  | [Connecting to your Oracle DB instance](USER_ConnectToOracleInstance.md) | 
| **Backup and restore**<br />You can configure your DB instance to take automated backups, or take manual snapshots, and then restore instances from the backups or snapshots.  | [Backing up, restoring, and exporting data](CHAP_CommonTasks.BackupRestore.md) | 
| **Monitoring**<br />You can monitor an Oracle DB instance by using CloudWatch Amazon RDS metrics, events, and enhanced monitoring.  | [Viewing metrics in the Amazon RDS console](USER_Monitoring.md)<br />[Viewing Amazon RDS events](USER_ListEvents.md) | 
| **Log files**<br />You can access the log files for your Oracle DB instance.  | [Monitoring Amazon RDS log files](USER_LogAccess.md) | 

Following, you can find a description for Amazon RDS–specific implementations of common DBA tasks for RDS Oracle. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances. Also, RDS restricts access to certain system procedures and tables that require advanced privileges. In many of the tasks, you run the `rdsadmin` package, which is an Amazon RDS–specific tool that enables you to administer your database.

The following are common DBA tasks for DB instances running Oracle:
+ [System tasks](Appendix.Oracle.CommonDBATasks.System.md)    
<a name="dba-tasks-oracle-system-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [Database tasks](Appendix.Oracle.CommonDBATasks.Database.md)    
<a name="dba-tasks-oracle-database-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [Log tasks](Appendix.Oracle.CommonDBATasks.Log.md)    
<a name="dba-tasks-oracle-log-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [RMAN tasks](Appendix.Oracle.CommonDBATasks.RMAN.md)    
<a name="dba-tasks-oracle-rman-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [Oracle Scheduler tasks](Appendix.Oracle.CommonDBATasks.Scheduler.md)    
<a name="dba-tasks-oracle-scheduler-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [Diagnosing problems](Appendix.Oracle.CommonDBATasks.Diagnostics.md)    
<a name="dba-tasks-oracle-diagnostic-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 
+ [Other tasks](Appendix.Oracle.CommonDBATasks.Misc.md)    
<a name="dba-tasks-oracle-misc-reference"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

 

You can also use Amazon RDS procedures for Amazon S3 integration with Oracle and for running OEM Management Agent database tasks. For more information, see [Amazon S3 integration](oracle-s3-integration.md) and [Performing database tasks with the Management Agent](Oracle.Options.OEMAgent.md#Oracle.Options.OEMAgent.DBTasks).

## Purging the recycle bin
<a name="Appendix.Oracle.CommonDBATasks.PurgeRecycleBin"></a>

When you drop a table, your Oracle database doesn't immediately remove its storage space. The database renames the table and places it and any associated objects in a recycle bin. Purging the recycle bin removes these items and releases their storage space. 

To purge the entire recycle bin, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.purge_dba_recyclebin`. However, this procedure can't purge the recycle bin of `SYS` and `RDSADMIN` objects. If you need to purge these objects, contact AWS Support. 

The following example purges the entire recycle bin.

```
EXEC rdsadmin.rdsadmin_util.purge_dba_recyclebin;
```