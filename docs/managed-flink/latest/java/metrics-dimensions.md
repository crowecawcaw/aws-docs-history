

# Metrics and dimensions in Managed Service for Apache Flink
<a name="metrics-dimensions"></a>

When your Managed Service for Apache Flink processes a data source, Managed Service for Apache Flink reports the following metrics and dimensions to Amazon CloudWatch.

**Flink 2.2 metric changes**  
Flink 2.2 introduces metric changes that may affect your monitoring and alarms. Review the following changes before upgrading:  
The `fullRestarts` metric has been removed. Use `numRestarts` instead.
The `uptime` and `downtime` metrics are deprecated and will be removed in a future release. Migrate to the new state-specific metrics.
The `bytesRequestedPerFetch` metric for Kinesis Data Streams connector 6.0.0 has been removed.

## Application metrics
<a name="metrics-dimensions-jobs"></a>


| Metric | Unit | Description | Level | Usage Notes | 
| --- | --- | --- | --- | --- | 
| backPressuredTimeMsPerSecond\* | Milliseconds | The time (in milliseconds) this task or operator is back pressured per second. | Task, Operator, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />These metrics can be useful in identifying bottlenecks in an application. | 
| busyTimeMsPerSecond\* | Milliseconds | The time (in milliseconds) this task or operator is busy (neither idle nor back pressured) per second. Can be NaN, if the value could not be calculated. | Task, Operator, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />These metrics can be useful in identifying bottlenecks in an application. | 
| cpuUtilization | Percentage | Overall percentage of CPU utilization across task managers. For example, if there are five task managers, Managed Service for Apache Flink publishes five samples of this metric per reporting interval. | Application | You can use this metric to monitor minimum, average, and maximum CPU utilization in your application. The CPUUtilization metric only accounts for CPU usage of the TaskManager JVM process running inside the container.  | 
| containerCPUUtilization | Percentage | Overall percentage of CPU utilization across task manager containers in Flink application cluster. For example, if there are five task managers, correspondingly there are five TaskManager containers and Managed Service for Apache Flink publishes 2 \* five samples of this metric per 1 minute reporting interval. | Application | It is calculated per container as:<br />*Total CPU time (in seconds) consumed by container \* 100 / Container CPU limit (in CPUs/seconds)*<br />The `CPUUtilization` metric only accounts for CPU usage of the TaskManager JVM process running inside the container. There are other components running outside the JVM within the same container. The `containerCPUUtilization` metric gives you a more complete picture, including all processes in terms of CPU exhaustion at the container and failures resulting from that. | 
| containerMemoryUtilization | Percentage | Overall percentage of memory utilization across task manager containers in Flink application cluster. For example, if there are five task managers, correspondingly there are five TaskManager containers and Managed Service for Apache Flink publishes 2 \* five samples of this metric per 1 minute reporting interval. | Application | It is calculated per container as:<br />*Container memory usage (bytes) \* 100 / Container memory limit as per pod deployment spec (in bytes)*<br />The `HeapMemoryUtilization` and `ManagedMemoryUtilzations` metrics only account for specific memory metrics like Heap Memory Usage of TaskManager JVM or Managed Memory (memory usage outside JVM for native processes like [RocksDB State Backend](https://flink.apache.org/2021/01/18/rocksdb.html#:~:text=Conclusion-,The%20RocksDB%20state%20backend%20(i.e.%2C%20RocksDBStateBackend)%20is%20one%20of,with%20exactly%2Donce%20processing%20guarantees.)). The `containerMemoryUtilization` metric gives you a more complete picture by including the working set memory, which is a better tracker of total memory exhaustion. Upon its exhaustion, it will result in `Out of Memory Error` for the TaskManager pod. | 
| containerDiskUtilization | Percentage | Overall percentage of disk utilization across task manager containers in Flink application cluster. For example, if there are five task managers, correspondingly there are five TaskManager containers and Managed Service for Apache Flink publishes 2 \* five samples of this metric per 1 minute reporting interval. | Application | It is calculated per container as:<br />*Disk usage in bytes \* 100 / Disk Limit for container in bytes*<br />For containers, it represents utilization of the filesystem on which root volume of the container is set up. | 
| currentInputWatermark | Milliseconds | The last watermark this application/operator/task/thread has received | Application, Operator, Task, Parallelism | This record is only emitted for dimensions with two inputs. This is the minimum value of the last received watermarks. | 
| currentOutputWatermark | Milliseconds | The last watermark this application/operator/task/thread has emitted | Application, Operator, Task, Parallelism |  | 
| downtime [DEPRECATED] | Milliseconds | For jobs currently in a failing/recovering situation, the time elapsed during this outage. | Application | This metric measures the time elapsed while a job is failing or recovering. This metric returns 0 for running jobs and -1 for completed jobs. If this metric is not 0 or -1, this indicates that the Apache Flink job for the application failed to run. **Deprecated in Flink 2.2.** Use `restartingTime`, `cancellingTime`, and/or `failingTime` instead. | 
| failingTime | Milliseconds | The time (in milliseconds) that the application has spent in a failing state. Use this metric to monitor application failures and trigger alerts. | Application, Flow | Available from Flink 2.2. Replaces part of the deprecated downtime metric. | 
| heapMemoryUtilization | Percentage | Overall heap memory utilization across task managers. For example, if there are five task managers, Managed Service for Apache Flink publishes five samples of this metric per reporting interval. | Application | You can use this metric to monitor minimum, average, and maximum heap memory utilization in your application. The HeapMemoryUtilization only accounts for specific memory metrics like Heap Memory Usage of TaskManager JVM. | 
| idleTimeMsPerSecond\* | Milliseconds | The time (in milliseconds) this task or operator is idle (has no data to process) per second. Idle time excludes back pressured time, so if the task is back pressured it is not idle. | Task, Operator, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />These metrics can be useful in identifying bottlenecks in an application. | 
| lastCheckpointSize | Bytes | The total size of the last checkpoint | Application | You can use this metric to determine running application storage utilization. If this metric is increasing in value, this may indicate that there is an issue with your application, such as a memory leak or bottleneck. | 
| lastCheckpointDuration | Milliseconds | The time it took to complete the last checkpoint | Application | This metric measures the time it took to complete the most recent checkpoint. If this metric is increasing in value, this may indicate that there is an issue with your application, such as a memory leak or bottleneck. In some cases, you can troubleshoot this issue by disabling checkpointing. | 
| managedMemoryUsed\* | Bytes | The amount of managed memory currently used. | Application, Operator, Task, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />This relates to memory managed by Flink outside the Java heap. It is used for the RocksDB state backend, and is also available to applications. | 
| managedMemoryTotal\* | Bytes | The total amount of managed memory. | Application, Operator, Task, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />This relates to memory managed by Flink outside the Java heap. It is used for the RocksDB state backend, and is also available to applications. The `ManagedMemoryUtilzations` metric only accounts for specific memory metrics like Managed Memory (memory usage outside JVM for native processes like [RocksDB State Backend](https://flink.apache.org/2021/01/18/rocksdb.html#:~:text=Conclusion-,The%20RocksDB%20state%20backend%20(i.e.%2C%20RocksDBStateBackend)%20is%20one%20of,with%20exactly%2Donce%20processing%20guarantees.)) | 
| managedMemoryUtilization\* | Percentage | Derived by managedMemoryUsed/managedMemoryTotal | Application, Operator, Task, Parallelism | \*Available for Managed Service for Apache Flink applications running Flink version 1.13 only.<br />This relates to memory managed by Flink outside the Java heap. It is used for the RocksDB state backend, and is also available to applications. | 
| numberOfFailedCheckpoints | Count | The number of times checkpointing has failed. | Application | You can use this metric to monitor application health and progress. Checkpoints may fail due to application problems, such as throughput or permissions issues.  | 
| numRecordsIn\* | Count | The total number of records this application, operator, or task has received. | Application, Operator, Task, Parallelism | \*To apply the SUM statistic over a period of time (second/minute):+ Select the metric at the correct Level. If you’re tracking the metric for an Operator, you need to select the corresponding operator metrics.<br />+ As Managed Service for Apache Flink takes 4 metric snapshots per minute, the following metric math should be used: m1/4 where m1 is the SUM statistic over a period (second/minute)<br />The metric's Level specifies whether this metric measures the total number of records the entire application, a specific operator, or a specific task has received. | 
| numRecordsInPerSecond\* | Count/Second | The total number of records this application, operator or task has received per second. | Application, Operator, Task, Parallelism | \*To apply the SUM statistic over a period of time (second/minute):+ Select the metric at the correct Level. If you’re tracking the metric for an Operator, you need to select the corresponding operator metrics.<br />+ As Managed Service for Apache Flink takes 4 metric snapshots per minute, the following metric math should be used: m1/4 where m1 is the SUM statistic over a period (second/minute)<br />The metric's Level specifies whether this metric measures the total number of records the entire application, a specific operator, or a specific task has received per second. | 
| numRecordsOut\* | Count | The total number of records this application, operator or task has emitted. | Application, Operator, Task, Parallelism | \*To apply the SUM statistic over a period of time (second/minute):+ Select the metric at the correct Level. If you’re tracking the metric for an Operator, you need to select the corresponding operator metrics.<br />+ As Managed Service for Apache Flink takes 4 metric snapshots per minute, the following metric math should be used: m1/4 where m1 is the SUM statistic over a period (second/minute)<br />The metric's Level specifies whether this metric measures the total number of records the entire application, a specific operator, or a specific task has emitted. | 
| numLateRecordsDropped\* | Count | Application, Operator, Task, Parallelism |  | \*To apply the SUM statistic over a period of time (second/minute):+ Select the metric at the correct Level. If you’re tracking the metric for an Operator, you need to select the corresponding operator metrics.<br />+ As Managed Service for Apache Flink takes 4 metric snapshots per minute, the following metric math should be used: m1/4 where m1 is the SUM statistic over a period (second/minute)<br />The number of records this operator or task has dropped due to arriving late. | 
| numRecordsOutPerSecond\* | Count/Second | The total number of records this application, operator or task has emitted per second. | Application, Operator, Task, Parallelism | \*To apply the SUM statistic over a period of time (second/minute):+ Select the metric at the correct Level. If you’re tracking the metric for an Operator, you need to select the corresponding operator metrics.<br />+ As Managed Service for Apache Flink takes 4 metric snapshots per minute, the following metric math should be used: m1/4 where m1 is the SUM statistic over a period (second/minute)<br />The metric's Level specifies whether this metric measures the total number of records the entire application, a specific operator, or a specific task has emitted per second. | 
| oldGenerationGCCount | Count | The total number of old garbage collection operations that have occurred across all task managers.  | Application |  | 
| oldGenerationGCTime | Milliseconds | The total time spent performing old garbage collection operations.  | Application | You can use this metric to monitor sum, average, and maximum garbage collection time. | 
| threadsCount | Count | The total number of live threads used by the application.  | Application | This metric measures the number of threads used by the application code. This is not the same as application parallelism. | 
| cancellingTime | Milliseconds | The time (in milliseconds) that the application has spent in a cancelling state. Use this metric to monitor application cancellation operations. | Application, Flow | Available from Flink 2.2. Replaces part of the deprecated downtime metric. | 
| restartingTime | Milliseconds | The time (in milliseconds) that the application has spent in a restarting state. Use this metric to monitor application restart behavior. | Application, Flow | Available from Flink 2.2. Replaces part of the deprecated downtime metric. | 
| runningTime | Milliseconds | The time (in milliseconds) that the application has been running without interruption. Replaces the deprecated uptime metric. | Application, Flow | Available from Flink 2.2. Use as a direct replacement for the deprecated uptime metric. | 
| uptime [DEPRECATED] | Milliseconds | The time that the job has been running without interruption. | Application | You can use this metric to determine if a job is running successfully. This metric returns -1 for completed jobs. **Deprecated in Flink 2.2.** Use `runningTime` instead. | 
| jobmanagerFileDescriptorsMax | Count | The maximum number of file descriptors available to the JobManager. | Application, Flow, Host | Use this metric to monitor file descriptor capacity. | 
| jobmanagerFileDescriptorsOpen | Count | The current number of open file descriptors for the JobManager. | Application, Flow, Host | Use this metric to monitor file descriptor usage and detect potential resource exhaustion. | 
| taskmanagerFileDescriptorsMax | Count | The maximum number of file descriptors available to each TaskManager. | Application, Flow, Host, tm\_id | Use this metric to monitor file descriptor capacity. | 
| taskmanagerFileDescriptorsOpen | Count | The current number of open file descriptors for each TaskManager. | Application, Flow, Host, tm\_id | Use this metric to monitor file descriptor usage and detect potential resource exhaustion. | 
| KPUs\* | Count | The total number of KPUs used by the application. | Application | \*This metric receives one sample per billing period (one hour). To visualize the number of KPUs over time, use MAX or AVG over a period of at least one (1) hour.<br />The KPU count includes the `orchestration` KPU. For more information, see [Managed Service for Apache Flink Pricing](https://aws.amazon.com/managed-service-apache-flink/pricing/). | 

**Flink 2.2 metric migration guidance**  
**Migration from fullRestarts:** The `fullRestarts` metric has been removed in Flink 2.2. Use the `numRestarts` metric instead. The `numRestarts` metric provides equivalent functionality and can be used as a direct replacement in CloudWatch alarms without requiring threshold adjustments.  
**Migration from uptime:** The `uptime` metric is deprecated in Flink 2.2 and will be removed in a future release. Use the `runningTime` metric instead. The `runningTime` metric provides equivalent functionality and can be used as a direct replacement in CloudWatch alarms without requiring threshold adjustments.  
**Migration from downtime:** The `downtime` metric is deprecated in Flink 2.2 and will be removed in a future release. Depending on what you want to monitor, use one or more of the following metrics:  
`restartingTime`: Monitor time spent restarting the application
`cancellingTime`: Monitor time spent cancelling the application
`failingTime`: Monitor time spent in a failing state

## Kinesis Data Streams connector metrics
<a name="metrics-dimensions-stream"></a>

AWS emits all records for Kinesis Data Streams in addition to the following:


| Metric | Unit | Description | Level | Usage Notes | 
| --- | --- | --- | --- | --- | 
| millisbehindLatest | Milliseconds | The number of milliseconds the consumer is behind the head of the stream, indicating how far behind current time the consumer is. | Application (for Stream), Parallelism (for ShardId) | + A value of 0 indicates that record processing is caught up, and there are no new records to process at this moment. A particular shard's metric can be specified by stream name and shard id.<br />+ A value of -1 indicates that the service has not yet reported a value for the metric.  | 

**Note**  
The `bytesRequestedPerFetch` metric has been removed in Flink AWS connector version 6.0.0 (the only connector version compatible with Flink 2.2). The only Kinesis Data Streams connector metric available in Flink 2.2 is `millisBehindLatest`.

## Amazon MSK connector metrics
<a name="metrics-dimensions-msk"></a>

AWS emits all records for Amazon MSK in addition to the following:


| Metric | Unit | Description | Level | Usage Notes | 
| --- | --- | --- | --- | --- | 
| currentoffsets | N/A | The consumer's current read offset, for each partition. A particular partition's metric can be specified by topic name and partition id. | Application (for Topic), Parallelism (for PartitionId) |  | 
| commitsFailed | N/A | The total number of offset commit failures to Kafka, if offset committing and checkpointing are enabled.  | Application, Operator, Task, Parallelism | Committing offsets back to Kafka is only a means to expose consumer progress, so a commit failure does not affect the integrity of Flink's checkpointed partition offsets. | 
| commitsSucceeded | N/A | The total number of successful offset commits to Kafka, if offset committing and checkpointing are enabled.  | Application, Operator, Task, Parallelism |  | 
| committedoffsets | N/A | The last successfully committed offsets to Kafka, for each partition. A particular partition's metric can be specified by topic name and partition id. | Application (for Topic), Parallelism (for PartitionId) |  | 
| records\_lag\_max | Count | The maximum lag in terms of number of records for any partition in this window | Application, Operator, Task, Parallelism |  | 
| bytes\_consumed\_rate | Bytes | The average number of bytes consumed per second for a topic | Application, Operator, Task, Parallelism |  | 

## Apache Zeppelin metrics
<a name="metrics-dimensions-zeppelin"></a>

For Studio notebooks, AWS emits the following metrics at the application level: `KPUs`, `cpuUtilization`, `heapMemoryUtilization`, `oldGenerationGCTime`, `oldGenerationGCCount`, and `threadCount`. In addition, it emits the metrics shown in the following table, also at the application level.



| Metric | Unit | Description | Prometheus name | 
| --- | --- | --- | --- | 
| zeppelinCpuUtilization | Percentage | Overall percentage of CPU utilization in the Apache Zeppelin server. | process\_cpu\_usage | 
| zeppelinHeapMemoryUtilization | Percentage | Overall percentage of heap memory utilization for the Apache Zeppelin server. | jvm\_memory\_used\_bytes | 
| zeppelinThreadCount | Count | The total number of live threads used by the Apache Zeppelin server. | jvm\_threads\_live\_threads | 
| zeppelinWaitingJobs | Count | The number of queued Apache Zeppelin jobs waiting for a thread. | jetty\_threads\_jobs | 
| zeppelinServerUptime | Seconds | The total time that the server has been up and running. | process\_uptime\_seconds | 