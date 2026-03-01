# Managing S3 on Outposts capacity with Amazon CloudWatch metrics

To help manage the fixed S3 capacity on your Outpost, we recommend that you create
CloudWatch alerts that tell you when your storage utilization exceeds a certain threshold. For
more information about the CloudWatch metrics for S3 on Outposts, see [CloudWatch metrics](#S3OutpostsCloudWatchMetrics "#S3OutpostsCloudWatchMetrics"). If there is not enough space to store an object on your Outpost, the API returns an
insufficient capacity exemption (ICE). To free up space, you can create CloudWatch alarms that
trigger explicit data deletion, or use a lifecycle expiration policy to expire objects.
To save data before deletion, you can use AWS DataSync to copy data from your
Amazon S3 on Outposts bucket to an S3 bucket in an AWS Region. For more information about
using DataSync, see [Getting Started with
AWS DataSync](../../../datasync/latest/userguide/getting-started.md "../../../datasync/latest/userguide/getting-started.md") in the _AWS DataSync User Guide_.

## CloudWatch metrics

The `S3Outposts` namespace includes the following metrics for
Amazon S3 on Outposts buckets. You can monitor the total number of S3 on Outposts bytes
provisioned, the total free bytes available for objects, and the total size of all
objects for a given bucket. Bucket or account-related metrics exist for all direct S3 usage.
Indirect S3 usage, such as storing Amazon Elastic Block Store local snapshots or Amazon Relational Database Service backups on an Outpost,
consumes S3 capacity, but is not included in bucket or account-related metrics.
For more information about Amazon EBS local snapshots, see
[Amazon EBS local snapshots on Outposts](../../../AWSEC2/latest/UserGuide/snapshots-outposts.md "../../../AWSEC2/latest/UserGuide/snapshots-outposts.md").
To see your Amazon EBS cost report, visit [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").

###### Note

S3 on Outposts supports only the following metrics, and no other Amazon S3
metrics.

Because S3 on Outposts has a fixed capacity limit, we recommend creating CloudWatch alarms to
notify you when your storage utilization exceeds a certain threshold.

| Metric                         | Description                                                                                                                                                                                                                                                                                                                                                   | Time Period | Units   | Type                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------- | ----------------------------------------- |
| `OutpostTotalBytes`            | The total provisioned capacity in bytes for an Outpost.                                                                                                                                                                                                                                                                                                       | 5 minutes   | Bytes   | S3 on Outposts                            |
| `OutpostFreeBytes`             | The count of free bytes available on an Outpost to store<br>customer data.                                                                                                                                                                                                                                                                                    | 5 minutes   | Bytes   | S3 on Outposts                            |
| `BucketUsedBytes`              | The total size of all objects for the given bucket.                                                                                                                                                                                                                                                                                                           | 5 minutes   | Bytes   | S3 on Outposts. Direct S3 usage only.     |
| `AccountUsedBytes`             | The total size of all objects for the specified Outposts<br>account.                                                                                                                                                                                                                                                                                          | 5 minutes   | Bytes   | S3 on Outposts. Direct S3 usage only.     |
| `BytesPendingReplication`      | The total number of bytes of objects that are pending replication for a given replication rule. For more information about how to enable replication metrics,<br>see [Creating replication rules between Outposts](../userguide/replication-between-outposts.md "../userguide/replication-between-outposts.md").                                              | 5 minutes   | Bytes   | Optional. For S3 Replication on Outposts. |
| `OperationsPendingReplication` | The total number of operations that are pending replication for a given replication rule. For more information about how to enable replication metrics,<br>see [Creating replication rules between Outposts](../userguide/replication-between-outposts.md "../userguide/replication-between-outposts.md").                                                    | 5 minutes   | Counts  | Optional. For S3 Replication on Outposts. |
| `ReplicationLatency`           | The current number of seconds delay by which the replication destination bucket is behind the source bucket for a given replication rule.<br>For more information about how to enable replication metrics,<br>see [Creating replication rules between Outposts](../userguide/replication-between-outposts.md "../userguide/replication-between-outposts.md"). | 5 minutes   | Seconds | Optional. For S3 Replication on Outposts. |
