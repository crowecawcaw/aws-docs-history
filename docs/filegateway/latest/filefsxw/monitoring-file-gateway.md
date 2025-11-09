Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Monitoring your FSx File Gateway

You can monitor your FSx File Gateway and associated resources in AWS Storage Gateway by
using Amazon CloudWatch metrics and audit logs. You can also use CloudWatch Events to get notified when your file
operations are done.

###### Topics

- [Getting FSx File Gateway health logs
  with CloudWatch log groups](#cw-log-groups "#cw-log-groups")
- [Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics")
- [Understanding
  gateway metrics](#understanding-file-gateway-metrics "#understanding-file-gateway-metrics")
- [Understanding
  file system metrics](#monitoring-file-gateway-resources "#monitoring-file-gateway-resources")
- [Understanding FSx File Gateway audit
  logs](#audit-logs "#audit-logs")

## Getting FSx File Gateway health logs

with CloudWatch log groups

You can use Amazon CloudWatch Logs to get information about the health of your FSx File Gateway
and related resources. You can use the logs to monitor your gateway for errors that it
encounters. In addition, you can use Amazon CloudWatch subscription filters to automate
processing of the log information in real time. For more information, see [Real-time
Processing of Log Data with Subscriptions](../../../AmazonCloudWatch/latest/logs/Subscriptions.md "../../../AmazonCloudWatch/latest/logs/Subscriptions.md") in the _Amazon CloudWatch User Guide._

For example, you can configure a CloudWatch log group to monitor your
gateway and get notified when your FSx File Gateway fails to upload files to an Amazon FSx file
system. You can configure the group either when you are activating the gateway or after
your gateway is activated and up and running. For information about how to configure a
CloudWatch log group when activating a gateway, see [Configure your Amazon FSx File Gateway](create-gateway-file.md#configure-gateway-fsx-file "create-gateway-file.md#configure-gateway-fsx-file"). For general information about CloudWatch log
groups, see [Working
with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the _Amazon CloudWatch User Guide._

For information about how to troubleshoot the errors that may be reported by FSx File Gateway, see [Troubleshooting: File Gateway
issues](troubleshooting-file-gateway-issues.md "troubleshooting-file-gateway-issues.md").

### Configuring a CloudWatch log group after your gateway is

activated

The following procedure shows you how to configure a CloudWatch Log Group after your
gateway is activated.

###### To configure a CloudWatch log group to work with your FSx File Gateway

1. Sign in to the AWS Management Console and open the Storage Gateway console at
   [https://console.aws.amazon.com/storagegateway/home](https://console.aws.amazon.com/storagegateway/ "https://console.aws.amazon.com/storagegateway/").
2. In the navigation pane, choose **Gateways**, and then
   choose the gateway that you want to configure the CloudWatch log group for.
3. For **Actions**, choose **Edit gateway
   information**.
4. For **Choose how to set up log group**, choose one of the
   following:
   - **Create a new log group** to create a new CloudWatch
     log group.
   - **Use an existing log group** to use a CloudWatch log
     group that already exists.

   Choose a log group from the **Existing log group
   list**.
   - **Deactivate logging** if you don't want to
     monitor your gateway using CloudWatch log groups.

5. Choose **Save changes**.
6. To see the health logs for your gateway, do the following:
   1. In the navigation pane, choose **Gateways**, and
      then choose the gateway that you configured the CloudWatch log group
      for.
   2. Choose the **Details** tab, and under
      **Health logs**, choose **CloudWatch
      Logs**. The **Log group details** page
      opens in the CloudWatch console.

## Using Amazon CloudWatch metrics

You can get monitoring data for your FSx File Gateway by using either
the AWS Management Console or the CloudWatch API. The console displays a series of graphs based on the raw
data from the CloudWatch API. The CloudWatch API can also be used through one of the [AWS SDKs](https://aws.amazon.com/tools "https://aws.amazon.com/tools") or [Amazon CloudWatch API](https://aws.amazon.com/cloudwatch "https://aws.amazon.com/cloudwatch") tools. Depending on your needs, you might
prefer to use either the graphs displayed in the console or retrieved from the
API.

Regardless of which method you use to work with metrics, you must specify the
following information:

- The metric dimension to work with. A _dimension_ is a
  name-value pair that helps you to uniquely identify a metric. The dimensions for
  Storage Gateway are `GatewayId` and `GatewayName`. In the
  CloudWatch console, you can use the `Gateway Metrics` view to select
  gateway-specific dimensions. For more information about dimensions, see [Dimensions](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") in the _Amazon CloudWatch User Guide_.
- The metric name, such as `ReadBytes`.

The following table summarizes the types of Storage Gateway metric data that are
available to you.

| Amazon CloudWatch namespace | Dimension                  | Description                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/StorageGateway`        | `GatewayId`, `GatewayName` | These dimensions filter for metric data that describes aspects of<br>the gateway. You can identify a FSx File Gateway to work with by specifying both the<br>`GatewayId` and the<br>`GatewayName` dimensions.<br>Throughput and latency data of a gateway are based on all the file<br>shares in the gateway.<br>Data is available automatically in 5-minute periods at no charge. |

Working with gateway and file metrics is similar to working with other service
metrics. You can find a discussion of some of the most common metrics tasks in the CloudWatch
documentation listed following:

- [Viewing available metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md")
- [Getting statistics for a metric](../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md "../../../AmazonCloudWatch/latest/monitoring/getting-metric-statistics.md")
- [Creating
  CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")

## Understanding

gateway metrics

The following table describes metrics that cover FSx File Gateways.
Each gateway has a set of metrics associated with it. Some gateway-specific metrics have
the same name as certain file-system-specific metrics. These metrics represent the same
kinds of measurements, but are scoped to the gateway rather than the file system.

Always specify whether you want to work with a gateway or a file
system when working with a particular metric. Specifically, when working with gateway
metrics, you must specify the `Gateway Name` for the gateway whose metric
data you want to view. For more information, see [Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

The following table describes the metrics that you can use to get information about
your FSx File Gateways.

| Metric                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AvailabilityNotifications` | This metric reports the number of availability-related health notifications that were generated by the gateway in the reporting period.<br>Units: Count                                                                                                                                                                                                                                                                                |
| `CacheDirectorySize`        | This metric tracks the size of folders in the gateway cache. Folder size is determined by the number of files and subfolders in its first level, this does not count recursively into subfolders.<br>Use this metric with the `Average` statistic to measure the average size of a folder in the gateway cache. Use this metric with the `Max` statistic to measure the maximum size of a folder in the gateway cache.<br>Units: Count |
| `CacheFileSize`             | This metric tracks the size of files in the gateway cache.<br>Use this metric with the `Average` statistic to measure the average size of a file in the gateway cache. Use this metric with the `Max` statistic to measure the maximum size of a file in the gateway cache.<br>Units: Bytes                                                                                                                                            |
| `CacheFree`                 | This metric reports the number of available bytes in the gateway cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                |
| `CacheHitPercent`           | Percent of application read operations from the gateway that are served from cache. The sample is taken at the end of the reporting period.<br>When there are no application read operations from the gateway, this metric reports 100 percent.<br>Units: Percent                                                                                                                                                                      |
| `CachePercentDirty`         | The overall percentage of the gateway cache that has not been persisted to AWS. The sample is taken at the end of the reporting period.<br>Units: Percent                                                                                                                                                                                                                                                                              |
| `CachePercentUsed`          | The overall percent of the gateway cache storage that is used. The sample is taken at the end of the reporting period.<br>Units: Percent                                                                                                                                                                                                                                                                                               |
| `CacheUsed`                 | This metric reports the number of used bytes in the gateway cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                     |
| `CloudBytesDownloaded`      | The total number of bytes that the gateway downloaded from AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure IOPS.<br>Units: Bytes                                                                                                                                                                                                        |
| `CloudBytesUploaded`        | The total number of bytes that the gateway uploaded to AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure input/output operations per second (IOPS).<br>Units: Bytes                                                                                                                                                                       |
| `FilesFailingUpload`        | This metric tracks the number of files which are failing to upload to AWS. These files will generate health notifications which contain more information on the issue.<br>Use this metric with the `Sum` statistic to show the number of files which are currently failing to upload to AWS.<br>Units: Count                                                                                                                           |
| `FileShares`                | This metric reports the number of file shares on the gateway.<br>Units: Count                                                                                                                                                                                                                                                                                                                                                          |
| `FileSystem-ERROR`          | This metric provides the number of file system associations on this gateways which are in the ERROR state.<br>If this metric reports any file system associations are in the ERROR state, then it is likely there is a problem with the gateway which is may cause disruption to your workflow. It is recommended to create an alarm for when this metric reports a non-zero value.<br>Units: Count                                    |
| `HealthNotifications`       | This metric reports the number of health notifications that were generated by this gateway in the reporting period.<br>Units: Count                                                                                                                                                                                                                                                                                                    |
| `IndexEvictions`            | This metric reports the number of files whose metadata was evicted from the cached index of file metadata to make room for new entries. The gateway maintains this metadata index, which is populated from the AWS Cloud on demand.<br>Units: Count                                                                                                                                                                                    |
| `IndexFetches`              | This metric reports the number of files for which metadata was fetched. The gateway maintains a cached index of file metadata, which is populated from the AWS Cloud on demand.<br>Units: Count                                                                                                                                                                                                                                        |
| `IoWaitPercent`             | This metric reports the percentage of time that the CPU is waiting for a response from the local disk.<br>Units: Percent                                                                                                                                                                                                                                                                                                               |
| `MemTotalBytes`             | This metric reports the total amount of memory on the gateway.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                         |
| `MemUsedBytes`              | This metric reports the amount of used memory on the gateway.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                          |
| `RootDiskFreeBytes`         | This metric reports the number of available bytes on the root disk of the gateway.<br>If this metric reports less than 20 GB are free, you should increase the size of the root disk.<br>To increase the root disk size, you can increase the size of existing root disk on the VM. When the VM is rebooted, gateway recognizes the increased size on the root disk.<br>Units: Bytes                                                   |
| `SmbV2Sessions`             | This metric reports the number of SMBv2 sessions that are active on the gateway. This metric is emitted once for each file system associated with the gateway. Use the SUM stat to calculate the total number of active SMBv2 sessions across all file systems.<br>Units: Count                                                                                                                                                        |
| `SmbV3Sessions`             | This metric reports the number of SMBv3 sessions that are active on the gateway. This metric is emitted once for each file system associated with the gateway. Use the SUM stat to calculate the total number of active SMBv3 sessions across all file systems.<br>Units: Count                                                                                                                                                        |
| `TotalCacheSize`            | This metric reports the total size of the cache.<br>Units: Bytes                                                                                                                                                                                                                                                                                                                                                                       |
| `UserCpuPercent`            | This metric reports the percentage of time that is spent on gateway processing.<br>Units: Percent                                                                                                                                                                                                                                                                                                                                      |

## Understanding

file system metrics

You can find information following about the Storage Gateway metrics that
cover file systems. Each file
system has a set of metrics associated with it. Some file system-specific metrics have
the same name as certain gateway-specific metrics. These metrics represent the same
kinds of measurements, but are scoped to the file system instead.

Always specify whether you want to work with either a gateway or
a file system metric before working with a metric. Specifically, when working with file
system metrics, you must specify the `File system ID` that identifies the
file system for which you are interested in viewing metrics. For more information, see
[Using Amazon CloudWatch metrics](#using-CloudWatch-metrics "#using-CloudWatch-metrics").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

The following table describes the Storage Gateway metrics that you can use to get
information about your file shares.

| Metric                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CacheHitPercent`      | Percent of application read operations from the file shares that<br>are served from cache. The sample is taken at the end of the reporting<br>period.<br>When there are no application read operations from the file share,<br>this metric reports 100 percent.<br>Units: Percent                                                                                                                                                                   |
| `CachePercentDirty`    | The file share's contribution to the overall percentage of the<br>gateway's cache that has not been persisted to AWS. The<br>sample is taken at the end of the reporting period.<br>Use this metric with the `Sum` statistic.<br>Ideally, this metric should remain low.<br>NoteUse the `CachePercentDirty` metric of the gateway<br>to view the overall percentage of the gateway's cache that has<br>not been persisted to AWS.<br>Units: Percent |
| `CachePercentUsed`     | The percent of the data cache used across the entire gateway. The sample is taken at the end of the reporting<br>period. This file share-specific metric reports the same value as the corresponding gateway-specific metric.<br>Units: Percent                                                                                                                                                                                                     |
| `CloudBytesUploaded`   | The total number of bytes that the<br>gateway uploaded to AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                                                |
| `CloudBytesDownloaded` | The total number of bytes that the gateway<br>downloaded from AWS during the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure input/output operations per second (IOPS).<br>Units: Bytes                                                                                                                                                                       |
| `FilesFailingUpload`   | This metric tracks the number of files which are failing to upload to AWS. These files will generate health notifications which contain more information on the issue.<br>Use this metric with the `Sum` statistic to show the number of files which are currently failing to upload to AWS.<br>Units: Count                                                                                                                                        |
| `ReadBytes`            | The total number of bytes read from your on-premises<br>applications in the reporting period for a file share.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                            |
| `WriteBytes`           | The total number of bytes written to your on-premises<br>applications in the reporting period.<br>Use this metric with the `Sum` statistic to measure<br>throughput and with the `Samples` statistic to<br>measure IOPS.<br>Units: Bytes                                                                                                                                                                                                            |

## Understanding FSx File Gateway audit

logs

Amazon FSx File Gateway (FSx File Gateway) audit logs provide you with details
about user access to files and folders within a file system association. You can use
audit logs to monitor user activities and take action if inappropriate activity patterns
are identified. The logs are formatted similar to Windows Server security log events, to
support compatibility with existing log processing tools for Windows security events.

**Operations**

The following table describes the FSx File Gateway audit log file access operations.

| Operation name   | Definition                                                           |
| ---------------- | -------------------------------------------------------------------- |
| Read Data        | Read the contents of a file.                                         |
| Write Data       | Change the contents of a file.                                       |
| Create           | Create a new file or folder.                                         |
| Rename           | Rename an existing file or folder.                                   |
| Delete           | Delete a file or folder.                                             |
| Write Attributes | Update file or folder metadata (ACLs, owner, group,<br>permissions). |

**Attributes**

The following table describes FSx File Gateway audit log file access
attributes.

| Attribute            | Definition                                                                                                                                      |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `securityDescriptor` | Shows the discretionary access control list (DACL) set on an<br>object, in SDDL format.                                                         |
| `sourceAddress`      | The IP address of file share client machine.                                                                                                    |
| `SubjectDomainName`  | The Active Directory (AD) domain that the client’s account<br>belongs to.                                                                       |
| `SubjectUserName`    | The Active Directory user name of the client.                                                                                                   |
| `source`             | The ID of the Storage Gateway `FileSystemAssociation`<br>that is being audited.                                                                 |
| `mtime`              | This time that the object's content was modified, set by<br>the client.                                                                         |
| `version`            | The version of the audit log format.                                                                                                            |
| `ObjectType`         | Defines whether the object is a file or folder.                                                                                                 |
| `locationDnsName`    | The FSx File Gateway system DNS name.                                                                                                           |
| `objectName`         | The full path to the object.                                                                                                                    |
| `ctime`              | The time that the object’s content or metadata was modified,<br>set by the client.                                                              |
| `shareName`          | The name of the share that is being accessed.                                                                                                   |
| `operation`          | The name of the object access operation.                                                                                                        |
| `newObjectName`      | The full path to the new object after it has been<br>renamed.                                                                                   |
| `gateway`            | The Storage Gateway ID.                                                                                                                         |
| `status`             | The status of the operation. Only success is logged (failures<br>are logged with the exception of failures arising from permissions<br>denied). |
| `fileSizeInBytes`    | The size of the file in bytes, set by the client at file<br>creation time.                                                                      |

**Attributes logged per operation**

The following table describes the FSx File Gateway audit log attributes
logged in each file access operation.

|                      | Read data | Write data | Create folder | Create file | Rename file/folder | Delete file/folder | Write attributes (change ACL) | Write attributes (chown) | Write attributes (chmod) | Write attributes (chgrp) |
| -------------------- | --------- | ---------- | ------------- | ----------- | ------------------ | ------------------ | ----------------------------- | ------------------------ | ------------------------ | ------------------------ |
| `securityDescriptor` |           |            |               |             |                    |                    | X                             |                          |                          |                          |
| `sourceAddress`      | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `SubjectDomainName`  | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `SubjectUserName`    | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `source`             | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `mtime`              |           |            | X             | X           |                    |                    |                               |                          |                          |                          |
| `version`            | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `objectType`         | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `locationDnsName`    | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `objectName`         | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `ctime`              |           |            | X             | X           |                    |                    |                               |                          |                          |                          |
| `shareName`          | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `operation`          | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `newObjectName`      |           |            |               |             | X                  |                    |                               |                          |                          |                          |
| `gateway`            | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `status`             | X         | X          | X             | X           | X                  | X                  | X                             | X                        | X                        | X                        |
| `fileSizeInBytes`    |           |            |               | X           |                    |                    |                               |                          |                          |                          |
