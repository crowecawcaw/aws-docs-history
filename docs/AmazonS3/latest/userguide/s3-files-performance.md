

# Performance specifications
<a name="s3-files-performance"></a>

S3 Files automatically scales throughput and IOPS to match your workload without requiring you to provision or manage capacity. This page describes the performance characteristics of S3 Files.

## Performance summary
<a name="s3-files-performance-summary"></a>


| Specification | Value | 
| --- | --- | 
| Aggregate read throughput per file system | Up to terabytes per second | 
| Aggregate write throughput per file system | 1–5 GiB/s | 
| Maximum read IOPS per S3 bucket with S3 Files | No limit (attach multiple file systems to the same bucket) | 
| Maximum write IOPS per S3 bucket with S3 Files | No limit (attach multiple file systems to the same bucket) | 
| Maximum read IOPS per file system | 250,000 | 
| Maximum write IOPS per file system | 50,000 | 
| Maximum per-client read throughput | 3 GiB/s | 

## How S3 Files delivers performance
<a name="s3-files-performance-how"></a>

S3 Files serves data from two storage tiers, and automatically routes each operation to the tier best suited for it.

**High-performance storage** – The low-latency storage layer within your file system where actively used file data and metadata reside. S3 Files automatically manages this storage, copying data onto it when you access files and removing data that has not been read within a configurable expiration window. You pay a storage rate for data residing on the high-performance storage.

**Direct from S3** – S3 Files streams file reads directly from your S3 bucket in two cases: when the file's data is not stored in the file system's high-performance storage, and for large reads >= 1 MiB, even when the data also resides on the file system's high-performance storage. The S3 bucket is optimized for high throughput while the file system's high-performance storage layer is optimized for low-latency access. This tiering approach for streaming data directly from S3 bucket provides high throughput for sequential reads, making it well suited for analytics, media processing, and other streaming workloads. S3 Files asynchronously imports data for small files (< 128 KiB by default) to the file system's high-performance storage for low latency access on subsequent reads.

Since S3 Files automatically applies this two-tier model, you do not have to choose between latency and throughput. Small-file workloads get file system performance. Large-file workloads get S3 throughput. Mixed workloads get both.

## Read performance
<a name="s3-files-performance-read"></a>

Read throughput scales with the number of connected compute instances and the degree of parallelism within each instance. The maximum per-client read throughput is 3 GiB/s. S3 Files supports up to terabytes per second of aggregate read throughput and up to 250,000 read IOPS per file system.

## Write performance
<a name="s3-files-performance-write"></a>

Writes go to the high-performance storage and are durable immediately. Depending on the region, S3 Files supports 1–5 GiB/s of aggregate write throughput and up to 50,000 write IOPS per file system. Write performance scales elastically with workload activity.

When you modify a file in the file system, S3 Files waits approximately 60 seconds, aggregating any successive changes to the file in that time, before copying to your S3 bucket. This means that rapid successive writes to the same file are captured in a single S3 PUT request rather than generating a new object version for every individual change, reducing your S3 request costs and storage costs. If you continue to modify the file after S3 Files has copied your changes back to the S3 bucket, it will copy subsequent changes as needed.

## First access latency
<a name="s3-files-performance-first-access"></a>

The first time you access a directory, S3 Files imports metadata for all files in that directory and, depending on your import configuration, data for small files. So your initial access takes longer than subsequent operations. Once imported, all subsequent directory listings and file access return at low latency.

## Synchronization performance
<a name="s3-files-performance-sync"></a>

S3 Files synchronizes changes between your file system and S3 bucket in the background.

**Importing changes from S3** – When another application adds or modifies an object in your S3 bucket, S3 Files reflects the change in your file system typically within seconds. S3 Files processes up to 2,400 object changes per second per file system, with import data throughput of up to 700 megabytes per second.

**Exporting changes to S3** – When you write a file through the file system, S3 Files batches your changes for approximately 60 seconds to consolidate rapid successive writes into a single S3 object version, reducing your S3 request and storage version costs. After the batching window, S3 Files copies the file to your S3 bucket. S3 Files exports up to 800 files per second per file system, with export data throughput of up to 2,700 megabytes per second.


| Operation metric | Value | Unit | 
| --- | --- | --- | 
| Import from S3 bucket IOPS | 2,400 | objects per second per file system | 
| Import from S3 bucket throughput | 700 | megabytes per second | 
| Export to S3 bucket IOPS | 800 | files per second per file system | 
| Export to S3 bucket throughput | 2,700 | megabytes per second | 

Amazon S3 uses a flat storage structure where objects are identified by their key names. While S3 Files lets you organize your data in directories, S3 has no native concept of directories. What appears as a directory in your file system is a common prefix shared by the keys of the objects within the S3 bucket. Additionally, S3 objects are immutable and do not support atomic renames. As a result, when you rename or move a file, S3 Files must write the data to a new object with the updated key and delete the original. When you rename or move a directory, S3 Files must repeat this process for every object that shares that prefix. Therefore, when you rename or move a directory containing tens of millions of files, your S3 request costs and the synchronization time increase significantly. A directory rename of 100,000 files takes a few minutes to fully reflect in the S3 bucket, though the rename is instant on the file system. For more information, see [Understanding the impact of rename and move operations](s3-files-synchronization.md#s3-files-sync-rename-move).

If your workload generates changes faster than the synchronization rate, S3 Files queues the changes and processes them in order. You can monitor the count of pending exports using the `PendingExports` CloudWatch metric. For more information, see [Monitoring S3 Files with Amazon CloudWatch](s3-files-monitoring-cloudwatch.md).

## Monitoring performance
<a name="s3-files-performance-monitoring"></a>

You can monitor your file system's performance using Amazon CloudWatch. S3 Files publishes metrics including `DataReadBytes`, `DataWriteBytes`, `MetadataReadBytes`, and `MetadataWriteBytes`, which you can use to track throughput and IOPS over time. For more information, see [Monitoring S3 Files with Amazon CloudWatch](s3-files-monitoring-cloudwatch.md).