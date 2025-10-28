# Configure your workload on Amazon EC2 for torn write prevention

Torn write prevention is enabled by default on [supported instance types with
supported volumes](supported-block-sizes.md "supported-block-sizes.md"). You do not need to enabled any additional settings to enable your volume or instance for torn
write prevention.

###### Note

There is no performance impact on workloads that do not support torn write prevention. You do not need to make any
changes for these workloads.

Workloads that do support torn write prevention, but are not configured to use it,
continue to use the doublewrite buffer and do not receive any performance benefits.

To configure your MySQL or MariaDB software stack to disable the doublewrite buffer and
use torn write prevention, complete the following steps:

1. Configure your volume to use ext4 file system with the BigAlloc option and set the cluster size to 4 KiB, 8 KiB,
   or 16 KiB. Using BigAlloc with a cluster size of 4 KiB, 8 KiB, or 16 KiB ensures that the file system allocates files
   that align with the respective boundary.

```
`$`  mkfs.ext4 -O bigalloc -C `4096|8192|16384` `device_name`
```

###### Note

For MySQL and MariaDB, you must use `-C 16384` to match the database page size. Setting allocation
granularity to a value other than a multiple of the page size can result in allocations that might be mismatched
with torn write prevention boundaries of the storage device.

For example:

```
`$`  mkfs.ext4 -O bigalloc -C 16384 /dev/nvme1n1
```

2. Configure InnoDB to use the `0_DIRECT` flushing method and turn off InnoDB doublewrite. Use your
   preferred text editor to open `/etc/my.cnf`, and update the `innodb_flush_method`
   and `innodb_doublewrite` parameters as follows:

```
innodb_flush_method=O_DIRECT
innodb_doublewrite=0
```

###### Important

If you are using Logical Volume Manager (LVM) or other storage virtualization layer,
make sure that the starting offsets of the volumes are aligned on 16 KiB multiples. This is
relative to the underlying NVMe storage to account for the metadata headers and superblocks
used by the storage virtualization layer. If you add an offset to the LVM physical volume,
it can cause misalignment between the file system allocations and the NVMe device's offsets,
which would invalidate torn write prevention. For more information, see
`--dataalignmentoffset` in the [Linux manual
page](https://man7.org/linux/man-pages/man8/pvcreate.8.html "https://man7.org/linux/man-pages/man8/pvcreate.8.html").
