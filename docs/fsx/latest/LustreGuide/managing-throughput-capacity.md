# Managing provisioned throughput capacity

Every FSx for Lustre file system has a throughput capacity that is configured when you create
the file system. For file systems using SSD or HDD storage, the throughput capacity is measured in megabytes per second
per tebibyte (MBps/TiB). For file systems using Intelligent-Tiering storage, the throughput capacity is measured
in megabytes per second (MBps) for the file system. Throughput capacity is one factor that determines the speed
at which the file server hosting the file system can serve file data. Higher levels of throughput capacity also
come with higher levels of I/O operations per second (IOPS) and more memory for caching of data on the file server.
For more information, see
[Amazon FSx for Lustre performance](performance.md "performance.md").

You can modify the throughput tier of a persistent SSD-based file system
by increasing or decreasing the value of the file system's throughput per unit of storage.
Valid values depend on the deployment type of the file system, as follows:

- For Persistent 1 SSD-based deployment types, valid values
  are 50, 100, and 200 MBps/TiB.
- For Persistent 2 SSD-based deployment types, valid values
  are 125, 250, 500, and 1000 MBps/TiB.
  You can modify the throughput capacity of an Intelligent-Tiering file system
  by increasing the value of the total throughput capacity for the file system. Valid values
  are 4,000 MBps or increments of 4,000 MBps, up to a maximum of 2,000,000 MBps.

You can view the current value of the file system's throughput capacity
as follows:

- Using the console – On the **Summary** panel of the
  file system details page, the **Throughput per unit of storage**
  field shows the current value for SSD-based file systems while the **Throughput capacity**
  field shows the current value for Intelligent-Tiering file systems.
- Using the CLI or API – Use the
  [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command or the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation, and look for
  the `PerUnitStorageThroughput` property.
  When you modify your file system's throughput capacity, behind the scenes, Amazon FSx
  switches out the file system's file servers on SSD file systems or adds new file servers on
  Intelligent-Tiering file systems. Your file system will be unavailable for a few minutes
  during throughput capacity scaling. You are billed for the new amount of throughput capacity once
  it is available to your file system.

###### Topics

- [Considerations when
  updating throughput capacity](#throughput-capacity-considerations "#throughput-capacity-considerations")
- [When to modify throughput capacity](#when-to-modify-throughput-capacity "#when-to-modify-throughput-capacity")
- [Modifying throughput capacity](increase-throughput-capacity.md "increase-throughput-capacity.md")
- [Monitoring throughput capacity
  changes](monitoring-throughput-capacity-changes.md "monitoring-throughput-capacity-changes.md")

## Considerations when

updating throughput capacity

Here are a few important items to consider when updating throughput capacity:

- **Increase or decrease** – You can
  increase or decrease the amount of throughput capacity for an SSD-based file system. You can
  only increase the amount of throughput capacity for an Intelligent-Tiering file system.
- **Update increments** – When
  you modify throughput capacity, use the increments listed in the
  **Update throughput tier** dialog box for SSD-based file systems or in the
  **Update throughput capacity** dialog box for Intelligent-Tiering
  file systems.
- **Time between increases** – You
  can't make further throughput capacity changes on a file system until 6 hours
  after the last request, or until the throughput optimization process has completed,
  whichever time is longer.
- **Automatic scaling of SSD read cache** –
  For the SSD read cache default mode (Proportional to throughput capacity), Amazon FSx automatically
  provisions 5 GiB of data storage for every MBps of throughput capacity you provision. As
  you scale your file system’s throughput capacity, Amazon FSx automatically scales your SSD data
  cache by attaching additional cache storage to any newly added file servers.
- **Deployment type** – You can only
  update the throughput capacity of persistent SSD-based or Intelligent-Tiering deployment types. You
  cannot modify the throughput capacity of EFA-enabled SSD-based file systems.

## When to modify throughput capacity

Amazon FSx integrates with Amazon CloudWatch, enabling you to monitor your file system's ongoing
throughput usage levels. The performance (throughput and IOPS) that you can drive through your
file system depends on your specific workload’s characteristics, in addition to your file
system’s throughput capacity, storage capacity, and storage class. For information about how
to determine your file system's current throughput,
see [How to use Amazon FSx for Lustre CloudWatch metrics](how_to_use_metrics.md "how_to_use_metrics.md"). For information
about CloudWatch metrics,
see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
