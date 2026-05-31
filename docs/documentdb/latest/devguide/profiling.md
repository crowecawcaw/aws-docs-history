# Profiling Amazon DocumentDB operations

You can use the profiler in Amazon DocumentDB (with MongoDB compatibility) to log the execution time and
details of operations that were performed on your cluster. The profiler is
useful for monitoring the slowest operations on your cluster to help you
improve individual query performance and overall cluster performance.

By default, the profiler feature is disabled. When enabled, the
profiler logs operations that are taking longer than a customer-defined
threshold value (for example, 100 ms) to Amazon CloudWatch Logs. Logged details include
the profiled command, time, plan summary, and client metadata. After the
operations are logged to CloudWatch Logs, you can use CloudWatch Logs Insights to analyze,
monitor, and archive your Amazon DocumentDB profiling data. Common queries are
provided in the section [Common queries](#profiling.common-queries "#profiling.common-queries").

When enabled, the profiler uses additional resources in your cluster.
We recommend that you start with a high threshold value (for example, 500
ms) and gradually lower the value to identify slow operations. Starting
with a threshold value of 50 ms can cause performance issues on your
cluster for high throughput applications. The profiler is enabled at the
cluster level and works on all instances and databases in a cluster.
Amazon DocumentDB logs operations to Amazon CloudWatch Logs on a best-effort basis.

Although Amazon DocumentDB imposes no additional charge to enable the profiler,
you are charged the standard rates for the usage of CloudWatch Logs. For information
about CloudWatch Logs pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

###### Topics

- [Supported operations](#profiling.supported-commands "#profiling.supported-commands")
- [Limitations](#profiling.limitations "#profiling.limitations")
- [Enabling the profiler](#profiling.enable-profiling "#profiling.enable-profiling")
- [Disabling the profiler](#profiling.disable-profiling "#profiling.disable-profiling")
- [Disabling profiler logs export](#profiling.disabling-logs-export "#profiling.disabling-logs-export")
- [Accessing your profiler logs](#profiling.accessing "#profiling.accessing")
- [Common queries](#profiling.common-queries "#profiling.common-queries")

## Supported operations

Amazon DocumentDB profiler supports the following operations:

- `aggregate`
- `count`
- `delete`
- `distinct`
- `find` (OP_QUERY and command)
- `findAndModify`
- `insert`
- `update`

## Limitations

The slow query profiler is only able to emit profiler logs if the entire result set of the query is able to fit in one batch, and if the result set is under 16MB (maximum BSON size). Result sets greater than 16MB are automatically split into multiple batches.

Most drivers or shells may set a default batch size that is small. You can specify the batch size as part of your query. For the purpose of capturing slow query logs, we recommend a batch size that exceeds the size of your expected result set. If you are unsure of the result set size, or if it varies, you can also set the batch size to a large number (e.g., 100k).

However, using a larger batch size means more results will have to be retrieved from the database before a response is sent to the client. For some queries, that may create longer delays before you get results. If you do not plan to consume the entire result set, it is possible that you will spend more I/Os to process the query and throw away the result.

## Enabling the Amazon DocumentDB profiler

Enabling the profiler on a cluster is a three-step process. Ensure
that all steps are completed, or profiling logs will not be sent to
CloudWatch Logs. Profiler is set at the cluster level and is performed on all of
the cluster's databases and instances.

###### To enable the profiler on a cluster

1. Because you can't modify a default cluster parameter group,
   ensure that you have an available custom cluster parameter group.
   For more information, see [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md").
2. Using an available custom cluster parameter group, modify the
   following parameters: `profiler`,
   `profiler_threshold_ms`, and
   `profiler_sampling_rate`. For more information, see [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md").
3. Create or modify your cluster to use the custom cluster
   parameter group and to enable exporting `profiler`
   logs to CloudWatch Logs.

The following sections show how to implement these steps using the
AWS Management Console and the AWS Command Line Interface (AWS CLI).

Using the AWS Management Console

1. Before you begin, create a Amazon DocumentDB cluster and a custom
   cluster parameter group if you don't already have one. For
   more information, see [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md") and [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md").
2. Using an available custom cluster parameter group,
   modify the following parameters. For more information, see
   [Modifying Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-modify.md "cluster_parameter_groups-modify.md").
   - `profiler` — Enables or disables
     query profiling. Permitted values are `enabled` and `disabled`. The default value
     is `disabled`. To enable profiling, set
     the value to `enabled`.
   - `profiler_threshold_ms` — When
     `profiler` is set to `enabled`,
     all commands that are taking longer than `profiler_threshold_ms` are logged to CloudWatch.
     Permitted values are `[50-INT_MAX]`. The
     default value is `100`.
   - `profiler_sampling_rate` — The
     fraction of slow operations that should be profiled
     or logged. Permitted values are `[0.0-1.0]`. The default value is `1.0`.

3. Modify your cluster to use the custom cluster parameter
   group and set the profiler log exports to publish to
   Amazon CloudWatch.
   1. In the navigation pane, choose **Clusters** to add your custom parameter group to a
      cluster.
   2. Choose the button to the left of the name of the
      cluster that you want to associate your parameter
      group with. Select **Actions**, and
      then **Modify** to modify your
      cluster.
   3. Under **Cluster options**, choose
      the custom parameter group from the step above to add
      it to your cluster.
   4. Under **Log exports**, select
      **Profiler logs** to publish to
      Amazon CloudWatch.
   5. Choose **Continue** to view a
      summary of your modifications.
   6. After verifying your changes, you can apply them
      immediately or during the next maintenance window
      under **Scheduling of modifications** .
   7. Choose **Modify cluster** to
      update your cluster with your new parameter group.

Using the AWS CLI
The following procedure enables the profiler on all supported
operations for the cluster `sample-cluster`.

1. Before you begin, ensure that you have an available
   custom cluster parameter group by running the following
   command, and reviewing the output for a cluster parameter
   group that doesn't have `default` in the name
   and has `docdb3.6` as the parameter group family.
   If you don't have a non-default cluster parameter group, see
   [Creating Amazon DocumentDB cluster parameter groups](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md").

```
aws docdb describe-db-cluster-parameter-groups \
    --query 'DBClusterParameterGroups[*].[DBClusterParameterGroupName,DBParameterGroupFamily]'
```

In the following output, only `sample-parameter-group` meets both criteria.

```
[
       [
           "default.docdb3.6",
           "docdb3.6"
       ],
       [
           `"sample-parameter-group"`,
           "docdb3.6"
       ]
]
```

2. Using your custom cluster parameter group, modify the
   following parameters:
   - `profiler` — Enables or disables
     query profiling. Permitted values are `enabled` and `disabled`. The default value
     is `disabled`. To enable profiling, set
     the value to `enabled`.
   - `profiler_threshold_ms` — When
     `profiler` is set to `enabled`,
     all commands taking longer than `profiler_threshold_ms` are logged to CloudWatch. Permitted
     values are `[50-INT_MAX]`. The default value is `100`.
   - `profiler_sampling_rate` — The
     fraction of slow operations that should be profiled
     or logged. Permitted values are `[0.0-1.0]`.
     The default value is `1.0`.

```
aws docdb modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name sample-parameter-group \
    --parameters ParameterName=profiler,ParameterValue=enabled,ApplyMethod=immediate \
                 ParameterName=profiler_threshold_ms,ParameterValue=100,ApplyMethod=immediate \
                 ParameterName=profiler_sampling_rate,ParameterValue=0.5,ApplyMethod=immediate
```

3. Modify your Amazon DocumentDB cluster so that it uses the
   `sample-parameter-group` custom cluster parameter
   group from the previous step and sets the parameter
   `--enable-cloudwatch-logs-exports` to
   `profiler`.

The following code modifies the cluster
`sample-cluster` to use the
`sample-parameter-group` from the previous step,
and adds `profiler` to the enabled CloudWatch Logs exports.

```
aws docdb modify-db-cluster \
       --db-cluster-identifier sample-cluster \
       --db-cluster-parameter-group-name sample-parameter-group \
       --cloudwatch-logs-export-configuration '{"EnableLogTypes":["profiler"]}'

```

Output from this operation looks something like the
following.

```
{
    "DBCluster": {
        "AvailabilityZones": [
            "us-east-1c",
            "us-east-1b",
            "us-east-1a"
        ],
        "BackupRetentionPeriod": 1,
        "DBClusterIdentifier": "sample-cluster",
        "DBClusterParameterGroup": "sample-parameter-group",
        "DBSubnetGroup": "default",
        "Status": "available",
        "EarliestRestorableTime": "2020-04-07T02:05:12.479Z",
        "Endpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "ReaderEndpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "MultiAZ": false,
        "Engine": "docdb",
        "EngineVersion": "3.6.0",
        "LatestRestorableTime": "2020-04-08T22:08:59.317Z",
        "Port": 27017,
        "MasterUsername": "test",
        "PreferredBackupWindow": "02:00-02:30",
        "PreferredMaintenanceWindow": "tue:09:50-tue:10:20",
        "DBClusterMembers": [
            {
                "DBInstanceIdentifier": "sample-instance-1",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            },
            {
                "DBInstanceIdentifier": "sample-instance-2",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            }
        ],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcd0123",
                "Status": "active"
            }
        ],
        "HostedZoneId": "ABCDEFGHIJKLM",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DbClusterResourceId": "cluster-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "DBClusterArn": "arn:aws:rds:us-east-1:<accountID>:cluster:sample-cluster",
        "AssociatedRoles": [],
        "ClusterCreateTime": "2020-01-10T22:13:38.261Z",
        "**EnabledCloudwatchLogsExports": [
 "profiler"
 ],
 "DeletionProtection": true**
    }
}
```

## Disabling the Amazon DocumentDB profiler

To disable the profiler, you disable both the `profiler`
parameter and the export of `profiler` logs to CloudWatch Logs.

### Disabling the Profiler

You can disable the `profiler` parameter using either
the AWS Management Console or AWS CLI, as follows.

Using the AWS Management Console
The following procedure uses the AWS Management Console to disable
Amazon DocumentDB `profiler`.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Parameter
   groups**. Then choose the name of the cluster
   parameter group that you want to disable the profiler
   on.
3. In the resulting **Cluster parameters** page, select the button to the left of the
   `profiler` parameter and choose
   **Edit**.
4. In the **Modify profiler** dialog
   box, choose `disabled` in the list.
5. Choose **Modify cluster parameter**.

Using the AWS CLI
To disable `profiler` on a cluster using the
AWS CLI, modify the cluster as follows.

```
aws docdb modify-db-cluster-parameter-group \
    --db-cluster-parameter-group-name sample-parameter-group \
    --parameters ParameterName=profiler,ParameterValue=disabled,ApplyMethod=immediate
```

## Disabling profiler logs export

You can disable exporting `profiler` logs to CloudWatch Logs by
using either the AWS Management Console or AWS CLI, as follows.

Using the AWS Management Console
The following procedure uses the AWS Management Console to disable
Amazon DocumentDB exporting logs to CloudWatch.

1. Open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose
   **Clusters**. Choose the button to the
   left of the name of the cluster for which you want to
   disable exporting logs.
3. On the **Actions** menu, choose
   **Modify**.
4. Scroll down to the **Log exports**
   section and unselect **Profiler logs**.
5. Choose **Continue**.
6. Review your changes, and then choose when you want
   this change applied to your cluster:
   - **Apply during the next scheduled
     maintenance window**
   - **Apply immediately**

7. Choose **Modify cluster**.

Using the AWS CLI
The following code modifies the cluster `sample-cluster` and disables CloudWatch profiler logs.

###### Example

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster \
   --db-cluster-identifier sample-cluster \
   --cloudwatch-logs-export-configuration '{"DisableLogTypes":["profiler"]}'
```

For Windows:

```
aws docdb modify-db-cluster ^
   --db-cluster-identifier sample-cluster ^
   --cloudwatch-logs-export-configuration '{"DisableLogTypes":["profiler"]}'
```

Output from this operation looks something like the
following.

```
{
    "DBCluster": {
        "AvailabilityZones": [
            "us-east-1c",
            "us-east-1b",
            "us-east-1a"
        ],
        "BackupRetentionPeriod": 1,
        "DBClusterIdentifier": "sample-cluster",
        "DBClusterParameterGroup": "sample-parameter-group",
        "DBSubnetGroup": "default",
        "Status": "available",
        "EarliestRestorableTime": "2020-04-08T02:05:17.266Z",
        "Endpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "ReaderEndpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "MultiAZ": false,
        "Engine": "docdb",
        "EngineVersion": "3.6.0",
        "LatestRestorableTime": "2020-04-09T05:14:44.356Z",
        "Port": 27017,
        "MasterUsername": "test",
        "PreferredBackupWindow": "02:00-02:30",
        "PreferredMaintenanceWindow": "tue:09:50-tue:10:20",
        "DBClusterMembers": [
            {
                "DBInstanceIdentifier": "sample-instance-1",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            },
            {
                "DBInstanceIdentifier": "sample-instance-2",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            }
        ],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcd0123",
                "Status": "active"
            }
        ],
        "HostedZoneId": "ABCDEFGHIJKLM",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DbClusterResourceId": "cluster-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "DBClusterArn": "arn:aws:rds:us-east-1:<accountID>:cluster:sample-cluster",
        "AssociatedRoles": [],
        "ClusterCreateTime": "2020-01-10T22:13:38.261Z",
        "DeletionProtection": true
    }
}

```

## Accessing your Amazon DocumentDB profiler logs

Follow these steps to access your profile logs on Amazon CloudWatch.

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Make sure that you are in the same Region as your Amazon DocumentDB
   cluster.
3. In the navigation pane, choose **Logs**.
4. To find the profiler logs for your cluster, in the list, choose
   `/aws/docdb/`yourClusterName`/profiler`.

The profile logs for each of your instances are available under each of the respective instance names.

## Common queries

The following are some common queries you can use to analyze your
profiled commands. For more information about CloudWatch Logs Insights, see [Analyzing Log Data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md")
and [Sample Queries](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md").

### Get the 10 slowest operations on a specified collection

```
filter ns="test.foo" | sort millis desc | limit 10
```

### Get all the update operations on a collection that took more than 60 ms

```
filter millis > 60 and op = "update"
```

### Get the 10 slowest operations in the last month

```
sort millis desc | limit 10
```

### Get all the queries with a COLLSCAN plan summary

```
filter planSummary="COLLSCAN"
```
