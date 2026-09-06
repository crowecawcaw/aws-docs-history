

# Publishing MariaDB logs to Amazon CloudWatch Logs
<a name="USER_LogAccess.MariaDB.PublishtoCloudWatchLogs"></a>

You can configure your MariaDB DB instance to publish log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, and use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to store your log records in highly durable storage. 

Amazon RDS publishes each MariaDB database log as a separate database stream in the log group. For example, suppose that you configure the export function to include the slow query log. Then slow query data is stored in a slow query log stream in the `/aws/rds/instance/{{my_instance}}/slowquery` log group.

The error log is enabled by default. The following table summarizes the requirements for the other MariaDB logs.


| Log | Requirement | 
| --- | --- | 
| Audit log | The DB instance must use a custom option group with the `MARIADB_AUDIT_PLUGIN` option. | 
| General log | The DB instance must use a custom parameter group with the parameter setting `general_log = 1` to enable the general log. | 
| Slow query log | The DB instance must use a custom parameter group with the parameter setting `slow_query_log = 1` or `log_slow_query = 1` to enable the slow query log. | 
| IAM database authentication error log | You must enable the log type `iam-db-auth-error` for a DB instance by creating or modifying a DB instance. | 
| Log output | The DB instance must use a custom parameter group with the parameter setting `log_output = FILE` to write logs to the file system and publish them to CloudWatch Logs. | 

## Console
<a name="USER_LogAccess.MariaDB.PublishtoCloudWatchLogs.CON"></a>

**To publish MariaDB logs to CloudWatch Logs from the console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the DB instance that you want to modify.

1. Choose **Modify**.

1. In the **Log exports** section, choose the logs that you want to start publishing to CloudWatch Logs.

1. Choose **Continue**, and then choose **Modify DB Instance** on the summary page.

## AWS CLI
<a name="USER_LogAccess.MariaDB.PublishtoCloudWatchLogs.CLI"></a>

You can publish a MariaDB logs with the AWS CLI. You can call the [`modify-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) command with the following parameters: 
+ `--db-instance-identifier`
+ `--cloudwatch-logs-export-configuration`

**Note**  
A change to the `--cloudwatch-logs-export-configuration` option is always applied to the DB instance immediately. Therefore, the `--apply-immediately` and `--no-apply-immediately` options have no effect.

You can also publish MariaDB logs by calling the following AWS CLI commands: 
+ [`create-db-instance`](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html)
+ [`restore-db-instance-from-db-snapshot`](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-db-snapshot.html)
+ [`restore-db-instance-from-s3`](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-s3.html)
+ [`restore-db-instance-to-point-in-time`](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-to-point-in-time.html)

Run one of these AWS CLI commands with the following options: 
+ `--db-instance-identifier`
+ `--enable-cloudwatch-logs-exports`
+ `--db-instance-class`
+ `--engine`

Other options might be required depending on the AWS CLI command you run.

**Example**  
The following example modifies an existing MariaDB DB instance to publish log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration` value is a JSON object. The key for this object is `EnableLogTypes`, and its value is an array of strings with any combination of `audit`, `error`, `general`, and `slowquery`.  
For Linux, macOS, or Unix:  

```
1. aws rds modify-db-instance \
2.     --db-instance-identifier {{mydbinstance}} \
3.     --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit","error","general","slowquery"]}'
```
For Windows:  

```
1. aws rds modify-db-instance ^
2.     --db-instance-identifier {{mydbinstance}} ^
3.     --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit","error","general","slowquery"]}'
```

**Example**  
The following command creates a MariaDB DB instance and publishes log files to CloudWatch Logs. The `--enable-cloudwatch-logs-exports` value is a JSON array of strings. The strings can be any combination of `audit`, `error`, `general`, and `slowquery`.  
For Linux, macOS, or Unix:  

```
1. aws rds create-db-instance \
2.     --db-instance-identifier {{mydbinstance}} \
3.     --enable-cloudwatch-logs-exports '["audit","error","general","slowquery"]' \
4.     --db-instance-class {{db.m4.large}} \
5.     --engine {{mariadb}}
```
For Windows:  

```
1. aws rds create-db-instance ^
2.     --db-instance-identifier {{mydbinstance}} ^
3.     --enable-cloudwatch-logs-exports '["audit","error","general","slowquery"]' ^
4.     --db-instance-class {{db.m4.large}} ^
5.     --engine {{mariadb}}
```

## RDS API
<a name="USER_LogAccess.MariaDB.PublishtoCloudWatchLogs.API"></a>

You can publish MariaDB logs with the RDS API. You can call the [`ModifyDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) operation with the following parameters: 
+ `DBInstanceIdentifier`
+ `CloudwatchLogsExportConfiguration`

**Note**  
A change to the `CloudwatchLogsExportConfiguration` parameter is always applied to the DB instance immediately. Therefore, the `ApplyImmediately` parameter has no effect.

You can also publish MariaDB logs by calling the following RDS API operations: 
+ [`CreateDBInstance`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html)
+ [`RestoreDBInstanceFromDBSnapshot`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromDBSnapshot.html)
+ [`RestoreDBInstanceFromS3`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html)
+ [`RestoreDBInstanceToPointInTime`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceToPointInTime.html)

Run one of these RDS API operations with the following parameters: 
+ `DBInstanceIdentifier`
+ `EnableCloudwatchLogsExports`
+ `Engine`
+ `DBInstanceClass`

Other parameters might be required depending on the AWS CLI command you run.