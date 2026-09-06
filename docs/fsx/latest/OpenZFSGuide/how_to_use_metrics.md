

# Using Amazon FSx for OpenZFS CloudWatch metrics
<a name="how_to_use_metrics"></a>

There are two primary architectural components of each Amazon FSx file system:
+ The **file server** that serves data to clients that access the file system.
+ The **storage volumes** that host the data in your file system.

FSx for OpenZFS reports metrics in CloudWatch that track performance and resource utilization for your file system's file server and storage volumes. The following diagram illustrates an Amazon FSx file system with its architectural components, and the performance and resource CloudWatch metrics that are available for monitoring. The key property for a set of metrics is the file system property that determines the capacity for those metrics. Adjusting that property modifies the file system's performance for that set of metrics.

![Diagram displaying the different types of FSx for OpenZFS Cloudwatch metrics.](http://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/images/file-server-metrics-FSxZ.png)


You can use the **Monitoring & performance** panel on your file system's dashboard in the Amazon FSx console to view the metrics that are described in the following table. For more information, see [Accessing CloudWatch metrics](accessingmetrics.md).



- **Summary**
  - **How do I...:** ...determine my file system's total throughput? / **Chart:** Total throughput / **Relevant metrics:** SUM(`DataReadBytes` \+ `DataWriteBytes`)/Period (in seconds)
  - **How do I...:** ...determine my file system's total IOPS? / **Chart:** Total IOPS / **Relevant metrics:** SUM(`DataReadOperations` \+ `DataWriteOperations` \+ `MetadataOperations`)/Period (in seconds)
  - **How do I...:** ...determine the number of connections that are established between clients and the file server? / **Chart:** Client connections / **Relevant metrics:** ClientConnections

- **Storage**
  - **How do I...:** ...determine how much primary storage is available? / **Chart:** Available primary storage capacity (bytes) / **Relevant metrics:** `StorageCapacity` {`SSD`} - `UsedStorageCapacity` {`SSD`}
  - **How do I...:** ...determine the percentage of used primary storage for my file system? / **Chart:** Primary storage capacity utilization (percent) / **Relevant metrics:** `StorageCapacity` {`SSD`} \* 100/`UsedStorageCapacity` {`SSD`}

- **File server performance**
  - **How do I...:** ...determine the network throughput for clients that access the file system as a percentage of the file system's provisioned throughput? / **Chart:** Network throughput utilization / **Relevant metrics:** NetworkThroughputUtilization
  - **How do I...:** ...determine the disk throughput between the file server and its storage volumes as a percentage of the provisioned limit, which is determined by throughput capacity? / **Chart:** Disk throughput utilization / **Relevant metrics:** FileServerDiskThroughputUtilization
  - **How do I...:** ...determine the percentage of available burst credits for disk throughput between the file server and its storage volumes? / **Chart:** Disk throughput burst balance / **Relevant metrics:** FileServerDiskThroughputBalance
  - **How do I...:** ...determine if the file system is approaching the file server’s maximum SSD IOPS capacity? Do I need to increase throughput on my file system? / **Chart:** Disk IOPS utilization / **Relevant metrics:** FileServerDiskIopsUtilization
  - **How do I...:** ...determine if the file system is approaching the file server’s maximum SSD IOPS capacity? Do I need to increase my file system' throughput capacity? / **Chart:** Disk IOPS burst balance / **Relevant metrics:** FileServerDiskIopsBalance
  - **How do I...:** ...determine the file server's CPU utilization percentage? / **Chart:** CPU utilization / **Relevant metrics:** CPUUtilization
  - **How do I...:** ...determine the file server's memory utilization percentage? / **Chart:** Memory utilization / **Relevant metrics:** MemoryUtilization
  - **How do I...:** ...determine my workload's usage of the file system's in-memory (ARC), NVMe (L2ARC), and Intelligent-Tiering SSD read caches? / **Chart:** Cache hit ratio  / **Relevant metrics:** FileServerCacheHitRatio

- **Disk performance**
  - **How do I...:** ....determine if the file system is approaching the file server’s current provisioned SSD IOPS capacity? Do I need to provision more IOPS for my file system? / **Chart:** Disk IOPS utilization (SSD) / **Relevant metrics:** DiskIopsUtilization
  - **How do I...:** ...determine if the file system is approaching the file server’s current provisioned SSD IOPS capacity? Do I need to provision more IOPS for my file system? / **Chart:** Compression ratio / **Relevant metrics:** (UsedStorageCapacity/CompressionRatio) - UsedStorageCapacity



**Note**  
We recommend that you provision throughput capacity so that the utilization of any performance-related dimension,—such as typical network, CPU, and memory utilization is less than 50%. This ensures that you have enough spare throughput capacity for unexpected spikes in your workload, as well as for background storage operations.