# Expand storage and

performance with Lightsail block storage disks

System disks offer the consistent and low-latency performance you need to run your
workloads. With Lightsail disks, you can scale your usage up or down within minutes—and
pay a low price for only what you provision.

You can select up to an 80 GB system disk on your Linux/Unix-based or Windows Server-based
instance. See [Get
started with Linux-based instances in Lightsail](getting-started-with-amazon-lightsail.md "getting-started-with-amazon-lightsail.md") or [Get
started with Windows Server-based instances](get-started-with-windows-based-instances-in-lightsail.md "get-started-with-windows-based-instances-in-lightsail.md").

You can also add more storage to your virtual private server by creating additional block
storage disks. See [Create and attach block storage disks to your Linux-based instance](create-and-attach-additional-block-storage-disks-linux-unix.md "create-and-attach-additional-block-storage-disks-linux-unix.md") or
[Create
and attach block storage disks to your Windows Server instance](create-and-attach-additional-block-storage-disks-windows.md "create-and-attach-additional-block-storage-disks-windows.md").

## Block storage disks

Block storage is a storage architecture that manages data as "blocks". Each storage block
(known as a "disk" in Lightsail) acts like an individual hard disk that you can attach to
your server. In general, you can use additional block storage for applications or software
that must separate out specific data from their core service, and to protect application data
in case of a failure or other issue with your instance and boot storage disk.

Lightsail offers solid-state drives (SSD) for block storage. This type of block storage
balances a reasonable price and good performance. It's intended to support the vast majority
of workloads that run on Lightsail. Lightsail additional block storage disks offer
consistent performance and the low latency needed for applications or software that frequently
access stored data.

###### Note

For customers with applications that require sustained IOPS performance or high amounts
of throughput per disk, or for customers running large databases like MongoDB, Cassandra,
etc., we recommend using Amazon EC2 with GP2 or Provisioned IOPS SSD storage instead of
Lightsail.

You can learn more about [Amazon EBS volumes](../../../AWSEC2/latest/WindowsGuide/EBSVolumes.md "../../../AWSEC2/latest/WindowsGuide/EBSVolumes.md") in the
_Amazon EC2 User Guide_.

## Disk Quotas

- 20,000 GB per Region.
- 16 TB per disk maximum, or 8 GB per disk minimum.
- Each instance can have up to 15 attached disks, and 1 boot volume disk.
