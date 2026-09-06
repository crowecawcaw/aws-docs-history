

# Store and restore an AMI using S3
<a name="ami-store-restore"></a>

You can store an Amazon Machine Image (AMI) in an Amazon S3 bucket, copy the AMI to another S3 bucket, and then restore it from the S3 bucket. By storing and restoring an AMI using S3 buckets, you can copy AMIs from one AWS partition to another, for example, from the main commercial partition to the AWS GovCloud (US) partition. You can also make archival copies of AMIs by storing them in an S3 bucket.

The supported APIs for storing and restoring an AMI using S3 are `CreateStoreImageTask`, `DescribeStoreImageTasks`, and `CreateRestoreImageTask`.

`CopyImage` is the recommended API to use for copying AMIs *within* an AWS partition. However, `CopyImage` can’t copy an AMI to *another* partition.

For information about the AWS partitions, see {{partition}} on the [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) page in the *IAM User Guide*.

**Warning**  
Ensure that you comply with all applicable laws and business requirements when moving data between AWS partitions or AWS Regions, including, but not limited to, any applicable government regulations and data residency requirements.

**Topics**
+ [Use cases](#use-cases)
+ [Limitations](#ami-store-restore-limitations)
+ [Costs](#store-restore-costs)
+ [How AMI store and restore works](store-restore-how-it-works.md)
+ [Create a store image task](work-with-ami-store-restore.md)

## Use cases
<a name="use-cases"></a>

**Topics**
+ [Copy an AMI between AWS partitions](#copy-to-partition)
+ [Make archival copies of AMIs](#archival-copies)

### Copy an AMI between AWS partitions
<a name="copy-to-partition"></a>

By storing and restoring an AMI using S3 buckets, you can copy an AMI from one AWS partition to another, or from one AWS Region to another. In the following example, you copy an AMI from the main commercial partition to the AWS GovCloud (US) partition, specifically from the `us-east-2` Region to the `us-gov-east-1` Region.

To copy an AMI from one partition to another, follow these steps:
+ Store the AMI in an S3 bucket in the current Region by using `CreateStoreImageTask`. In this example, the S3 bucket is located in `us-east-2`.
+ Monitor the progress of the store task by using `DescribeStoreImageTasks`. The object becomes visible in the S3 bucket when the task is completed.
+ Copy the stored AMI object to an S3 bucket in the target partition using a procedure of your choice. In this example, the S3 bucket is located in `us-gov-east-1`.
**Note**  
Because you need different AWS credentials for each partition, you can’t copy an S3 object directly from one partition to another. The process for copying an S3 object across partitions is outside the scope of this documentation. We provide the following copy processes as examples, but you must use the copy process that meets your security requirements.  
To copy one AMI across partitions, the copy process could be as straightforward as the following: [Download the object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) from the source bucket to an intermediate host (for example, an EC2 instance or a laptop), and then [upload the object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) from the intermediate host to the target bucket. For each stage of the process, use the AWS credentials for the partition.
For more sustained usage, consider developing an application that manages the copies, potentially using S3 [multipart downloads and uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html).
+ Restore the AMI from the S3 bucket in the target partition by using `CreateRestoreImageTask`. In this example, the S3 bucket is located in `us-gov-east-1`.
+ Monitor the progress of the restore task by describing the AMI to check when its state becomes available. You can also monitor the progress percentages of the snapshots that make up the restored AMI by describing the snapshots.

### Make archival copies of AMIs
<a name="archival-copies"></a>

You can make archival copies of AMIs by storing them in an S3 bucket. The AMI is packed into a single object in S3, and all of the AMI metadata (excluding sharing information) is preserved as part of the stored AMI. The AMI data is compressed as part of the storage process. AMIs that contain data that can easily be compressed will result in smaller objects in S3. To reduce costs, you can use less expensive S3 storage tiers. For more information, see [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) and [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)

## Limitations
<a name="ami-store-restore-limitations"></a>
+ To store an AMI, your AWS account must either own the AMI and its snapshots, or the AMI and its snapshots must be [shared directly with your account](sharingamis-explicit.md). You can't store an AMI if it is only [publicly shared](sharingamis-intro.md).
+ Only EBS-backed AMIs can be stored using these APIs.
+ Paravirtual (PV) AMIs are not supported.
+ The size of an AMI (before compression) that can be stored is limited to 5,000 GB.
+ Quota on store image requests: 1,200 GB of storage work (snapshot data) in progress.
+ Quota on restore image requests: 600 GB of restore work (snapshot data) in progress.
+ For the duration of the store task, the snapshots must not be deleted and the IAM principal doing the store must have access to the snapshots, otherwise the store process will fail.
+ You can’t create multiple copies of an AMI in the same S3 bucket.
+ An AMI that is stored in an S3 bucket can’t be restored with its original AMI ID. You can mitigate this by using [AMI aliasing](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html).
+ Currently the store and restore APIs are only supported by using the AWS Command Line Interface, AWS SDKs, and Amazon EC2 API. You can’t store and restore an AMI using the Amazon EC2 console.

## Costs
<a name="store-restore-costs"></a>

When you store and restore AMIs using S3, you are charged for the services that are used by the store and restore APIs, and for data transfer. The APIs use S3 and the EBS Direct API (used internally by these APIs to access the snapshot data). For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) and [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).