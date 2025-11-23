# Migrating existing files to FSx for Windows File Server using

AWS DataSync

We recommend using AWS DataSync to transfer data between FSx for Windows File Server file systems. DataSync is a
data transfer service that simplifies, automates, and accelerates moving and replicating data
between on-premises storage systems and other AWS storage services over the internet or
Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps,
and access permissions.

DataSync supports copying NTFS access control lists (ACLs), and also supports copying file
audit control information, also known as NTFS system access control lists (SACLs), which
are used by administrators to control audit logging of user attempts to access files.

You can use DataSync to transfer files between two FSx for Windows File Server file systems, and also move data to
a file system in a different AWS Region or AWS account. You can
use DataSync with FSx for Windows File Server file systems for other tasks. For example, you can perform
one-time data migrations, periodically ingest data for distributed workloads, and schedule
replication for data protection and recovery.

In AWS DataSync, a _location_ for FSx for Windows File Server is an endpoint
for an FSx for Windows File Server. You can transfer files between a location for FSx for Windows File Server and a location
for other file systems. For information, see [Working with
Locations](../../../datasync/latest/userguide/working-with-locations.md "../../../datasync/latest/userguide/working-with-locations.md") in the _AWS DataSync User Guide_.

DataSync accesses your FSx for Windows File Server using the Server Message Block (SMB) protocol. It
authenticates with the user name and password that you configure in the AWS DataSync console or AWS CLI.

## Prerequisites

To migrate data into your Amazon FSx for Windows File Server setup, you need a server and network that meet
the DataSync requirements. To learn more, see [Requirements for DataSync](../../../datasync/latest/userguide/requirements.md "../../../datasync/latest/userguide/requirements.md")
in the _AWS DataSync User Guide_.

If you are performing a large data migration, or a migration involving many small files, we recommend using an Amazon FSx File System with SSD storage type. This is because DataSync tasks involve scans of
file metadata which can exhaust the disk IOPS limits of HDD file systems, leading to long-running migrations and file system performance impact.
For more information, see: [Best practices for migrating existing file storage to
FSx for Windows File Server](migrate-files-fsx.md#migrate-best-practices "migrate-files-fsx.md#migrate-best-practices").

If your dataset consists of mostly small files, with file counts in the millions,
or if you have more available network bandwidth than a single DataSync task can consume, you can also
accelerate your data transfers with scale out architecture.
For more information, see: [How to accelerate your data transfers with AWS DataSync scale out architectures](https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/ "https://aws.amazon.com/blogs/storage/how-to-accelerate-your-data-transfers-with-aws-datasync-scale-out-architectures/").

You can monitor the disk I/O utilization of your file system using [FSx performance metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Basic steps for migrating files using

DataSync

To transfer files from a source location to a destination location using DataSync, take the
following basic steps:

- Download and deploy an agent in your environment and activate it.
- Create and configure a source and destination location.
- Create and configure a task.
- Run the task to transfer files from the source to the destination.

To learn how to transfer files from an existing on-premises file system to your
FSx for Windows File Server, see
[Data transfer between self-managed storage and AWS](../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws "../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws"),
[Creating a location for SMB](../../../datasync/latest/userguide/create-smb-location.md "../../../datasync/latest/userguide/create-smb-location.md"), and
[Creating a location for Amazon FSx for Windows File Server](../../../datasync/latest/userguide/create-fsx-location.md "../../../datasync/latest/userguide/create-fsx-location.md")
in the _AWS DataSync User Guide_.

To learn how to transfer files from an existing in-cloud file system to your FSx for Windows File Server,
see [Deploy your agent as an Amazon EC2
instance](../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent "../../../datasync/latest/userguide/deploy-agents.md#ec2-deploy-agent") in the _AWS DataSync User Guide_.

## Migrating between two Amazon FSx file systems

You can use DataSync to migrate data between two Amazon FSx file systems. This can be helpful if
you need to move your workload from an existing file system to a new file system with a
different configuration, such as from a Single-AZ to a Multi-AZ configuration. You can also use
DataSync to split your workload between two file systems.

Here is a sample overview of the migration process:

1. Create DataSync locations for the source and destination file systems.
   Note that the source and destination must belong to the same Active Directory (AD) domain, or have an AD trust relationship between their domains.
2. Create and configure a DataSync task to transfer data from the source to the destination.
   You can run the task as a one-time instance, or set the task to run automatically on a
   schedule that you configure.
3. After the task completes successfully, the data in your destination file system is an
   exact copy of your source. Note that you will need to temporarily pause any write activity
   or file updates on your source file system to complete the task. You can then cut over to your destination file system and delete
   the source file system.

Before migrating from your production file system, you can test the migration process on a
file system that's restored from a recent backup. This enables you to estimate how long the
data transfer process takes, and to troubleshoot DataSync errors in advance.

To minimize your cutover time, you can run DataSync tasks in advance, moving the majority of
your data from your source file system to your destination file system. After stopping traffic
to your source file system, you can run one final task transfer to sync any data that’s been newly
updated since you stopped traffic, and then cut over to your destination file system.

You can configure DataSync tasks to only run in certain directories, or to include or exclude
certain paths. This can be useful if you’re running multiple tasks in parallel, or if you want
to migrate a subset of your data.

You can create a DNS alias on your destination file system that's the same as the DNS name
of your source file system. This enables your end-users and applications to continue accessing
file data using the DNS name of your source file system. For more information about how to set
up a DNS alias, see: [Accessing data using DNS aliases](dns-aliases.md "dns-aliases.md").

When performing this type of migration, we recommend the following:

- Schedule your migration to avoid any file system backups, your weekly maintenance window, and `Data Deduplication` jobs. Specifically, we recommend disabling the `Data Deduplication GarbageCollection` job if it coincides with your planned migration.
- Use an SSD storage type for both your source and destination file systems. You can switch
  between HDD and SSD storage types by restoring from backup. For more information see: [Migrating existing file storage to FSx for Windows File Server](migrate-files-fsx.md "migrate-files-fsx.md").
- Configure your source and destination file systems with sufficient throughput capacity
  for the amount of data that you need to transfer. During DataSync task processes, monitor the
  performance utilization of both the source and the destination file systems. For more
  information, see: [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- Set up [DataSync monitoring](../../../datasync/latest/userguide/monitor-datasync.md "../../../datasync/latest/userguide/monitor-datasync.md") to help you understand the progress of ongoing tasks. You can also
  send DataSync logs to the Amazon CloudWatch Logs group to assist you with debugging your tasks if you encounter any errors.
