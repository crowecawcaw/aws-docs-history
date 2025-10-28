# Amazon EFS performance tips

When using Amazon EFS, keep the following performance tips in mind.

## Average I/O size

The distributed nature of Amazon EFS enables high levels of availability, durability, and
scalability. This distributed architecture results in a small latency overhead for each file
operation. Because of this per-operation latency, overall throughput generally increases as
the average I/O size increases, because the overhead is amortized over a larger amount of
data.

## Optimizing workloads that demand high throughput and

IOPS

For workloads that require high throughput and IOPS, use Regional file
systems configured with the General Purpose performance mode and Elastic
throughput.

###### Note

To achieve the maximum read IOPS for frequently accessed data, the file system must
use Elastic throughput.

To achieve the highest levels of performance, you must leverage parallelization by
configuring your application or workload as follows.

1. Distribute the workload evenly across all clients and directories, with at least the same
   number of directories as the number of utilized clients.
2. Minimize contention by aligning individual threads to distinct datasets or files.
3. Distribute the workload across 10 or more NFS clients, with at least 64 threads per
   client in a single mount target.

## Simultaneous connections

You can mount Amazon EFS file systems on up to thousands of Amazon EC2 and other AWS compute
instances concurrently. You can drive higher throughput levels on your
file system in aggregate across compute instances if you can parallelize
your application across more instances.

## Request model

If you enable asynchronous writes to your file system, pending write operations are
buffered on the Amazon EC2 instance before they're written to Amazon EFS asynchronously. Asynchronous
writes typically have lower latencies. When performing asynchronous writes, the kernel uses
additional memory for caching.

A file system that has enabled synchronous writes, or one that opens files using an
option that bypasses the cache (for example, `O_DIRECT`), issues synchronous
requests to Amazon EFS. Every operation goes through a round trip between the client and
Amazon EFS.

###### Note

Your chosen request model has tradeoffs in consistency (if you're using multiple
Amazon EC2 instances) and
speed. Using synchronous writes provides increased data consistency by completing each write
request transaction before processing the next request. Using asynchronous writes provides increased
throughput by buffering pending write operations.

## NFS client mount settings

Verify that you're using the recommended mount options as outlined in [Mounting EFS file systems](mounting-fs.md "mounting-fs.md") and in [Mounting considerations for Linux](mounting-fs-mount-cmd-general.md "mounting-fs-mount-cmd-general.md").

When mounting your file systems on Amazon EC2 instances, Amazon EFS supports the Network File
System version 4.0 and 4.1 (NFSv4) protocols. NFSv4.1 provides better performance for
parallel small-file read operations (greater than 10,000 files per second) compared to
NFSv4.0 (less than 1,000 files per second). For Amazon EC2 macOS instances running macOS Big Sur,
only NFSv4.0 is supported.

Don't use the following mount options:

- `noac`, `actimeo=0`, `acregmax=0`, `acdirmax=0`
  – These options disable the attribute cache, which has a very large performance
  impact.
- `lookupcache=pos`, `lookupcache=none` – These options disable the
  file name lookup cache, which has a very large impact on performance.
- `fsc` – This option enables local file caching, but does not change NFS cache
  coherency, and does not reduce latencies.

###### Note

When you mount your file system, consider increasing the size of the read and write
buffers for your NFS client to 1 MB.

## Optimizing small-file performance

You can improve small-file performance by minimizing file reopens, increasing
parallelism, and bundling reference files where possible.

- Minimize the number of round trips to the server.

Don't unnecessarily close files if you will need them later in a workflow. Keeping
file descriptors open enables direct access to the local copy in the cache. File open,
close, and metadata operations generally cannot be made asynchronously or through a
pipeline.

When reading or writing small files, the two additional round trips are significant.

Each round trip (file open, file close) can take as much time as reading or writing
megabytes of bulk data. It's more efficient to open an input or output file once, at the
beginning of your compute job, and hold it open for the entire length of the job.

- Use parallelism to reduce the impact of round-trip times.
- Bundle reference files in a `.zip` file. Some applications
  use a large set of small, mostly read-only reference files. Bundling these in a
  `.zip` file allows you to read many files with one open-close round
  trip.

The `.zip` format allows for random access to individual files.

## Optimizing directory performance

When performing a listing (**ls**) on very large directories (over 100k
files) that are being modified concurrently, Linux NFS clients can hang, not returning a response.
This issue is fixed in kernel 5.11, which has been ported to Amazon Linux 2 kernels 4.14, 5.4, and 5.10.

We recommend keeping the number of directories on your file system to less than 10,000, if possible.
Use nested subdirectories as much as possible.

When listing a directory, avoid getting file attributes if they are not required,
because they are not stored in the directory itself.

## Optimizing the NFS read_ahead_kb size

The NFS `read_ahead_kb` attribute defines the number of kilobytes for the
Linux kernel to read ahead or prefetch during a sequential read operation.

For Linux kernel versions prior to 5.4.\*, the `read_ahead_kb` value is set by
multiplying `NFS_MAX_READAHEAD` by the value for `rsize` (the client
configured read buffer size set in the mount options). When using the [recommended mount options](mounting-fs-mount-cmd-general.md "mounting-fs-mount-cmd-general.md"), this formula
sets `read_ahead_kb` to 15 MB.

###### Note

Starting with Linux kernel versions 5.4.\*, the Linux NFS client uses a default
`read_ahead_kb` value of 128 KB. We recommend increasing this value to 15
MB.

The Amazon EFS mount helper that is available in `amazon-efs-utils`
version 1.33.2 and later automatically modifies the `read_ahead_kb` value to
equal 15 \* `rsize`, or 15 MB, after mounting the file system.

For Linux kernels 5.4 or later, if you do not use the mount helper to mount your file
systems, consider manually setting `read_ahead_kb` to 15 MB for improved
performance. After mounting the file system, you can reset the `read_ahead_kb`
value by using the following command. Before using this command, replace the following
values:

- Replace `read-ahead-value-kb` with the desired size in
  kilobytes.
- Replace `efs-mount-point` with the file system's
  mount point.

```
device_number=$(stat -c '%d' `efs-mount-point`)
((major = ($device_number & 0xFFF00) >> 8))
((minor = ($device_number & 0xFF) | (($device_number >> 12) & 0xFFF00)))
sudo bash -c "echo `read-ahead-value-kb` > /sys/class/bdi/$major:$minor/read_ahead_kb"
```

The following example sets the `read_ahead_kb` size to 15 MB.

```
device_number=$(stat -c '%d' efs)
((major = ($device_number & 0xFFF00) >> 8))
((minor = ($device_number & 0xFF) | (($device_number >> 12) & 0xFFF00)))
sudo bash -c "echo 15000 > /sys/class/bdi/$major:$minor/read_ahead_kb"
```
