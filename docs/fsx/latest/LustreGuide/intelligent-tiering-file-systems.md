# Performance characteristics of Intelligent-Tiering storage class

The FSx for Lustre Intelligent-Tiering storage class offers elastic, cost-optimized storage for workloads that
traditionally run on HDD-based or mixed HDD-/SDD-based high-performance file storage
file systems.
File systems using the Intelligent-Tiering storage class utilize fully elastic, intelligently tiered, regional
storage which automatically grows and shrinks to fit your workload as it changes. For information on how
it tiers data, see [How the Intelligent-Tiering storage class tiers data](using-fsx-lustre.md#how-INT-tiering-works "using-fsx-lustre.md#how-INT-tiering-works").

The throughput that an FSx for Lustre file system with Intelligent-Tiering storage class supports is independent
to its storage. Intelligent-Tiering file systems scale to multiple TBps of throughput and millions of IOPS.
File systems using the Intelligent-Tiering storage class also provide an optional provisioned SSD read cache
for low-latency access to frequently accessed data. By default, Amazon FSx for Lustre provisions an SSD read cache for frequently
accessed metadata. As most workloads tend to be read-heavy and actively work with only a small subset of the overall
dataset at any given time, the hybrid model of Intelligent-Tiering storage and the SSD read caches allows file systems
using the Intelligent-Tiering storage class to provide storage that performs at levels comparable to SSD file systems
for most workloads, while delivering storage cost savings relative to the SSD and HDD storage classes.

When reading and writing data to an Intelligent-Tiering file system, especially data that hasn't been accessed
recently or frequently enough to be in the file server's in-memory cache, performance depends on the size of the
SSD read cache. Data access from Intelligent-Tiering storage has time-to-first-byte latencies of roughly tens of
milliseconds as well as per-request costs, while accesses from the SSD read cache return with sub-millisecond latency
and no per-request costs.

When configuring the size of the SSD read cache for your file system, you should consider both the size
of your frequently accessed dataset within the workload and the workload's sensitivity to higher latency for
reads of less-frequently accessed data. You can switch between SSD read cache sizing modes after
your file system has been created and scale the cache up or down. For more information on how to modify your SSD read cache,
see [Managing provisioned SSD read cache](managing-ssd-read-cache.md "managing-ssd-read-cache.md").

A write request occurs when FSx for Lustre writes a block of data to Intelligent-Tiering storage. When you write data to the
file system, write requests are aggregated and written to Intelligent-Tiering storage, increasing throughput and lowering
request costs. Reads can be served from the file server’s in-memory cache, SSD read cache, or directly from Intelligent-Tiering
storage. When a read is served from Intelligent-Tiering storage, a read request occurs for each block of retrieved data.
When you read data sequentially, FSx for Lustre will prefetch data to improve performance.

Data from the in-memory cache on file systems using the Intelligent-Tiering storage class is served directly to the requesting client as _network I/O_.
When a client accesses data that is not in the in-memory cache, it is read from either the SSD read cache or Intelligent-Tiering storage as _disk I/O_ and then served
to the client as network I/O.

## File system performance for Intelligent-Tiering

The following table shows the performance that FSx for Lustre Intelligent-Tiering file systems are designed for.

| Provisioned throughput capacity (MBps) | **Network throughput (MBps)** | **Network IOPS** | **In-memory cache storage (GB)** | **Maximum SSD cache disk throughput (MBps)** | **Maximum SSD cache disk IOPS** |
| -------------------------------------- | ----------------------------- | ---------------- | -------------------------------- | -------------------------------------------- | ------------------------------- | ------------ | --------- |
|                                        | **Baseline**                  | **Burst**        |                                  |                                              |                                 | **Baseline** | **Burst** |
| Every 4000                             | 12500                         | ‐                | Hundreds of thousands            | 76.8                                         | 4000                            | 160000       | ‐         |
