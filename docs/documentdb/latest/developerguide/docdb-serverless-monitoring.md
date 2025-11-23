# Monitoring Amazon DocumentDB serverless

To learn more about monitoring in Amazon DocumentDB, see [Monitoring Amazon DocumentDB](monitoring_docdb.md "monitoring_docdb.md").

###### Topics

- [Out of Memory: incompatible-parameters status](#w2aac41c27b7 "#w2aac41c27b7")
- [Amazon CloudWatch metrics for DocumentDB serverless](#w2aac41c27b9 "#w2aac41c27b9")
- [Monitoring DocumentDB serverless performance with Performance Insights](#w2aac41c27c11 "#w2aac41c27c11")

## Out of Memory: incompatible-parameters status

If one of your serverless instances consistently reaches the limit of its maximum capacity, Amazon DocumentDB indicates this condition by setting the instance to a status of incompatible-parameters.
For more information, see [Avoiding out-of-memory errors](docdb-serverless-scaling-config.md#docdb-serverless-scaling-mem-errors "docdb-serverless-scaling-config.md#docdb-serverless-scaling-mem-errors").

## Amazon CloudWatch metrics for DocumentDB serverless

To learn more about using CloudWatch with Amazon DocumentDB, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").

You can view your serverless instances in CloudWatch to monitor the capacity consumed by each instance with the `ServerlessDatabaseCapacity` metric.
You can also monitor all of the standard DocumentDB CloudWatch metrics, such as `DatabaseConnections` and Queries.
For the full list of CloudWatch metrics that you can monitor for Amazon DocumentDB, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").
The following CloudWatch instance-level metrics are important to monitor for you to understand how your DocumentDB serverless instances are scaling up and down.
All of these metrics are calculated every second.
That way, you can monitor the current status of your serverless instances.
You can set alarms to notify you if any serverless instance approaches a threshold for metrics related to capacity.
You can determine if the minimum and maximum capacity settings are appropriate, or if you need to adjust them.
You can determine where to focus your efforts for optimizing the efficiency of your database.

- **`ServerlessDatabaseCapacity`** — As an instance-level metric, it reports the number of DCUs represented by the current instance capacity.
  As a cluster-level metric, it represents the average of the `ServerlessDatabaseCapacity` values of all the DocumentDB serverless instances in the cluster.
- **`DCUUtilization.`** — This metric is new in DocumentDB serverless.
  This value is represented as a percentage.
  It's calculated as the value of the `ServerlessDatabaseCapacity` metric divided by the maximum DCU value of the cluster.
  Consider the following guidelines to interpret this metric and take action:
  - If this metric approaches a value of `100.0`, the instance has scaled up as high as it can.
    Consider increasing the maximum DCU setting for the cluster.
    That way, both writer and reader instances can scale to a higher capacity.
  - Suppose that a read-only workload causes a reader instance to approach a `DCUUtilization` of `100.0`, while the writer instance isn't close to its maximum capacity.
    In this case, consider adding additional reader instances to the cluster.
    That way, you can spread the read-only part of the workload across more instances, reducing the load on each reader instance.
  - Suppose that you are running a production application, where performance and scalability are the primary considerations.
    In this case, you can set the maximum DCU value for the cluster to a high number.
    Your goal is for the `DCUUtilization` metric to always be below 100.0.
    With a high maximum DCU value, you can be confident that there's enough room in case there are unexpected spikes in database activity.
    You are only charged for the database capacity that's actually consumed.

- **`CPUUtilization`** — This metric is interpreted differently in DocumentDB serverless than in provisioned instances.
  For DocumentDB serverless, this value is a percentage that's calculated as the amount of CPU currently being used, divided by the CPU capacity that's available under the maximum DCU value of the cluster.
  Amazon DocumentDB monitors this value automatically and scales up your serverless instance when the instance consistently uses a high proportion of its CPU capacity.

If this metric approaches a value of `100.0`, the instance has reached its maximum CPU capacity.
Consider increasing the maximum DCU setting for the cluster.
If this metric approaches a value of `100.0` on a reader instance, consider adding additional reader instances to the cluster.
That way, you can spread the read-only part of the workload spread across more instances, reducing the load on each reader instance.

- **`FreeableMemory`** — This value represents the amount of unused memory that is available when the DocumentDB serverless instance is scaled to its maximum capacity.
  For every DCU that the current capacity is below the maximum capacity, this value increases by approximately 2 GiB.
  Thus, this metric doesn't approach zero until the instance is scaled up as high as it can.

If this metric approaches a value of zero, the instance has scaled up as much as it can and is nearing the limit of its available memory.
Consider increasing the maximum DCU setting for the cluster.
If this metric approaches a value of zero on a reader instance, consider adding additional reader instances to the cluster.
That way, the read-only part of the workload can be spread across more instances, reducing the memory usage on each reader instance.

- **`TempStorageIops`** — The number of IOPS done on local storage attached to the instance.
  It includes the IOPS for both reads and writes.
  This metric represents a count and is measured once per second.
  This is a new metric for DocumentDB serverless. For details, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").
- **`TempStorageThroughput`** — The amount of data transferred to and from local storage associated with the instance.
  This metric represents bytes and is measured once per second.
  This is a new metric for DocumentDB serverless.
  For details, see [Monitoring Amazon DocumentDB with CloudWatch](cloud_watch.md "cloud_watch.md").

Typically, most scaling up for DocumentDB serverless instances is caused by memory usage and CPU activity.
The `TempStorageIops` and `TempStorageThroughput` metrics can help you to diagnose the rare cases where network activity for transfers between your instance and local storage devices is responsible for unexpected capacity increases.
To monitor other network activity, you can use these existing metrics:

- `NetworkReceiveThroughput`
- `NetworkThroughput`
- `NetworkTransmitThroughput`
- `StorageNetworkReceiveThroughput`
- `StorageNetworkThroughput`
- `StorageNetworkTransmitThroughput`

### How DocumentDB serverless CloudWatch metrics apply to your AWS bill

The DocumentDB serverless charges on your AWS bill are calculated based on the same `ServerlessDatabaseCapacity` metric that you can monitor.
The billing mechanism can differ from the computed CloudWatch average for this metric in cases where you use DocumentDB serverless capacity for only part of an hour.
It can also differ if system issues make the CloudWatch metric unavailable for brief periods.
Thus, you might see a slightly different value of DCU-hours on your bill than if you compute the number yourself from the `ServerlessDatabaseCapacity` average value.

### Examples of Amazon CloudWatch CLI commands for DocumentDB serverless metrics

The following AWS CLI examples demonstrate how you can monitor the most important CloudWatch metrics related to DocumentDB serverless.
In each case, replace the `Value=` string for the `--dimensions` parameter with the identifier of your own DocumentDB serverless instance.

The following Linux example displays the minimum, maximum, and average capacity values for an instance, measured every 10 minutes over one hour.
The Linux date commands specifies the start and end times relative to the current date and time.
The `sort_by` function in the `--query` parameter sorts the results chronologically based on the `Timestamp` field.

```
aws cloudwatch get-metric-statistics \
    --metric-name "ServerlessDatabaseCapacity" \
    --start-time "$(date -d '1 hour ago')" \
    --end-time "$(date -d 'now')" \
    --period 600 \
    --namespace "AWS/DocDB" \
    --statistics Minimum Maximum Average \
    --dimensions Name=DBInstanceIdentifier,Value=`my_instance` \
    --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
    --output table
```

The following Linux example demonstrates monitoring the capacity of an instance in a cluster.
It measures the minimum, maximum, and average capacity utilization of an instance.
The measurements are taken once each hour over a three-hour period.
These examples use the `DCUUtilization` metric representing a percentage of the upper limit on DCUs, instead of `ServerlessDatabaseCapacity` representing a fixed number of DCUs.
That way, you don't need to know the actual numbers for the minimum and maximum DCU values in the capacity range.
You can see percentages ranging from 0 to 100.

```
aws cloudwatch get-metric-statistics \
    --metric-name "DCUUtilization" \
    --start-time "$(date -d '3 hours ago')" \
    --end-time "$(date -d 'now')" \
    --period 3600 \
    --namespace "AWS/DocDB" \
    --statistics Minimum Maximum Average \
    --dimensions Name=DBInstanceIdentifier,Value=`my_instance` \
    --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
    --output table
```

The following Linux example does similar measurements as the previous ones.
In this case, the measurements are for the `CPUUtilization` metric.
The measurements are taken every 10 minutes over a 1-hour period.
The numbers represent the percentage of available CPU used, based on the CPU resources available to the maximum capacity setting for the instance.

```
aws cloudwatch get-metric-statistics \
    --metric-name "CPUUtilization" \
    --start-time "$(date -d '1 hour ago')" \
    --end-time "$(date -d 'now')" \
    --period 600 \
    --namespace "AWS/DocDB" \
    --statistics Minimum Maximum Average \
    --dimensions Name=DBInstanceIdentifier,Value=`my_instance` \
    --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
    --output table
```

The following Linux example does similar measurements as the previous ones.
In this case, the measurements are for the `FreeableMemory` metric.
The measurements are taken every 10 minutes over a 1-hour period.

```
aws cloudwatch get-metric-statistics \
    --metric-name "FreeableMemory" \
    --start-time "$(date -d '1 hour ago')" \
    --end-time "$(date -d 'now')" \
    --period 600 \
    --namespace "AWS/DocDB" \
    --statistics Minimum Maximum Average \
    --dimensions Name=DBInstanceIdentifier,Value=`my_instance` \
    --query 'sort_by(Datapoints[*].{min:Minimum,max:Maximum,avg:Average,ts:Timestamp},&ts)' \
    --output table
```

## Monitoring DocumentDB serverless performance with Performance Insights

You can use Performance Insights to monitor the performance of DocumentDB serverless instances.
For Performance Insights procedures, see [Monitoring with Performance Insights](performance-insights.md "performance-insights.md").

The following new Performance Insights counters apply to DocumentDB serverless instances:

- **`os.general.serverlessDBCapacity`** — The current capacity of the instance in DCUs.
  The value corresponds to the `ServerlessDatabaseCapacity` CloudWatch metric for the instance.
- **`os.general.dcuUtilization`** — The percentage of current capacity out of the maximum configured capacity.
  The value corresponds to the `DCUUtilization` CloudWatch metric for the instance.
- **`os.general.maxConfiguredDcu`** — The maximum capacity that you configured for this DocumentDB serverless instance.
  It's measured in DCUs.
- **`os.general.minConfiguredDcu`** — The minimum capacity that you configured for this DocumentDB serverless instance. It's measured in DCUs.

For the full list of Performance Insights counters, see [Performance Insights for counter metrics](performance-insights-counter-metrics.md "performance-insights-counter-metrics.md").

When vCPU values are shown for a DocumentDB serverless instance in Performance Insights, those values represent estimates based on the DCU value for the instance.
At the default interval of one minute, any fractional vCPU values are rounded up to the nearest whole number.
For longer intervals, the vCPU value shown is the average of the integer vCPU values for each minute.
