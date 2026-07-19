# Monitoring S3 Files with Amazon CloudWatch

You can monitor S3 Files file systems using [Amazon
CloudWatch](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md"), which collects and processes raw data from Amazon S3 Files into
readable metrics. These metrics are retained for 15 months, so you can access historical
information and gain a better perspective on how your file systems are performing.

S3 Files metric data is automatically sent to CloudWatch. Most metrics are sent at
1-minute intervals, while storage metrics are sent every 15 minutes. You can create [CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.md") that send notifications when a metric exceeds a threshold you specify.
You can also use CloudWatch dashboards, which are customizable home pages in the CloudWatch
Console that you can use to monitor your resources in a single view. For more information,
see [Creating a customized
CloudWatch dashboard](../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md "../../../AmazonCloudWatch/latest/monitoring/create_dashboard.md").

## S3 Files CloudWatch metrics

S3 Files metrics use the `AWS/S3/Files` namespace. All metrics are reported
for a single dimension `FileSystemId`. The `AWS/S3/Files` namespace
includes the following metrics:

| Metric               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Units and valid statistics                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `StorageBytes`       | The total size of the file system in bytes, which includes data and<br>metadata. This metric is emitted to CloudWatch every 15<br>minutes.                                                                                                                                                                                                                                                                                                                                                                                 | Units: Bytes. Minimum, Maximum, Average                            |
| `Inodes`             | The total number of inodes (such as files, directories, symlinks) in<br>an S3 Files file system. This metric is emitted to CloudWatch every 15<br>minutes.                                                                                                                                                                                                                                                                                                                                                                 | Units: Count. Sum                                                  |
| `PendingExports`     | The total number of files and directories pending export to the S3<br>bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                              | Units: Count. Sum                                                  |
| `ImportFailures`     | The total number of objects that failed to import to the file system<br>after retries (for example, incorrect IAM permissions).                                                                                                                                                                                                                                                                                                                                                                                            | Units: Count. Sum                                                  |
| `ExportFailures`     | Total number of files and directories that failed export and will not<br>be retried. This metric helps you identify terminal export failures so<br>you can troubleshoot and take action (for example, update IAM<br>permissions).                                                                                                                                                                                                                                                                                          | Units: Count. Sum                                                  |
| `ImportAge`          | The age of in-progress changes that the file system imports from the<br>linked S3 bucket. The age is measured from when each change occurred in<br>the bucket. Use this metric to monitor whether imports are up to date. A<br>sustained increase means imports are falling behind changes in the<br>bucket.                                                                                                                                                                                                               | Units: Seconds                                                     |
| `ExportAge`          | The age of in-progress changes that the file system exports to the<br>linked S3 bucket. The age is measured from when each change occurred in<br>the file system. Use this metric to monitor whether exports are up to<br>date. A<br>sustained increase means exports are falling behind changes in the file<br>system.                                                                                                                                                                                                    | Units: Seconds                                                     |
| `DataReadBytes`      | The number of bytes read from the file system.<br>`SampleCount` gives the number of data read operations.<br>You can calculate data read throughput by viewing this metric per unit<br>time.                                                                                                                                                                                                                                                                                                                               | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) |
| `DataWriteBytes`     | The number of bytes written to the file system.<br>`SampleCount` gives the number of data write operations.<br>You can calculate data write throughput by viewing this metric per unit<br>time.                                                                                                                                                                                                                                                                                                                            | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) |
| `MetadataReadBytes`  | The number of metadata bytes read from the file system.<br>`SampleCount` gives the number of metadata read<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                  | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) |
| `MetadataWriteBytes` | The number of metadata bytes written to the file system.<br>`SampleCount` gives the number of metadata write<br>operations.                                                                                                                                                                                                                                                                                                                                                                                                | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) |
| `LostAndFoundFiles`  | Total number of files in the lost and found directory. The lost and<br>found directory is located in your file system's root directory under the<br>name<br>`.s3files-lost+found-`file-system-id``.<br>Files in the lost and found directory are not copied to your S3 bucket.<br>When a conflict occurs due to concurrent changes to the same data in both<br>the file system and the S3 bucket, S3 Files treats the S3 bucket as the<br>source of truth and moves the conflicting file to a lost and found<br>directory. | Units: Count. Sum                                                  |
| `ClientConnections`  | The number of active client connections to a file system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Units: Count. Sum                                                  |

## Client connectivity metrics

S3 Files can optimize read performance by allowing clients to read file data directly
from the linked S3 bucket. To support this, the S3 Files client emits connectivity
metrics that monitor whether the client can establish the necessary connections.

These metrics are emitted by the S3 Files client (amazon-efs-utils) and are published
to the `efs-utils/S3Files` CloudWatch namespace. Metrics emission is enabled
by default as part of the S3 Files experience.

| Metric                    | Description                                                                                                                                                                                                                                    | Units and valid statistics             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `NFSConnectionAccessible` | Indicates whether the client can connect to the file system through<br>the NFS mount. A value of 1 means the connection is accessible. A value<br>of 0 means the connection is not accessible.                                                 | Units: None. Minimum, Maximum, Average |
| `S3BucketAccessible`      | Indicates whether the client has the required permissions to read<br>data from the linked S3 bucket. A value of 1 means the client has the<br>necessary permissions. A value of 0 means the client does not have the<br>necessary permissions. | Units: None. Minimum, Maximum, Average |
| `S3BucketReachable`       | Indicates whether the linked S3 bucket and prefix exist and are<br>reachable from the client. A value of 1 means the bucket and prefix are<br>reachable. A value of 0 means the bucket or prefix is not<br>reachable.                          | Units: None. Minimum, Maximum, Average |

## Accessing CloudWatch metrics

You can view S3 Files metrics using the CloudWatch console, the AWS CLI, or the
CloudWatch API.

### To view metrics using the CloudWatch console

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, then choose **All
   metrics**.
3. Choose the **S3Files**
   namespace.
4. Choose **File System
   Metrics**.
5. Select the metrics you want to view.
6. Choose the **Graphed metrics** tab to
   configure the graph display.

### To view metrics using the AWS CLI

Use the `get-metric-statistics` command. For example, to view
`DataReadBytes`:

```
aws cloudwatch get-metric-statistics \
  --namespace AWS/S3/Files \
  --metric-name DataReadBytes \
  --dimensions Name=FileSystemId,Value=`file-system-id` \
  --start-time 2025-01-20T00:00:00Z \
  --end-time 2025-01-20T23:59:59Z \
  --period 3600 \
  --statistics Sum
```
