# NVMe-backed instances

NVMe-backed instances offer up to 7x faster query performance for applications with large datasets that exceed the memory of a regular instance.
These instances leverage the local non-volatile memory express (NVMe)-based Solid-State Drive (SSD) storage available on r6gd instances to store ephemeral data, reducing network-based storage access, and improving read latency and throughput.

The local SSD space is divided into two sections:

- **Tiered cache** — Approximately 73% of the local SSD is allocated as a database cache, allowing the system to store up to five times more database pages than the main memory alone.
  The local SSD acts as a second-tier cache, while the existing in-memory buffer cache remains the first-tier cache.
  The query only accesses external storage if both the buffer cache and the SSD cache experience a miss.
- **Temporary storage** — The remaining 27% is reserved for non-persistent temporary file storage, used for complex queries involving sorts or resource-intensive operations like index builds.
  On regular instances, the temporary space resides on an Amazon Elastic Block Store (EBS) volume.
  The locally hosted temporary storage on the SSD reduces query latency involving sorts by up to two times and accelerates resource-intensive operations like index builds.
  The details regarding the type of NVMe-backed instances supported and its specification can be found in [Instance class specifications](db-instance-classes.md#db-instance-class-specs "db-instance-classes.md#db-instance-class-specs").

###### Topics

- [Recommended use cases for NVMe-backed instances](#nvme-use-cases "#nvme-use-cases")
- [Using NVMe-backed instances with Amazon DocumentDB](#using-nvme "#using-nvme")
- [Monitoring NVMe-backed instances](#monitoring-nvme "#monitoring-nvme")

## Recommended use cases for NVMe-backed instances

We recommend you use NVMe-backed instances in the following scenarios:

- **Read-heavy workloads** — If your workload is read-intensive, and your dataset is larger than the buffer cache, indicated by low `BufferCacheHitRatio` and high `ReadIOPS` metrics, NVMe-backed instances can provide performance benefits.
- **Update-heavy workloads** — If your workload is update-intensive, and garbage collection is unable to keep up due to read latency on network storage, NVMe-backed instances could help mitigate the issue.

NVMe-backed instances can benefit various use cases, including:

- **Internet-scale applications** — Applications such as payment processing, billing, and e-commerce with strict performance Service Level Agreements (SLAs) can leverage the performance advantages of NVMe-backed instances.
- **Real-time reporting dashboards** — Dashboards that run hundreds of queries for metrics/data collection can benefit from the low latency and high throughput of NVMe-backed instances.
- **Generative AI applications** — Applications using vector search to find exact or nearest neighbors across millions of vector embeddings can leverage the high performance of NVMe-backed instances.

## Using NVMe-backed instances with Amazon DocumentDB

To use NVMe-backed instances of Amazon DocumentDB:

- Create an Amazon DocumentDB cluster and add one of the NVMe-backed instance classes. For more information, see [Creating an Amazon DocumentDB cluster](db-cluster-create.md "db-cluster-create.md").
- Alternatively, modify an existing Amazon DocumentDB cluster to use one of the NVMe-backed instance classes. For more information, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

To check the availability of NVMe-backed instances across different AWS Regions, see [Supported instance classes by region](db-instance-classes.md#db-instance-classes-by-region "db-instance-classes.md#db-instance-classes-by-region").

If you want to switch back from an NVMe-backed instance to a regular instance, modify the database instance class of your Amazon DocumentDB instance to a similar instance class without the NVMe storage.
For example, if your current instance class is 'db.r6gd.4xlarge', choose 'db.r6g.4xlarge' to switch back.
For more information, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

## Monitoring NVMe-backed instances

In addition to the regular instance metrics available in Amazon CloudWatch, NVMe-backed instances emit additional metrics specific to NVMe-based SSD storage, IOPS, and throughput.

```
NVMeStorageCacheHitRatio
FreeNVMeStorage
ReadIOPSNVMeStorage
ReadLatencyNVMeStorage
ReadThroughputNVMeStorage
WriteIOPSNVMeStorage
WriteLatencyNVMeStorage
WriteThroughputNVMeStorage
```

For more information about these metrics, see [NVMe-backed instance metrics](cloud_watch.md#nvme-metrics "cloud_watch.md#nvme-metrics")
