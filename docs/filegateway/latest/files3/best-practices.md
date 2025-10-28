# Best practices for File Gateway

This section contains the following topics, which provide information about the best
practices for working with gateways, file shares, buckets, and data. We recommend that you
familiarize yourself with the information outlined in this section, and attempt to follow these
guidelines in order to avoid problems with your AWS Storage Gateway. For additional guidance on diagnosing
and solving common issues you might encounter with your deployment, see [Troubleshooting problems with your Storage Gateway
deployment](troubleshooting-gateway-issues.md "troubleshooting-gateway-issues.md").

###### Topics

- [Best practices: recovering your data](#recover-data-from-gateway "#recover-data-from-gateway")
- [Best practices: managing multipart
  uploads](#best-practices-managing-multi-part-uploads "#best-practices-managing-multi-part-uploads")
- [Best practices: Unzip compressed files
  locally before copying to a gateway](#best-practices-unzipping-on-gateway "#best-practices-unzipping-on-gateway")
- [Retain file attributes when copying
  data from Windows Server](#best-practices-copying-files-on-windows "#best-practices-copying-files-on-windows")
- [Best practices: Proper sizing of cache
  disks](#proper-sizing-of-cache-disks "#proper-sizing-of-cache-disks")
- [Working with multiple file shares and Amazon S3
  buckets](#prevent-multiple-writes "#prevent-multiple-writes")
- [Clean up unnecessary resources](#cleanup-file "#cleanup-file")

## Best practices: recovering your data

Although it is rare, your gateway might encounter an unrecoverable failure. Such a failure
can occur in your virtual machine (VM), the gateway itself, the local storage, or elsewhere.
If a failure occurs, we recommend that you follow the instructions in the appropriate
section following to recover your data.

###### Important

Storage Gateway doesn’t support recovering a gateway VM from a snapshot that is created by
your hypervisor or from your Amazon EC2 Amazon Machine Image (AMI). If your gateway VM
malfunctions, activate a new gateway and recover your data to that gateway using the
instructions following.

### Recovering from an unexpected virtual

machine shutdown

If your VM shuts down unexpectedly, for example during a power outage, your gateway
becomes unreachable. When power and network connectivity are restored, your gateway
becomes reachable and starts to function normally. Following are some steps you can take
at that point to help recover your data:

- If an outage causes network connectivity issues, you can troubleshoot the
  issue. For information about how to test network connectivity, see [Testing your gateway's network
  connectivity](MaintenanceTestGatewayConnectivity-fgw.md "MaintenanceTestGatewayConnectivity-fgw.md").

### Recovering your data from a malfunctioning

cache disk

If your cache disk encounters a failure, we recommend you use the following steps to
recover your data depending on your situation:

- If the malfunction occurred because a cache disk was removed from your host,
  shut down the gateway, re-add the disk, and restart the gateway.

### Recovering your data from an inaccessible data

center

If your gateway or data center becomes inaccessible for some reason, you can recover
your data to another gateway in a different data center or recover to a gateway hosted
on an Amazon EC2 instance. If you don't have access to another data center, we recommend
creating the gateway on an Amazon EC2 instance. The steps you follow depends on the gateway
type you are covering the data from.

###### To recover data from a File Gateway in an inaccessible data center

For File Gateway, you map a new to the Amazon S3 bucket that contains the data you want to recover.

1. Create and activate a new File Gateway on an Amazon EC2 host. For more
   information, see [Deploy a default Amazon EC2 host for
   S3 File Gateway](ec2-gateway-file.md "ec2-gateway-file.md").
2. Create a new on the EC2 gateway you created.
   For more information, see [Create a
   file share](GettingStartedCreateFileShare.md "GettingStartedCreateFileShare.md").
3. Mount your file share on your client and map it to the
   S3 bucket that contains the data that you want to recover. For
   more information, see [Mount and
   use your file share](getting-started-use-fileshare.md "getting-started-use-fileshare.md").

## Best practices: managing multipart

uploads

When transferring large files, S3 File Gateway makes use of the Amazon S3 multipart upload feature to
split the files into smaller parts and transfer them in parallel for improved efficiency. For
more information about multipart upload, see [Uploading and copying objects using multipart
upload](../../../AmazonS3/latest/userguide/mpuoverview.md "../../../AmazonS3/latest/userguide/mpuoverview.md") in the _Amazon Simple Storage Service User Guide_.

If a multipart upload doesn't complete successfully for any reason, the gateway typically
stops the transfer, deletes any partially-transferred pieces of the file from Amazon S3, and attempts
the transfer again. In rare cases, such as when hardware or network failure prevent the gateway
from cleaning up after an unsuccessful multipart upload, pieces of the partially-transferred file
might remain on Amazon S3 where they can incur storage charges.

As a best practice for minimizing Amazon S3 storage costs from incomplete multipart uploads, we
recommend configuring an Amazon S3 bucket lifecycle rule that uses the
`AbortIncompleteMultipartUpload` API action to automatically stop unsuccessful
transfers and delete associated file parts after a designated number of days. For instructions,
see
[Configuring a
bucket lifecycle configuration to delete incomplete multipart uploads](../../../AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.md "../../../AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.md") in the
_Amazon Simple Storage Service User Guide_.

## Best practices: Unzip compressed files

locally before copying to a gateway

If you try to unzip a compressed archive containing thousands of files while it is stored on
your gateway, you might encounter significant performance-related delays. The process of
unzipping an archive that contains large numbers of files on any type of network file share
inherently involves a high volume of input/output operations, metadata cache manipulation,
network overhead, and latency. Additionally, Storage Gateway is unable to determine when each file from
the archive has finished unzipping, and can begin uploading files before the process is complete,
which further impacts performance. These issues are compounded when the files inside the archive
are numerous, but small in size.

As a best practice, we recommend transferring compressed archives from your gateway to your
local machine first, before you unzip them. Then, if necessary, you can use a tool such as
_robocopy_ or _rsync_ to transfer the unzipped files back
to the gateway.

## Retain file attributes when copying

data from Windows Server

It is possible to copy files to your File Gateway using the basic `copy` command
on Microsoft Windows, but this command copies only the file data by default - omitting certain
file attributes such as security descriptors. If the files are copied to the gateway without the
corresponding security restrictions and Discretionary Access Control List (DACL) information, it
is possible that they could be accessed by unauthorized users.

As a best practice for preserving all file attributes and security information when copying
files to your gateway on Microsoft Windows Server, we recommend using the `robocopy`
or `xcopy` commands, with the `/copy:DS` or `/o` flags,
respectively. For more information, see [robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy") and [xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy "https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy") in the Microsoft Windows Server command reference documentation.

## Best practices: Proper sizing of cache

disks

For best performance, the total disk cache size must be large enough to cover the size of
your active working set. For read-heavy and mixed read/write workloads, this ensures that you can
achieve a high percentage of cache hits on reads, which is desirable. You can monitor this via
the `CacheHitPercent` metric for your S3 File Gateway.

For write-heavy workloads (e.g. for backup and archival), the S3 File Gateway buffers incoming
writes on the disk cache prior to copying this data asynchronously to Amazon S3. You should ensure
that you have sufficient cache capacity to buffer written data. The
`CachePercentDirty` metric provides an indication of the percentage of the disk cache
that has not yet been persisted to AWS.

Low values of `CachePercentDirty` are desirable. Values that are consistently
close to 100% indicate that the S3 File Gateway is unable to keep up with the rate of incoming write
traffic. You can avoid this by either increasing the provisioned disk cache capacity, or
increasing the dedicated network bandwidth available from the S3 File Gateway to Amazon S3, or both.

For more information about cache disk sizing, see [Amazon S3 File Gateway cache sizing best
practices](https://www.youtube.com/watch?v=-ibL1eEcROI "https://www.youtube.com/watch?v=-ibL1eEcROI") on the official Amazon Web Services YouTube channel.

## Working with multiple file shares and Amazon S3

buckets

When you configure a single Amazon S3 bucket to allow multiple gateways or file shares to write
to it, the results can be unpredictable. You can configure your buckets in one of two ways to
avoid unpredictable results. Choose the configuration method that best fits your use case from
the following options:

- Configure your S3 buckets so that only one file share can write to each bucket. Use a
  different file share to write to each bucket.

To do this, create an S3 bucket policy that denies all roles except for the role that's
used for a specific file share to put or delete objects in the bucket. Attach a similar policy
to each bucket, specifying a different file share to write to each bucket.

The following example policy denies S3 bucket write permissions to all roles except for
the role that created the bucket. The `s3:DeleteObject` and
`s3:PutObject` actions are denied for all roles except `"TestUser"`. The
policy applies to all objects in the `"arn:aws:s3:::amzn-s3-demo-bucket/*"`
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"DenyMultiWrite",
 "Effect":"Deny",
 "Principal":"*",
 "Action":[
 "s3:DeleteObject",
 "s3:PutObject"
 ],
 "Resource":"arn:aws:s3:::amzn-s3-demo-bucket/*",
 "Condition":{
 "StringNotLike":{
 "aws:userid":"TestUser:*"
 }
 }
 }
 ]
}`

```

- If you do want multiple file shares to write to the same Amazon S3 bucket, you must prevent the
  file shares from trying to write to the same objects simultaneously.

To do this, configure a separate, unique object prefix for each file share. This means
that each file share only writes to objects with the corresponding prefix, and doesn't write to
objects that are associated with the other file shares in your deployment. You configure the
object prefix in the **S3 prefix name** field when you create a new file
share.

## Clean up unnecessary resources

As a best practice, we recommend cleaning up Storage Gateway resources to avoid unexpected or
unnecessary charges. For example, if you created a gateway as a demonstration exercise or a test,
consider deleting it and its virtual appliance from your deployment. Use the following procedure
to clean up resources.

###### To clean up resources you don't need

1. If you no longer plan to continue using a gateway, delete it. For more information, see
   [Deleting your gateway and removing associated
   resources](deleting-gateway-common.md "deleting-gateway-common.md").
2. Delete the Storage Gateway VM from your on-premises host. If you created your gateway on an Amazon EC2
   instance, terminate the instance.
