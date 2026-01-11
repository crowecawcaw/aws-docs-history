# Configuring MariaDB binary

logging

The _binary log_ is a set of log files that contain information
about data modifications made to a MariaDB server instance. The binary log contains
information such as the following:

- Events that describe database changes such as table creation or row
  modifications
- Information about the duration of each statement that updated data
- Events for statements that could have updated data but didn't
  The binary log records statements that are sent during replication. It is also
  required for some recovery operations. For more information, see [Binary Log](https://mariadb.com/kb/en/binary-log/ "https://mariadb.com/kb/en/binary-log/") in the MariaDB
  documentation.

The automated backups feature determines whether binary logging is turned on or off
for MariaDB. You have the following options:

Turn binary logging on

Set the backup retention period to a positive nonzero value.

Turn binary logging off

Set the backup retention period to zero.

For more information, see [Enabling automated
backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

MariaDB on Amazon RDS supports the _row-based_,
_statement-based_, and _mixed_ binary logging
formats. The default binary logging format is _mixed_. For details on
the different MariaDB binary log formats, see [Binary Log
Formats](http://mariadb.com/kb/en/mariadb/binary-log-formats/ "http://mariadb.com/kb/en/mariadb/binary-log-formats/") in the MariaDB documentation.

If you plan to use replication, the binary logging format is important. This is
because it determines the record of data changes that is recorded in the source and sent
to the replication targets. For information about the advantages and disadvantages of
different binary logging formats for replication, see [Advantages
and Disadvantages of Statement-Based and Row-Based Replication](https://dev.mysql.com/doc/refman/5.7/en/replication-sbr-rbr.html "https://dev.mysql.com/doc/refman/5.7/en/replication-sbr-rbr.html") in the MySQL
documentation.

###### Important

Setting the binary logging format to row-based can result in very large binary log
files. Large binary log files reduce the amount of storage available for a DB
instance. They also can increase the amount of time to perform a restore operation
of a DB instance.

Statement-based replication can cause inconsistencies between the source DB
instance and a read replica. For more information, see [Unsafe Statements for Statement-based Replication](https://mariadb.com/kb/en/library/unsafe-statements-for-statement-based-replication/ "https://mariadb.com/kb/en/library/unsafe-statements-for-statement-based-replication/") in the MariaDB
documentation.

Enabling binary logging increases the number of write disk I/O operations to the DB
instance. You can monitor IOPS usage with the `WriteIOPS` CloudWatch
metric.

###### To set the MariaDB binary logging format

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the parameter group that is used by the DB instance that you want to
   modify.

You can't modify a default parameter group. If the DB instance is using a
default parameter group, create a new parameter group and associate it with the
DB instance.

For more information on DB parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 4. For **Parameter group actions**, choose
**Edit**. 5. Set the `binlog_format` parameter to the binary logging format of
your choice (**ROW**, **STATEMENT**, or **MIXED**).

You can turn off binary logging by setting the backup retention period of a DB instance to
zero, but this disables daily automated backups. Disabling automated backups
turns off or disables the `log_bin` session variable. This disables
binary logging on the RDS for MariaDB DB instance, which in turn resets the
`binlog_format` session variable to the default value of
`ROW` in the database. We recommend that you don't disable
backups. For more information about the **Backup retention
period** setting, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md"). 6. Choose **Save changes** to save the updates to the DB
parameter group.
Because the `binlog_format` parameter is dynamic in RDS for MariaDB, you don't need to reboot the DB
instance for the changes to apply.

###### Important

Changing a DB parameter group affects all DB instances that use that parameter group. If you want to specify
different binary logging formats for different MariaDB DB instances in an AWS Region, the DB instances must use
different DB parameter groups. These parameter groups identify different logging formats. Assign the appropriate
DB parameter group to the each DB instance.
