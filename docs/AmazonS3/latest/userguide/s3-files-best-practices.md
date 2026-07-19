# S3 Files best practices

This page describes the recommended best practices for working with S3 file
systems.

## Performance and cost optimization

- **Parallelize your workloads** – S3 Files
  is designed to support highly parallel workloads. Distributing reads across
  multiple files and multiple compute instances helps maximize aggregate throughput.
  You can also create multiple file systems scoped to different specific prefixes
  within the same bucket (instead of creating one file system over the entire
  bucket) to scale horizontally and improve aggregate
  throughput.
- **Scope your file system to the smallest prefix your
  workload needs to minimize impact of renames** – S3 has no native
  concept of directories. When you rename or move a directory, S3 Files must write
  the data to a new object with the updated key and delete the original for every
  file in that directory. Renaming directories with tens of millions of files can
  significantly increase S3 request costs and synchronization time. Scope your file
  system to your active dataset, or structure your data so that directories you
  expect to rename contain fewer files. For more information, see [Understanding the impact of rename and move operations](s3-files-synchronization.md#s3-files-sync-rename-move "s3-files-synchronization.md#s3-files-sync-rename-move").
- **Use large IO sizes** – S3 Files meters
  each read and write operation at a minimum of 32 KB. Using larger IO sizes (1 MB
  or more) amortizes per-operation overhead and is more cost effective than many
  small reads or writes. When using the mount helper, the default NFS read and
  write buffer sizes are set to 1 MB for optimal
  performance.
- **Tune your sizeLessThan value in import
  configuration to match your file sizes** – By default, S3 Files
  caches data for files smaller than 128 KB when you first access a directory.
  Files larger than this threshold are read directly from S3. If your workload
  performs small, latency-sensitive reads on larger files, increase the
  sizeLessThan threshold to match the file sizes you need on the file system's high
  performance storage for low-latency access. For more information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md "s3-files-synchronization-customizing.md").
- **Set expiration windows to match your workload
  lifecycle** – Data that has not been read within the expiration
  window is automatically removed from the file system. For short-lived workloads
  such as batch jobs or training runs, use a shorter expiration (1–7 days) to
  minimize storage costs. For workloads that revisit the same data over weeks, use
  a longer expiration (30–90 days) to continue benefiting from the low latency. For
  more information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md "s3-files-synchronization-customizing.md").
- **Use prefix-scoped rules for mixed
  workloads** – If your bucket contains both frequently accessed and
  infrequently accessed data, create separate import rules for each prefix. This
  lets you import data aggressively for hot prefixes while keeping cold prefixes
  metadata-only. For more information, see [Customizing synchronization for S3 Files](s3-files-synchronization-customizing.md "s3-files-synchronization-customizing.md").
- **Create a mount target in every Availability
  Zone** – We recommend creating one mount target in each Availability
  Zone you operate in so that you can reduce cross-AZ data transfer costs and
  improve performance. This ensures that your compute resources always have a local
  network path to the file system, improving both availability and latency. When
  you create a file system using the AWS Management Console, S3 Files
  automatically creates one mount target in every Availability Zone in your
  selected VPC.

## Synchronization

- **Understand the S3 Files consistency
  model** – When a file in the file system is modified at the same
  time as its corresponding object in the S3 bucket, S3 Files treats the S3 bucket
  as the source of truth and moves the file to the lost and found directory. To
  avoid conflicts, designate one path (file system or S3) as the primary
  writer.
- **Monitor synchronization health** – Use
  CloudWatch metrics to track the status of synchronization between your file
  system and S3 bucket. A growing `PendingExports` indicates that your
  workload is generating changes faster than the synchronization rate, which means
  synchronization will take longer to complete. A non-zero
  `ExportFailures` CloudWatch metric indicates files that could not
  be exported and require action. For more information, see [Troubleshooting S3 Files](s3-files-troubleshooting.md "s3-files-troubleshooting.md").

## Access control

- **Follow the principle of least
  privilege** – Grant only the minimum permissions required for each
  IAM role and file system policy. For example, if a compute resource only needs to
  read data from the file system, attach the
  `AmazonS3FilesClientReadOnlyAccess` managed policy instead of
  `AmazonS3FilesClientFullAccess`. Additionally, consider creating
  your file system scoped to a specific prefix rather than the entire bucket, so
  that clients can only access data within that prefix.
- **Do not modify the S3 Files IAM
  role** – Do not modify or delete the IAM role that S3 Files assumes
  to synchronize with your S3 bucket. Changing or removing this role can break
  synchronization between your file system and S3
  bucket.
- **Do not modify the S3 Files EventBridge
  rule** – S3 Files creates an EventBridge rule (prefixed with
  DO-NOT-DELETE-S3-Files) to detect changes in your S3 bucket. Do not disable,
  modify, or delete this rule. Removing it prevents S3 Files from detecting new or
  changed objects in your bucket, causing your file system to become
  stale.
- **Consider restricting access to logs written by
  `efs-utils`** – `efs-utils` writes S3
  object key names directly in logs which it stores in the directory
  `/var/log/amazon/efs`. If your S3 key names contain sensitive
  information, you should restrict access to this directory via POSIX permissions.
  For example, you could restrict access via the command
  `sudo chmod 700 /var/log/amazon/efs`.

## Monitoring

- **Set alarms on synchronization
  failures** – Create CloudWatch alarms on
  `ImportFailures` and `ExportFailures` to be notified
  when files fail to synchronize. Failed exports may indicate permission issues,
  encryption key problems, or path length limits. For more information, see [Troubleshooting S3 Files](s3-files-troubleshooting.md "s3-files-troubleshooting.md").

## Migration

To migrate data from on-premises storage to your S3 bucket for the first time, we
recommend using AWS DataSync. DataSync automates and accelerates the transfer of large
datasets and preserves file metadata and permissions during migration. For more
information, see [What is AWS
DataSync?](../../../datasync/latest/userguide/what-is-datasync.md "../../../datasync/latest/userguide/what-is-datasync.md").
