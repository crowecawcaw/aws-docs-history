# RDS for PostgreSQL database log files

You can monitor the following types of
log files:

- PostgreSQL log
- Upgrade log
- IAM database authentication error log

###### Note

To enable IAM database authentication error logs, you must first enable IAM database authentication for your RDS for PostgreSQL DB instance. For more information about enabling IAM database authentication, see [Enabling and disabling IAM database
authentication](UsingWithRDS.IAMDBAuth.md "UsingWithRDS.IAMDBAuth.md").
RDS for PostgreSQL logs database activities to the default PostgreSQL log file. For
an on-premises PostgreSQL DB instance, these messages are stored locally in
`log/postgresql.log`. For
an RDS for PostgreSQL DB instance, the log file is
available on the Amazon RDS instance. These logs are also accessible via
the AWS Management Console, where you can view or download them. The default logging level captures login
failures, fatal server errors, deadlocks, and query failures.

For more information about how you can view, download, and watch file-based database logs,
see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md"). To learn more about
PostgreSQL logs, see [Working with Amazon RDS
and Aurora PostgreSQL logs: Part 1](https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/ "https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-1/") and [Working with Amazon RDS
and Aurora PostgreSQL logs: Part 2](https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-2/ "https://aws.amazon.com/blogs/database/working-with-rds-and-aurora-postgresql-logs-part-2/").

In addition to the standard PostgreSQL logs discussed in this topic, RDS for PostgreSQL also supports the PostgreSQL Audit extension
(`pgAudit`). Most regulated industries and government agencies need to
maintain an audit log or audit trail of changes made to data to comply with legal
requirements. For information about installing and using pgAudit, see [Using pgAudit to log database activity](Appendix.PostgreSQL.CommonDBATasks.md "Appendix.PostgreSQL.CommonDBATasks.md").

###### Topics

- [Parameters for logging in RDS for PostgreSQL](USER_LogAccess.Concepts.PostgreSQL.overview.md "USER_LogAccess.Concepts.PostgreSQL.overview.md")
- [Turning on query
  logging for your RDS for PostgreSQL DB instance](USER_LogAccess.Concepts.PostgreSQL.md "USER_LogAccess.Concepts.PostgreSQL.md")
- [Publishing
  PostgreSQL logs to Amazon CloudWatch Logs](#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs "#USER_LogAccess.Concepts.PostgreSQL.PublishtoCloudWatchLogs")

## Publishing

PostgreSQL logs to Amazon CloudWatch Logs

To store your PostgreSQL log records in highly durable storage, you can use Amazon CloudWatch Logs.
With CloudWatch Logs, you can also perform real-time analysis of log data and use CloudWatch to view
metrics and create alarms. For example, if you set `log_statement` to
`ddl`, you can set up an alarm to alert you whenever a DDL statement is
executed. You can choose to have your PostgreSQL logs uploaded to CloudWatch Logs during the
process of creating your RDS for PostgreSQL DB instance. If you chose not to upload logs at
that time, you can later modify your instance to start uploading logs from that point
forward. In other words, existing logs aren't uploaded. Only new logs are uploaded
as they're created on your modified RDS for PostgreSQL DB instance.

All currently available RDS for PostgreSQL versions support publishing log files to CloudWatch Logs.
For more information, see [Amazon
RDS for PostgreSQL updates](../PostgreSQLReleaseNotes/postgresql-versions.md "../PostgreSQLReleaseNotes/postgresql-versions.md") in the _Amazon RDS for PostgreSQL Release Notes._.

To work with CloudWatch Logs, configure your RDS for PostgreSQL DB instance to publish log data to a
log group.

You can publish the following log types to CloudWatch Logs for RDS for PostgreSQL:

- PostgreSQL log
- Upgrade log
- IAM database authentication error log

After you complete the configuration, Amazon RDS publishes the log events to log streams
within a CloudWatch log group. For example, the PostgreSQL log data is stored within the log
group `/aws/rds/instance/`my_instance`/postgresql`.
To view your logs, open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

###### To publish PostgreSQL logs to CloudWatch Logs using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the DB instance that you want to modify, and then choose
   **Modify**.
4. In the **Log exports** section, choose the logs that
   you want to start publishing to CloudWatch Logs.

The **Log exports** section is available only for
PostgreSQL versions that support publishing to CloudWatch Logs. 5. Choose **Continue**, and then choose **Modify
DB Instance** on the summary page.
You can publish PostgreSQL logs with the AWS CLI. You can call the [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the following
parameters.

- `--db-instance-identifier`
- `--cloudwatch-logs-export-configuration`

###### Note

A change to the `--cloudwatch-logs-export-configuration` option
is always applied to the DB instance immediately. Therefore, the
`--apply-immediately` and `--no-apply-immediately`
options have no effect.

You can also publish PostgreSQL logs by calling the following CLI
commands:

- [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
- [`restore-db-instance-from-db-snapshot`](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md")
- [`restore-db-instance-to-point-in-time`](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")
  Run one of these CLI commands with the following options:

- `--db-instance-identifier`
- `--enable-cloudwatch-logs-exports`
- `--db-instance-class`
- `--engine`
  Other options might be required depending on the CLI command you run.

###### Example Modify an instance to publish logs to CloudWatch Logs

The following example modifies an existing PostgreSQL DB instance to
publish log files to CloudWatch Logs. The
`--cloudwatch-logs-export-configuration` value is a JSON
object. The key for this object is `EnableLogTypes`, and its
value is an array of strings with any combination of `postgresql`
and `upgrade`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["postgresql", "upgrade"]}'

```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["postgresql","upgrade"]}'

```

###### Example Create an instance to publish logs to CloudWatch Logs

The following example creates a PostgreSQL DB instance and publishes log
files to CloudWatch Logs. The `--enable-cloudwatch-logs-exports` value is a
JSON array of strings. The strings can be any combination of
`postgresql` and `upgrade`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --enable-cloudwatch-logs-exports '["postgresql","upgrade"]' \
    --db-instance-class `db.m4.large` \
    --engine `postgres`

```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --enable-cloudwatch-logs-exports '["postgresql","upgrade"]' ^
    --db-instance-class `db.m4.large` ^
    --engine `postgres`

```

You can publish PostgreSQL logs with the RDS API. You can call the [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action with the following parameters:

- `DBInstanceIdentifier`
- `CloudwatchLogsExportConfiguration`

###### Note

A change to the `CloudwatchLogsExportConfiguration` parameter
is always applied to the DB instance immediately. Therefore, the
`ApplyImmediately` parameter has no effect.

You can also publish PostgreSQL logs by calling the following RDS API
operations:

- [`CreateDBInstance`](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
- [`RestoreDBInstanceFromDBSnapshot`](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md")
- [`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")
  Run one of these RDS API operations with the following parameters:

- `DBInstanceIdentifier`
- `EnableCloudwatchLogsExports`
- `Engine`
- `DBInstanceClass`
  Other parameters might be required depending on the operation that you
  run.
