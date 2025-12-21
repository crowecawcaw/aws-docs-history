# Amazon RDS for Db2 database log files

You can access RDS for Db2 diagnostic logs and notify logs by using the Amazon RDS console, AWS CLI,
or RDS API. For more information about viewing, downloading, and watching file-based
database logs, see [Monitoring Amazon RDS log files](USER_LogAccess.md "USER_LogAccess.md").

###### Topics

- [Retention schedule](#USER_LogAccess.Concepts.Db2.Retention "#USER_LogAccess.Concepts.Db2.Retention")
- [Publishing Db2 logs to
  Amazon CloudWatch Logs](#USER_LogAccess.Db2.PublishtoCloudWatchLogs "#USER_LogAccess.Db2.PublishtoCloudWatchLogs")

## Retention schedule

Log files are rotated each day and whenever your DB instance is restarted. The
following is the retention schedule for RDS for Db2 logs on Amazon RDS.

| Log type        | Retention schedule                                                                                                                              |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Diagnostic logs | Db2 deletes logs outside of the retention settings in the<br>instance-level configuration. Amazon RDS sets the `diagsize`<br>parameter to 1000. |
| Notify logs     | Db2 deletes logs outside of the retention settings in the<br>instance-level configuration. Amazon RDS sets the `diagsize`<br>parameter to 1000. |

## Publishing Db2 logs to

Amazon CloudWatch Logs

With RDS for Db2, you can publish diagnostic and notify log events directly to Amazon CloudWatch Logs.
Analyze the log data with CloudWatch Logs, then use CloudWatch to create alarms and view metrics.

With CloudWatch Logs, you can do the following:

- Store logs in highly durable storage space with a retention period that you
  define.
- Search and filter log data.
- Share log data between accounts.
- Export logs to Amazon S3.
- Stream data to Amazon OpenSearch Service.
- Process log data in real time with Amazon Kinesis Data Streams. For more information, see [Working with Amazon CloudWatch Logs](../../../kinesisanalytics/latest/dev/cloudwatch-logs.md "../../../kinesisanalytics/latest/dev/cloudwatch-logs.md") in the _Amazon Managed Service for Apache Flink for SQL
  Applications Developer Guide_.

Amazon RDS publishes each RDS for Db2 database log as a separate database stream in the log
group. For example, if you publish the diagnostic logs and notify logs, diagnostic data
is stored in a diagnostic log stream in the
`/aws/rds/instance/`my_instance`/diagnostic`
log group, and notify log data is stored in the
`/aws/rds/instance/`my_instance`/notify` log
group.

###### Note

Publishing RDS for Db2 logs to CloudWatch Logs isn't enabled by default. Publishing
self-tuning memory manager (STMM) and optimizer statistics logs isn't supported.
Publishing RDS for Db2 logs to CloudWatch Logs is supported in all Regions, except for
Asia Pacific (Hong Kong).

###### To publish RDS for Db2 logs to CloudWatch Logs from the AWS Management Console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and
   then choose the DB instance that you want to modify.
3. Choose **Modify**.
4. In the **Log exports** section, choose the logs that
   you want to start publishing to CloudWatch Logs.

You can choose **diag.log**,
**notify.log**, or both. 5. Choose **Continue**, and then choose **Modify
DB Instance** on the summary page.
To publish RDS for Db2 logs, you can use the [`modify-db-instance`](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md") command with the following
parameters:

- `--db-instance-identifier`
- `--cloudwatch-logs-export-configuration`

###### Note

A change to the `--cloudwatch-logs-export-configuration` option
is always applied to the DB instance immediately. Therefore, the
`--apply-immediately` and `--no-apply-immediately`
options have no effect.

You can also publish RDS for Db2 logs using the following commands:

- [`create-db-instance`](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md")
- [`restore-db-instance-from-db-snapshot`](../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md "../../../cli/latest/reference/rds/restore-db-instance-from-db-snapshot.md")
- [`restore-db-instance-to-point-in-time`](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md")

###### Example

The following example creates an RDS for Db2 DB instance with CloudWatch Logs
publishing enabled. The `--enable-cloudwatch-logs-exports` value
is a JSON array of strings that can include `diag.log`,
`notify.log`, or both.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --db-instance-identifier `mydbinstance` \
    --enable-cloudwatch-logs-exports '["diag.log","notify.log"]' \
    --db-instance-class `db.m4.large` \
    --engine `db2-se`
```

For Windows:

```
aws rds create-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --enable-cloudwatch-logs-exports "[\"diag.log\",\"notify.log\"]" ^
    --db-instance-class `db.m4.large` ^
    --engine `db2-se`
```

###### Note

When using the Windows command prompt, you must escape double quotes
(") in JSON code by prefixing them with a backslash (\).

###### Example

The following example modifies an existing RDS for Db2 DB instance to publish
log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration`
value is a JSON object. The key for this object is
`EnableLogTypes`, and its value is an array of strings that
can include `diag.log`, `notify.log`, or both.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["diag.log","notify.log"]}'
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration "{\"EnableLogTypes\":[\"diag.log\",\"notify.log\"]}"
```

###### Note

When using the Windows command prompt, you must escape double quotes
(") in JSON code by prefixing them with a backslash (\).

###### Example

The following example modifies an existing RDS for Db2 DB instance to disable
publishing diagnostic log files to CloudWatch Logs. The
`--cloudwatch-logs-export-configuration` value is a JSON
object. The key for this object is `DisableLogTypes`, and its
value is an array of strings that can include `diag.log`,
`notify.log`, or both.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"DisableLogTypes":["diag.log"]}'
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration "{\"DisableLogTypes\":[\"diag.log\"]}"
```

###### Note

When using the Windows command prompt, you must escape double quotes
(") in JSON code by prefixing them with a backslash (\).
