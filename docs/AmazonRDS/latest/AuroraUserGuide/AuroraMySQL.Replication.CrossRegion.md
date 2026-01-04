# Troubleshooting cross-Region replicas for Amazon Aurora MySQL

Following you can find a list of common error messages that you might encounter when creating an Amazon Aurora
cross-Region read replica, and how to resolve the specified errors.

## Source cluster [DB cluster ARN] doesn't have binlogs enabled

To resolve this issue, turn on binary logging on the source DB cluster. For more information, see
[Before you begin](AuroraMySQL.Replication.md#AuroraMySQL.Replication.CrossRegion.Prerequisites "AuroraMySQL.Replication.md#AuroraMySQL.Replication.CrossRegion.Prerequisites").

## Source cluster [DB cluster ARN] doesn't have cluster parameter group in sync on writer

You receive this error if you have updated the `binlog_format` DB cluster parameter, but have
not rebooted the primary instance for the DB cluster. Reboot the primary instance (that is, the writer)
for the DB cluster and try again.

## Source cluster [DB cluster ARN] already has a read replica in this region

You can have up to five cross-Region DB clusters that are read replicas for each source DB cluster in any
AWS Region. If you already have the maximum number of read replicas for a DB cluster in a particular
AWS Region, you must delete an existing one before you can create a new cross-Region DB cluster in that
Region.

## DB cluster [DB cluster ARN] requires a database engine upgrade for cross-Region replication support

To resolve this issue, upgrade the database engine version for all of the instances in the source DB
cluster to the most recent database engine version, and then try creating a cross-Region read replica DB
again.
