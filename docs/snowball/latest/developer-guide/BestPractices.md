Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Best practices for using a Snowball Edge device

To help get the maximum benefit and satisfaction with your AWS Snowball Edge device, we recommend
that you follow these best practices.

## Security recommendations for Snowball Edge

The following are recommendations and best practices for maintaining security while
working with an AWS Snowball Edge device.

###### General

Security

- If you notice anything that looks suspicious about the AWS Snowball Edge device, don't
  connect it to your internal network. Instead, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/"), and a new
  AWS Snowball Edge device will be shipped to you.
- We recommend that you don't save a copy of the unlock code in the same
  location on the workstation as the manifest for that job. Saving these in
  different locations helps prevent unauthorized parties from gaining access to
  the AWS Snowball Edge device. For example, you can save a copy of the manifest to your
  local server, and email the code to a user that unlocks the device. This
  approach limits access to the AWS Snowball Edge device to individuals who have access to
  files saved on the server and the user's email address.
- The credentials displayed, when you run the Snowball Edge client commands
  list-access-keys and get-secret-access-key, are a pair of access keys used to
  access your device.

These keys are only associated with the job and the local resources on the
device. They don't map to your AWS account or any other AWS account. If you try to use these keys to access services and
resources in the AWS Cloud, they will fail because they only work
for the local resources associated with your job.

- If you feel your credentials are lost or have been compromised, request a new manifest file and unlock code by following the process to update the device's SSL certificate. See [Updating the SSL certificate on Snowball Edge devices](update-ssl-cert.md "update-ssl-cert.md").

For information about how to use AWS Identity and Access Management (IAM) policies to control access, see [AWS-Managed (Predefined)
Policies for AWS Snowball Edge](authentication-and-access-control.md#access-policy-examples-aws-managed "authentication-and-access-control.md#access-policy-examples-aws-managed").

###### Network

Security

- We recommend that you only use one method at a time for reading and writing data
  to a local bucket on an AWS Snowball Edge device.
- To prevent corrupting your data, don't disconnect the AWS Snowball Edge device or change its
  network settings while transferring data.
- Files that are being written to on the device should be in a static state. Files
  that are modified while they are being written to can result in read/write
  conflicts.
- For more information about improving performance of your AWS Snowball Edge device, see [Recommendations for best data transfer performance to or from a Snowball Edge](#performance "#performance").

## Best practices for managing resources of a Snowball Edge

Consider the following best practices for managing jobs and resources on your
AWS Snowball Edge device.

- The 15 free days for performing your on-premises data
  transfer start the day after the AWS Snowball Edge device arrives at your data center. This
  applies only to Snowball Edge device types.
- The **Job created** status is the only status in which you
  can cancel a job. When a job changes to a different status, you can't cancel the
  job. This applies to clusters.
- For import jobs, don't delete your local copies of the transferred data until
  the import into Amazon S3 is successful. As part of your process, be sure to verify
  the results of the data transfer.

## Recommendations for best data transfer performance to or from a Snowball Edge

###### Note

The data transfer performance you experience will vary based on the network environment, operating systems, copy method, protocol, source data read performance, and dataset characteristics such as file size. To determine the accurate data transfer rates and data transfer times, we recommend you to measure performance through proof-of-concept testing in your environment.

Following, you can find recommendations and information about AWS Snowball Edge device
performance. This section describes performance in general terms, because on-premises
environments have a different way of doing things—different network technologies,
different hardware, different operating systems, different procedures, and so on.

The following table outlines how your network's transfer rate impacts how long it
takes to fill a Snowball Edge device with data. Transferring smaller files reduces
your transfer speed due to increased overhead. If you have many small files, we
recommend that you zip them up into larger archives before transferring them onto a
Snowball Edge device.

| Rate (MB/s) | 82 TB transfer time |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 800         | 1.22 days           |
| 450         | 2.11 days           |
| 400         | 2.37 days           |
| 300         | 3.16 days           |
| 277         | 3.42 days           |
| 200         | 4.75 days           |
| 100         | 9.49 days           |
| 60          | 15.53 days          |
| 30          | 31.06 days          |
| 10          | 85.42 days          | To provide meaningful guidance about performance, the following sections describe how to determine when to use the AWS Snowball Edge device and how to get the most out of the service. The following practices are highly recommended, because they have the largest impact on improving the performance of your data transfer: <br>• We recommend that you have no more than 500,000 files or directories within each directory. <br>• We recommend that all files transferred to a Snowball Edge device be no smaller than 1 MB in size. <br>• If you have many files smaller than 1 MB in size, we recommend that you zip them up into larger archives before transferring them onto a Snowball Edge device. ### Improving speed of data transfer to and from a Snowball Edge One of the best ways that you can improve the performance of an AWS Snowball Edge device is to speed up the transfer of data going to and from a device. In general, you can improve the transfer speed from your data source to the device in the following ways. This following list is ordered from largest to smallest positive impact on performance: 1. **Perform multiple write operations at one time** – To do this, run each command from multiple terminal windows on a computer with a network connection to a single AWS Snowball Edge device. 2. **Transfer small files in batches** – Each copy operation has some overhead because of encryption. To speed up the process, batch files together in a single archive. When you batch files together, they can be auto-extracted when they are imported into Amazon S3. For more information, see [Batching small files to improve data transfer performance to Snowball Edge](batching-small-files.md "batching-small-files.md"). 3. **Don't perform other operations on files during transfer** – Renaming files during transfer, changing their metadata, or writing data to the files during a copy operation has a negative impact on transfer performance. We recommend that your files remain in a static state while you transfer them. 4. **Reduce local network use** – Your AWS Snowball Edge device communicates across your local network. So you can improve data transfer speeds by reducing other local network traffic between the AWS Snowball Edge device, the switch it's connected to, and the computer that hosts your data source. 5. **Eliminate unnecessary hops** – We recommend that you set up your AWS Snowball Edge device, your data source, and the computer running the terminal connection between them so that they're the only machines communicating across a single switch. Doing so can improve data transfer speeds. |
