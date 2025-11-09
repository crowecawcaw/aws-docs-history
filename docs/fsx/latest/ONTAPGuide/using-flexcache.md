# Replicating your data with FlexCache

FlexCache is NetApp ONTAP's remote caching capability that brings datasets closer to clients, improving access performance and reducing costs.
It simplifies file distribution and reduces WAN costs. When you create a FlexCache volume, it initially copies only the metadata from the origin file system.
This approach is faster and more space-efficient than a full data copy, consuming only a fraction of the storage capacity.

## How FlexCache works

A FlexCache volume is a sparsely-populated cache that provides access to data stored in an origin volume.
The cache can be located in a different, optionally remote, file system. Instead of copying all data from the origin volume, FlexCache copies data only as needed.
FlexCache volumes are best suited for read-intensive workflows with infrequent data changes because any changes to the origin data require the cache to be refreshed.

You can use FlexCache with FSx for ONTAP in the following configurations:

| Origin volume           | FlexCache volume        |
| ----------------------- | ----------------------- |
| On-premise NetApp ONTAP | FSx for ONTAP           |
| FSx for ONTAP           | On-premise NetApp ONTAP |
| FSx for ONTAP           | FSx for ONTAP           |

## FlexCache write modes

FlexCache volumes support two modes of operation for write operations: write-around mode and write-back mode.

In write-around mode, which is the default mode, writes are forwarded from the cache to the origin volume.
The write operation isn't acknowledged to the client until after the data is committed to storage at the origin volume and the origin acknowledges
the write back to the cache. Because each write must traverse the network between the cache and origin,
this mode has higher latency than write-back mode.

In write-back mode, introduced in ONTAP 9.15.1, writes are committed to storage at the cache location and immediately acknowledged to the client.
The data is then asynchronously written to the origin volume. This mode enables writes to perform at near-local speeds, which can significantly improve
performance for distributed workloads.

Use write-back mode for write-heavy workloads that require low-latency cache writes.
Use write-around mode for read-heavy workloads that are not latency-sensitive, or when your origin file system has more than 10 FlexCache origin volumes.

## FlexCache volume creation overview

Creating a FlexCache volume consists of the following steps:

1. Gather source and destination logical interfaces (LIFs)
2. Establish cluster peering between the origin and cache file systems
3. Create a storage virtual machine (SVM) peering relationship
4. Create the FlexCache volume and select a write mode
5. Mount the FlexCache volume on your clients

For detailed instructions, see
[Creating a FlexCache](create-flexcache.md "create-flexcache.md").
