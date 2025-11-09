# Aurora and RDS database metrics

Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora and RDS databases.

RDS DB instances
Compute Optimizer analyzes the following CloudWatch metrics of your Amazon RDS DB instances.

| Metric                      | Description                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CPUUtilization`            | The percentage of allocated compute units that are in use on the DB instance.<br>This metric identifies the processing power that's required to run an application on<br>an instance. |
| `DatabaseConnections`       | The number of client sessions that are connected to the DB instance.                                                                                                                  |
| `NetworkReceiveThroughput`  | The incoming (receive) network traffic on the DB instance, including both customer<br>database traffic and Amazon RDS traffic used for monitoring and replication.                    |
| `NetworkTransmitThroughput` | The outgoing (transmit) network traffic on the DB instance, including both customer<br>database traffic and Amazon RDS traffic used for monitoring and replication.                   |
| `ReadIOPS`                  | The average number of disk read I/O operations per second.                                                                                                                            |
| `WriteIOPS`                 | The average number of disk write I/O operations per second.                                                                                                                           |
| `ReadThroughput`            | The average number of bytes read from disk per second.                                                                                                                                |
| `WriteThroughput`           | The average number of bytes written to disk per second.                                                                                                                               |
| `EBSIOBalance%`             | The percentage of I/O credits remaining in the burst bucket of your<br>RDS database. This metric is available for basic monitoring only.                                              |
| `EBSByteBalance%`           | The percentage of throughput credits remaining in the burst bucket of<br>your RDS database. This metric is available for basic monitoring only.                                       |
| `FreeStorageSpace`          | The amount of available storage space.                                                                                                                                                |

If you enabled Amazon RDS Performance Insights, Compute Optimizer also analyzes the
following metrics of your Amazon RDS DB instance. To enable Performance Insights for your DB instances, see
[Turning Performance Insights on and off for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md")
in the _Amazon Relational Database Service User Guide_.

###### Note

If Performance Insights isn’t enabled, Compute Optimizer doesn’t provide recommendations to
reduce vCPU capacity.

| Metric        | Description                                                                                                                                                                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DBLoad`      | The level of session activity in your database. For more information, see<br>[Database load](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.md") in the _Amazon Relational Database Service User Guide_. |
| `os.swap.in`  | The amount of memory, in kilobytes, swapped in from disk.                                                                                                                                                                                                                                   |
| `os.swap.out` | The amount of memory, in kilobytes, swapped out to disk.                                                                                                                                                                                                                                    |

For more information about Amazon RDS metrics, see [Metrics reference for Amazon RDS](../../../AmazonRDS/latest/UserGuide/metrics-reference.md "../../../AmazonRDS/latest/UserGuide/metrics-reference.md") in the _Amazon Relational Database Service User Guide_.

Aurora DB instances
Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora DB instances.

| Metric                            | Description                                                                                                                                                                                                                             |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CPUUtilization`                  | The percentage of CPU used by an Aurora DB instance.                                                                                                                                                                                    |
| `DatabaseConnections`             | The number of client network connections to the database instance.                                                                                                                                                                      |
| `NetworkReceiveThroughput`        | The amount of network throughput received from clients by each instance in the Aurora DB cluster.<br>This throughput doesn't include network traffic between instances in the Aurora DB cluster and the<br>cluster volume.              |
| `NetworkTransmitThroughput`       | The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This<br>throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.                              |
| `StorageNetworkReadThroughput`    | The amount of network throughput received from the Aurora storage subsystem by each instance in the DB cluster.                                                                                                                         |
| `StorageNetworkWriteThroughput`   | The amount of network throughput sent to the Aurora storage subsystem by each instance in the Aurora DB cluster.                                                                                                                        |
| `AuroraMemoryHealthState`         | Indicates the memory health state. A value of `0` equals `NORMAL`. A value of `10` equals<br>`RESERVED`, which means that the server is approaching a critical level of memory usage.<br>NoteThis metric applies to Aurora MySQL only.  |
| `AuroraMemoryNumDeclinedSqlTotal` | The total number of queries declined as part of out-of-memory (OOM) avoidance.<br>NoteThis metric applies to Aurora MySQL only.                                                                                                         |
| `AuroraMemoryNumKillConnTotal`    | The total number of connections closed as part of OOM avoidance.<br>NoteThis metric applies to Aurora MySQL only.                                                                                                                       |
| `AuroraMemoryNumKillQueryTotal`   | The total number of queries ended as part of OOM avoidance.<br>NoteThis metric applies to Aurora MySQL only.                                                                                                                            |
| `ReadIOPSEphemeralStorage`        | The average number of disk read I/O operations to Ephemeral NVMe storage.<br>NoteThis metric applies to instances that support locally attached non-volatile<br>memory express (NVMe) storage.                                          |
| `WriteIOPSEphemeralStorage`       | The average number of disk write I/O operations to Ephemeral NVMe storage.<br>NoteThis metric applies to instances that support locally attached non-volatile<br>memory express (NVMe) storage.                                         |
| `ReadIOPS`                        | The average number of disk I/O operations per second but the reports read and write separately, in 1-minute intervals.                                                                                                                  |
| `WriteIOPS`                       | The number of Aurora storage write records generated per second. This is more or less the number of log records<br>generated by the database. These do not correspond to 8K page writes, and do not correspond to network packets sent. |

For more information, see [Amazon CloudWatch metrics for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.md") in the _Amazon Aurora User Guide_.

If you enabled Performance Insights for Aurora, Compute Optimizer also analyzes the
following metrics of your Aurora DB instances. To enable Performance Insights for Aurora, see
[Turning Performance Insights on and off for Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.md")
in the _Amazon Aurora User Guide_.

| Metric                           | Description                                                                                                                                                                              |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DBLoad`                         | The number of active sessions for the database. Typically, you want the data for the average number of active sessions.<br>In Performance Insights, this data is queried as db.load.avg. |
| `os.memory.outOfMemoryKillCount` | The number of OOM kills that happened over the last collection interval.                                                                                                                 |

For more information about Aurora metrics, see [Metrics reference for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/metrics-reference.md "../../../AmazonRDS/latest/AuroraUserGuide/metrics-reference.md") in the _Amazon Aurora User Guide_.

Aurora DB clusters
Compute Optimizer analyzes the following CloudWatch metrics of your Amazon Aurora DB clusters.

| Metric            | Description                                                                                    |
| ----------------- | ---------------------------------------------------------------------------------------------- |
| `VolumeReadIOPs`  | The number of billed read I/O operations from a cluster volume within a 5-minute interval.     |
| `VolumeWriteIOPs` | The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals. |

###### Note

Compute Optimizer analyzes these metrics to estimate the I/O cost variability over the lookback period. The Aurora DB cluster storage
recommendations are based on analyzing instance costs, storage costs, and I/O costs.
