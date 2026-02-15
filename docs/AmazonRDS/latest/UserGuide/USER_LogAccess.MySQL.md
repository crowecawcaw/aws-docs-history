# Configuring RDS for MySQL binary logging for Single-AZ databases

The _binary log_ is a set of log files that contain information about
data modifications made to an MySQL server
instance. The binary log contains information such as the following:

- Events that describe database changes such as table creation or row
  modifications
- Information about the duration of each statement that updated data
- Events for statements that could have updated data but didn't
  The binary log records statements that are sent during replication. It is also required
  for some recovery operations. For more information, see [The Binary Log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log.html") in
  the MySQL documentation.

The automated backups feature determines whether binary logging is
turned on or off for MySQL. You have the following options:

Turn binary logging on

Set the backup retention period to a positive nonzero value.

Turn binary logging off

Set the backup retention period to zero.

For more information, see [Enabling automated
backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

MySQL on Amazon RDS supports the _row-based_,
_statement-based_, and _mixed_ binary logging
formats. We recommend mixed unless you need a specific binlog format. For details on the
different MySQL binary log formats, see [Binary Logging
Formats](https://dev.mysql.com/doc/refman/8.0/en/binary-log-formats.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log-formats.html") in the MySQL documentation.

If you plan to use replication, the binary logging format is important because it
determines the record of data changes that is recorded in the source and sent to the
replication targets. For information about the advantages and disadvantages of different
binary logging formats for replication, see [Advantages and
Disadvantages of Statement-Based and Row-Based Replication](https://dev.mysql.com/doc/refman/8.0/en/replication-sbr-rbr.html "https://dev.mysql.com/doc/refman/8.0/en/replication-sbr-rbr.html") in the MySQL
documentation.

###### Important

With MySQL 8.0.34, MySQL deprecated the `binlog_format` parameter. In later MySQL
versions, MySQL plans to remove the parameter and only support row-based replication. As
a result, we recommend using row-based logging for new MySQL replication setups. For
more information, see [binlog_format](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_format "https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_binlog_format") in the MySQL documentation.

MySQL versions 8.0 and 8.4 accept the parameter `binlog_format`. When using this parameter, MySQL
issues a deprecation warning. In a future major release, MySQL will remove the parameter `binlog_format`.

Statement-based replication can cause inconsistencies between the source DB instance
and a read replica. For more information, see [Determination of Safe and Unsafe Statements in Binary Logging](https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html") in the MySQL
documentation.

Enabling binary logging increases the number of write disk I/O operations to the DB
instance. You can monitor IOPS usage with the `WriteIOPS` CloudWatch metric.

###### To set the MySQL binary logging format

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the DB parameter group,
   associated with the DB instance, that you want to modify.

You can't modify a default parameter group. If the DB instance is using a default parameter group, create a new parameter
group and associate it with the DB instance.

For more information on parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 4. From **Actions**, choose **Edit**. 5. Set the `binlog_format` parameter to the binary logging format of your
choice (`ROW`, `STATEMENT`, or `MIXED`).

You can turn off binary logging by setting the backup
retention period of a DB instance to zero, but this disables daily automated
backups. Disabling automated backups turns off or disables the `log_bin`
session variable. This disables binary logging on the RDS for MySQL DB instance, which
in turn resets the `binlog_format` session variable to the default value
of `ROW` in the database. We recommend that you don't disable backups.
For more information about the **Backup retention
period** setting, see [Settings for DB instances](USER_ModifyInstance.md "USER_ModifyInstance.md"). 6. Choose **Save changes** to save the updates to the DB parameter group.
Because the `binlog_format` parameter is dynamic in
RDS for MySQL, you don't need to reboot the DB instance for the changes to apply. (Note that in
Aurora MySQL, this parameter is static. For more information, see [Configuring Aurora MySQL binary logging](../AuroraUserGuide/USER_LogAccess.MySQL.md "../AuroraUserGuide/USER_LogAccess.MySQL.md").)

###### Important

Changing a DB parameter group affects all DB instances that use that parameter group.
If you want to specify different binary logging formats for different MySQL DB instances
in an AWS Region, the DB instances must use different DB parameter groups. These
parameter groups identify different logging formats. Assign the appropriate DB parameter
group to the each DB instance.
