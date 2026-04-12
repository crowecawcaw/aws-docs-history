# How S3 Files is metered

S3 Files pricing is based on two dimensions: the amount of data stored on your file
system's high performance storage, and the file system operations that your applications and
the synchronization process perform. This page explains how each dimension is metered so you
can understand and optimize your costs.

For current pricing, see [Amazon S3
Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## How file system storage is metered

When you work with files through your S3 file system, S3 Files stores the data you
actively use from your S3 bucket onto the file system's high performance storage. You pay
for the amount of data residing on the file system's high performance storage, measured
in GB-month. This includes data that has been copied from your S3 bucket, data you have
written through the file system, and the metadata for your files and
directories.

If a file in your file system has not been read within a configurable window (1 to 365
days, default 30 days) and its changes have already been synchronized to your S3 bucket,
S3 Files removes that file's data from the file system's high performance storage
automatically. This keeps your storage costs proportional to your active working data set
rather than the total size of your S3 bucket. Your data remains safely stored in your S3
bucket. S3 Files only removes the copy from the file system's high performance storage.
The next time you read that file, S3 Files retrieves the latest version of the
corresponding object from the S3 bucket and copies it back onto the file system's high
performance storage. For more information, see [Understanding how synchronization works](s3-files-synchronization.md "s3-files-synchronization.md").

## How file system operations are metered

S3 Files meters every file system operation as either a read or a write. Each
operation has a minimum metered size.

**Data reads** such as reading a file's contents are
metered at the size of the data read, with a minimum of 32 KB per read operation. There
are also cases when a read is served directly from your S3 bucket (see below) for
performance optimization, and such operations are not metered for data read and are only
metered for a 4 KB metadata read.

**Data writes** such as writing or appending to a file
are metered at the size of the data written, with a minimum of 32 KB per write
operation.

**Metadata operations** such as listing a directory,
viewing file attributes, creating or deleting files and directories, renaming, and
changing permissions are metered as reads at 4 KB per operation. The commit operation
(triggered by `fsync` or closing file after write) is the only metadata
operation metered as a write, at 4 KB.

All metered sizes are rounded up to the next 1 KB boundary.

## How reads are metered when served directly from Amazon S3

For reads of 128 KB or larger on data that has already been synchronized to S3, S3 Files
automatically streams directly from S3 even if the data resides on the high-performance
storage, since S3 is optimized for high throughput while the file system's high
performance storage is optimized for low-latency small-file access.

In such cases, you pay for S3 GET requests instead of file system data reads. S3 Files
meters only a 4 KB metadata read operation for such reads.

## How synchronization is metered

S3 Files keeps your file system and the linked S3 bucket synchronized automatically.
These synchronization operations are metered as file system operations, in addition to
the standard S3 request charges that S3 Files incurs on your behalf.

**Importing data onto the file system:** When S3 Files
copies data from your S3 bucket onto the file system's high performance storage, the
operation is metered as a file system write. This includes the data that is copied when
you first access a directory, when you read a file whose data is not on the file system's
high performance storage, and when S3 Files reflects changes made directly to your S3
bucket. The metered size is the amount of data written to the file system's high
performance storage.

**Exporting changes to your S3 bucket:** When S3 Files
copies your file system changes back to your S3 bucket, the operation is metered as a
file system read. Only the data that is read from the file system counts toward this
charge. If the file that you changed contains data that was never copied onto the file
system's high performance storage, that part of the data is read from your S3 bucket at
S3 GET request pricing and does not incur a file system read charge. For example, if you
append data to a file, S3 Files uses multipart uploads to avoid importing the entire
object into the file system's high performance storage before appending data to it. This
optimizes your file system storage cost.

**Rename and move operations:** S3 has no native concept
of directories. What appears as a directory in your file system is a common prefix shared
by the keys of the objects within the S3 bucket. Additionally, S3 objects are immutable
and do not support atomic renames. As a result, when you rename or move a file, S3 Files
must write the data to a new object with the updated key (metered as an S3 PUT request)
and delete the original. The synchronization of rename operations also meters as a file
system read for any data read from the file system. If the file's data was never copied
onto the file system's high performance storage, the file system meters only for a 4 KB
metadata read operation. When you rename or move a directory, S3 Files must repeat this
process (and meter) for every object that shares that prefix. For more information, see
[Understanding the impact of rename and move operations](s3-files-synchronization.md#s3-files-sync-rename-move "s3-files-synchronization.md#s3-files-sync-rename-move").

**Data expiration:** When S3 Files removes unused data
from the file system, no file system operation charges apply.

## Metering examples

**Listing a large directory for the first time**

When you first list a directory, S3 Files imports metadata for all files in that
directory. Each file's metadata import is metered as a 4 KB write. Depending on your
import configuration, S3 Files may also prefetch and copy data for small files in that
directory on to the file system's high performance storage to optimize performance. Each
file's data import is metered as a write at the file's size (32 KB minimum). You can
control which files have their data imported by configuring your import rules. For more
information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md "s3-files-synchronization-customizing.md").

**Reading a large file**

For reads of 128 KB or larger on data that has already been synchronized to S3, S3 Files
streams directly from S3 even if the data resides on the high-performance storage, since
S3 is optimized for high throughput while the file system's high performance storage
layer is optimized for low-latency small-file access. You pay the S3 GET request pricing
along with a 4 KB metadata read operation. No file system data read charge
applies.

**Reading a small file that is not in the file system's high
performance storage**

S3 Files reads the data from S3 bucket and serves to the client, and asynchronously
imports the data into the file system's high performance storage so that future reads are
faster. This is metered as a file system read at the size of the data transferred (32 KB
minimum). The asynchronous import of data into the file system's high performance storage
is metered as a write at the size of the data transferred. A similar process is followed
when you read a file whose data has been expired from the file system. The expiration of
data does not incur any additional file system operation charges.

**Writing a file**

Your write is metered as a file system write at the size of the data written (32 KB
minimum). Approximately 60 seconds after your last write, S3 Files copies the file to
your S3 bucket. This is because when you modify a file in the file system, S3 Files
waits up to 60 seconds, aggregating any successive changes to the file in that time,
before copying to your S3 bucket. This means that rapid successive writes to the same
file are captured in a single S3 PUT request rather than generating a new object version
for every individual change, reducing your S3 request costs and storage costs. This
synchronization is metered as a file system read for data read from the file system's
high performance storage, plus a standard S3 PUT request.
