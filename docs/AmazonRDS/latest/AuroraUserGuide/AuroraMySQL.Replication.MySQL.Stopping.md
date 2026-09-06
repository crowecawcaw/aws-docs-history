

# Stopping binary log replication for Aurora MySQL
<a name="AuroraMySQL.Replication.MySQL.Stopping"></a>

To stop binary log replication with a MySQL DB instance, external MySQL database, or another Aurora DB cluster, follow these steps, discussed in detail following in this topic.

[1. Stop binary log replication on the replica target](#AuroraMySQL.Replication.MySQL.Stopping.StopReplication)

[2. Turn off binary logging on the replication source](#AuroraMySQL.Replication.MySQL.Stopping.DisableBinaryLogging)

## 1. Stop binary log replication on the replica target
<a name="AuroraMySQL.Replication.MySQL.Stopping.StopReplication"></a>

Use the following instructions to stop binary log replication for your database engine.


|  Database engine  |  Instructions  | 
| --- | --- | 
|  Aurora MySQL  | **To stop binary log replication on an Aurora MySQL DB cluster replica target**<br />Connect to the Aurora DB cluster that is the replica target, and call the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication) procedure. | 
|  RDS for MySQL  | **To stop binary log replication on an Amazon RDS DB instance**<br />Connect to the RDS DB instance that is the replica target and call the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication) procedure. | 
|  MySQL (external)  | **To stop binary log replication on an external MySQL database**<br />Connect to the MySQL database and run the `STOP SLAVE` (version 5.7) or `STOP REPLICA` (version 8.0) command. | 

## 2. Turn off binary logging on the replication source
<a name="AuroraMySQL.Replication.MySQL.Stopping.DisableBinaryLogging"></a>

Use the instructions in the following table to turn off binary logging on the replication source for your database engine.


| Database engine | Instructions | 
| --- | --- | 
|  Aurora MySQL  | **To turn off binary logging on an Amazon Aurora DB cluster**1.  Connect to the Aurora DB cluster that is the replication source. <br />2.  Use the [mysql.rds\_set\_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration) procedure and specify the configuration parameter `binlog retention hours`, with the value `NULL`, as shown in the following example. <pre>CALL mysql.rds_set_configuration('binlog retention hours', NULL);</pre>  You can't use the value `0` for `binlog retention hours`.  <br />3.  Set the `binlog_format` parameter to `OFF` on the replication source. The `binlog_format` parameter is in the custom DB cluster parameter group associated with your DB cluster. <br />After you've changed the `binlog_format` parameter value, reboot your DB cluster for the change to take effect. <br />For more information, see [Amazon Aurora DB cluster and DB instance parameters](USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups) and [Modifying parameters in a DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.Modifying.md).  | 
|  RDS for MySQL  | **To turn off binary logging on an Amazon RDS DB instance**<br />You can't turn off binary logging directly for an Amazon RDS DB instance, but you can turn it off by doing the following:1.  Turn off automated backups for the DB instance. You can turn off automated backups by modifying an existing DB instance and setting the **Backup Retention Period** to 0. For more information, see [Modifying an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) and [ Working with backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) in the *Amazon Relational Database Service User Guide*. <br />2.  Delete all read replicas for the DB instance. For more information, see [Working with read replicas of MariaDB, MySQL, and PostgreSQL DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) in the *Amazon Relational Database Service User Guide*.  | 
|  MySQL (external)  | **To turn off binary logging on an external MySQL database**<br />Connect to the MySQL database and call the `STOP REPLICATION` command.1.  From a command shell, stop the `mysqld` service, <pre>sudo service mysqld stop</pre> <br />2.  Edit the `my.cnf` file (this file is usually under `/etc`). <pre>sudo vi /etc/my.cnf</pre> <br />Delete the `log_bin` and `server_id `options from the `[mysqld]` section.  <br />For more information, see [Setting the replication source configuration](http://dev.mysql.com/doc/refman/8.0/en/replication-howto-masterbaseconfig.html) in the MySQL documentation. <br />3.  Start the mysql service. <pre>sudo service mysqld start</pre>  | 