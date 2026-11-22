

# Viewing Aurora and RDS database recommendations

Compute Optimizer gives recommendations for DB instances, RDS DB instance storage, and Aurora DB cluster storage. It covers RDS for MySQL, RDS for PostgreSQL, and Amazon Aurora databases. You can see these recommendations on two pages in the Compute Optimizer console: the **Recommendations for Aurora and RDS databases** page and the **Aurora and RDS databases details** page. Each page has two tabs: **Instance** and **Storage**.

To learn which metrics Compute Optimizer uses for these databases, see [Aurora and RDS database metrics](rds-metrics-analyzed.md).
+ **Recommendations for Aurora and RDS databases** page

  **Instance**

  This tab lists each of your current Aurora and RDS DB instances. For each one, it shows the finding, the finding reasons, the current instance type, the estimated savings, and the savings opportunity. Next to each instance, Compute Optimizer shows its top recommendation. The recommendation includes the instance type, the On-Demand price, and the price change from your current instance. Use this tab to compare each instance with its top recommendation. This can help you decide whether to size up or size down.

  **Storage**

  This tab lists each of your current RDS instance storage volumes and Aurora DB cluster storage setups. For each one, it shows the finding, the current storage type, and the current price. Next to each volume or cluster, Compute Optimizer shows its top recommendation. For RDS DB instance storage, the recommendation includes the volume type, the IOPS, the price, and the price change from your current volume. For Aurora DB clusters, it includes the storage type, the estimated cluster costs for instance, storage, and I/O, and the potential savings. Use this tab to compare each storage setup with its top recommendation. This can help you decide whether to change your storage type.

  To learn how to view these recommendations, see [Accessing Aurora and RDS database recommendations and details](rds-view-recommendations.md).
+ **Aurora and RDS database details** page

  **Instance**

  This tab shows the recommendations for one RDS DB instance or Aurora DB instance. For each recommendation, it lists the specs, such as the performance risk, the price change, and the On-Demand price.

  **Storage**

  This tab shows the recommendation for one RDS DB instance storage or Aurora DB cluster storage. For RDS DB instance storage, it lists the specs for each recommendation, such as the allocated storage, the provisioned IOPS, the throughput, and the storage price change. For Aurora DB clusters, it shows storage type recommendations. It breaks the estimated costs down by instance, storage, and I/O. It also shows how much the I/O cost can vary when enhanced infrastructure metrics is turned on.

  Both details tabs show utilization graphs. Use them to compare your current instance or storage with the projected use for each recommendation. The graphs help you see the impact of a recommendation.

  To learn how to view these details, see [Accessing Aurora and RDS database details page](rds-view-recommendations.md#rds-viewing-details).

The recommendations are refreshed daily and they can take up to 12 hours to generate. Keep in mind that Compute Optimizer requires at least 30 hours of Amazon CloudWatch metrics to generate recommendations for Amazon RDS DB instances. For more information, see [Resource requirements](requirements.md).

**Topics**
+ [Finding classifications](#rds-recommendations-findings)
+ [Finding reasons](#rds-finding-reasons)
+ [AWS Graviton-based instance recommendations](#rds-graviton-recommendations)
+ [Estimated monthly savings and savings opportunity](#rds-savings-calculation)
+ [Performance risk](#rds-performance-risk)
+ [Comparison graphs](#rds-utilization-graphs)
+ [Accessing Aurora and RDS database recommendations and details](rds-view-recommendations.md)

## Finding classifications
<a name="rds-recommendations-findings"></a>

The **Finding** column on the **Recommendations for Aurora and RDS databases** page provides a summary of how your Amazon Aurora and RDS DB instances, RDS DB instances storage, and Aurora DB clusters performed during the lookback period.

------
#### [ Aurora and RDS DB instances ]

The following findings classifications apply to DB instances.


**DB instance finding classifications**  

| Classification | Description | 
| --- | --- | 
| Under-provisioned | When Compute Optimizer detects that there isn't enough CPU, memory, network bandwidth, EBS IOPS, or EBS throughput, an RDS DB instance is considered under-provisioned. Compute Optimizer displays finding reasons, such as **CPU under-provisioned**, **Memory under-provisioned**, **EBS IOPS under-provisioned**, and **Network bandwidth under-provisioned**. An under-provisioned RDS DB instance might result in poor application performance. | 
| Over-provisioned | When Compute Optimizer detects that there is excessive CPU, EBS IOPS, network bandwidth, or EBS throughput, an RDS DB instance is considered over-provisioned. Compute Optimizer displays finding reasons, such as **CPU over-provisioned**, **EBS IOPS over-provisioned**, **Network bandwidth over-provisioned**, and **EBS throughput over-provisioned**. An over-provisioned RDS DB instance might result in additional infrastructure costs. | 
| Optimized | When the specifications of your RDS DB instance meet the performance requirements of your workload, the RDS DB instance is considered optimized. For optimized instances, Compute Optimizer might recommend a new generation DB instance class or that a new engine version is available. | 

------
#### [ RDS DB instance storage ]

The following findings classifications apply to RDS DB storage.


**Amazon RDS DB instance storage finding classifications**  

| Classification | Description | 
| --- | --- | 
| Under-provisioned | When Compute Optimizer detects that there isn't enough allocated storage or EBS throughput, an RDS storage volume is considered under-provisioned. Compute Optimizer displays a finding reason of **EBS volume allocated storage under-provisioned** or **EBS volume throughput under-provisioned**. An under-provisioned RDS DB instance storage volume might result in poor application performance. | 
| Over-provisioned | When Compute Optimizer detects that there is excessive IOPS or EBS throughput, an RDS DB instance storage volume is considered over-provisioned. Compute Optimizer displays a finding reason of **EBS volume IOPS over-provisioned** or **EBS volume throughput over-provisioned**. An over-provisioned DB instance storage volume might result in additional infrastructure costs. | 
| Optimized | When the specifications of your RDS DB instance storage volume meet the performance requirements of your workload, the storage is considered optimized. For optimized DB instance storage, Compute Optimizer might recommend a new generation storage type. | 

For more information about under and over-provisioned RDS DB instances, see [Finding reasons](#rds-finding-reasons) in the [Viewing Aurora and RDS database recommendations](view-rds-recommendations.md) topic.

------
#### [ Aurora DB clusters ]

The following findings classifications apply to Aurora DB clusters.


**Aurora DB cluster finding classifications**  

| Classification | Description | 
| --- | --- | 
| Optimized | Compute Optimizer found the configurations of your Aurora DB cluster storage to be optimized from a cost perspective. | 
| Not optimized | Compute Optimizer found potential cost savings if you switch your Aurora DB cluster from Aurora Standard storage to Aurora I/O-Optimized storage. Compute Optimizer displays a finding reason of **DBClusterStorageSavingsAvailable** when Aurora I/O-Optimized is identified as the top option. | 

For more information about Amazon Aurora DB clusters, see [Amazon Aurora storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html) in the *Amazon Aurora User Guide for Aurora*.

------

## Finding reasons
<a name="rds-finding-reasons"></a>

The **Finding reasons** column on the **Recommendations for RDS DB instances** and **RDS DB instance details** pages shows the specifications of Compute Optimizer findings for Amazon Aurora and RDS DB instances, RDS DB instances storage, and Aurora DB clusters.

------
#### [ Aurora and RDS DB instances ]

The following finding reasons apply to RDS DB instances:


**Amazon RDS DB instance finding reasons**  

| Finding reason | Description | 
| --- | --- | 
| CPU over-provisioned | The DB instance’s CPU configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current instance during the lookback period. | 
| CPU under-provisioned | The DB instance’s CPU configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better CPU performance. This is identified by analyzing the `CPUUtilization` metric of the current instance during the lookback period. | 
| Memory under-provisioned | The DB instance’s memory configuration doesn't meet the performance requirements of your workload and there isn't an alternative instance type that provides better memory performance.<br />For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `os.swap.in` and `os.swap.out` metrics of the current instance if Amazon RDS Performance Insights is enabled. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*.<br />For Aurora DB instances, this is identified by analyzing the `os.memory.outOfMemoryKillCount` metric of the current instance if Amazon RDS Performance Insights is enabled. For Aurora MySQL DB instances, Compute Optimizer also analyzes Aurora memory health state metrics. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*. | 
| EBS throughput over-provisioned | The DB instance’s EBS throughput configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes attached to the current instance during the lookback period. | 
| EBS throughput under-provisioned | The DB instance’s EBS throughput configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metric of EBS volumes that are attached to the current instance during the lookback period. | 
| EBS IOPS over-provisioned | The DB instance’s EBS IOPS configuration can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS IOPS under-provisioned | The DB instance’s EBS IOPS configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better EBS throughput performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| Network bandwidth over-provisioned | The DB instance’s network bandwidth configuration can be sized down while still meeting the performance requirements of your workload. For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `NetworkIn` and `NetworkOut `metrics of the current instance during the lookback period. | 
| Network bandwidth under-provisioned | The DB instance’s network bandwidth configuration doesn't meet the performance requirements of your workload and there is an alternative instance type that provides better network bandwidth performance.<br />For RDS MySQL and RDS PostgreSQL DB instances, this is identified by analyzing the `NetworkIn` and `NetworkOut` metrics of the current instance during the lookback period. <br />For Aurora DB instances, this is identified by analyzing the `NetworkThroughput` and `StorageNetworkThroughput` metrics of the current instance during the lookback period. | 
| Instance storage read IOPS under-provisioned | The DB instance's instance storage read IOPS limit doesn't meet the performance requirement of your workload and there is an alternative instance type that provides better performance. For Aurora DB instances, this is identified by analyzing the `ReadIOPSEphemeralStorage` metric during the lookback period. | 
| Instance storage write IOPS under-provisioned | The DB instance's instance storage write IOPS limit doesn't meet the performance requirement of your workload and there is an alternative instance type that provides better performance. For Aurora DB instances, this is identified by analyzing the `WriteIOPSEphemeralStorage` metric during the lookback period. | 
| DB cluster writer under-provisioned | This indicates that Compute Optimizer has synchornized the recommendation for this Aurora DB instance read replica with the DB cluster's writer because it has a promotion tier < or = to 1. Compute Optimizer does this to help you maintain your failover capacity. | 
| New generation DB instance class available | If the current DB instance is a previous generation instance type, Compute Optimizer generates this finding reason to indicate that there is a new generation DB instance type available. We encourage you to use current generation instance types to get the best performance. | 
| New engine version available | If the current engine version is deprecated, Compute Optimizer generates this finding reason to indicate that there is a new engine version available.  | 

------
#### [ RDS DB instance storage ]

The following finding reasons apply to RDS DB instance storage.


**Amazon RDS DB instance storage finding reasons**  

| Finding reason | Description | 
| --- | --- | 
| EBS volume allocated storage under-provisioned | The amount EBS volume allocated storage space attached to the DB instance doesn't meet the performance requirements of your workload and there is an alternative volume type that provides better allocated storage performance. This is identified by analyzing the `VolumeReadOps` and `VolumeWriteOps` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS volume IOPS over-provisioned | The EBS volume IOPS configuration attached the DB instance can be sized down and also meet the performance requirements of your workload. This is identified by analyzing the `VolumeReadBytes` and `VolumeWriteBytes` metrics of EBS volumes attached to the current instance during the lookback period. | 
| EBS volume throughput under-provisioned | The size of the EBS volume throughput attached the DB instance doesn't meet the performance requirements of your workload and there is an alternative volume type that provides better volume throughput performance. | 
| EBS volume throughput over-provisioned | The EBS volume throughput attached the DB instance can be sized down and also meet the performance requirements of your workload.  | 
| New generation storage type available | If the current DB instance storage is a previous generation storage type, Compute Optimizer generates this finding reason to indicate that there is a new generation storage type available. We encourage you to use current generation storage types to get the best performance.  | 

------
#### [ Aurora DB clusters ]

The following finding reasons apply to Aurora DB clusters.


**Aurora DB cluster finding reasons**  

| Classification | Description | 
| --- | --- | 
| DBClusterStorageSavingsAvailable | Potential cost savings were found by switching your Aurora DB cluster from Aurora Standard storage to Aurora I/O-Optimized storage. Your cluster's I/O usage pattern suggests that the predictable pricing model of Aurora I/O-Optimized would be more cost-effective than the variable I/O costs of Aurora Standard. This finding reason appears when I/O Optimized is identified as the top recommended option for your cluster. | 
| DBClusterStorageOptionAvailable | Aurora I/O-Optimized was found to be a viable alternative storage option for your Aurora DB cluster. While your current storage configuration is considered optimized from a cost perspective, switching to Aurora I/O-Optimized could provide benefits such as more predictable monthly costs and simplified budgeting by eliminating variable I/O charges. This finding reason appears when I/O-Optimized is displayed as the second recommended option for your cluster. | 

------

## AWS Graviton-based instance recommendations
<a name="rds-graviton-recommendations"></a>

When viewing Amazon RDS DB instance recommendations, you can view the price and performance impact of running your workload on AWS Graviton-based instances. To do so, choose **Graviton (aws-arm64)** in the **CPU architecture preference** dropdown. Otherwise, choose **Current** to view recommendations that are based on the same CPU vendor and architecture as the current RDS DB instance.

The **Current price**, **Recommended price**, **Price difference**, **Price difference (%)**, and **Estimated monthly savings** columns are updated to provide a price comparison between the current DB instance type and the instance type of the selected CPU architecture preference. For example, if you choose **Graviton (aws-arm64)**, prices are compared between the current DB instance type and the recommended Graviton-based instance type.

## Estimated monthly savings and savings opportunity
<a name="rds-savings-calculation"></a>

**Estimated monthly savings (after discounts)**

**Instance tab**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current DB instance or type to the recommended type under the Reserved Instances pricing models. To receive recommendations with Reserved Instances discounts, activate the savings estimation mode preference.

**Storage tab**

This column lists the approximate monthly cost savings that you experience by migrating your RDS DB instance storage volumes from the current specifications to the recommended specifications under specific discounts. For Aurora DB clusters, this represents the savings from changing between Aurora Standard and Aurora I/O-Optimized storage types, considering all cost components (instance, storage, and I/O costs). To receive recommendations with specific discounts, activate the savings estimation mode preference.

For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

**Note**  
If you don't activate the savings estimation mode preference, this column on both the Instance and Storage tabs display the default On-Demand pricing discount information.

**Estimated monthly savings (On-Demand)**

**Instance tab**

This column lists the approximate monthly cost savings that you experience by migrating your workloads from the current DB instance type to the recommended instance type under the On-Demand pricing model.

**Storage tab**

This column lists the approximate monthly cost savings that you experience by migrating your RDS DB instance storage volumes from the current specifications to the recommended specifications. For Aurora DB clusters, this includes the difference in total costs between your current storage type and the recommended storage type, considering instance, storage, and I/O cost components.

**Savings opportunity (%)**

This column lists the percentage difference between the price of the current instance and the price of the recommended DB instance type. If savings estimation mode is activated, Compute Optimizer analyzes the Reserved Instances pricing discounts to generate the savings opportunity percentage. If savings estimation mode isn’t activated, Compute Optimizer only uses On-Demand pricing information. For more information, see [Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode).

For Aurora DB cluster storage recommendations, this represents the percentage difference in total costs (instance, storage, and I/O) between the current and recommended storage types.

**Important**  
If you enable Cost Optimization Hub in AWS Cost Explorer, Compute Optimizer uses Cost Optimization Hub data, which includes your specific pricing discounts to generate your recommendations. If Cost Optimization Hub isn't enabled, Compute Optimizer uses Cost Explorer data and On-Demand pricing information to generate your recommendations. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [ Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the in the *AWS Cost Management User Guide*.

### Estimated monthly savings calculation
<a name="rds-estimated-monthly-savings-calculation"></a>

For each recommendation, Compute Optimizer calculate the cost to operate a new RDS DB instance or storage using the recommended specifications. Estimated monthly savings are calculated based on the number of running hours for the current instance or storage and the difference in rates between the current specifications and the recommended specifications. The estimated monthly savings for RDS DB instances and storage that are displayed on the Compute Optimizer dashboard is a sum of the estimated monthly savings for all over-provisioned findings in the account.

## Performance risk
<a name="rds-performance-risk"></a>

The performance risk columns on the **RDS DB instance details** page and the **RDS DB instance recommendations** page define the likelihood of the current and recommended instance type not meeting your workload requirements. Compute Optimizer calculates an individual performance risk score for each specification of the current and recommended instance. This includes specifications such as CPU, EBS throughput, and EBS IOPS. The performance risk of the current and recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.

The values range from very low, low, medium, high, and very high. A very low performance risk means that the instance type is predicted to always provide enough capability. The higher the performance risk means that you should validate whether the instance meets the performance requirements of your workload before migrating your resource. Decide whether to optimize for performance improvement, for cost reduction, or for a combination of these two. 

## Comparison graphs
<a name="rds-utilization-graphs"></a>

The **Amazon RDS database details** page displays utilization metric graphs for your current and recommended RDS DB instance and storage data for the lookback period. Compute Optimizer uses the maximum utilization point within each 5-minute time interval to generate RDS DB instance and storage recommendations.

You can change the graphs to display data for the last 24 hours, three days, one week, or two weeks. You can also change the statistic of the graphs between average and maximum.

The following comparison graphs are displayed on the **Aurora and RDS database details** page. For more information about these metrics, see [Aurora and RDS database metrics](rds-metrics-analyzed.md).

------
#### [ RDS DB instances ]

The following graphs are displayed for RDS DB instances:


**Amazon RDS DB instance comparison graphs**  

| Graph name | Description | 
| --- | --- | 
| CPU utilization | The percentage of allocated compute units that are in use on the DB instance. This metric identifies the processing power that's required to run an application on an instance. | 
| Database connections (count) | The number of client sessions that are connected to the DB instance. | 
| Network receive throughput (MiB/second) | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
| Network transmit throughput (MiB/second) | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS traffic used for monitoring and replication. | 
| EBS read operations (per second) | The average number of disk read I/O operations per second. | 
| EBS write operations (per second) | The average number of disk write I/O operations per second. | 
| EBS read throughput (MiB/second) | The average number of bytes read from disk per second. | 
| EBS write throughput (MiB/second) | The average number of bytes written to disk per second. | 
| EBS IO balance (percent) | The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
| EBS Byte Balance (percent) | The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available for basic monitoring only. | 
| Free storage space | The amount of available storage space. | 
| DB Load | The level of session activity in your database. For more information, see [ Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html) in the *Amazon Relational Database Service User Guide*. | 
| Swap in (KB) | The amount of memory, in kilobytes, swapped in from disk. | 
| Swap out (KB) | The amount of memory, in kilobytes, swapped out to disk. | 

**Note**  
The **DB Load**, **Swap in (KB)**, and **Swap out (KB)** metrics are only available if you enabled Amazon RDS Performance Insights. To enable Performance Insights for your DB instances, see [ Turning Performance Insights on and off for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Relational Database Service User Guide*.

------
#### [ Aurora DB instances ]

The following graphs are displayed for Aurora DB instances:


**Aurora DB instance comparison graphs**  

| Graph name | Description | 
| --- | --- | 
| CPU utilization | The percentage of CPU used by an Aurora DB instance. | 
| Memory utilization | The percentage of memory allocated by applications and the operating system as used. | 
| Database connections (count) | The number of client sessions that are connected to the DB instance. | 
| Network receive throughput (MiB/second) | The amount of network throughput received from clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the Aurora DB cluster and the cluster volume. | 
| Network transmit throughput (MiB/second) | The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | 
| Storage network read throughput (MiB/second) | The amount of network throughput received from the Aurora storage subsystem by each instance in the DB cluster. | 
| Storage network write throughput (MiB/second) | The amount of network throughput sent to the Aurora storage subsystem by each instance in the Aurora DB cluster. | 
| Aurora memory health state | Indicates the memory health state. A value of `0` equals `NORMAL`. A value of `10` equals `RESERVED`, which means that the server is approaching a critical level of memory usage.  This metric applies to Aurora MySQL only.  | 
| Aurora memory number of declined SQL queries | The total number of queries declined as part of out-of-memory (OOM) avoidance. This metric applies to Aurora MySQL only.  | 
| Aurora memory number of connections closed | The total number of connections closed as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
| Aurora memory number of queries killed | The total number of queries ended as part of OOM avoidance. This metric applies to Aurora MySQL only.  | 
| Buffer cache hit ratio | The percentage of requests that are served by the buffer cache. This graph is shown when an Optimized Reads DB instance class type is recommended an as option to help you evaluate whether it is the right fit for your workload. | 
| Read IOPS ephermal storage | The average number of disk read operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
| Write IOPS ephermal storage | The average number of disk write operations to Ephemeral NVMe storage. This metric applies to instances that support locally attached non-volatile memory express (NVMe) storage.  | 
| Read IOPS | The average number of disk read operations per second.  | 
| Write IOPS | The number of Aurora storage write records generated per second. This is more or less the number of log records generated by the database. These do not correspond to 8K page writes, and do not correspond to network packets sent. | 
| DB Load | The number of active sessions for the database. Typically, you want the data for the average number of active sessions. In Performance Insights, this data is queried as db.load.avg. | 

For more information, see [ Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html) in the *Amazon Aurora User Guide*.

**Note**  
The **DB Load** graph is only available if you enabled Performance Insights for Aurora. To enable Performance Insights for Aurora, see [ Turning Performance Insights on and off for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html) in the *Amazon Aurora User Guide*.

------
#### [ Aurora DB clusters ]

The following graphs are displayed for Aurora DB clusters:


**Aurora DB cluster comparison graphs**  

| Graph name | Description | 
| --- | --- | 
| VolumeBytesUsed | The amount of storage used by your Aurora DB cluster. | 
| VolumeReadIOPs | The number of billed read I/O operations from a cluster volume within a 5-minute interval. | 
| VolumeWriteIOPs | The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals. | 

------