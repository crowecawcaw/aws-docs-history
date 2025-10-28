# Managing throughput capacity

FSx for ONTAP configures throughput capacity when you create the file system. You can modify
your file system's throughput capacity at any time. Keep in mind that your file system
requires a specific configuration to achieve the maximum amount of throughput capacity. For example, to provision 4 GBps
of throughput capacity for a first-generation file system, your file system requires a configuration with a minimum
of 5,120 GiB of SSD storage capacity and 160,000
SSD IOPS. For more information, see [Impact of throughput capacity on
performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").

Throughput capacity is one factor that
determines the speed at which the file server that's hosting the file system can serve the file
data. Higher levels of throughput capacity come with higher levels of network, disk read I/O
operations per second (IOPS), and data caching capacity on the file server. For more
information, see [Amazon FSx for NetApp ONTAP performance](performance.md "performance.md").

When you modify your file system's throughput capacity, Amazon FSx switches out the file server
that's powering your file system. Both Single-AZ and Multi-AZ file systems experience an automatic failover and failback
during this process, which typically takes a few minutes to complete. The failover and failback
processes are transparent to NFS (Network File Sharing), SMB (Server Message Block), and iSCSI
(Internet Small Computer Systems Interface) clients, allowing your workloads to continue running
without interruption or manual intervention. You are billed for the new amount of throughput
capacity once it's available to your file system.

###### Note

To ensure data integrity during maintenance activity, FSx for ONTAP closes all opportunistic
locks and completes any pending write operations to the underlying storage volumes that are
hosting your file system before maintenance begins. During a scheduled file system maintenance
window, system modifications (such as modifications to your throughput capacity) may be
delayed. System maintenance can cause these changes to queue up until they are processed. For
more information, see [Optimizing performance with Amazon FSx maintenance windows](maintenance-windows.md "maintenance-windows.md").

###### Topics

- [When to modify throughput
  capacity](#when-to-modify-throughput-capacity "#when-to-modify-throughput-capacity")
- [How concurrent requests are handled](#concurrent-throughput-and-storage-requests "#concurrent-throughput-and-storage-requests")
- [Updating throughput capacity](increase-throughput-capacity.md "increase-throughput-capacity.md")
- [Monitoring throughput capacity
  changes](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md")

## When to modify throughput

capacity

Amazon FSx integrates with Amazon CloudWatch, which helps you to monitor your file system's ongoing
throughput usage levels. The throughput and IOPS performance that you can drive through your
file system depends on your specific workload’s characteristics, in addition to your file
system’s throughput capacity. As a rule, you should provision enough throughput capacity to
support your workload's read throughput plus twice your workload's write throughput. You can
use CloudWatch metrics to determine which of these dimensions to change to improve performance. For
more information, see [Monitoring in the Amazon FSx console](monitor-throughput-cloudwatch.md "monitor-throughput-cloudwatch.md").

## How concurrent requests are handled

For first-generation file systems, you can request a throughput capacity update just before an SSD storage capacity and
provisioned IOPS update workflow begins or while it is in progress. The sequence of
how Amazon FSx handles the two requests is as follows:

- If you submit an SSD/IOPS update and throughput capacity update at the same time, both
  requests are accepted. The SSD/IOPS update is prioritized before the throughput capacity
  update.
- If you submit a throughput capacity update while an SSD/IOPS update is in progress, the
  throughput capacity update request is accepted and queued to occur after the SSD/IOPS
  update. The throughput capacity update starts after SSD/IOPS is updated (new values are
  available) and during the optimization step. This typically takes less than 10
  minutes.
- If you submit a SSD/IOPS update while a throughput capacity update is in progress, the
  SSD/IOPS storage update request is accepted and queued to start after the throughput
  capacity update has completed (new throughput capacity is available). This typically takes
  20 minutes.

Consider the following points when requesting a throughput capacity update for second-generation file systems:

- You must wait a minimum of six hours between updating the throughput capacity for second-generation file systems.
- The throughput capacity cooldown period is shared with SSD/IOPS scaling.
- Throughput capacity scaling and SSD/IOPS scaling can't be done simulatenously or queued while either is in progress.
- You can't add high-availability (HA) pairs in conjunction with or while throughput capacity scaling or SSD/IOPS scaling are in progress. However, adding
  HA pairs doesn't share a cooldown with SSD/IOPS scaling and throughput capacity scaling. For more information, see [Adding high-availability (HA) pairs](adding-HA-pairs.md "adding-HA-pairs.md").

For more information on SSD storage and provisioned IOPS updates,
see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").
