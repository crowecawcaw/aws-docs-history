# Configuring Amazon S3 Files access

Amazon S3 Files delivers a shared file system that connects any AWS compute resource directly with your data in Amazon S3. Amazon S3 Files provides access to your Amazon S3
objects as files using standard file system operations such as read and write on the local mount path. Learn more about [Amazon S3 Files](../../../AmazonS3/latest/userguide/s3-files.md "../../../AmazonS3/latest/userguide/s3-files.md").

###### Sections

- [Prerequisites and setup](#configuration-filesystem-s3files-setup "#configuration-filesystem-s3files-setup")
- [Execution role and user permissions](#configuration-filesystem-s3files-permissions "#configuration-filesystem-s3files-permissions")
- [Connecting to a file system (console)](#configuration-filesystem-s3files-config "#configuration-filesystem-s3files-config")
- [Configuring direct reads](#configuration-filesystem-s3files-directreads "#configuration-filesystem-s3files-directreads")

## Prerequisites and setup

Before you set up Amazon S3 Files with your Lambda function, make sure you have the following:

- An Amazon S3 file system and mount targets in available state in the same account and AWS Region as your Lambda function.
- A Lambda function in the same VPC as the mount target. You must have a mount target in each subnet where your function is deployed.
- Security groups that allow NFS traffic (port 2049) between your Lambda function and the mount targets. [Learn more about configuring security groups](../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md#s3-files-prereq-security-groups "../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md#s3-files-prereq-security-groups").

For more information, see the following topics in the _Amazon S3 User Guide_:

- [Getting started with Amazon S3 Files](../../../AmazonS3/latest/userguide/s3-files-getting-started.md "../../../AmazonS3/latest/userguide/s3-files-getting-started.md")
- [Amazon S3 Files prerequisites](../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md "../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md")
- [Amazon S3 Files best practices](../../../AmazonS3/latest/userguide/s3-files-best-practices.md "../../../AmazonS3/latest/userguide/s3-files-best-practices.md")

## Execution role and user permissions

Your function's execution role must have the following permissions to access an Amazon S3 Files file system:

###### Execution role permissions

- **s3files:ClientMount** – Required to mount the file system.
- **s3files:ClientWrite** – Required for read-write access. Not needed
  for read-only connections.

These permissions are included in the [AmazonS3FilesClientReadWriteAccess](../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadWriteAccess.md "../../../aws-managed-policy/latest/reference/AmazonS3FilesClientReadWriteAccess.md")
managed policy. Additionally, your execution role must have the [permissions
required to connect to the file system's VPC](configuration-vpc.md#configuration-vpc-permissions "configuration-vpc.md#configuration-vpc-permissions").

###### Note

Amazon S3 Files optimizes throughput by streaming eligible read requests directly from your Amazon S3 bucket.
Direct reads are enabled by default for functions configured with 512 MB or more of memory.
For more information, see
[Configuring direct reads](#configuration-filesystem-s3files-directreads "#configuration-filesystem-s3files-directreads").

Your function also needs the following permissions to read directly from Amazon S3:

- **s3:GetObject**
- **s3:GetObjectVersion**

For more information about required permissions, see [IAM permissions for Amazon S3 Files](../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md#s3-files-prereq-iam "../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md#s3-files-prereq-iam") in the _Amazon S3 User Guide_.

When you configure a file system in the console, Lambda uses your permissions to verify mount targets and
access points. To configure a function to connect to a file system, your user needs the following
permissions:

###### User permissions

- **s3files:ListFileSystems**
- **s3files:ListAccessPoints**
- **s3files:GetFileSystem**
- **s3files:GetAccessPoint**
- **s3files:CreateAccessPoint** – Needed if attaching the file system
  to the function from the console.

The following example policy grants your function's execution role permissions to mount an Amazon S3 file system
with read-write access and read directly from Amazon S3.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3FilesLambdaAccess",
            "Effect": "Allow",
            "Action": [
                "s3files:ClientMount",
                "s3files:ClientWrite"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3DirectRead",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::`bucket-name`/*"
        },
        {
            "Sid": "S3FilesConsoleSetup",
            "Effect": "Allow",
            "Action": [
                "s3files:ListFileSystems",
                "s3files:ListAccessPoints",
                "s3files:GetFileSystem",
                "s3files:GetAccessPoint",
                "s3files:CreateAccessPoint"
            ],
            "Resource": "*"
        }
    ]
}
```

## Connecting to a file system (console)

A function connects to a file system over the local network in a VPC. The subnets that your function connects to
can be the same subnets that contain mount points for your file system, or subnets in the same Availability Zone
that can route NFS traffic (port 2049) to the file system.

###### Note

If your function is not already connected to a VPC, see [Giving Lambda functions access to resources in an Amazon VPC](configuration-vpc.md "configuration-vpc.md").

###### To configure S3 Files access

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. Choose **Configuration**, then choose **File systems**.
4. Choose **Add file system** (or **Edit** to modify an existing
   configuration).
5. Select **S3 Files**.
6. Configure the following properties:

   - **S3 file system** – Choose a file system from the dropdown.
   - **Access point** (optional) – Choose an access point. If the file system
     has no access points, Lambda automatically creates one when you save (UID/GID 1000:1000, root directory
     `/lambda`, permissions 755). If access points exist, you must select one.
   - **Local mount path** – The location where the file system is mounted on the
     Lambda function, starting with `/mnt/`.
   - **Advanced configuration**

     - **Direct S3 Reads** – Controls whether Lambda can stream
       eligible reads directly from your Amazon S3 bucket for higher throughput. For more information, see
       [Configuring direct reads](#configuration-filesystem-s3files-directreads "#configuration-filesystem-s3files-directreads").

7. Choose **Save**.

Your file system is attached the next time you invoke your Lambda function.

## Configuring direct reads

Direct reads optimize throughput by streaming data directly from your Amazon S3 bucket. Lambda uses direct reads
for large reads and when the file system's high-performance storage does not hold the file data. For more
information, see
[How
S3 Files delivers performance](../../../AmazonS3/latest/userguide/s3-files-performance.md#s3-files-performance-how "../../../AmazonS3/latest/userguide/s3-files-performance.md#s3-files-performance-how"). This optional configuration is part of the `FileSystemConfigs`
for your function and applies only to Amazon S3 file systems. The `DirectS3Read` setting accepts
the following values:

- `AUTO` (default) – Enables direct reads for functions configured with
  512 MB or more of memory.
- `ENABLED` – Enables direct reads for your function, including functions with less than
  512 MB of memory.
- `DISABLED` – Routes all reads through the file system's high-performance storage.

###### Note

If a direct read fails, Lambda automatically falls back to reading through the file system.

To use direct reads, your function's execution role must have the required permissions.
For more information, see
[Amazon
S3 Files prerequisite policies](../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md "../../../AmazonS3/latest/userguide/s3-files-prereq-policies.md").
