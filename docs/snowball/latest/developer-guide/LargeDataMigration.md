AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Large

data migration with Snowball Edge

Large data migration from on-premises locations requires careful planning, orchestration, and execution to ensure that your data is successfully migrated to AWS.

We recommend that you have a data migration strategy in place before starting your
migration to avoid the potential for missed deadlines, exceeding budgets and migration
failures. AWS Snow services helps you to place, order, and track your large data migration
projects via the Snowball Edge Large Data Migration Manager (LDMM) feature in the AWS Snow Family Management Console.

The topics, [Planning your large transfer with Snowball Edge](#copy-general-planning "#copy-general-planning")
and [Calibrating a large transfer with Snowball Edge](calibrating-large-transfer.md "calibrating-large-transfer.md")
describe a manual data migration process. You can streamline the manual steps using the Snowball Edge LDMM migration plan.

###### Topics

- [Planning your large transfer with Snowball Edge](#copy-general-planning "#copy-general-planning")
- [Calibrating a large transfer with Snowball Edge](calibrating-large-transfer.md "calibrating-large-transfer.md")
- [Creating a large data migration
  plan with Snowball Edge](create-data-migration-plan.md "create-data-migration-plan.md")
- [Using the large data migration
  plan with Snowball Edge](understanding-data-migration-plan.md "understanding-data-migration-plan.md")

## Planning your large transfer with Snowball Edge

We recommend that you plan and calibrate large data transfers between the
AWS Snowball Edge devices that you have on site and your servers using the guidelines
in the following sections.

###### Topics

- [Step 1: Understand what you're moving to
  the cloud](#understand-the-transfer "#understand-the-transfer")
- [Step 2: Calculate your target transfer rate](#calculate-rate "#calculate-rate")
- [Step 3: Determine how many Snowball Edge you need](#number-of-snowballs "#number-of-snowballs")
- [Step 4: Create your jobs](#make-jobs "#make-jobs")
- [Step 5: Separate your data into transfer segments](#prepare-segments "#prepare-segments")

### Step 1: Understand what you're moving to

the cloud

Before you create your first job using the AWS Snow Family Management Console, ensure that you assess the volume of data you need to transfer, where it is currently stored, and the
destination that you want to transfer it to. For data transfers that are a petabyte
in scale or larger, this administrative housekeeping makes it much easier when your
Snowball Edge arrive.

If you're migrating data into the AWS Cloud for the first time, we
recommend that you design a cloud migration model. Cloud migration doesn’t happen
overnight. It requires a careful planning process to ensure that all systems work as
expected.

When you're done with this step, you should know the total amount of data that
you're going to move into the cloud.

### Step 2: Calculate your target transfer rate

It's important to estimate how quickly you can transfer data to the Snowball Edge that are connected to each of your servers. This estimated speed in MB/Sec determines how fast you can transfer the data from your data source to Snowball Edge devices using your local network infrastructure.

###### Note

For large data transfers, we recommend using the Amazon S3 data transfer method. You must select this option when the you order devices in the AWS Snow Family Management Console.

To determine a baseline transfer rate, transfer a small subset of your data to the Snowball Edge device, or transfer a 10 GB sample file and observe the throughput.

While determining your target transfer speed, keep in mind that you can improve the throughput by tuning your environment, including network configuration, by changing the network speed, the size of the files being transferred, and
the speed at which data can be read from your local servers. The Amazon S3 adapter
copies data to Snowball Edge as quickly as your conditions allow.

### Step 3: Determine how many Snowball Edge you need

Using the total amount of data that you plan to move into the cloud, the estimated transfer speed, and the number of days that you want to allow to move the data into AWS, determine how many Snowball Edge you need for your large-scale data migration. Depending on the device type, Snowball Edge devices have approximately 39.5 TB or 210 TB of usable storage space. For example, if you want to move 300 TB of data to AWS over 10 days and you have a transfer speed of 250 MB/s, you need 2 Snowball Edge devices with 210 TB of storage.

###### Note

The Snowball Edge LDMM provides a wizard to estimate the number of Snowball Edge that can be supported concurrently. For more information, see [Creating a large data migration
plan with Snowball Edge](create-data-migration-plan.md "create-data-migration-plan.md").

### Step 4: Create your jobs

After you know how many Snowball Edge you need, you need to create an
import job for each device. Creation of multiple jobs are simplified by the Snowball Edge LDMM. For more information,
see [Placing your next job order](understanding-data-migration-plan.md#placing-next-job-order "understanding-data-migration-plan.md#placing-next-job-order").

###### Note

You can place your next job order and automatically add it to your plan directly from the **Recommended job ordering** schedule. For more information, see [Recommended job ordering schedule](understanding-data-migration-plan.md#job-ordering-schedule "understanding-data-migration-plan.md#job-ordering-schedule").

### Step 5: Separate your data into transfer segments

As a best practice for large data transfers involving multiple jobs, we recommend
that you logically split your data into a number of smaller, more manageable data sets. This allows you to transfer each partition at a time, or multiple partitions
in parallel. When planning your partitions, make sure that the data for the partitions
combined fit on the Snowball Edge for the job. For example, you can separate your
transfer into partitions in any of the following ways:

- You can create 10 partitions of 20 TB each for use with a Snowball Edge device with 210 TB of storage, for example.
- For large files, each file can be an individual partition up to the 5 TB
  size limit for objects in Amazon S3.
- Each partition can be a different size, and each individual partition can be
  made up of the same kind of data—for example, small files in one
  partition, compressed archives in another, large files in another partition, and
  so on. This approach can help you to determine your average transfer rate
  for different types of files.

###### Note

Metadata operations are performed for each file that's transferred. Regardless
of a file's size, this overhead remains the same. Therefore, you get faster
performance by compressing small files into a larger bundle, batching your
files, or transferring larger individual files.

Creating data transfer segments can make it easier for you to quickly resolve
transfer issues because trying to troubleshoot a large, heterogeneous transfer after
the transfer runs for a day or more can be complex.

When you've finished planning your petabyte-scale data transfer, we recommend that
you transfer a few segments onto the Snowball Edge device from your server to calibrate
your speed and total transfer time.
