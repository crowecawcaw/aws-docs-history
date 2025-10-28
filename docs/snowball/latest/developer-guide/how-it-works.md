Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# How AWS Snowball Edge works

AWS Snowball Edge devices are owned by AWS, and they reside at your on-premises location
while they're in use.

There are three job types you can use with an AWS Snowball Edge device.
Although the job types differ in their
use cases, every job type has the same workflow for how you order, receive, and return devices.
Regardless of the job type, every job follows a data erasure of the National Institute of
Standards and Technology (NIST) 800-88 standard after the job completes.

###### The shared workflow

1. **Create the job** – Each job is created in the
   AWS Snow Family Management Console or programmatically through the job management API. The status for a job can
   be tracked in the console or through the API.
2. **A device is prepared for your job** – We prepare an
   AWS Snowball Edge device for your job, and the status of your job is now **Preparing
   Snowball**. This preparation process may take up to 4 weeks from when the job to order the device was created. This timeline should be factored into your project plan to ensure a seamless transition.
3. **A device is shipped to you by your region's carrier**
   – The carrier takes over from here, and the status of your job is now **In
   transit to you**. You can find your tracking number and a link to the tracking
   website on the console or with the job management API. For information about who your
   region's carrier is, see [Shipping considerations for Snowball Edge](shipping.md "shipping.md").
4. **Receive the device** – A few days later, your
   region's carrier delivers the AWS Snowball Edge device to the address that you provided when you
   created the job, and the status of your job changes to **Delivered to
   you**. When it arrives, you’ll notice that it didn’t arrive in a box, because the
   device is its own shipping container.
5. **Get your credentials and download the Snowball Edge
   client** – Get ready to start transferring data by getting your
   credentials, your job manifest, and the manifest's unlock code, and then downloading the
   Snowball Edge client.
   - The Snowball Edge client is the tool that you use to manage the flow of data from
     the device to your on-premises data destination.

   You can download and install the Snowball Edge client from the [AWS Snowball Edge resources](https://aws.amazon.com/snowball/resources/ "https://aws.amazon.com/snowball/resources/")
   page.

   You must download the Snowball Edge client from the
   [AWS Snowball Edge Resources](http://aws.amazon.com/snowball/resources/ "http://aws.amazon.com/snowball/resources/") page and install on a powerful workstation that you own.
   - The manifest is used to authenticate your access to the device, and it is encrypted
     so that only the unlock code can decrypt it. You can get the manifest from the console
     or with the job management API when the device is on-premises at your location.
   - The unlock code is a 29-character code used to decrypt the manifest. You can get the
     unlock code from the console or with the job management API. We recommend that you keep
     the unlock code saved somewhere separate from the manifest to prevent unauthorized
     access to the device while it’s at your facility.

6. **Position the hardware** – Move the device into your
   data center and open it following the instructions on the case. Connect the device to power
   and your local network.
7. **Power on the device** – Next, power on the device
   by pressing the power button above the LCD display. Wait a few minutes, and the
   **Ready** screen appears.
8. **Get the IP address for the device** – The LCD
   display has a **CONNECTION** tab on it. Tap this tab and get the IP address
   for the AWS Snowball Edge device.
9. **Use the Snowball Edge client to unlock the device**
   – When you use the Snowball Edge client to unlock the AWS Snowball Edge device, enter the IP
   address of the device, the path to your manifest, and the unlock code. The Snowball Edge
   client decrypts the manifest and uses it to authenticate your access to the device.
10. **Use the device** – The device is up and running.
    You can use it to transfer data with the Amazon S3 adapter or the Network File System (NFS) mount point or for local compute and storage with Amazon S3 compatible storage on Snowball Edge.
11. **Prepare the device for its return trip** – After
    you're done with the device in your on-premises location, press the power button above the LCD display. It takes
    about 20 seconds or so for the device to power off. Unplug the device and its power cables
    into the cable nook on top of the device, and shut all three of the device's doors. The
    device is now ready to be returned.
12. **Your region's carrier returns the device to AWS** –
    When the carrier has the AWS Snowball Edge device, the status for the job becomes **In transit
    to AWS**.

###### Note

There are additional steps for export and cluster jobs. For more information, see
[How Snowball Edge export jobs work](#how-export "#how-export") and [How Snowball Edge clustered local compute and storage jobs work](#how-cluster "#how-cluster").

###### Topics

- [How Snowball Edge import jobs work](#how-import "#how-import")
- [How Snowball Edge export jobs work](#how-export "#how-export")
- [How Snowball Edge local compute and storage jobs work](#how-localcompute "#how-localcompute")
- [Snowball Edge videos and blogs](#blog-videos "#blog-videos")

## How Snowball Edge import jobs work

Each import job uses a single Snowball appliance. After you create a job to order a Snowball Edge device in the
AWS Snow Family Management Console or the job management API, we ship a Snowball to you. When it arrives in a few
days, you connect the Snowball Edge device to your network and transfer the data that you
want imported into Amazon S3 onto the device. When you’re done transferring data, ship the
Snowball back to AWS, and we import your data into Amazon S3.

###### Important

The import process cannot write to buckets in Amazon S3 from the Snow device if you have turned on S3 Object Lock and enabled Default retention settings. After Amazon S3 Object Lock is enabled, you can't disable it or suspend bucket versioning for the bucket. If your buckets have S3 Object Lock with Default retention settings enabled, before returning the Snowball Edge, disable the retention setting of S3 Object Lock. After the data is imported from the device by AWS, enable the retetion setting on the bucket again. For more information, see [Set or modify a retention period on an S3 object](../../../AmazonS3/latest/userguide/object-lock-configure.md#object-lock-configure-set-retention-period-object "../../../AmazonS3/latest/userguide/object-lock-configure.md#object-lock-configure-set-retention-period-object").

The import process also cannot write to your bucket in Amazon S3 if IAM policies on the bucket prevent writing to the bucket. For more information, see [Identity and Access Management for Amazon S3](../../../AmazonS3/latest/userguide/security-iam.md "../../../AmazonS3/latest/userguide/security-iam.md").

## How Snowball Edge export jobs work

Each export job can use any number of AWS Snowball Edge devices.

If the listing contains more data than can fit on a single device, multiple devices are
provided to you. Each job part has exactly one device associated with it. After your job parts
are created, your ﬁrst job part enters the **Preparing Snowball**
status.

###### Note

The listing operation used to split your job into parts is a function of Amazon S3, and you
are billed for it the same way as any Amazon S3 operation.

Soon after that, we start exporting your data onto a device. The time required to export your data will vary based on the the nature of your data set. For example, exporting many small files (less than 10 MB) takes significantly longer. When the export is done, AWS gets the device ready for pickup by your region's
carrier. When it arrives, you connect the AWS AWS Snowball Edge device to your network and
transfer the data from the device to storage on your network.

When you’re done transferring data, ship the device back to AWS. When we receive the
device for your export job part, we erase it completely. This erasure follows the National
Institute of Standards and Technology (NIST) 800-88 standards. This step marks the completion
of that particular job part.

- For keylisting

Before we export the objects in the S3 bucket, we scan the bucket. If the bucket is
altered after the scan, the job could encounter delays because we scan for missing or
altered objects.

- For S3 Glacier Flexible Retrieval

It is important to note that AWS Snowball Edge cannot export objects that are in Amazon Glacier storage class. These objects must be restored before
AWS Snowball Edge can successfully export the objects in the bucket.

## How Snowball Edge local compute and storage jobs work

You can use the local compute and storage functionality of an AWS Snowball Edge device by running AWS EC2-compatible compute instances or Kubernetes containers in Amazon EKS Anywhere on Snow. For compute functionality, data storage is provided by Amazon S3 compatible storage on Snowball Edge.

You can create Amazon S3 buckets on the Snowball Edge devices to store and retrieve objects on premises for applications that require local data access, local data processing, and data residency. Amazon S3 compatible storage on Snowball Edge provides a new storage class, `SNOW`, which uses the Amazon S3 APIs, and is designed to store data durably and redundantly across multiple Snowball Edge devices. You can use the same APIs and features on Snowball Edge buckets that you do on Amazon S3, including bucket lifecycle policies, encryption, and tagging. When the device or devices are returned to AWS, all data created or stored in Amazon S3 compatible storage on Snowball Edge is erased. For more information, see [Local Compute and Storage Only Jobs](computetype.md "computetype.md").

For more information, see [Information about using Snowball Edge devices to provide local compute and storage functionality](computetype.md "computetype.md").

### How Snowball Edge clustered local compute and storage jobs work

A cluster job is a special kind of job for local storage and compute only. It is for
those workloads that require increased data durability and storage capacity. For more
information, see [Information about jobs providing local storage on a cluster of Snowball Edge devices](computetype.md#clusteroption "computetype.md#clusteroption").

###### Note

Like standalone local storage and compute jobs, the data stored in a cluster
can't be imported into Amazon S3 without ordering additional devices as a part of separate
import jobs. If you order these devices, you can transfer the data from the cluster to the
devices and import the data when you return the devices for the import jobs.

Clusters have 3 to 16 AWS Snowball Edge devices, called _nodes_. When you receive the nodes from your regional carrier, connect all the
nodes to power and your network to obtain their IP addresses. You use these IP addresses to
unlock all the nodes of the cluster at once with a single unlock command, using the IP
address of one of the nodes. For more information, see [Configuring and using the Snowball Edge Client](using-client-commands.md "using-client-commands.md").

You can write data to an unlocked cluster by using or using Amazon S3 compatible storage on Snowball Edge
and the data distributed among the other nodes.

When you’re done with your cluster, ship all the nodes back to AWS. When we receive the
cluster node, we perform a complete erasure of the Snowball. This erasure follows the
National Institute of Standards and Technology (NIST) 800-88 standards.

## Snowball Edge videos and blogs

- [Migrating mixed file sizes with the snow-transfer-tool on AWS Snowball Edge devices](https://aws.amazon.com/blogs/storage/migrating-mixed-file-sizes-with-the-snow-transfer-tool-on-aws-snowball-edge-devices/ "https://aws.amazon.com/blogs/storage/migrating-mixed-file-sizes-with-the-snow-transfer-tool-on-aws-snowball-edge-devices/")
- [AWS Snowball Edge Data Migration](https://d1.awsstatic.com/whitepapers/snowball-edge-data-migration-guide.pdf "https://d1.awsstatic.com/whitepapers/snowball-edge-data-migration-guide.pdf")
- [AWS OpsHub for Snow Family](https://www.youtube.com/watch?v=_A3A47Vuu0I "https://www.youtube.com/watch?v=_A3A47Vuu0I")
- [Novetta delivers IoT and Machine Learning to the edge for disaster response](https://aws.amazon.com/blogs/storage/novetta-delivers-iot-and-machine-learning-to-the-edge-for-disaster-response/ "https://aws.amazon.com/blogs/storage/novetta-delivers-iot-and-machine-learning-to-the-edge-for-disaster-response/")
- [Enable large-scale database migrations with DMS and AWS Snowball Edge](https://aws.amazon.com/blogs/storage/enable-large-scale-database-migrations-with-aws-dms-and-aws-snowball/ "https://aws.amazon.com/blogs/storage/enable-large-scale-database-migrations-with-aws-dms-and-aws-snowball/")
- [Data Migration Best Practices with AWS Snowball Edge](https://aws.amazon.com/blogs/storage/data-migration-best-practices-with-snowball-edge/ "https://aws.amazon.com/blogs/storage/data-migration-best-practices-with-snowball-edge/")
- [AWS Snowball Edge resources](https://aws.amazon.com/snowball/resources/ "https://aws.amazon.com/snowball/resources/")
- [Amazon S3 Compatible Storage on AWS Snowball Edge Compute Optimized Devices Now Generally Available](https://aws.amazon.com/blogs/aws/amazon-s3-compatible-storage-on-aws-snowball-edge-compute-optimized-devices-now-generally-available/ "https://aws.amazon.com/blogs/aws/amazon-s3-compatible-storage-on-aws-snowball-edge-compute-optimized-devices-now-generally-available/")
- [Getting started with Amazon S3 compatible storage on Snowball Edge on AWS Snowball Edge devices](https://aws.amazon.com/blogs/storage/getting-started-with-amazon-s3-compatible-storage-on-snowball-edge-devices/ "https://aws.amazon.com/blogs/storage/getting-started-with-amazon-s3-compatible-storage-on-snowball-edge-devices/")
