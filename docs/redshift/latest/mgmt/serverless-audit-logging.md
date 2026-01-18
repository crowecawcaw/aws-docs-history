Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Audit logging for Amazon Redshift Serverless

You can configure Amazon Redshift Serverless to export connection, user, and user-activity log
data to a log group in Amazon CloudWatch Logs. With Amazon CloudWatch Logs, you can perform real-time analysis of
the log data and use CloudWatch to create alarms and view metrics. You can use CloudWatch Logs to store
your log records in durable storage.

You can create CloudWatch alarms to track your metrics using the Amazon Redshift console. For more
information on creating alarms, see [Managing
alarms](performance-metrics-alarms.md "performance-metrics-alarms.md").

To export generated log data to Amazon CloudWatch Logs, the respective logs must be selected for
export in your Amazon Redshift Serverless configuration settings, on the console. You can do this
by choosing the **Namespace configuration** settings, under
**Security and encryption**.

## Log events in

CloudWatch

After selecting which Redshift logs to export, you can monitor events in
Amazon CloudWatch Logs. A new log group is automatically created for Amazon Redshift Serverless, in which
`log_type` represents the log type.

```
/aws/redshift/<namespace>/<log_type>
```

When you create your first workgroup and namespace, _default_
is the namespace name. The log group name varies according to what you call the
namespace.

For example, if you export the connection log, log data is stored in the following
log group.

```
/aws/redshift/default/connectionlog
```

Log events are exported to a log group using the serverless log stream. The
behavior depends on which of the following conditions are true:

- **A log group with the specified name
  exists.** Redshift exports log data using the existing log
  group. To create log groups with predefined log-retention periods, metric
  filters, and customer access, you can use automated configuration, such as
  that provided by **AWS CloudFormation**.
- **A log group with the specified name doesn't
  exist.** When a matching log entry is detected in the log for
  the instance, Amazon Redshift Serverless creates a new log group in Amazon CloudWatch Logs
  automatically. The log group uses the default log-retention period of
  _Never Expire_. To change the log-retention period,
  use the Amazon CloudWatch Logs console, the AWS CLI, or the Amazon CloudWatch Logs API. For more
  information about changing log-retention periods in CloudWatch Logs, see
  _Change log data retention_ in [Working
  with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

To search for information within log events, use the Amazon CloudWatch Logs console, the AWS CLI,
or the Amazon CloudWatch Logs API. For more information about searching and filtering log data,
see [Searching and filtering log
data](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md").

## CloudWatch

metrics

Amazon Redshift Serverless metrics are divided into compute metrics and data and storage
metrics, falling under the workgroup and namespace dimension sets, respectively. For
more information about workgroups and namespaces, see [Workgroups
and namespaces](serverless-workgroups-and-namespaces.md "serverless-workgroups-and-namespaces.md").

CloudWatch compute metrics are the following:

| Metric name                                          | Units                 | Description                                                                                                                                                                                                                                                                                                                                                                                                          | Dimension sets                                                    |
| ---------------------------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `QueriesCompletedPerSecond`                          | Number of queries     | The number of queries completed each second.                                                                                                                                                                                                                                                                                                                                                                         | {Database, LatencyRange, Workgroup}, {LatencyRange,<br>Workgroup} |
| `QueryDuration`                                      | Microseconds          | The average amount of time to complete a query.                                                                                                                                                                                                                                                                                                                                                                      | {Database, LatencyRange, Workgroup}, {LatencyRange,<br>Workgroup} |
| `QueriesRunning`                                     | Number of queries     | The number of running queries at a point in time.                                                                                                                                                                                                                                                                                                                                                                    | {Database, QueryType, Workgroup}, {QueryType, Workgroup}          |
| `QueriesQueued`                                      | Number of queries     | The number of queries in the queue at a point in time.                                                                                                                                                                                                                                                                                                                                                               | {Database, QueryType, Workgroup}, {QueryType, Workgroup}          |
| `DatabaseConnections`                                | Number of connections | The number of connections to a database at a point in<br>time.                                                                                                                                                                                                                                                                                                                                                       | {Database, Workgroup}, {Workgroup}                                |
| `QueryRuntimeBreakdown`                              | Milliseconds          | The total time queries ran, by query stage.                                                                                                                                                                                                                                                                                                                                                                          | {Database, Stage, Workgroup}, {Stage, Workgroup}                  |
| `ComputeCapacity`                                    | RPU                   | Average number of compute units allocated during the past 30<br>minutes, rounded up to the nearest integer.                                                                                                                                                                                                                                                                                                          | {Workgroup}                                                       |
| `ComputeSeconds`                                     | RPU-seconds           | Accumulated compute-unit seconds used in the last 30<br>minutes.                                                                                                                                                                                                                                                                                                                                                     | {Workgroup}                                                       |
| `QueriesSucceeded`                                   | Number of queries     | The number of queries that succeeded in the last 5<br>minutes.                                                                                                                                                                                                                                                                                                                                                       | {Database, QueryType, Workgroup}, {QueryType, Workgroup}          |
| `QueriesFailed`                                      | Number of queries     | The number of queries that failed in the last 5 minutes.                                                                                                                                                                                                                                                                                                                                                             | {Database, QueryType, Workgroup}, {QueryType, Workgroup}          |
| `UsageLimitAvailable`                                | RPU-hours or TBs      | Depending on the UsageType, UsageLimitAvailable returns the<br>following:<br>• If the UsageType is SERVERLESS_COMPUTE,<br>UsageLimitAvailable returns the remaining number of<br>RPU-hours that the workgroup can query in the given<br>limit.<br>• If the UsageType is CROSS_REGION_DATASHARING,<br>UsageLimitAvailable returns the remaining number of TBs<br>that the customer can scan in the given limit.       | {UsageLimitId, UsageType, Workgroup}                              |
| `UsageLimitConsumed`                                 | RPU-hours or TBs      | Depending on the UsageType, UsageLimitConsumed returns the<br>following:<br>• If the UsageType is SERVERLESS_COMPUTE,<br>UsageLimitConsumed returns the number of RPU-hours that<br>the workgroup has already queried in the given<br>limit.<br>• If the UsageType is CROSS_REGION_DATASHARING,<br>UsageLimitConsumed returns the number of TBs that the<br>customer has already used to scan in the given<br>limit. | {UsageLimitId, UsageType, Workgroup}                              |
| `ExtraComputeForAutomaticOptimizationChargedSeconds` | RPU-seconds           | Number of compute-unit seconds charged<br>for automatic optimization operations in the<br>last 30 minutes.                                                                                                                                                                                                                                                                                                           | {Workgroup}                                                       |

CloudWatch data and storage metrics are the following:

| Metric name       | Units            | Description                                                                                                           | Dimension sets        |
| ----------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `TotalTableCount` | Number of tables | The number of user tables existing at a point in time. This total<br>doesn't include Amazon Redshift Spectrum tables. | {Database, Namespace} |
| `DataStorage`     | Megabytes        | The number of megabytes used, in disk or storage space, for<br>Redshift data.                                         | {Namespace}           |

The `SnapshotStorage` metric is namespace- and workgroup-agnostic.
CloudWatch's `SnapshotStorage` metric is as follows:

| Metric name       | Units     | Description                                                               | Dimension sets |
| ----------------- | --------- | ------------------------------------------------------------------------- | -------------- |
| `SnapshotStorage` | Megabytes | The number of megabytes used, in disk or storage space, for<br>Snapshots. | {}             |

Dimension sets are the grouping dimensions applied to your metrics. You can use
these dimension groups to specify how your statistics are retrieved.

The following table details dimensions and dimension values for specific
metrics:

| Dimension      | Description and values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DatabaseName` | The name of the database. A custom value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Latency`      | Possible values are as follows:<br>• Short – under 10 seconds<br>• Medium – between 10 seconds and 10<br>minutes<br>• Long – over 10 minutes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `QueryType`    | Possible values are `INSERT`, `DELETE`,<br>`UPDATE`, `UNLOAD`, `LOAD`,<br>`SELECT`, `CTAS`, and<br>`OTHER`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `stage`        | The execution stages for a query. Possible values are as<br>follows:<br>• QueryPlanning: Time spent parsing and optimizing SQL<br>statements.<br>• QueryWaiting: Time spent waiting in the WLM<br>queue.<br>• QueryExecutingRead: Time spent executing read<br>queries.<br>• QueryExecutingInsert: Time spent executing insert<br>queries.<br>• QueryExecutingDelete: Time spent executing delete<br>queries.<br>• QueryExecutingUpdate: Time spent executing update<br>queries.<br>• QueryExecutingCtas: Time spent executing create table<br>as queries.<br>• QueryExecutingUnload: Time spent executing unload<br>queries.<br>• QueryExecutingCopy: Time spent executing copy<br>queries.<br>• QueryCommit: Time spent committing. |
| `Namespace`    | The name of the namespace. A custom value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `Workgroup`    | The name of the workgroup. A custom value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `UsageLimitId` | The identifier of the usage limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `UsageType`    | The Amazon Redshift Serverless feature being limited. Possible<br>values are as follows:<br>• SERVERLESS_COMPUTE<br>• CROSS_REGION_DATASHARING                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
