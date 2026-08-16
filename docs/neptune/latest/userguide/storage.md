# Storage

Neptune data is stored in a cluster volume, which is a single, virtual volume
that uses Non-Volatile Memory Express (NVMe) SSD-based drives. The cluster volume
consists of a collection of logical blocks known as segments. Each of these segments
is allocated 10 gigabytes (GB) of storage. The data in each segment is replicated
across three Availability Zones (AZs) in a single AWS Region where the DB cluster
resides.

When a Neptune DB cluster is created, it is allocated a single segment of 10 GB.
As the volume of data increases and exceeds the currently allocated storage, Neptune
automatically expands the cluster volume by adding new segments. A Neptune cluster
volume can grow to a maximum size of 128 tebibytes (TiB) in all supported Regions
except the China Regions and the AWS GovCloud (US) Regions, where it is limited to
64 TiB.

The DB cluster volume contains all your user data, indices and dictionaries
(described in the [Neptune Graph Data Model](feature-overview-data-model.md "feature-overview-data-model.md") section), as well as internal metadata
such as internal transaction logs. All this graph data, including indices and internal
logs, cannot exceed the maximum size of the cluster volume.

## I/O–Optimized storage option

Neptune offers two pricing models for storage:

- **Standard storage**   –  
  Standard storage provides cost-effective database storage for applications with
  moderate to low I/O usage.
- **I/O–Optimized storage**   –  
  With I/O–Optimized storage, you pay only for the storage you are using, at a
  higher cost than for standard storage, and you pay nothing for the I/O
  that you use.

With I/O–Optimized storage, you get predictable costs, low I/O latency,
and consistent I/O throughput for I/O–intensive graph workloads.

For more information, see [I/O–Optimized storage](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage").

## Neptune storage allocation

Even though a Neptune cluster volume can grow to 128 TiB (or 64 TiB in a few
regions), you are charged for space allocated. The total
space allocated is determined by the storage _high water mark_,
which is the maximum amount allocated to the cluster volume at any time during its
existence.

This means that even if you remove user data from a cluster volume, such as by
running a drop query like `g.V().drop()`, the total allocated space remains
the same. Neptune does automatically optimize the unused allocated space for reuse in
the future.

In addition to user data, dictionary data and internal transaction logs also
consume storage. Dictionary data persists even after you delete the graph data it
supports, though Neptune can re-use those entries if you re-introduce the data. To
clean up unused dictionary entries, you can enable [Dictionary garbage collection](storage-gc.md "storage-gc.md"). Internal logs use a separate
storage space with its own high water mark. Expired logs are re-used only for other
logs, not for graph data. The space allocated for logs is included in the total
reported by the `VolumeBytesUsed` [CloudWatch
metric](cloudwatch.md "cloudwatch.md").

Check [Storage best practices](#storage-best-practices "#storage-best-practices") for ways to keep
allocated storage to a minimum and to re-use space.

## Neptune storage billing

Storage costs are billed based on the storage _high water mark_,
as described in the preceding section. Amazon Neptune replicates your data across
multiple Availability Zones, but you pay for only one copy of the data.

You can determine what the current storage high water mark of your DB cluster is
by monitoring the `VolumeBytesUsed` CloudWatch metric (see [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md")).

Other factors that can affect your Neptune storage costs include database snapshots
and backup, which are billed separately as backup storage and are based on the Neptune
storage costs (see [CloudWatch metrics that are useful for managing Neptune backup storage](backup-restore-overview-metrics.md "backup-restore-overview-metrics.md")).

If you create a [clone](manage-console-cloning.md "manage-console-cloning.md") of your database,
however, the clone points to the same cluster volume that your DB cluster itself uses,
so there is no additional storage charge for the original data. Subsequent changes to
the clone use the [copy-on-write protocol](manage-console-cloning.md#manage-console-cloning-protocol "manage-console-cloning.md#manage-console-cloning-protocol"),
and do result in additional storage costs.

For more Neptune pricing information, see [Amazon Neptune Pricing](https://aws.amazon.com/neptune/pricing "https://aws.amazon.com/neptune/pricing") on the
AWS website.

## Neptune storage best practices

Because certain types of data consume permanent storage in Neptune, use these best
practices to avoid large spikes in storage growth:

- When designing your graph data model, avoid as much as possible using
  property keys and user-facing values that are temporary in nature.
- If you plan on making changes to your data model, do not load data
  onto an existing DB cluster using the new model until you have cleared the data in
  that DB cluster using the [fast reset API](manage-console-fast-reset.md "manage-console-fast-reset.md").
  The best thing is often to load data that uses a new model onto a new DB cluster.
- Transactions that operate on large amounts of data generate correspondingly
  large internal logs, which can permanently increase the high water mark of the
  internal log space. For example, a single transaction that deletes all the data
  in your DB cluster can generate a large internal log. This log requires allocating
  a great deal of internal storage, which permanently reduces the space available
  for graph data.

To avoid this, split large transactions into smaller ones and allow time between
them so that the associated internal logs have a chance to expire and release their
internal storage for re-use by subsequent logs.

- For monitoring the growth of your Neptune cluster volume, you can
  set a CloudWatch alarm on the `VolumeBytesUsed` CloudWatch metric. This can be
  particularly helpful if your data is reaching the maximum size of the cluster volume.
  For more information, see [Using
  Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

If your DB cluster has a large amount of unused allocated space, you can shrink
its storage. To do this, export all the data in your graph and then reload it into a
new DB cluster. See the [Neptune data export service and
utility](machine-learning-data-export.md "machine-learning-data-export.md") for an easy way to export data from a DB cluster, and the [Neptune bulk loader](bulk-load.md "bulk-load.md") for an easy way to import
data back into Neptune.

###### Note

Creating and restoring a [snapshot](backup-restore-restore-snapshot.md "backup-restore-restore-snapshot.md")
does not reduce the amount of storage allocated for your DB cluster, because a
snapshot retains the original image of the cluster's underlying storage.
If a substantial amount of your allocated storage is not being used, the only
way to shrink the amount of allocated storage is to export your graph data and
reload it into a new DB cluster.

## Neptune storage reliability and high availability

Amazon Neptune is designed to be reliable, durable, and fault tolerant.

Because copies of your Neptune data are maintained across three
Availability Zones (AZs), storage of the data is highly durable, with
very low likelihood of data loss. Amazon Neptune replicates the data automatically
across the Availability Zones, regardless of whether there are DB instances in them.
The amount of replication is independent of the number of DB instances in your
cluster.

This means that you can add a read-replica quickly, because Neptune doesn't make
a new copy of the graph data. Instead, the read-replica connects to the cluster volume
that already contains your data. Similarly, removing a read-replica doesn't remove
any of the underlying data.

You can delete the cluster volume and its data only after deleting all of its
DB instances.

Neptune also automatically detects failures in the segments that make up
the cluster volume. When a copy of the data in a segment is corrupted, Neptune
immediately repairs that segment, using other copies of the data within the same
segment to ensure that the repaired data is current. As a result, Neptune avoids
data loss and reduces the need to perform point-in-time restore to recover from
a disk failure.
