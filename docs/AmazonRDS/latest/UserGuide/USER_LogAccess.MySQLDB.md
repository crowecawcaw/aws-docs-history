# Publishing MySQL logs to Amazon CloudWatch Logs

You can configure your MySQL DB instance to publish log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can
perform real-time analysis of the log data, and use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to
store your log records in highly durable storage.

Amazon RDS publishes each MySQL database log as a separate database stream in the log group. For example, if you
configure the export function to include the slow query log, slow query data is stored in a slow query log stream
in the `/aws/rds/instance/`my_instance`/slowquery` log group.

The error log is enabled by default. The following table summarizes the requirements for the other MySQL
logs.

| Log                                   | Requirement                                                                                                                                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Audit log                             | The DB instance must use a custom option group with the `MARIADB_AUDIT_PLUGIN`<br>option.                                                                                    |
| General log                           | The DB instance must use a custom parameter group with the parameter setting<br>`general_log = 1` to enable the general log.                                                 |
| Slow query log                        | The DB instance must use a custom parameter group with the parameter setting<br>`slow_query_log = 1` to enable the slow query log.                                           |
| IAM database authentication error log | You must enable the log type `iam-db-auth-error` for a DB instance by creating or modifying a DB instance.                                                                   |
| Log output                            | The DB instance must use a custom parameter group with the parameter setting<br>`log_output = FILE` to write logs to the file system and publish them to<br>CloudWatch Logs. |

###### To publish MySQL logs to CloudWatch Logs using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB instance
   that you want to modify.
3. Choose **Modify**.
4. In the **Log exports** section, choose the logs that you want to start
   publishing to CloudWatch Logs.
5. Choose **Continue**, and then choose **Modify DB Instance**
   on the summary page.
   You can publish MySQL logs with the AWS CLI. You can call the [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with
   the following parameters:

- `--db-instance-identifier`
- `--cloudwatch-logs-export-configuration`

###### Note

A change to the `--cloudwatch-logs-export-configuration` option is always applied to the
DB instance immediately. Therefore, the `--apply-immediately` and
`--no-apply-immediately` options have no effect.

You can also publish MySQL logs by calling the following AWS CLI commands:

- [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
- [`restore-db-instance-from-db-snapshot`](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md")
- [`restore-db-instance-from-s3`](../../../cli/latest/reference/rds/restore-db-instance-from-s3.md "../../../cli/latest/reference/rds/restore-db-instance-from-s3.md")
- [`restore-db-instance-to-point-in-time`](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")
  Run one of these AWS CLI commands with the following options:

- `--db-instance-identifier`
- `--enable-cloudwatch-logs-exports`
- `--db-instance-class`
- `--engine`
  Other options might be required depending on the AWS CLI command you run.

###### Example

The following example modifies an existing MySQL DB instance to publish log files to CloudWatch Logs. The
`--cloudwatch-logs-export-configuration` value is a JSON object. The key for this
object is `EnableLogTypes`, and its value is an array of strings with any combination of
`audit`, `error`, `general`, and `slowquery`.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit","error","general","slowquery"]}'

```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit","error","general","slowquery"]}'

```

###### Example

The following example creates a MySQL DB instance and publishes log files to CloudWatch Logs. The
`--enable-cloudwatch-logs-exports` value is a JSON array of strings. The strings can
be any combination of `audit`, `error`, `general`, and
`slowquery`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --enable-cloudwatch-logs-exports '["audit","error","general","slowquery"]' \
    --db-instance-class `db.m4.large` \
    --engine `MySQL`

```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --enable-cloudwatch-logs-exports '["audit","error","general","slowquery"]' ^
    --db-instance-class `db.m4.large` ^
    --engine `MySQL`

```

You can publish MySQL logs with the RDS API. You can call the [`ModifyDBInstance`](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md") action with the
following parameters:

- `DBInstanceIdentifier`
- `CloudwatchLogsExportConfiguration`

###### Note

A change to the `CloudwatchLogsExportConfiguration` parameter is always applied to the
DB instance immediately. Therefore, the `ApplyImmediately` parameter has no effect.

You can also publish MySQL logs by calling the following RDS API operations:

- [`CreateDBInstance`](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md")
- [`RestoreDBInstanceFromDBSnapshot`](../APIReference/API_RestoreDBInstanceFromDBSnapshot.md "../APIReference/API_RestoreDBInstanceFromDBSnapshot.md")
- [`RestoreDBInstanceFromS3`](../APIReference/API_RestoreDBInstanceFromS3.md "../APIReference/API_RestoreDBInstanceFromS3.md")
- [`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")
  Run one of these RDS API operations with the following parameters:

- `DBInstanceIdentifier`
- `EnableCloudwatchLogsExports`
- `Engine`
- `DBInstanceClass`
  Other parameters might be required depending on the AWS CLI command you run.
