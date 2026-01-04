# Publishing Amazon Aurora MySQL logs to Amazon CloudWatch Logs

You can configure your Aurora MySQL DB cluster to publish general, slow, audit, and error log data
to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can perform real-time analysis of the log data, and
use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to store your log records in highly
durable storage.

To publish logs to CloudWatch Logs, the respective logs must be enabled. Error logs are enabled
by default, but you must enable the other types of logs explicitly. For information about
enabling logs in MySQL, see [Selecting general
query and slow query log output destinations](https://dev.mysql.com/doc/refman/8.0/en/log-destinations.html "https://dev.mysql.com/doc/refman/8.0/en/log-destinations.html") in the MySQL documentation. For
more information about enabling Aurora MySQL audit logs, see [Enabling Advanced Auditing](AuroraMySQL.md#AuroraMySQL.Auditing.Enable "AuroraMySQL.md#AuroraMySQL.Auditing.Enable").

###### Note

- If exporting log data is disabled, Aurora doesn't delete existing log
  groups or log streams. If exporting log data is disabled, existing log data
  remains available in CloudWatch Logs, depending on log retention, and you still incur
  charges for stored audit log data. You can delete log streams and log groups
  using the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API.
- An alternative way to publish audit logs to CloudWatch Logs is by enabling Advanced Auditing, then creating a custom DB
  cluster parameter group and setting the `server_audit_logs_upload` parameter to `1`. The default
  for the `server_audit_logs_upload` DB cluster parameter is `0`. For information on enabling
  Advanced Auditing, see [Using Advanced Auditing with an Amazon Aurora MySQL DB cluster](AuroraMySQL.md "AuroraMySQL.md").

If you use this alternative method, you must have an IAM role to access
CloudWatch Logs and set the `aws_default_logs_role` cluster-level parameter to
the ARN for this role. For information about creating the role, see [Setting up IAM roles to
access AWS services](AuroraMySQL.Integrating.Authorizing.md "AuroraMySQL.Integrating.Authorizing.md"). However, if you have
the `AWSServiceRoleForRDS` service-linked role, it provides access to
CloudWatch Logs and overrides any custom-defined roles. For information about
service-linked roles for Amazon RDS, see [Using service-linked roles for
Amazon Aurora](UsingWithRDS.IAM.md "UsingWithRDS.IAM.md").

- If you don't want to export audit logs to CloudWatch Logs, make sure that all methods of exporting audit logs are disabled. These methods are the
  AWS Management Console, the AWS CLI, the RDS API, and the `server_audit_logs_upload` parameter.
- The procedure is slightly different for Aurora Serverless v1 DB clusters than
  for DB clusters with provisioned or Aurora Serverless v2 DB instances.
  Aurora Serverless v1 clusters automatically upload all of the logs that you enable
  through configuration parameters.

Therefore, you turn on or turn off log upload for Aurora Serverless v1 DB
clusters by turning different log types on and off in the DB cluster parameter
group. You don't modify the settings of the cluster itself through the
AWS Management Console, AWS CLI, or RDS API. For information about turning on and off MySQL
logs for Aurora Serverless v1 clusters, see [Parameter groups for
Aurora Serverless v1](aurora-serverless-v1.md#aurora-serverless.parameter-groups "aurora-serverless-v1.md#aurora-serverless.parameter-groups").
You can publish Aurora MySQL logs for provisioned clusters to CloudWatch Logs with the console.

###### To publish Aurora MySQL logs from the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Aurora MySQL DB cluster that you want to publish the log data
   for.
4. Choose **Modify**.
5. In the **Log exports** section, choose the logs that
   you want to start publishing to CloudWatch Logs.
6. Choose **Continue**, and then choose **Modify DB
   Cluster** on the summary page.
   You can publish Aurora MySQL logs for provisioned clusters with the AWS CLI. To do so, you
   run the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
   AWS CLI command with the following options:

- `--db-cluster-identifier`—The DB cluster identifier.
- `--cloudwatch-logs-export-configuration`—The configuration setting for the log types to
  be enabled for export to CloudWatch Logs for the DB cluster.
  You can also publish Aurora MySQL logs by running one of the following AWS CLI
  commands:

- [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md")
- [restore-db-cluster-from-s3](../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md "../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md")
- [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md")
- [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
  Run one of these AWS CLI commands with the following options:

- `--db-cluster-identifier`—The DB cluster identifier.
- `--engine`—The database engine.
- `--enable-cloudwatch-logs-exports`—The configuration setting for the log types to
  be enabled for export to CloudWatch Logs for the DB cluster.
  Other options might be required depending on the AWS CLI command that you
  run.

The following command modifies an existing Aurora MySQL DB cluster to publish log files to CloudWatch Logs.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["error","general","slowquery","audit","instance"]}'

```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["error","general","slowquery","audit","instance"]}'

```

The following command creates an Aurora MySQL DB cluster to publish log files to
CloudWatch Logs.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --db-cluster-identifier `mydbcluster` \
    --engine aurora \
    --enable-cloudwatch-logs-exports '["error","general","slowquery","audit","instance"]'

```

For Windows:

```
aws rds create-db-cluster ^
    --db-cluster-identifier `mydbcluster` ^
    --engine aurora ^
    --enable-cloudwatch-logs-exports '["error","general","slowquery","audit","instance"]'

```

You can publish Aurora MySQL logs for provisioned clusters with the RDS API. To do so, you
run the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation
with the following options:

- `DBClusterIdentifier`—The DB cluster identifier.
- `CloudwatchLogsExportConfiguration`—The configuration setting for the log types to
  be enabled for export to CloudWatch Logs for the DB cluster.
  You can also publish Aurora MySQL logs with the RDS API by running one of the
  following RDS API operations:

- [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md")
- [RestoreDBClusterFromS3](../APIReference/API_RestoreDBClusterFromS3.md "../APIReference/API_RestoreDBClusterFromS3.md")
- [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md")
- [RestoreDBClusterToPointInTime](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md")
  Run the RDS API operation with the following parameters:

- `DBClusterIdentifier`—The DB cluster identifier.
- `Engine`—The database engine.
- `EnableCloudwatchLogsExports`—The configuration setting for the log types to
  be enabled for export to CloudWatch Logs for the DB cluster.
  Other parameters might be required depending on the AWS CLI command that you
  run.

## Monitoring log events in Amazon CloudWatch

After enabling Aurora MySQL log events, you can monitor the events in Amazon CloudWatch Logs. A new
log group is automatically created for the Aurora DB cluster under the following
prefix, in which `cluster-name` represents the
DB cluster name, and `log_type` represents the log type.

```
/aws/rds/cluster/`cluster-name`/`log_type`
```

For example, if you configure the export function to include the slow query log for a DB cluster
named `mydbcluster`, slow query data is stored in the
`/aws/rds/cluster/mydbcluster/slowquery` log group.

The events from all instances in your cluster are pushed to a log group using different log streams.
The behavior depends on which of the following conditions is true:

- A log group with the specified name exists.

Aurora uses the existing log group to export log data for the cluster. To create log groups with
predefined log retention periods, metric filters, and customer access, you can use automated
configuration, such as AWS CloudFormation.

- A log group with the specified name doesn't exist.

When a matching log entry is detected in the log file for the instance, Aurora MySQL creates a new log
group in CloudWatch Logs automatically. The log group uses the default log retention period of
**Never Expire**.

To change the log retention period, use the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API. For more
information about changing log retention periods in CloudWatch Logs, see [Change log data retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md "../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md").

To search for information within the log events for a DB cluster, use the CloudWatch Logs console, the AWS CLI, or
the CloudWatch Logs API. For more information about searching and filtering log data, see [Searching and filtering log data](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md").
