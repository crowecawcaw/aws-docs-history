# Amazon Neptune storage, reliability and availability

Amazon Neptune uses a distributed and shared storage architecture that scales
automatically as your database storage needs grow.

Neptune data is stored in a cluster volume, which is a single, virtual volume
that uses Non-Volatile Memory Express (NVMe) SSD-based drives. A cluster volume can
grow to a maximum size of 128 tebibytes (TiB) (64 TiB in the China Regions and the
AWS GovCloud (US) Regions).
A cluster volume consists of copies of the data across three Availability Zones (AZs)
in a single AWS Region, which provides high durability and availability.

The [Storage](storage.md "storage.md") section covers these
topics in detail:

- **[Allocation](storage.md#storage-allocation "storage.md#storage-allocation")** – You are charged
  for space allocated, as determined by the storage high water
  mark.
- **[Storage billing](storage.md#storage-billing "storage.md#storage-billing")** – Storage costs are
  billed based on the high water mark, and Neptune also offers an
  [I/O–Optimized](storage-types.md#provisioned-iops-storage "storage-types.md#provisioned-iops-storage") pricing
  option for I/O–intensive workloads.
- **[Reliability and high availability](storage.md#storage-reliability "storage.md#storage-reliability")** – Neptune replicates
  your data across three Availability Zones for high durability and
  automatic fault recovery.
