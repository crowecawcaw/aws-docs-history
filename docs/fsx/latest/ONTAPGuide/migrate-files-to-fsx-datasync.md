# Migrating to FSx for ONTAP using

AWS DataSync

We recommend using AWS DataSync to transfer data between FSx for ONTAP file systems and non-ONTAP file
systems, including FSx for Lustre, FSx for OpenZFS, FSx for Windows File Server, Amazon EFS, Amazon S3, and on-premises filers.
If you're transferring files between FSx for ONTAP and NetApp ONTAP, we recommend using
[NetApp SnapMirror](migrating-fsx-ontap-snapmirror.md "migrating-fsx-ontap-snapmirror.md"). AWS DataSync is a
data transfer service that simplifies, automates, and accelerates moving and replicating data
between self-managed storage systems and AWS storage services over the internet or
Direct Connect. DataSync can transfer your file system data and metadata, such as ownership, timestamps,
and access permissions.

You can use DataSync to transfer files between two FSx for ONTAP file systems, and also move data to
a file system in a different AWS Region or AWS account. You can
also use DataSync with FSx for ONTAP file systems for other tasks. For example, you can perform
one-time data migrations, periodically ingest data for distributed workloads, and schedule
replication for data protection and recovery.

In DataSync, a _location_ is an endpoint
for an FSx for ONTAP file system. For information about specific transfer scenarios, see
[Working with
locations](../../../datasync/latest/userguide/working-with-locations.md "../../../datasync/latest/userguide/working-with-locations.md") in the _AWS DataSync User Guide_.

###### Note

If you plan to use the `All` tiering policy to migrate your data to the capacity pool tier, keep in mind that
file metadata is always stored on the SSD tier, and that all new user data is first written to the SSD tier. When data is written to
the SSD tier, the background tiering process will begin tiering your data to capacity pool storage, but the tiering process is not
immediate and consumes network resources. You need to size your SSD tier to account for file metadata (3-7% of the size of user data),
as a buffer for user data before it is tiered to capacity pool storage. We recommend that you do not exceed 80% SSD utilization.

While migrating data, be sure to monitor your SSD tier using [CloudWatch File system metrics](file-system-metrics.md "file-system-metrics.md")
to ensure that it is not filling faster than the tiering process can move data to the capacity pool storage. You can also throttle
DataSync transfers to a rate that is lower than the rate that tiering is occurring to ensure that your SSD tier does not exceed 80% utilization.
For example, for file systems with a throughput capacity of at least 512 MBps, a 200 MBps throttle will typically balance out the data
transfer and data tiering rates.

## Prerequisites

To migrate data into your FSx for ONTAP setup, you need a server and network that meet
the DataSync requirements. To learn more, see [Requirements for DataSync](../../../datasync/latest/userguide/requirements.md "../../../datasync/latest/userguide/requirements.md")
in the _AWS DataSync User Guide_.

## Basic steps for migrating files using

DataSync

Transferring files from a source to a destination using DataSync involves the
following basic steps:

- Download and deploy an agent in your environment and activate it (not required if
  transferring between AWS services).
- Create a source and destination location.
- Create a task.
- Run the task to transfer files from the source to the destination.

For more information, see the following topics in the _AWS DataSync User Guide_:

- [Data transfer between self-managed storage and AWS](../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws "../../../datasync/latest/userguide/how-datasync-works.md#onprem-aws")
- [Creating a location for Amazon FSx for NetApp ONTAP](../../../datasync/latest/userguide/create-ontap-location.md "../../../datasync/latest/userguide/create-ontap-location.md")
