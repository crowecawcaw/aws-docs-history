# Configuring Aurora MySQL binary logging for Single-AZ databases

The _binary log_ is a set of log files that contain information about
data modifications made to an Aurora MySQL server
instance. The binary log contains information such as the following:

- Events that describe database changes such as table creation or row
  modifications
- Information about the duration of each statement that updated data
- Events for statements that could have updated data but didn't
  The binary log records statements that are sent during replication. It is also required
  for some recovery operations. For more information, see [The Binary Log](https://dev.mysql.com/doc/refman/8.0/en/binary-log.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log.html") in
  the MySQL documentation.

Binary logs are accessible only from the primary DB instance, not from
the replicas.

MySQL on Amazon Aurora supports the _row-based_,
_statement-based_, and _mixed_ binary logging
formats. We recommend mixed unless you need a specific binlog format. For details on the
different Aurora MySQL binary log formats, see [Binary Logging
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

Statement-based replication can cause inconsistencies between the source DB cluster
and a read replica. For more information, see [Determination of Safe and Unsafe Statements in Binary Logging](https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rbr-safe-unsafe.html") in the MySQL
documentation.

Enabling binary logging increases the number of write disk I/O operations to the DB
cluster. You can monitor IOPS usage with the `VolumeWriteIOPs` CloudWatch metric.

###### To set the MySQL binary logging format

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Parameter groups**.
3. Choose the DB cluster parameter group,
   associated with the DB cluster, that you want to modify.

You can't modify a default parameter group. If the DB cluster is using a default parameter group, create a new parameter
group and associate it with the DB cluster.

For more information on parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 4. From **Actions**, choose **Edit**. 5. Set the `binlog_format` parameter to the binary logging format of your
choice (`ROW`, `STATEMENT`, or `MIXED`). You can also use the value `OFF` to turn off
binary logging.

###### Note

Setting `binlog_format` to `OFF` in the DB cluster
parameter group disables the `log_bin` session variable. This
disables binary logging on the Aurora MySQL DB cluster, which in turn resets the
`binlog_format` session variable to the default value of
`ROW` in the database. 6. Choose **Save changes** to save the updates to the DB cluster parameter group.
After you perform these steps, you must reboot the writer instance in
the DB cluster for your changes to apply. In Aurora MySQL version 2.09 and lower, when you
reboot the writer instance, all of the reader instances in the DB cluster are also rebooted.
In Aurora MySQL version 2.10 and higher, you must reboot all of the reader instances manually.
For more information, see [Rebooting an Amazon Aurora DB cluster or Amazon Aurora DB instance](USER_RebootCluster.md "USER_RebootCluster.md").

###### Important

Changing a DB cluster parameter group affects all DB clusters that use that parameter
group. If you want to specify different binary logging formats for different Aurora MySQL
DB clusters in an AWS Region, the DB clusters must use different DB cluster parameter
groups. These parameter groups identify different logging formats. Assign the
appropriate DB cluster parameter group to each DB clusters. For more information about
Aurora MySQL parameters, see [Aurora MySQL configuration parameters](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").
