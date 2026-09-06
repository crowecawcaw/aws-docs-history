

# Importing data into an Amazon RDS for MySQL DB instance
<a name="MySQL.Procedural.Importing.Other"></a>

You can use several different techniques to import data into an RDS for MySQL DB instance. The best approach depends on a number of factors:
+ Source of the data
+ Amount of data
+ One-time import or ongoing
+ Amount of downtime

 If you are also migrating an application with the data, the amount of downtime is important to consider.

The following table lists techniques to importing data into an RDS for MySQL DB instance:


| Source | Amount of data | One time or ongoing | Application downtime | Technique | More information | 
| --- | --- | --- | --- | --- | --- | 
| Existing MySQL database on premises or on Amazon EC2 | Any | One time | Some | Create a backup of your on-premises database, store it on Amazon S3, and then restore the backup file to a new Amazon RDS DB instance running MySQL. | [Restoring a backup into an Amazon RDS for MySQL DB instance](MySQL.Procedural.Importing.md) | 
| Existing MySQL database on premises or on Amazon EC2 | Any | Ongoing | Minimal | Configure replication with an existing MySQL database as the replication source. | [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.Repl.md)<br />[Importing data to an Amazon RDS for MySQL database with reduced downtime](mysql-importing-data-reduced-downtime.md) | 
| Any existing database | Any | One time or ongoing | Minimal | Use AWS Database Migration Service to migrate the database with minimal downtime and, for many database DB engines, continue ongoing replication. | [What is AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) and [Using a MySQL-compatible database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html) in the *AWS Database Migration Service User Guide*  | 
| Existing MySQL DB instance | Any | One time or ongoing | Minimal | Create a read replica for ongoing replication. Promote the read replica for one-time creation of a new DB instance. | [Working with DB instance read replicas](USER_ReadRepl.md) | 
| Existing MySQL database | Small | One time | Some | Copy the data directly to your MySQL DB instance using a command-line utility. | [Importing data from an external MySQL database to an Amazon RDS for MySQL DB instance](mysql-importing-data-external-database.md) | 
| Data not stored in an existing database | Medium | One time | Some | Create flat files and import them using MySQL LOAD DATA LOCAL INFILE statements. | [Importing data from any source to an Amazon RDS for MySQL DB instance](mysql-importing-data-any-source.md) | 

**Note**  
The `mysql` system database contains authentication and authorization information required to log in to your DB instance and access your data. Dropping, altering, renaming, or truncating tables, data, or other contents of the `mysql` database in your DB instance can result in error and might render the DB instance and your data inaccessible. If this occurs, you can restore the DB instance from a snapshot using the AWS CLI [restore-db-instance-from-db-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html) command. You can recover the DB instance using the AWS CLI [restore-db-instance-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html) command. 