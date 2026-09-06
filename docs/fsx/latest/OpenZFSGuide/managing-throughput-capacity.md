

# Modifying throughput capacity
<a name="managing-throughput-capacity"></a>

 Every FSx for OpenZFS file system has a throughput capacity that is configured when you create the file system. You can modify your file system's throughput capacity at any time, as needed. Throughput capacity is one factor that determines the speed at which the file server hosting the file system can serve file data. Higher levels of throughput capacity also come with higher levels of I/O operations per second (IOPS) and more memory for caching of data on the file server. For more information, see [Performance for Amazon FSx for OpenZFS](performance.md). 

 When you modify your file system's throughput capacity, behind the scenes, Amazon FSx switches out the file system's file server. For Single-AZ (HA) and Multi-AZ (HA) file systems, it results in an automatic failover and failback while Amazon FSx switches out the preferred and secondary file servers. Single-AZ (non-HA) file systems will be unavailable for a few minutes during throughput capacity scaling. You are billed for the new amount of throughput capacity once it is available to your file system.

 For all FSx for OpenZFS file systems, you can't request a throughput capacity update if there is an ongoing SSD storage capacity or provisioned SSD IOPS update. You must wait until the SSD storage capacity or provisioned SSD IOPS update has completed before requesting a throughput capacity update. For Multi-AZ and Intelligent-Tiering file systems, you must wait a minimum of six hours between requests to update the throughput capacity, SSD storage capacity, or provisioned SSD IOPS. For more information on SSD storage and provisioned IOPS updates, see [Modifying provisioned SSD storage capacity and IOPS](managing-storage-capacity.md).

File systems offer varying levels of throughput capacity, depending on your deployment type. The values of throughput capacity (in MBps) for all Single-AZ deployment types and Multi-AZ (HA) are as follows:
+ **Single-AZ 2 (non-HA and HA) and Multi-AZ (HA)** – 160, 320, 640, 1280, 2560, 3840, 5120, 7680, 10240
+ **Single-AZ 1 (HA)** – 128, 256, 512, 1024, 2048, 3072, 4096
+ **Single-AZ 1 (non-HA)** – 64, 128, 256, 512, 1024, 2048, 3072, 4096

**Topics**
+ [When to modify throughput capacity](#when-to-modify-throughput-capacity)
+ [Modifying throughput capacity](#increase-throughput-capacity)

## When to modify throughput capacity
<a name="when-to-modify-throughput-capacity"></a>

Amazon FSx integrates with Amazon CloudWatch, enabling you to monitor your file system's ongoing throughput usage levels. The performance (throughput and IOPS) that you can drive through your file system depends on your specific workload’s characteristics, in addition to your file system’s throughput capacity, storage capacity, and storage type. You can use CloudWatch metrics to determine which of these dimensions to change to improve performance. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md).

## Modifying throughput capacity
<a name="increase-throughput-capacity"></a>

You can modify a file system's throughput capacity using the Amazon FSx console, the AWS Command Line Interface (AWS CLI), or the Amazon FSx API.

### To modify a file system's throughput capacity (console)
<a name="increase-throughput-console"></a>

1. Open the Amazon FSx console at [https://console.aws.amazon.com/fsx/](https://console.aws.amazon.com/fsx/).

1. Navigate to **File systems**, and choose the FSx for OpenZFS file system that you want to increase the throughput capacity for.

1. For **Actions**, choose **Update throughput capacity**. Or, in the **Summary** panel, choose **Update** next to the file system's **Throughput capacity**.

   The **Update throughput capacity** window appears.

1. Choose the new value for **Desired throughput capacity** from the list.

1. Choose **Update** to initiate the throughput capacity update.
**Note**  
Your file system may experience a very brief period of unavailability during the update.

### To modify a file system's throughput capacity (CLI)
<a name="increase-throughput-cli"></a>
+ To modify a file system's throughput capacity, use the [update-file-system](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-file-system.html) CLI command (or the equivalent [UpdateFileSystem](https://docs.aws.amazon.com/fsx/latest/APIReference/API_UpdateFileSystem.html) API operation), as shown in the following example.

  ```
  aws fsx update-file-system \
      --file-system-id fs-0123456789abcdef0 \
      --open-zfs-configuration '{"ThroughputCapacity":512}'
  ```