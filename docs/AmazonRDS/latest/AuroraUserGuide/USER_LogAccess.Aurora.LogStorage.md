

# Planning storage for Aurora database log files

Aurora MySQL and Aurora PostgreSQL store database log files on each DB instance. Aurora deletes log files when they reach the end of their retention period or when they use more storage than the DB instance allows, and it might delete files that it hasn't published to CloudWatch Logs yet. When it does, you receive [RDS-EVENT-0610](USER_Events.Messages.md#RDS-EVENT-0610) for a file past its retention period, or [RDS-EVENT-0611](USER_Events.Messages.md#RDS-EVENT-0611) for a file deleted because of storage.

If you need to keep a complete record of your logs, such as audit logs for compliance requirements, plan the storage for log files based on the amount of logs that your workload generates.

**Topics**
+ [Storage available for log files](#USER_LogAccess.Aurora.LogStorage.Location)
+ [When log files are deleted](#USER_LogAccess.Aurora.LogStorage.Deletion)
+ [Estimating the storage used by log files](#USER_LogAccess.Aurora.LogStorage.Estimating)
+ [Reducing the amount of logs](#USER_LogAccess.Aurora.LogStorage.Reducing)
+ [If you can't reduce audit logs](#USER_LogAccess.Aurora.LogStorage.Compliance)

## Storage available for log files
<a name="USER_LogAccess.Aurora.LogStorage.Location"></a>

For most DB instance classes, Aurora stores log files on a separate permanent storage volume. This volume has a fixed size according to the DB instance class, and it's separate from the local storage that Aurora uses for temporary files. The storage available for log files is 60 GiB for DB instance classes up to 2xlarge, and 500 GiB for DB instance classes of 4xlarge and larger. Burstable-performance instance classes, such as db.t3 and db.t4g, store log files on local storage.

For the storage available for each DB instance class, see the following:
+ [Temporary storage limits for Aurora MySQL](AuroraMySQL.Managing.Performance.md#AuroraMySQL.Managing.TempStorage)
+ [Temporary storage limits for Aurora PostgreSQL](AuroraPostgreSQL.Managing.md#AuroraPostgreSQL.Managing.TempStorage)

The `FreeLocalStorage` metric shows the free local storage. On DB instance classes that store log files on a separate volume, this metric doesn't include the storage used by log files.

## When log files are deleted
<a name="USER_LogAccess.Aurora.LogStorage.Deletion"></a>

Aurora deletes log files when they reach the end of their retention period or when they use too much storage, whichever comes first.
+ Aurora MySQL deletes log files when they reach 15 percent of the storage for log files. This threshold applies separately to the error logs and to the audit, general, and slow query logs combined. When a group reaches this threshold, Aurora MySQL first deletes the log files in that group that it has already published to CloudWatch Logs. If the threshold is still exceeded, it deletes more log files, including files that it hasn't published yet. Audit log files count against the threshold before general and slow query log files, so a large audit log can cause general and slow query log files to be deleted before they're published. For more information, see [Log rotation and retention for Aurora MySQL](USER_LogAccess.MySQL.LogFileSize.md#USER_LogAccess.AMS.LogFileSize.retention).
+ Aurora PostgreSQL keeps all PostgreSQL log files within one threshold, about half of the storage for log files. When the log files reach it, Aurora PostgreSQL compresses older log files. If that isn't enough, it deletes compressed log files that it has already published to CloudWatch Logs. If the storage fills up, it might also delete log files that it hasn't published yet. For more information, see [Setting the log retention period](USER_LogAccess.Concepts.PostgreSQL.overview.parameter-groups.md#USER_LogAccess.Concepts.PostgreSQL.log_retention_period).

## Estimating the storage used by log files
<a name="USER_LogAccess.Aurora.LogStorage.Estimating"></a>

To estimate how much storage your log files use, list the log files and their sizes by using the AWS Management Console or the `DescribeDBLogFiles` operation. For more information, see [Viewing and listing database log files](USER_LogAccess.Procedural.Viewing.md).

The listed total can be smaller than the amount of logs that your workload generates, because Aurora might have already deleted or compressed some log files.

Add up the sizes of the log files that Aurora generates in an hour, and compare the total with the storage available for log files. For Aurora MySQL, add up the audit, general, and slow query logs, and compare the total with 15 percent of the storage for log files. If your logs can exceed this amount before they're published to CloudWatch Logs, reduce the amount of logs or choose a DB instance class with more storage for log files.

## Reducing the amount of logs
<a name="USER_LogAccess.Aurora.LogStorage.Reducing"></a>

You can reduce the amount of logs by logging only the events that you need.
+ For Aurora MySQL audit logs, limit the audited events with `server_audit_events` and the audited users with `server_audit_incl_users` or `server_audit_excl_users`. For more information, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.Auditing.md).
+ For Aurora MySQL general and slow query logs, turn off `general_log` or increase `long_query_time`. For more information, see [Aurora MySQL slow query and general logs](USER_LogAccess.MySQL.LogFileSize.md#USER_LogAccess.MySQL.Generallog).
+ For Aurora PostgreSQL audit logs, limit the audited statement classes with `pgaudit.log`. For more information, see [Using pgAudit to log database activity](Appendix.PostgreSQL.CommonDBATasks.pgaudit.md).
+ For Aurora PostgreSQL query logging, adjust `log_statement` and `log_min_duration_statement`. For more information, see [Turning on query logging for your Aurora PostgreSQL DB cluster ](USER_LogAccess.Concepts.PostgreSQL.Query_Logging.md).
+ For Aurora PostgreSQL, remove `csvlog` from `log_destination` unless you need it. Aurora writes each entry to both files and doesn't publish the CSV files to CloudWatch Logs.

## If you can't reduce audit logs
<a name="USER_LogAccess.Aurora.LogStorage.Compliance"></a>

If you can't reduce audit logs because of compliance requirements or other reasons, consider the following:
+ For Aurora PostgreSQL, reduce other logs that share the same storage. pgAudit writes audit records to the PostgreSQL log files, so query logging uses the same storage.
+ If your DB instance class is 2xlarge or smaller, a DB instance class of 4xlarge or larger provides more storage for log files. DB instance classes of 4xlarge and larger all provide the same storage for log files.
+ Subscribe to the `notification` event category to receive [RDS-EVENT-0611](USER_Events.Messages.md#RDS-EVENT-0611). The event shows which log files Aurora deleted before publishing them to CloudWatch Logs. For more information, see [Subscribing to Amazon RDS event notification](USER_Events.Subscribing.md).