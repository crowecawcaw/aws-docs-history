# Aurora PostgreSQL database log files

You can monitor the following types of Aurora PostgreSQL
log files:

- PostgreSQL log
- Instance log
- IAM database authentication error log

###### Note

To enable IAM database authentication error logs, you must first enable IAM database authentication for your Aurora PostgreSQL DB cluster. For more information about enabling IAM database authentication, see [Enabling and disabling IAM database
authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").
Aurora PostgreSQL logs database activities to the default PostgreSQL log file. For
an on-premises PostgreSQL DB instance, these messages are stored locally in
`log/postgresql.log`. For an Aurora PostgreSQL DB
cluster,
the log file is
available on the Aurora cluster. These logs are also accessible via
the AWS Management Console, where you can view or download them. The default logging level captures login
failures, fatal server errors, deadlocks, and query failures.

For more information about how you can view, download, and watch file-based database logs,
see [Monitoring Amazon Aurora log files](USER_LogAccess.md "USER_LogAccess.md"). To learn more about
PostgreSQL logs, see [Working with Amazon RDS
and Aurora PostgreSQL logs: Part 1](https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/ "https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/") and [Working with Amazon RDS
and Aurora PostgreSQL logs: Part 2](https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-2/ "https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-2/").

In addition to the standard PostgreSQL logs discussed in this topic, Aurora PostgreSQL also supports the PostgreSQL Audit extension
(`pgAudit`). Most regulated industries and government agencies need to
maintain an audit log or audit trail of changes made to data to comply with legal
requirements. For information about installing and using pgAudit, see [Using pgAudit to log database activity](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

Aurora creates a separate log file for DB instances that have auto-pause
enabled. This instance.log file records any reasons why these DB instances couldn't be paused when
expected. For more information on instance log file behavior and Aurora auto-pause
capability, see [Monitoring Aurora Serverless v2 pause and resume activity](aurora-serverless-v2-administration.md#autopause-logging-instance-log "aurora-serverless-v2-administration.md#autopause-logging-instance-log").

###### Topics

- [Parameters for logging in Aurora PostgreSQL](USER_LogAccess.Concepts.PostgreSQL.overview.md "USER_LogAccess.Concepts.PostgreSQL.overview.md")
- [Turning on query
  logging for your Aurora PostgreSQL DB cluster](USER_LogAccess.Concepts.PostgreSQL.md "USER_LogAccess.Concepts.PostgreSQL.md")
