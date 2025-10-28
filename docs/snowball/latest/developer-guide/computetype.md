Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Information about using Snowball Edge devices to provide local compute and storage functionality

Local compute and storage jobs enable you to use Amazon S3 compatible storage on Snowball Edge locally, without an internet connection.
You can't export data from Amazon S3 to the device or import data into Amazon S3 when the device
is returned.

###### Topics

- [Information about jobs to store data locally on Snowball Edge devices](#aboutstorage "#aboutstorage")
- [Information about jobs providing local storage on a cluster of Snowball Edge devices](#clusteroption "#clusteroption")

## Information about jobs to store data locally on Snowball Edge devices

You can read and write objects to an AWS Snowball Edge device using Amazon S3 compatible storage on Snowball Edge or the
S3 adapter. When you order a device, if you choose to use the S3 adapter, you also choose which Amazon S3 buckets will be included on the device when you receive it. If you choose to use Amazon S3 compatible storage on Snowball Edge, no Amazon S3 buckets are included on the device when you receive it.

You can create Amazon S3 buckets on the Snowball Edge devices to store and retrieve objects on premises for applications that require local data access, local data processing, and data residency. Amazon S3 compatible storage on Snowball Edge provides a new storage class, `SNOW`, which uses the Amazon S3 APIs, and is designed to store data durably and redundantly across multiple Snowball Edge devices. You can use the same APIs and features on Snowball Edge buckets that you do on Amazon S3, including bucket lifecycle policies, encryption, and tagging. When the device or devices are returned to AWS, all data created or stored in Amazon S3 compatible storage on Snowball Edge is erased. For more information, see [Local Compute and Storage Only Jobs](computetype.md "computetype.md").

For more information, see [Amazon S3 compatible storage on Snowball Edge](s3compatible-on-snow.md "s3compatible-on-snow.md") in this guide.

When you've finished using the device, return it to AWS, and the device will be
erased. This erasure follows the National Institute of Standards and Technology
(NIST) 800-88 standards.

## Information about jobs providing local storage on a cluster of Snowball Edge devices

A cluster is a logical grouping of Snowball Edge devices, in groups of
3 to 16 devices. A cluster is created as a single job, which offers increased
durability and storage size when compared to other AWS Snowball Edge job offerings. For
more information about cluster jobs, see [Clustering overview](ClusterOverview.md "ClusterOverview.md") in this guide.
