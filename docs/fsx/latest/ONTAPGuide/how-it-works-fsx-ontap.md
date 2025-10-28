# How Amazon FSx for NetApp ONTAP works

This topic introduces the major features of Amazon FSx for NetApp ONTAP file systems and how they work,
with links to sections with in-depth descriptions, important implementation details, and
step-by-step configuration procedures.

###### Topics

- [FSx for ONTAP file systems](#fsx-ontap-file-system "#fsx-ontap-file-system")
- [Storage virtual machines](#svm-resource "#svm-resource")
- [Volumes](#volume-resource "#volume-resource")
- [Storage tiers](#storage-tiers-intro "#storage-tiers-intro")
- [Storage efficiency](#storage-efficiency-intro "#storage-efficiency-intro")
- [Accessing data stored on FSx for ONTAP file
  systems](#access-ontap-file-systems "#access-ontap-file-systems")
- [Managing FSx for ONTAP resources](#how-to-work-with-fsxontap "#how-to-work-with-fsxontap")

## FSx for ONTAP file systems

A file system is the primary FSx for ONTAP resource, analogous to an on-premises NetApp ONTAP
cluster. You specify the solid state drive (SSD) storage capacity and throughput capacity for
your file system, and choose an Amazon Virtual Private Cloud (VPC) where your file system is created. For more
information, see [Managing FSx for ONTAP file systems](managing-file-systems.md "managing-file-systems.md").

Your file system can have one to 12 high-availability (HA) pairs depending on its configuration. An HA pair
is made up of two file servers in an active-standby configuration. First-generation FSx for ONTAP file systems and second-generation
Multi-AZ file systems support one HA pair. Second-generation Single-AZ file systems support up to 12 HA pairs. For more information, see
[Managing high-availability (HA) pairs](HA-pairs.md "HA-pairs.md").

## Storage virtual machines

A storage virtual machine (SVM) is an isolated file server with its own administrative and data access endpoints
for administering and accessing data. When you access data in your FSx for ONTAP file system, your clients and workstations
interface with an SVM using the SVM's endpoint IP address. For more information, see
[Managing SVMs](managing-svms.md "managing-svms.md").

You can join SVMs to a Microsoft Active Directory for file access authentication and authorization.
For more information, see [Working with Microsoft Active Directory
in FSx for ONTAP](ad-integration-ontap.md "ad-integration-ontap.md").

## Volumes

FSx for ONTAP **volumes** are virtual resources that you use for
organizing and grouping your data. Volumes are logical containers that are hosted on SVMs, and data stored in them
consumes physical storage capacity on your file system.

When you create a volume, you set its size, which determines the amount of physical data that you can store in
it, regardless of which storage tier the data is stored on. You also set the volume type, either
RW (read-writable) or DP (data protection). A DP volume is read-only and can be used as the destination
in a NetApp SnapMirror or SnapVault relationship.

FSx for ONTAP volumes are thin provisioned, meaning that they only consume storage capacity for the data stored in them.
With thin-provisioned volumes, storage capacity is not reserved in advance. Instead, storage is allocated dynamically,
as it is needed. Free space is released back to the file system when data in the volume or LUN is deleted.
For example, you can create three 10 TiB volumes on a file system configured with 10 TiB of free storage capacity,
as long as the total amount of data stored in the three volumes doesn't exceed 10 TiB at any time.
The amount of data physically stored on a volume counts toward your overall storage capacity
consumption. For more information, see [Managing FSx for ONTAP volumes](managing-volumes.md "managing-volumes.md").

## Storage tiers

An FSx for ONTAP file system has two _storage tiers_: primary storage and
capacity pool storage. Primary storage is provisioned, scalable, high-performance SSD storage
that’s purpose-built for the active portion of your data set. Capacity pool storage is a fully
elastic storage tier that can scale to petabytes in size and is cost optimized for
infrequently accessed data. Data that you write to your volumes consumes capacity on your
storage tiers. For more information, see [FSx for ONTAP storage tiers](managing-storage-capacity.md#storage-tiers "managing-storage-capacity.md#storage-tiers"). You can increase the SSD storage capacity of your file system as your storage needs grow. On second-generation file systems, you can also decrease SSD storage capacity when your high-performance storage requirements change, allowing you to optimize storage costs. For more information, see [File system storage capacity and IOPS](storage-capacity-and-IOPS.md "storage-capacity-and-IOPS.md").

### Data tiering

Data tiering is the process by which Amazon FSx for NetApp ONTAP automatically moves data
between the _SSD_ and the _capacity pool_ storage tiers. Each volume has a tiering policy
that controls whether data is moved to the capacity tier when it becomes inactive (cold).
A volume's Tiering policy cooling period determines when data becomes inactive (cold). For more information, see
[Volume data tiering](volume-storage-capacity.md#volume-data-tiering "volume-storage-capacity.md#volume-data-tiering").

## Storage efficiency

Amazon FSx for NetApp ONTAP supports ONTAP’s block-level storage efficiency features—compaction,
compression, and deduplication—to reduce the storage capacity that your data consumes.
Storage efficiency features can reduce the footprint of your data in SSD storage, capacity
pool storage, and backups. The typical storage capacity savings for general purpose file
sharing workloads without sacrificing performance is 65% from compression,
deduplication, and compaction, on both the SSD and capacity pool storage tiers. For more
information, see [Storage efficiency](managing-storage-capacity.md#storage-efficiency "managing-storage-capacity.md#storage-efficiency").

## Accessing data stored on FSx for ONTAP file

systems

You can access your data on FSx for ONTAP volumes from multiple Linux, Windows, or macOS
clients simultaneously over the NFS (v3, v4, v4.1, v4.2) and SMB protocols. You can also
access data using the Non-Volatile Memory Express (NVMe) and Internet Small Computer
Systems Interface (iSCSI) block protocol. For more information, see [Accessing your FSx for ONTAP data](supported-fsx-clients.md "supported-fsx-clients.md").

## Managing FSx for ONTAP resources

There are several ways that you can interact with your FSx for ONTAP file system and manage
its resources. You can manage your FSx for ONTAP resources using both AWS and NetApp ONTAP
management tools:

- AWS management tools
  - The AWS Management Console
  - The AWS Command Line Interface (AWS CLI)
  - The Amazon FSx API and SDKs
  - AWS CloudFormation

- NetApp management tools:
  - NetApp Console
  - The NetApp ONTAP CLI
  - The NetApp ONTAP REST API

For more information, see [Administering resources](administering-file-systems.md "administering-file-systems.md").
