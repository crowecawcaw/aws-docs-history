# Mount an Amazon S3 bucket as a local file system

Mountpoint for Amazon S3 is a high-throughput open source file client for mounting an Amazon S3 bucket as a
local file system. With Mountpoint, your applications can access objects stored in Amazon S3
through file system operations, such as open and read. Mountpoint automatically
translates these operations into S3 object API calls, giving your applications access to the
elastic storage and throughput of Amazon S3 through a file interface.

Mountpoint for Amazon S3 is [available for production use on your large-scale read-heavy
applications](https://aws.amazon.com/blogs/aws/mountpoint-for-amazon-s3-generally-available-and-ready-for-production-workloads/ "https://aws.amazon.com/blogs/aws/mountpoint-for-amazon-s3-generally-available-and-ready-for-production-workloads/"): data lakes, machine learning training, image rendering, autonomous vehicle
simulation, extract, transform, and load (ETL), and more.

Mountpoint supports basic file system operations, and can read
files up to 5 TB in size. It can list and read existing files, and it can create new ones. It
cannot modify existing files or delete directories, and it does not support symbolic links or
file locking. Mountpoint is ideal for applications that do not need all of the features
of a shared file system and POSIX-style permissions but require Amazon S3's elastic throughput to
read and write large S3 datasets. For details, see [Mountpoint
file system behavior](https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md") on GitHub. For workloads that require full POSIX
support, we recommend [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/ "https://aws.amazon.com/fsx/lustre/")
and its [support for linking Amazon S3 buckets](../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md "../../../fsx/latest/LustreGuide/create-dra-linked-data-repo.md").

Mountpoint for Amazon S3 is available only for Linux operating systems. You can use
Mountpoint to access S3 objects in all storage classes except
S3 Glacier Flexible Retrieval, S3 Glacier Deep Archive, S3 Intelligent-Tiering Archive Access Tier, and
S3 Intelligent-Tiering Deep Archive Access Tier.

###### Topics

- [Installing Mountpoint](mountpoint-installation.md "mountpoint-installation.md")
- [Configuring and using Mountpoint](mountpoint-usage.md "mountpoint-usage.md")
- [Troubleshooting Mountpoint](mountpoint-troubleshooting.md "mountpoint-troubleshooting.md")
