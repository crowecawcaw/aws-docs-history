# Publishing Neptune Logs to Amazon CloudWatch Logs

You can configure a Neptune DB cluster to publish audit log data and/or
slow-query log data to a log group in Amazon CloudWatch Logs. With CloudWatch Logs, you can perform
real-time analysis of the log data, and use CloudWatch to create alarms and view
metrics. You can use CloudWatch Logs to store your log records in highly durable
storage.

To publish audit logs to CloudWatch Logs, audit logs must be explicitly enabled (see [Enable Audit Logs](auditing.md#auditing-enable "auditing.md#auditing-enable")). Similarly, to
publish slow-query logs to CloudWatch Logs, slow-query logs must be explicitly enabled (see [Using Amazon Neptune slow-query logging](slow-query-logs.md "slow-query-logs.md")).

###### Note

Be aware of the following:

- Additional charges apply when you publish logs to CloudWatch. See
  the [CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
  for details.
- You can't publish logs to CloudWatch Logs for the China (Beijing) or
  China (Ningxia) region.
- If exporting log data is disabled, Neptune doesn't delete
  existing log groups or log streams. If exporting log data is disabled, existing log data
  remains available in CloudWatch Logs, depending on log retention, and you still incur
  charges for stored audit log data. You can delete log streams and log groups
  using the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API.

## Using the Console to Publish Neptune Logs to CloudWatch Logs

###### To publish Neptune logs to CloudWatch Logs from the console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Databases**.
3. Choose the Neptune DB cluster that you want to publish the log data for.
4. For **Actions**, choose **Modify**.
5. In the **Log exports** section, choose the logs that you
   want to start publishing to CloudWatch Logs.
6. Choose **Continue**, and then choose **Modify DB
   Cluster** on the summary page.

## Using the CLI to publish Neptune audit logs to CloudWatch Logs

You can create a new DB cluster that publishes audit logs to CloudWatch Logs using the AWS CLI
`create-db-cluster` command with the following parameters:

```
aws neptune create-db-cluster \
    --region `us-east-1`  \
    --db-cluster-identifier `my_db_cluster_id` \
    --engine neptune \
    --enable-cloudwatch-logs-exports '["audit"]'
```

You can configure an existing DB cluster to publish audit logs to CloudWatch Logs using the
AWS CLI `modify-db-cluster` command with the following parameters:

```
aws neptune modify-db-cluster \
    --region `us-east-1`  \
    --db-cluster-identifier `my_db_cluster_id` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["audit"]}'
```

## Using the CLI to publish Neptune slow-query logs to CloudWatch Logs

You can also create a new DB cluster that publishes slow-query logs to CloudWatch Logs using the AWS CLI
`create-db-cluster` command with the following parameters:

```
aws neptune create-db-cluster \
    --region `us-east-1`  \
    --db-cluster-identifier `my_db_cluster_id` \
    --engine neptune \
    --enable-cloudwatch-logs-exports '["slowquery"]'
```

Similarly, you can configure an existing DB cluster to publish slow-query logs to CloudWatch Logs using the
AWS CLI `modify-db-cluster` command with the following parameters:

```
aws neptune modify-db-cluster --region `us-east-1`  \
    --db-cluster-identifier `my_db_cluster_id` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["slowquery"]}'
```

## Monitoring Neptune Log Events in Amazon CloudWatch

After enabling Neptune logs, you can monitor log events in Amazon CloudWatch Logs. A new
log group is automatically created for the Neptune DB cluster under the following
prefix, in which `cluster-name` represents the
DB cluster name, and `log_type` represents the
log type:

```
/aws/neptune/`cluster-name`/`log_type`
```

For example, if you configure the export function to include the audit log
for a DB cluster named `mydbcluster`, log data is stored in the
`/aws/neptune/mydbcluster/audit` log group.

All of the events from all of the DB instances in a DB cluster are pushed to
a log group using different log streams.

If a log group with the specified name exists, Neptune uses that log group to export
log data for the Neptune DB cluster. You can use automated configuration, such
as AWS CloudFormation, to create log groups with predefined log retention periods, metric
filters, and customer access. Otherwise, a new log group is automatically created
using the default log retention period, **Never Expire**, in CloudWatch Logs.

You can use the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API to change the log
retention period. For more information about changing log retention periods in
CloudWatch Logs, see [Change Log Data
Retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md "../../../AmazonCloudWatch/latest/logs/SettingLogRetention.md").

You can use the CloudWatch Logs console, the AWS CLI, or the CloudWatch Logs API to search for
information within the log events for a DB cluster. For more information about
searching and filtering log data, see [Searching
and Filtering Log Data](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md").
