

# Monitoring S3 Files with Amazon CloudWatch
<a name="s3-files-monitoring-cloudwatch"></a>

You can monitor S3 Files file systems using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), which collects and processes raw data from Amazon S3 Files into readable metrics. These metrics are retained for 15 months, so you can access historical information and gain a better perspective on how your file systems are performing.

S3 Files metric data is automatically sent to CloudWatch. Most metrics are sent at 1-minute intervals, while storage metrics are sent every 15 minutes. You can create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) that send notifications when a metric exceeds a threshold you specify. You can also use CloudWatch dashboards, which are customizable home pages in the CloudWatch Console that you can use to monitor your resources in a single view. For more information, see [Creating a customized CloudWatch dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html).

## S3 Files CloudWatch metrics
<a name="s3-files-monitoring-cloudwatch-metrics"></a>

S3 Files metrics use the `AWS/S3/Files` namespace. All metrics are reported for a single dimension `FileSystemId`. The `AWS/S3/Files` namespace includes the following metrics:


| Metric | Description | Units and valid statistics | 
| --- | --- | --- | 
| StorageBytes | The total size of the file system in bytes, which includes data and metadata. This metric is emitted to CloudWatch every 15 minutes. | Units: Bytes. Minimum, Maximum, Average | 
| Inodes | The total number of inodes (such as files, directories, symlinks) in an S3 Files file system. This metric is emitted to CloudWatch every 15 minutes. | Units: Count. Sum | 
| PendingExports | The total number of files and directories pending export to the S3 bucket. | Units: Count. Sum | 
| ImportFailures | The total number of objects that failed to import to the file system after retries (for example, incorrect IAM permissions). | Units: Count. Sum | 
| ExportFailures | Total number of files and directories that failed export and will not be retried. This metric helps you identify terminal export failures so you can troubleshoot and take action (for example, update IAM permissions). | Units: Count. Sum | 
| ImportAge | The age of in-progress changes that the file system imports from the linked S3 bucket. The age is measured from when each change occurred in the bucket. Use this metric to monitor whether imports are up to date. A sustained increase means imports are falling behind changes in the bucket. | Units: Seconds | 
| ExportAge | The age of in-progress changes that the file system exports to the linked S3 bucket. The age is measured from when each change occurred in the file system. Use this metric to monitor whether exports are up to date. A sustained increase means exports are falling behind changes in the file system. | Units: Seconds | 
| DataReadBytes | The number of bytes read from the file system. SampleCount gives the number of data read operations. You can calculate data read throughput by viewing this metric per unit time. | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) | 
| DataWriteBytes | The number of bytes written to the file system. SampleCount gives the number of data write operations. You can calculate data write throughput by viewing this metric per unit time. | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) | 
| MetadataReadBytes | The number of metadata bytes read from the file system. SampleCount gives the number of metadata read operations. | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) | 
| MetadataWriteBytes | The number of metadata bytes written to the file system. SampleCount gives the number of metadata write operations. | Units: Bytes (Minimum, Maximum, Average, Sum), Count (SampleCount) | 
| LostAndFoundFiles | Total number of files in the lost and found directory. The lost and found directory is located in your file system's root directory under the name .s3files-lost\+found-{{file-system-id}}. Files in the lost and found directory are not copied to your S3 bucket. When a conflict occurs due to concurrent changes to the same data in both the file system and the S3 bucket, S3 Files treats the S3 bucket as the source of truth and moves the conflicting file to a lost and found directory. | Units: Count. Sum | 
| ClientConnections | The number of active client connections to a file system. | Units: Count. Sum | 

## Client connectivity metrics
<a name="s3-files-monitoring-cloudwatch-client-metrics"></a>

S3 Files can optimize read performance by allowing clients to read file data directly from the linked S3 bucket. To support this, the S3 Files client emits connectivity metrics that monitor whether the client can establish the necessary connections.

These metrics are emitted by the S3 Files client (amazon-efs-utils) and are published to the `efs-utils/S3Files` CloudWatch namespace. Metrics emission is enabled by default as part of the S3 Files experience.


| Metric | Description | Units and valid statistics | 
| --- | --- | --- | 
| NFSConnectionAccessible | Indicates whether the client can connect to the file system through the NFS mount. A value of 1 means the connection is accessible. A value of 0 means the connection is not accessible. | Units: None. Minimum, Maximum, Average | 
| S3BucketAccessible | Indicates whether the client has the required permissions to read data from the linked S3 bucket. A value of 1 means the client has the necessary permissions. A value of 0 means the client does not have the necessary permissions. | Units: None. Minimum, Maximum, Average | 
| S3BucketReachable | Indicates whether the linked S3 bucket and prefix exist and are reachable from the client. A value of 1 means the bucket and prefix are reachable. A value of 0 means the bucket or prefix is not reachable. | Units: None. Minimum, Maximum, Average | 

## Accessing CloudWatch metrics
<a name="s3-files-monitoring-cloudwatch-access"></a>

You can view S3 Files metrics using the CloudWatch console, the AWS CLI, or the CloudWatch API.

### To view metrics using the CloudWatch console
<a name="s3-files-monitoring-cloudwatch-access-console"></a>

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**, then choose **All metrics**.

1. Choose the **S3Files** namespace.

1. Choose **File System Metrics**.

1. Select the metrics you want to view.

1. Choose the **Graphed metrics** tab to configure the graph display.

### To view metrics using the AWS CLI
<a name="s3-files-monitoring-cloudwatch-access-cli"></a>

Use the `get-metric-statistics` command. For example, to view `DataReadBytes`:

```
aws cloudwatch get-metric-statistics \
  --namespace AWS/S3/Files \
  --metric-name DataReadBytes \
  --dimensions Name=FileSystemId,Value={{file-system-id}} \
  --start-time 2025-01-20T00:00:00Z \
  --end-time 2025-01-20T23:59:59Z \
  --period 3600 \
  --statistics Sum
```