

# Monitoring in the Amazon FSx console
<a name="monitor-throughput-cloudwatch"></a>

The CloudWatch metrics reported by Amazon FSx provide valuable information about your FSx for ONTAP file systems and volumes. 

**Topics**
+ [Monitoring file system metrics in the Amazon FSx console](#fsxn-howtomonitor-fs)
+ [Monitoring volume metrics in the Amazon FSx console](#fsxn-howtomonitor-vol)
+ [Performance warnings and recommendations](performance-insights-FSxN.md)
+ [Creating Amazon CloudWatch alarms to monitor Amazon FSx](creating_alarms.md)

## Monitoring file system metrics in the Amazon FSx console
<a name="fsxn-howtomonitor-fs"></a>

You can use the **Monitoring & performance** panel on your file system's dashboard in the Amazon FSx console to view the metrics that are described in the following table. For more information, see [Accessing CloudWatch metrics](accessingmetrics.md). 



- **Summary**
  - **How do I...:** ...determine the amount of available storage capacity on my file system? / **Chart:** Available primary storage capacity (bytes) / **Relevant metrics:** `StorageCapacity` {`SSD`} - `StorageUsed` {`SSD`}
  - **How do I...:** ...determine my file system's total client throughput? / **Chart:** Total client throughput (bytes/sec) / **Relevant metrics:** SUM(`DataReadBytes` \+ `DataWriteBytes`)/PERIOD (in seconds)
  - **How do I...:** ...determine my file system's total client IOPS? / **Chart:** Total client IOPS (operations/sec) / **Relevant metrics:** SUM(`DataReadOperations` \+ `DataWriteOperations` \+ `MetadataOperations`)/PERIOD (in seconds)
  - **How do I...:** ...determine the average latency for the read, write, and metadata operations of my file system?  / **Chart:** Average latency (ms/operation) / **Relevant metrics:** Average read latency: `DataReadOperationTime` \* 1000/`DataReadOperations` <br />Average write latency: `DataWriteOperationTime` \* 1000/`DataWriteOperations` <br />Average metadata latency: `MetadataOperationTime` \* 1000/`MetadataOperations`
  - **How do I...:** ...determine the distribution of used and free storage capacity on my file system?  / **Chart:** Storage distribution / **Relevant metrics:** Primary tier available: `StorageCapacity` {`SSD`} - `StorageUsed` {`SSD`}<br />Primary tier used: `StorageUsed` {`SSD`}<br />Capacity pool used: `StorageUsed` {`StandardCapacityPool`}
  - **How do I...:** ...determine the savings from storage efficiencies (compression, deduplication, and compaction)? / **Chart:** Storage efficiency savings / **Relevant metrics:** `StorageEfficiencySavings`

- **Storage**
  - **How do I...:** ...determine how much primary storage is available? / **Chart:** Available primary storage capacity (bytes) / **Relevant metrics:** `StorageCapacity` {`SSD`} - `StorageUsed` {`SSD`}
  - **How do I...:** ...determine the percent of used primary storage for my file system? / **Chart:** Primary storage capacity utilization (percent) / **Relevant metrics:** `StorageUsed` {`SSD`} \* 100/`StorageCapacity` {`SSD`}

- **File server performance**
  - **How do I...:** ...determine if my file system is approaching its network throughput limit? / **Chart:** Network throughput – utilization (percent) / **Relevant metrics:** `NetworkThroughputUtilization`
  - **How do I...:** ...determine if my file system is approaching its disk throughput limit? / **Chart:** Disk throughput – utilization (percent) / **Relevant metrics:** `FileServerDiskThroughputUtilization`
  - **How do I...:** ...determine if my file system has exhausted its allowed burst credits for disk throughput? / **Chart:** Disk throughput – burst balance (percent) / **Relevant metrics:** `FileServerDiskThroughputBalance`
  - **How do I...:** ...determine if my file system is approaching its file servers' SSD IOPS limit? / **Chart:** Disk IOPS – utilization (percent) / **Relevant metrics:** `FileServerDiskIopsUtilization`
  - **How do I...:** ...determine if my file system has exhausted its file servers' allowed burst credits for disk SSD IOPS? / **Chart:** Disk IOPS – burst balance (percent) / **Relevant metrics:** `FileServerDiskIopsBalance`
  - **How do I...:** ...determine the average utilization of the file system's CPU? / **Chart:** CPU utilization (percent) / **Relevant metrics:** `CPUUtilization`
  - **How do I...:** ...determine if my workload is making efficient use of my file system's RAM and NVMe read caches? / **Chart:** Cache hit ratio (percent) / **Relevant metrics:** `FileServerCacheHitRatio`

- **Disk performance**
  - **How do I...:** ...determine if my file system is approaching its currently provisioned SSD IOPS capacity?
  - **Chart:** Disk IOPS – utilization (SSD) (percent)
  - **Relevant metrics:** `DiskIopsUtilization`



**Note**  
We recommend that you maintain an average throughput capacity utilization of any performance-related dimensions such as network utilization, CPU utilization, and SSD IOPS utilization to under 50%. This ensures that you have enough spare throughput capacity for unexpected spikes in your workload, as well as for any background storage operations (such as storage synchronization, data tiering, or backups).

## Monitoring volume metrics in the Amazon FSx console
<a name="fsxn-howtomonitor-vol"></a>

You can view the **Monitoring** panel on your volume's dashboard in the Amazon FSx console to see additional performance metrics. For more information, see [Accessing CloudWatch metrics](accessingmetrics.md). 



- ****
  - **How do I...:** ...determine my volume's available storage capacity?  / **Chart:** Available storage capacity / **Relevant metrics:** `StorageCapacity`
  - **How do I...:** ...determine my volume's total client throughput?  / **Chart:** Total client throughput (bytes/sec) / **Relevant metrics:** SUM(`DataReadBytes` \+ `DataWriteBytes`)/PERIOD (in seconds)
  - **How do I...:** ...determine my volume's total client IOPS? / **Chart:** Total client IOPS (operations/sec) / **Relevant metrics:** SUM(`DataReadOperations` \+ `DataWriteOperations` \+ `MetadataOperations`)/PERIOD (in seconds)
  - **How do I...:** ...determine how many read and write operations are coming from or going to the capacity pool tier? / **Chart:** Capacity Pool IOPS (operations/sec) / **Relevant metrics:** Read operations: `CapacityPoolReadOperations` <br />Write operations: `CapacityPoolWriteOperations`
  - **How do I...:** ...determine the average latency for the read, write, and metadata operations of my volume?  / **Chart:** Average latency (ms/operation) / **Relevant metrics:** Average read latency: `DataReadOperationTime` \* 1000/`DataReadOperations` <br />Average write latency: `DataWriteOperationTime` \* 1000/`DataWriteOperations` <br />Average metadata latency: `MetadataOperationTime` \* 1000/`MetadataOperations`
  - **How do I...:** ...determine the amount of files or inodes that are available on my volume? / **Chart:** Available files (inodes) / **Relevant metrics:** `FilesCapacity` - `FilesUsed`
  - **How do I...:** ...determine the distribution of used and free storage capacity on my volume?  / **Chart:** Storage distribution / **Relevant metrics:** `StorageCapacity` - `StorageUsed`

