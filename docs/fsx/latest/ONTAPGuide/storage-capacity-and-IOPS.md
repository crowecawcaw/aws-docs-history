# File system storage capacity and IOPS

When you create an FSx for ONTAP file system, you specify the storage capacity of the
SSD tier. For second-generation Single-AZ file systems, the storage capacity that you specify is spread evenly among
the storage pools of each high-availability (HA) pair; these storage pools are called
_aggregates_.

For each GiB of SSD storage that you provision, Amazon FSx automatically provisions
3 SSD input/output operations per second (IOPS) for the file system, up to a maximum of
160,000 SSD IOPS per file system. For second-generation Single-AZ file systems, your SSD IOPS are spread
evenly across each of your file system's aggregates. You have the option to specify a level
of provisioned SSD IOPS above the automatic 3 SSD IOPS per GiB. For more information about
the maximum number of SSD IOPS that you can provision for your FSx for ONTAP file system, see
[Impact of throughput capacity on
performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").

###### Topics

- [Updating file system SSD storage and IOPS](#increase-primary-storage "#increase-primary-storage")
- [When to increase SSD storage capacity](#when-to-increase-ssd-capacity "#when-to-increase-ssd-capacity")
- [Increasing SSD storage capacity](#increasing-ssd-capacity "#increasing-ssd-capacity")
- [Considerations for increasing SSD storage capacity](#increasing-considerations "#increasing-considerations")
- [When to decrease SSD storage capacity](#when-to-decrease-ssd-storage-capacity "#when-to-decrease-ssd-storage-capacity")
- [Decreasing SSD storage capacity](#decreasing-ssd-capacity "#decreasing-ssd-capacity")
- [Considerations for decreasing SSD storage capacity](#decreasing-considerations "#decreasing-considerations")
- [Limitations for decreasing SSD storage capacity](#decreasing-limitations "#decreasing-limitations")
- [Creating a storage capacity utilization alarm for your file system](alarm-low-primary-storage.md "alarm-low-primary-storage.md")
- [Updating storage capacity and provisioned IOPS](increase-storage-capacity.md "increase-storage-capacity.md")
- [Updating storage capacity dynamically](automate-storage-capacity-increase.md "automate-storage-capacity-increase.md")
- [Monitoring SSD storage utilization](monitor-fs-storage-console.md "monitor-fs-storage-console.md")
- [Monitoring storage efficiency savings](view-storage-efficiency.md "view-storage-efficiency.md")
- [Monitoring storage capacity and IOPS updates](monitoring-storage-capacity-increase.md "monitoring-storage-capacity-increase.md")

## Updating file system SSD storage and IOPS

When you need additional storage for the active portion of your data set, you can
increase the SSD storage capacity of your Amazon FSx for NetApp ONTAP file system. For second-generation
file systems, you can even decrease SSD storage capacity to match your workload's changing
storage needs. Use the Amazon FSx console, Amazon FSx API, or AWS Command Line Interface (AWS CLI) to increase or decrease
the SSD storage capacity. For more information, see
[Updating storage capacity and provisioned IOPS](increase-storage-capacity.md "increase-storage-capacity.md").

## When to increase SSD storage capacity

If you're running out of available SSD tier storage, we recommend that
you increase the storage capacity of your file system. Running out of storage
indicates that your SSD tier is undersized for the active portion of your data
set.

To monitor the amount of free storage that's available on the file
system, use the file system-level `StorageCapacity` and
`StorageUsed` Amazon CloudWatch metrics. You can create a CloudWatch alarm on a
metric and be notified when it drops below a specific threshold. For more
information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

###### Note

We recommend that you don't exceed 80% SSD storage capacity
utilization to ensure that data tiering, throughput scaling, and
other maintenance activities function properly, and that there
is capacity available for additional data. For second-generation file systems, this
recommendation applies to both the average utilization across all of your file system's
aggregates and to each individual aggregate.

For more information about how a file system's SSD storage is used and
how much SSD storage is reserved for file metadata and operating software, see
[Choosing the right amount of file system SSD storage](managing-storage-capacity.md#choose-ssd-capacity "managing-storage-capacity.md#choose-ssd-capacity").

## Increasing SSD storage capacity

When you increase the SSD storage capacity of your Amazon FSx file system, the new capacity is
typically available for use within minutes. You're billed for the new SSD storage capacity after
it becomes available to you. For more information, see
[Amazon FSx for NetApp ONTAP Pricing](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "https://aws.amazon.com/fsx/netapp-ontap/pricing/") and
[AWS billing and usage reports for FSx for ONTAP](FSxONTAP-Billing.md "FSxONTAP-Billing.md").

After you increase your storage capacity, Amazon FSx runs a storage optimization
process in the background to rebalance your data. For most file systems, storage
optimization takes a few hours with minimal noticeable impact to your workload
performance.

You can track the progress of the storage optimization process at any time by using the Amazon FSx
console, AWS CLI, and API. For more information, see
[Monitoring storage capacity and IOPS updates](monitoring-storage-capacity-increase.md "monitoring-storage-capacity-increase.md").

## Considerations for increasing SSD storage capacity

Here are a few important items to consider when increasing your file system's SSD storage capacity
and IOPS:

- **(First-generation file systems only) Storage capacity increase only** –
  You can only increase the amount of SSD storage capacity for a file system; you can't decrease the storage capacity.
- **Storage capacity minimum increase** –
  Each SSD storage capacity increase must be a minimum of 10% of the file system's current SSD storage capacity,
  up to the maximum SSD storage capacity for your file system's configuration.
- **Time between increases** – After increasing SSD storage capacity, provisioned IOPS, or throughput capacity on a file system,
  you must wait at least six hours before modifying any of these configurations on the same file system again.
  This is sometimes referred to as a cooldown period.
- **Provisioned IOPS modes** –
  For a provisioned IOPS change, you must specify one of the two IOPS modes:
  - **Automatic** mode – Amazon FSx automatically scales your SSD IOPS to maintain 3 provisioned SSD IOPS per GiB of SSD storage capacity,
    up to the maximum SSD IOPS for your file system configuration.

  ###### Note

  For more information about the maximum number of SSD IOPS that you can provision for your FSx for ONTAP file system,
  see [Impact of throughput capacity on
  performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").
  - **User-provisioned** mode – You specify the number of SSD IOPS,
    which must be greater than or equal to 3 IOPS per GiB of SSD storage capacity.
    If you choose to provision a higher level of IOPS, you pay for the average IOPS provisioned above your included rate for the month,
    which is measured in IOPS-months.

For more information about pricing, see [Amazon FSx for NetApp ONTAP Pricing](https://aws.amazon.com/fsx/netapp-ontap/pricing/ "https://aws.amazon.com/fsx/netapp-ontap/pricing/").

##

When to decrease SSD storage capacity

You might want to decrease your FSx for ONTAP second-generation file system's SSD storage
capacity in scenarios such as the following:

- After completing project-based workloads where high-performance storage is no longer
  needed
- After completing large-scale data migrations where temporary extra capacity was used
  to accelerate data ingestion

## Decreasing SSD storage capacity

When you decrease SSD storage capacity of your file system, Amazon FSx attaches a new, smaller
set of disks (aggregate) to each of your file system's HA pairs. Amazon FSx then runs a storage
optimization process in the background to move data on a per-volume basis from the old disks to the new disks. After data in each volume has been moved, Amazon FSx redirects client access to volumes on the new disks. Amazon FSx then detaches the old disks from your file system.

You are billed for the existing and newly requested size of your SSD tier throughout
the SSD decrease operation. For example, when you decrease SSD storage capacity from
10 tebibytes (TiB) to 5 TiB, you are billed for 15 TiB during the SSD decrease operation
and 5 TiB after the SSD decrease operation is complete. For more information about
billing, see [AWS billing and usage reports for FSx for ONTAP](FSxONTAP-Billing.md "FSxONTAP-Billing.md").

Decreasing SSD storage capacity can take between a few hours and a few weeks depending on
factors such as the amount of data stored on your file system, the amount of
net-new writes driven to your file system during the decrease operation, and the amount of
network and disk resources available on the file system.

During the decrease operation, your data remains available for reads and writes. Most workloads
experience minimal performance impact, though write-heavy workloads might experience temporary performance
degradation. Brief I/O pauses (up to 60 seconds) might occur as client access is redirected to
the new disks for each volume.

To minimize performance impact, you should maintain adequate headroom in your file system by ensuring that ongoing workloads don't consistently consume more than 50% CPU, 50% disk throughput, or 50% SSD IOPS before initiating an SSD decrease operation.
You can monitor these utilization metrics in the **Monitoring & performance**
tab of your file system in the Amazon FSx console.

###### Note

If your SSD storage tier exceeds 80% utilization during the decrease operation,
Amazon FSx pauses the operation and automatically resumes it after utilization falls
below 80%. To decrease SSD utilization on the new disks, you can either tier data
to capacity pool or delete data from volumes for which client access has been
successfully redirected to the new set of disks.

If you need additional SSD capacity during a decrease operation, you can submit a request
to increase SSD capacity by calling [`update-file-system`](../../../cli/latest/reference/fsx/update-file-system.md "../../../cli/latest/reference/fsx/update-file-system.md")
in the AWS CLI or the equivalent [UpdateFileSystem](../APIReference/API_UpdateFileSystem.md "../APIReference/API_UpdateFileSystem.md") API operation
and providing a new target value. Amazon FSx prioritizes completing the SSD increase request, so
that the new SSD capacity is available for use within minutes before resuming the SSD decrease
operation.

## Considerations for decreasing SSD storage capacity

Here are a few important items to consider when decreasing a file system's SSD storage capacity and provisioned IOPS:

- **Increasing storage capacity during a decrease operation**
  – You can increase SSD storage capacity of your file system even while a decrease
  operation is in progress. This flexibility allows you to ensure performance and availability
  in case any of your aggregates fill up during the decrease operation. If you increase SSD
  capacity to a size lower than the original capacity, Amazon FSx only adjusts the size of the
  newly requested (target) aggregate. However, if you increase the SSD capacity to a size
  greater than the original, Amazon FSx increases the size of both aggregates to match the new
  target value. For example, if you're decreasing storage capacity from 10,000 GiB to
  5,000 GiB, and then request an increase to 7,000 GiB, only the target aggregate is
  increased to 7,000 GiB, resulting in a final SSD storage capacity of 7,000 GiB for your
  file system. But if you request an increase to 12,000 GiB, both aggregates are increased
  to 12,000 GiB. We suggest careful planning to avoid a scenario in which you have to increase SSD capacity to a size equal to or larger than the original SSD capacity.
- **Pausing SSD decrease** – Amazon FSx pauses an SSD decrease operation if you exceed 80% utilization on the new aggregate and automatically resumes the decrease operation once utilization falls below 80%.
- **(Second-generation Single-AZ file systems only) Storage capacity spread** – The new storage capacity or SSD IOPS that you select for your file system is spread evenly across each of your file system's aggregates.
- **Patching during storage capacity decrease** – Amazon FSx aborts moving data for a volume if your file system is patched during an SSD decrease operation. As a result, you may lose progress on the SSD decrease operation if a patch occurs during the operation. Amazon FSx automatically restarts the `vol move` after the patch operation is complete.
- **Provisioned IOPS modes** – For a provisioned IOPS change, you must specify one of the two IOPS modes:
  - **Automatic** mode – Amazon FSx automatically scales your SSD IOPS to maintain 3 provisioned SSD IOPS per GiB of SSD storage capacity, up to the maximum SSD IOPS for your file system configuration. When decreasing SSD capacity, your automatic SSD IOPS will scale down proportionally.

  ###### Note

  For more information about the maximum number of SSD IOPS that you can provision for your
  FSx for ONTAP file system, see [Impact of throughput capacity on
  performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").
  - **User-provisioned** mode – You must provide an IOPS value
    that is equal to or higher than your currently provisioned IOPS. When decreasing SSD
    capacity, you can retain additional user-provisioned SSD IOPS as long as they don't
    exceed the maximum SSD IOPS supported by the smaller aggregate (50 IOPS per GB of
    requested SSD capacity). If your provisioned IOPS are higher than the maximum supported
    by the smaller aggregate, reduce IOPS before decreasing SSD capacity.

## Limitations for decreasing SSD storage capacity

The following limitations apply while decreasing SSD storage capacity of your file system:

- **(Second-generation file systems only) Storage capacity decrease** – You can decrease the storage capacity only on second-generation file systems.
- **Storage capacity minimum decrease** – Each SSD storage capacity decrease must be a minimum of 9 percent of the file system's current SSD storage capacity.
  The decrease should also ensure that your file system's resulting SSD capacity does not exceed 80% utilization after the decrease operation. For example, if your file system has 10,000 GiB of storage capacity and 5,000 GiB of storage used,
  you can decrease storage capacity down to 6,251 GiB such that your SSD utilization remains under 80%. You can decrease SSD storage capacity down to the minimum supported size of 1,024 GiB per HA pair.
- To decrease SSD storage capacity on file systems that contain one or more volumes with more than 50 TiB of data in the SSD tier, you must provision at least 1,536 MB/s of throughput capacity per HA pair. If any volume contains more than 100 TiB of data in the SSD tier, you must provision at least 3,072 MB/s of throughput capacity per HA pair. For volumes with more than 200 TiB of data in the SSD tier, you must provision 6,144 MB/s of throughput capacity per HA pair.
- **Time between updates** – After modifying SSD storage capacity,
  provisioned IOPS, or throughput capacity on a file system, you must wait at least six hours before modifying any
  of these configurations on the same file system again. This is sometimes referred to as a cooldown period.
- You can increase but not decrease throughput capacity for your file system
- You cannot add HA pairs to your file system
- You cannot revert a volume to a previous state (using `volume snapshot restore`) while data in
  that volume is being moved to the new aggregate. However, you can run `volume snapshot restore`
  on other volumes that aren't being moved currently.
- You cannot offline volumes, move volumes, create FlexClones, create SnapLock volumes,
  or modify storage efficiency settings of volumes during the decrease operation.
