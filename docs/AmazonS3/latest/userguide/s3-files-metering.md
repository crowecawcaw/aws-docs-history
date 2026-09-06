

# How S3 Files is metered
<a name="s3-files-metering"></a>

S3 Files is a shared file system linked to your S3 bucket, designed to deliver low-latency file access while keeping costs proportional to your active working set. The file system maintains a view of the objects in your bucket and intelligently translates your file system operations into efficient S3 requests on your behalf. As you work with specific files and directories through the file system, associated file metadata and contents are placed onto the file system's high-performance storage, in particular the portions that benefit from low-latency access. Many read operations bypass the file system entirely, with data served directly from your S3 bucket at S3 GET request rates with no S3 file data charges. Your authoritative data always remains in your S3 bucket. When you write data, it is stored on the file system's highly durable high-performance storage and then synced back to your S3 bucket, keeping the file system and your S3 bucket consistent in both directions.

With S3 Files, you pay a storage charge for the fraction of active data on the file system's high-performance storage, and you pay data access charges when reading from and writing to the file system's high-performance storage. This page explains how each dimension is metered so you can understand and optimize your costs. For pricing by AWS Region, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

## How file system storage is metered
<a name="s3-files-metering-storage"></a>

When you access data, the file system loads portions of file metadata and contents on demand onto the file system's high-performance storage, delivering fast reads without duplicating your entire dataset. You configure a file size threshold (default 128 KiB) that determines which files are stored on high-performance storage. Files at or below this threshold benefit most from low-latency access. Files that exceed the threshold are streamed directly from your S3 bucket and incur no S3 Files storage charges. Data not accessed within a configurable window (1 – 365 days, default 30 days) automatically expires from high-performance storage. You pay a storage rate for the fraction of active data residing on high-performance storage. Typically, the fraction is small, since large files stream directly from your S3 bucket, stale data expires automatically, and only small, latency-sensitive files are stored on high-performance storage. The minimum billable file size on high-performance storage is 10 KiB.

## How data access is metered
<a name="s3-files-metering-data-access"></a>

You pay data access charges for metadata operations and for reads and writes to the file system's high-performance storage. Large file reads (1 MiB or larger file IO) are always streamed directly from your S3 bucket, even if data resides on the file system's high-performance storage. S3 is optimized for high throughput reads, while high-performance storage is optimized for low-latency small-file access. Direct reads incur S3 GET requests and an S3 Files metadata read (4 KiB) with no file read charges. Background sync operations also incur data access charges and S3 request charges. Importing data onto high-performance storage incurs write charges, and exporting changes back to your S3 bucket incurs read charges.

## How data access is metered from the file system
<a name="s3-files-metering-operations"></a>

S3 Files meters every file system operation as either a read or a write and applies to a file or metadata. Each operation has a minimum metered size and is then rounded up to the next 1 KiB increment. This means every operation falls into one or two of four categories: a data read, a metadata read, a data write, or a metadata write. For example, reading a file is metered as both a data read and a metadata read, while renaming a file is metered as a metadata read and a metadata write. No single operation is ever metered as more than two categories.

**File reads from high-performance storage** are metered at the size of the data read, with a minimum of 32 KiB per read operation.

**File writes to high-performance storage** are metered at the size of the data written, with a minimum of 32 KiB per write operation.

**Metadata reads** are metered at a 4 KiB minimum size and apply as S3 Files reads. Metadata read operation examples include listing a directory and viewing file attributes.

**Metadata writes** are metered at a 4 KiB minimum size and apply as S3 Files writes. Metadata write operation examples include creating or deleting files and directories, renaming, changing permissions, and calling `fsync`.

## How streaming directly from your S3 bucket is metered
<a name="s3-files-metering-s3-reads"></a>

S3 Files streams reads directly from your S3 bucket in two cases: the file's data is not stored on high-performance storage, or the read is 1 MiB or larger, even if the data also resides on high-performance storage. This design reflects the strengths of each storage layer. The S3 bucket is optimized for high throughput, while the file system is optimized for low-latency access.

For small files (less than 128 KiB by default), S3 Files asynchronously imports data onto high-performance storage so that subsequent reads are served at low latency. For direct bucket streams, you pay for the S3 GET requests and an S3 Files metadata read (4 KiB), with no file read charges.

## How bucket synchronization is metered
<a name="s3-files-metering-sync"></a>

S3 Files automatically keeps your file system and your linked S3 bucket synchronized. Synchronization is metered as file reads, file writes, and S3 request charges. For more information, see [Understanding how synchronization works](s3-files-synchronization.md).

**Importing data onto the file system:** When S3 copies data from your S3 bucket onto high-performance storage based on your settings, the operation is metered as a file system write. Import writes occur when you access a directory for the first time, when you read a file not stored on high-performance storage, and when S3 Files reflects changes made directly to your S3 bucket. The metered size is the amount of data written to high-performance storage and a metadata write.

**Exporting changes to your S3 bucket:** When S3 Files copies your file system changes back to your S3 bucket, the operation is metered as a file system metadata and a file read. Only data read from high-performance storage counts toward this charge. For example, if you append data to a file, S3 Files uses `UploadPartCopy` to avoid importing the entire object onto high-performance storage before appending. This optimizes your high-performance storage costs.

**Rename and move operations:** S3 buckets do not natively support directories or renames. What appears as a directory in your S3 file system is a common prefix shared by object keys in the bucket, and S3 objects are immutable. As a result, when you rename or move a file, S3 Files copies the data to a new object with the updated key (metered as an S3 PUT request) and deletes the original. The synchronization is metered as a metadata read and a file read based on the data's location. If the file data is not stored on high-performance storage, only a 4 KiB metadata read applies. For file renames or directory moves, S3 Files repeats this copy-and-delete for every object under that prefix. For more information, see [Understanding the impact of rename and move operations](s3-files-synchronization.md#s3-files-sync-rename-move).

**File data expiration:** File data not accessed within a configurable window of 1 to 365 days (default 30 days) automatically expires from high-performance storage. Expiration incurs no data access or metadata charges.

**Metadata updates:** Your file system metadata (inodes) reflects the contents of your linked S3 bucket. As your bucket changes, metadata is updated to stay consistent with the current state of your bucket. Metadata for accessed directories never expires. You can use the Inodes CloudWatch metric to monitor your metadata usage. Metadata expiration incurs no charges. POSIX metadata changes such as chown and chmod update the object in your S3 bucket. S3 objects are immutable, so S3 Files writes a new version of the object with the updated metadata, metered as an S3 PUT request and S3 Files export. Each metadata change creates an additional version of the object.

## Metering examples
<a name="s3-files-metering-examples"></a>

**Listing a large directory for the first time**

When you first list a directory, S3 Files imports metadata for all files in that directory. Each file's metadata import is metered as a 4 KiB write. Depending on your import configuration (default 128 KiB), S3 Files also prefetches and copies data for small files in that directory onto the file system's high-performance storage to optimize for the lowest latency. Each file's data import is metered as a write at the file's size (32 KiB minimum). You can control which files have their data imported by configuring your import rules. For more information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md).

**Reading a small file not stored on high-performance storage**

S3 Files streams read directly from your S3 bucket to your client and asynchronously imports data to the file system's high-performance storage, so future reads are faster. This is metered as a file system read at the size of the data transferred (32 KiB minimum). The asynchronous import of data into the file system's high-performance storage is metered as a write at the size of the data transferred. A similar process is followed when you read a file whose data has been expired from the file system. When files expire from the high-performance storage, it does not incur any file system operation charges.

**Writing to the file system**

All file writes are stored on high-performance storage and metered at the size of the data written with a 32 KiB minimum. S3 Files waits for a period of inactive write activity (60 seconds) in order to aggregate successive changes to the same file before copying to your S3 bucket. Rapid writes are captured in a single S3 PUT rather than generating a new object version for each individual change. This reduces both S3 request costs and file high-performance storage costs. This bucket synchronization is metered as a file system read for data read from high-performance storage, and an S3 PUT request.