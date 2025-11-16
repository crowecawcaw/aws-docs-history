AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using Amazon S3 compatible storage on Snowball Edge

Amazon S3 compatible storage on Snowball Edge delivers secure object storage with increased resiliency, scale, and an
expanded Amazon S3 API feature-set to rugged, mobile edge, and disconnected environments. Using
Amazon S3 compatible storage on Snowball Edge, you can store data and run highly available applications on Snowball Edge for
edge computing.

You can create Amazon S3 buckets on the Snowball Edge devices to store and retrieve objects on premises for applications that require local data access, local data processing, and data residency. Amazon S3 compatible storage on Snowball Edge provides a new storage class, `SNOW`, which uses the Amazon S3 APIs, and is designed to store data durably and redundantly across multiple Snowball Edge devices. You can use the same APIs and features on Snowball Edge buckets that you do on Amazon S3, including bucket lifecycle policies, encryption, and tagging. When the device or devices are returned to AWS, all data created or stored in Amazon S3 compatible storage on Snowball Edge is erased. For more information, see [Local Compute and Storage Only Jobs](computetype.md "computetype.md").

You can deploy Amazon S3 compatible storage on Snowball Edge in standalone configuration or in cluster configuration. In
standalone configuration, you can provision S3 capacity on the device and the balance is
available as block storage. In cluster configuration, all data disk capacity is used for S3
storage. A cluster may consist of a minimum of 3 devices up to a maximum of 16 devices.
Depending on the size of cluster, S3 service is designed to sustain device fault tolerance
of 1 or 2 devices.

With AWS DataSync, you can transfer objects between Amazon S3 compatible storage on Snowball Edge on a Snowball Edge device
and AWS storage services. For more information, see [Configuring transfers
with S3 compatible storage on Snowball Edge](../../../datasync/latest/userguide/s3-compatible-storage-snow.md "../../../datasync/latest/userguide/s3-compatible-storage-snow.md") in the AWS DataSync User Guide.

Following is the Amazon S3 compatible storage on Snowball Edge storage capacity and block storage capacity for a standalone
device using Amazon S3 compatible storage on Snowball Edge. For fault tolerance and storage capacity of clusters, see [this table](ClusterOverview.md#cluster-table "ClusterOverview.md#cluster-table").

Snowball Edge Compute Optimized with NVMe storage

Storage capacity of Amazon S3 compatible storage on Snowball Edge and block storage of Snowball Edge
Compute Optimized (Compute Optimized with AMD EPYC Gen2 and NVMe)
devices| Amazon S3 compatible storage on Snowball Edge storage capacity (in TB) | Block storage capacity (in TB) |
| --- | --- |
| 3 | 17.5 |
| 5.5 | 14.5 |
| 10.5 | 8.5 |
| 12 | 6.5 |
| 13 | 5.5 |
| 16.5 | 1.5 |

Snowball Edge storage optimized 210 TB

Storage capacity of Amazon S3 compatible storage on Snowball Edge and block storage of Snowball Edge
storage optimized 210 TB devices| Amazon S3 compatible storage on Snowball Edge storage capacity (in TB) | Block storage capacity (in TB) |
| --- | --- |
| 20 | 206 |
| 40 | 182 |
| 60 | 158 |
| 80 | 134 |
| 100 | 110 |
| 120 | 86 |
| 140 | 62 |
| 160 | 38 |
| 180 | 14 |
| 190 | 2 |

Amazon S3 compatible storage on Snowball Edge specifications:

- The maximum number of Snowball Edge buckets is 100 per device or per cluster.
- The S3 on Snowball Edge bucket owner account owns all objects in the bucket.
- Only the S3 on Snowball Edge bucket owner account can perform operations on the
  bucket.
- Object size limitations are consistent with those in Amazon S3.
- All objects stored on S3 on Snowball Edge have SNOW as the storage class.
- By default, all objects stored in the SNOW storage class are stored using
  server-side encryption with Amazon S3 managed encryption keys (SSE-S3). You can also
  explicitly choose to store objects by using server-side encryption with
  customer-provided encryption keys (SSE-C).
- If there is not enough space to store an object on your Snowball Edge, the API returns an
  insufficient capacity exception (ICE).

###### Topics

- [Order Amazon S3 compatible storage on Snowball Edge](s3-edge-snow-order-device.md "s3-edge-snow-order-device.md")
- [Setting up and starting Amazon S3 compatible storage on Snowball Edge](s3-edge-snow-setting-up.md "s3-edge-snow-setting-up.md")
- [Working with S3 buckets with Amazon S3 compatible storage on Snowball Edge](working-s3-snow-buckets.md "working-s3-snow-buckets.md")
- [Determining whether you can access an Amazon S3 compatible storage on Snowball Edge
  bucket on a Snowball Edge](working-s3-snow-buckets-determine-bucket-access-s3-snow.md "working-s3-snow-buckets-determine-bucket-access-s3-snow.md")
- [Retrieving a list of buckets or regional buckets in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](working-s3-snow-buckets-list-buckets-s3-snow.md "working-s3-snow-buckets-list-buckets-s3-snow.md")
- [Getting a bucket with Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](working-s3-snow-buckets-get-bucket-s3-snow.md "working-s3-snow-buckets-get-bucket-s3-snow.md")
- [Creating an S3 bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](working-s3-snow-buckets-creating-s3-snow-bucket.md "working-s3-snow-buckets-creating-s3-snow-bucket.md")
- [Deleting a bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](working-s3-snow-buckets-delete-bucket-s3-snow.md "working-s3-snow-buckets-delete-bucket-s3-snow.md")
- [Creating and managing an object lifecycle
  configuration using the AWS CLI](working-s3-snow-buckets-lifecycle-s3-snow.md "working-s3-snow-buckets-lifecycle-s3-snow.md")
- [Copying an object to an Amazon S3 compatible storage on Snowball Edge bucket on a Snowball Edge](objects-copy-s3-snow.md "objects-copy-s3-snow.md")
- [Listing objects in a bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](objects-list-s3-snow.md "objects-list-s3-snow.md")
- [Getting an object from a bucket in Amazon S3 compatible storage on Snowball Edge on a Snowball Edge](objects-get-s3-snow.md "objects-get-s3-snow.md")
- [Deleting objects in buckets in Amazon S3 compatible storage on Snowball Edge](objects-delete-s3-snow.md "objects-delete-s3-snow.md")
- [Supported REST API actions for Amazon S3 compatible storage on Snowball Edge](s3-snow-api.md "s3-snow-api.md")
- [Using Amazon S3 compatible storage on Snowball Edge with a cluster of Snow devices](ClusterOverview.md "ClusterOverview.md")
- [Configuring Amazon S3 compatible storage on Snowball Edge event
  notifications](s3-snow-event-notifications.md "s3-snow-event-notifications.md")
- [Configuring local SMTP
  notifications on Snowball Edge](s3-snow-smtp-notifications.md "s3-snow-smtp-notifications.md")
