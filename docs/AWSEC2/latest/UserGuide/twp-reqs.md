# Requirements for using torn write prevention on Amazon EC2

For torn write prevention to work properly, an I/O operation must meet size, alignment, and boundary
requirements, as specified in the `NTWPU`, `NTWGU`, `NTWBU` fields. You
must configure your operating system to ensure that the specific storage subsystem (file system, LVM, RAID,
etc) does not modify I/O properties down the storage stack, including block merges, splits, or block
address relocation, before being submitted to the device.

Torn write prevent has been tested with the following configuration:

- An instance type and storage type that supports the required block size.
- Amazon Linux 2 with kernel version 5.10 or later.
- ext4 with `bigalloc` enabled and a cluster size of 16 KiB, and the most recent ext4
  utilities (e2fsprogs 1.46.5 or later).
- `O_DIRECT` file access mode to bypass Linux kernel buffer cache.

###### Note

You do not need to disable I/O merging for MySQL and MariaDB workloads.
