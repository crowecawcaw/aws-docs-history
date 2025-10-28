# Troubleshooting latency issues in AWS Database Migration Service

This section provides an overview of the common causes for AWS DMS task latency during the ongoing replication phase (CDC).
AWS DMS replicates data asynchronously. Latency is the delay between when a change was committed on the source and when the
change was replicated to the target. Latency can be caused due to misconfiguration of replication components, such as
the following:

- Source endpoint or data source
- Target endpoint or data source
- Replication instances
- The network between these components
  We recommend that you use a test migration as a proof of concept to gather information about your replication. You can then use this information
  for tuning your replication configuration to minimize latency. For information about running a proof of concept migration,
  see [Running a proof of concept](CHAP_BestPractices.md#CHAP_BestPractices.RunPOC "CHAP_BestPractices.md#CHAP_BestPractices.RunPOC").

###### Topics

- [Types of CDC latency](#CHAP_Troubleshooting_Latency_Types "#CHAP_Troubleshooting_Latency_Types")
- [Common causes of CDC latency](#CHAP_Troubleshooting_Latency_Causes "#CHAP_Troubleshooting_Latency_Causes")
- [Troubleshooting latency issues](CHAP_Troubleshooting_Latency_Troubleshooting.md "CHAP_Troubleshooting_Latency_Troubleshooting.md")

## Types of CDC latency

This section contains types of replication latency that may occur during CDC.

### Source latency

The delay, in seconds, between the commit time of the last event captured from the source
endpoint, and the current system timestamp of the replication instance. You can monitor the
latency between the data source and your replication instance using the `CDCLatencySource`
CloudWatch metric. A high `CDCLatencySource` metric indicates that the process of capturing
changes from the source is delayed. For example, if your application commits an insert to the
source at 10:00, and AWS DMS consumes the change at 10:02, the `CDCLatencySource` metric
is 120 seconds.

For information about CloudWatch metrics for AWS DMS, see
[Replication task metrics](CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task "CHAP_Monitoring.md#CHAP_Monitoring.Metrics.Task").

### Target latency

The delay, in seconds, between the commit time on the source of the first event waiting to commit
to the target, and the current timestamp of the DMS replication instance. You can monitor the
latency between commits on the data source and your data target using the `CDCLatencyTarget`
CloudWatch metric. This means that `CDCLatencyTarget` includes any delays in reading from the source.
As a result, `CDCLatencyTarget` is always greater than or equal to `CDCLatencySource`.

For example, if your application commits an insert to the source at 10:00, and AWS DMS consumes it at 10:02 and
writes it to the target at 10:05, the `CDCLatencyTarget` metric is 300 seconds.

## Common causes of CDC latency

This section contains causes of latency that your replication may experience during CDC.

###### Topics

- [Endpoint resources](#CHAP_Troubleshooting_Latency_Causes_Endpoint "#CHAP_Troubleshooting_Latency_Causes_Endpoint")
- [Replication instance resources](#CHAP_Troubleshooting_Latency_Causes_Replication_Instance "#CHAP_Troubleshooting_Latency_Causes_Replication_Instance")
- [Network speed and bandwidth](#CHAP_Troubleshooting_Latency_Causes_Replication_Network "#CHAP_Troubleshooting_Latency_Causes_Replication_Network")
- [DMS configuration](#CHAP_Troubleshooting_Latency_Causes_Replication_DMS_Config "#CHAP_Troubleshooting_Latency_Causes_Replication_DMS_Config")
- [Replication scenarios](#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios "#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios")

### Endpoint resources

The following factors significantly affect replication performance and latency:

- Source and target database configurations
- Instance size
- Under-provisioned or misconfigured source or target data stores

To identify causes for latency caused by endpoint issues for AWS-hosted sources and targets, monitor the following
CloudWatch metrics:

- `FreeMemory`
- `CPUUtilization`
- Throughput and I/O metrics, such as `WriteIOPS`, `WriteThroughput`, or `ReadLatency`
- Transaction volume metrics such as `CDCIncomingChanges`.

For information about monitoring CloudWatch metrics, see [AWS Database Migration Service metrics](CHAP_Monitoring.md#CHAP_Monitoring.Metrics "CHAP_Monitoring.md#CHAP_Monitoring.Metrics").

### Replication instance resources

Replication instance resources are critical for replication, and you should make sure
that there are no resource bottlenecks, as they can lead to both source and target latency.

To identify resource bottlenecks for your replication instance, verify the following:

- Critical CloudWatch metrics such as CPU, Memory, I/O per second, and storage are not experiencing spikes
  or consistenly high values.
- Your replication instance is sized appropriately for your workload. For information about determining
  the correct size of a replication instance, see [Selecting the best size for a
  replication instance](CHAP_BestPractices.md "CHAP_BestPractices.md").

### Network speed and bandwidth

Network bandwith is a factor that affects data transmission. To analyze the network performance of your
replication, do one of the following:

- Check the `ReadThroughput` and `WriteThroughput` metrics at the instance level.
  For information about monitoring CloudWatch metrics, see [AWS Database Migration Service metrics](CHAP_Monitoring.md#CHAP_Monitoring.Metrics "CHAP_Monitoring.md#CHAP_Monitoring.Metrics").
- Use the AWS DMS Diagnostic Support AMI. If the Diagnostic Support AMI is not available in your region,
  you can download it from any supported region and copy it to your region to perform your network analysis. For information
  about the Diagnostic Support AMI, see [Working with the AWS DMS diagnostic support AMI](CHAP_SupportAmi.md "CHAP_SupportAmi.md").

CDC in AWS DMS is single-threaded to ensure data consistency. As a result, you can determine the data volume your network
can support by calculating your single-threaded data transfer rate.
For example, if your task connects to its source using a 100 Mbps (megabits per second) network, your replication has a
theoretical maximum bandwidth allocation of 12.5 MBps (megabytes per second). This is equal to 45 gigabits per hour. If the
rate of transaction log generation on the source is greater than 45 gigabits per hour, this means that the task has CDC latency.
For a 100 MBps network, these rates are theoretical maximums; other factors such as network traffic and resource overhead on the source and
target reduce the actual available bandwidth.

### DMS configuration

This section contains recommended replication configurations that can help reduce latency.

- **Endpoint settings**: Your source and target endpoint settings
  can cause your replication instance to suffer poor performance. Endpoint settings that turn on resource-intensive features
  will impact performance. For example, for an Oracle endpoint, disabling LogMiner and using Binary Reader improves
  performance, since LogMiner is resource-intensive. The following endpoing setting improves performance for an Oracle
  endpoint:

```
useLogminerReader=N;useBfile=Y
```

For more information about endpoint settings, see the documentation for your source and target endpoint engine
in the [Working with AWS DMS endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md") topic.

- **Task settings**: Some task settings
  for your particular replication scenario can cause your replication instance to suffer poor performance. For example,
  AWS DMS uses transactional apply mode by default (`BatchApplyEnabled=false`) for CDC for all endpoints
  except for Amazon Redshift. However, for sources with a large number of changes, setting `BatchApplyEnabled`
  to `true` may improve performance.

For more information about task settings, see [Specifying task settings
for AWS Database Migration Service tasks](CHAP_Tasks.CustomizingTasks.md "CHAP_Tasks.CustomizingTasks.md").

- **Start Position of a CDC only task**: Starting a CDC-only task from a
  position or timestamp in the past will start the task with increased CDC source latency. Depending on the
  volume of changes on the source, task latency will take time to subside.
- **LOB settings**: Large Object data types can hinder replication performance
  due to the way AWS DMS replicates large binary data. For more information, see the following topics:
  - [Setting LOB support for source databases in
    an AWS DMS task](CHAP_Tasks.md "CHAP_Tasks.md")
  - [Migrating large binary objects (LOBs)](CHAP_BestPractices.md#CHAP_BestPractices.LOBS "CHAP_BestPractices.md#CHAP_BestPractices.LOBS").

### Replication scenarios

This section describes specific replication scenarios and how they may affect latency.

###### Topics

- [Stopping a task for an
  extended period of time](#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Stoptask "#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Stoptask")
- [Cached changes](#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Cachedchanges "#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Cachedchanges")
- [Cross-region replication](#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Crossregion "#CHAP_Troubleshooting_Latency_Causes_Replication_Scenarios_Crossregion")

#### Stopping a task for an

extended period of time

When you stop a task, AWS DMS saves the position of the last transaction log that was read from the source.
When you resume the task, DMS tries to continue reading from the same transaction log position. Resuming a task after
several hours or days causes CDC source latency to increase until DMS finishes consuming the transaction backlog.

#### Cached changes

**Cached changes** are changes that your application writes to the data source
while AWS DMS runs the full-load replication phase. DMS doesn't apply these changes until the full-load phase completes and
the CDC phase starts. For a source with large number of transactions, cached changes take longer to apply, so source
latency increases when the CDC phase starts. We recommend that you run the full-load phase when transaction volumes are low
to minimize the number of cached changes.

#### Cross-region replication

Locating your DMS endpoints or your replication instance in different AWS regions increases network latency.
This increases replication latency. For best performance, locate your source endpoint, target endpoint, and replication instance
in the same AWS region.
