# Managing storage capacity

You can increase the SSD or HDD storage capacity that is configured on your FSx for Lustre file system as
you need additional storage and throughput. Because the throughput of an FSx for Lustre file system
scales linearly with storage capacity, you also get a comparable increase in throughput capacity.
To increase the storage capacity, you can use the Amazon FSx console, the AWS Command Line Interface (AWS CLI), or the
Amazon FSx API.

When you request an update to your file system's storage capacity, Amazon FSx automatically
adds new network file servers and scales your metadata server. While scaling storage capacity,
the file system may be unavailable for a few minutes. File operations issued by clients while
the file system is unavailable will transparently retry and eventually succeed after storage
scaling is complete. During the time that the file system is unavailable, the file system status
is set to `UPDATING`. Once storage scaling is complete, the file system status is set
to `AVAILABLE`.

Amazon FSx then runs a storage optimization process that transparently rebalances data across
the existing and newly added file servers. Rebalancing is performed in the background with
no impact to file system availability. During rebalancing, you might see decreased file
system performance as resources are consumed for data movement. For most file systems,
storage optimization takes a few hours up to a few days. You can access and use your file
system during the optimization phase.

You can track the storage optimization progress at any time using the Amazon FSx console, CLI, and
API. For more information, see [Monitoring storage capacity increases](monitoring-storage-capacity-increase.md "monitoring-storage-capacity-increase.md").

###### Topics

- [Considerations when
  increasing storage capacity](#storage-capacity-important-to-know "#storage-capacity-important-to-know")
- [When to increase storage capacity](#when-to-modify-storage-capacity "#when-to-modify-storage-capacity")
- [How concurrent storage scaling
  and backup requests are handled](#storage-capacity-changes-and-backups "#storage-capacity-changes-and-backups")
- [Increasing storage capacity](increase-storage-capacity.md "increase-storage-capacity.md")
- [Monitoring storage capacity increases](monitoring-storage-capacity-increase.md "monitoring-storage-capacity-increase.md")

## Considerations when

increasing storage capacity

Here are a few important items to consider when increasing storage capacity:

- **Increase only** – You can only
  _increase_ the amount of storage capacity for a
  file system; you cannot decrease storage capacity.
- **Increase increments** – When
  you increase storage capacity, use the increments listed in the
  **Increase storage capacity** dialog box.
- **Time between increases** – You
  can't make further storage capacity increases on a file system until 6 hours
  after the last increase was requested.
- **Throughput capacity** – You
  automatically increase throughput capacity when you increase the storage capacity.
  For persistent HDD file systems with SSD cache, the read cache storage capacity is
  also similarly increased to maintain an SSD cache that is sized to 20 percent of the
  HDD storage capacity. Amazon FSx calculates the new values for the storage and throughput
  capacity units and lists them in the **Increase storage capacity** dialog box.

###### Note

You can independently modify the throughput capacity of a persistent SSD-based
file system without having to update the file system's storage capacity. For more information,
see [Managing provisioned throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

- **Deployment type** – You can increase
  the storage capacity of all deployment types except for scratch 1 file systems.

## When to increase storage capacity

Increase your file system's storage capacity when it's running low on free
storage capacity. Use the `FreeStorageCapacity` CloudWatch metric to monitor the
amount of free storage that is available on the file system. You can create an Amazon CloudWatch
alarm on this metric and get notified when it drops below a specific threshold. For more
information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

You can use CloudWatch metrics to monitor your file system's ongoing throughput usage
levels. If you determine that your file system needs a higher throughput capacity, you
can use the metric information to help you decide how much to increase the storage
capacity. For information about how to determine your file system's current
throughput, see [How to use Amazon FSx for Lustre CloudWatch metrics](how_to_use_metrics.md "how_to_use_metrics.md").
For information about how storage capacity affects throughput capacity, see [Amazon FSx for Lustre performance](performance.md "performance.md").

You can also view your file system's storage capacity and total throughput on
the **Summary** panel of the file system details page.

## How concurrent storage scaling

and backup requests are handled

You can request a backup just before a storage scaling workflow begins or while it is
in progress. The sequence of how Amazon FSx handles the two requests is as follows:

- If a storage scaling workflow is in progress (storage scaling status is
  `IN_PROGRESS` and file system status is `UPDATING`)
  and you request a backup, the backup request is queued. The backup task is
  started when storage scaling is in the storage optimization phase (storage
  scaling status is `UPDATED_OPTIMIZING` and file system status is
  `AVAILABLE`).
- If the backup is in progress (backup status is `CREATING`)
  and you request storage scaling, the storage scaling request is queued. The storage
  scaling workflow is started when Amazon FSx is transferring the backup to Amazon S3 (backup
  status is `TRANSFERRING`).

If a storage scaling request is pending and a file system backup request is also
pending, the backup task has higher precedence. The storage scaling task does not start
until the backup task is finished.
