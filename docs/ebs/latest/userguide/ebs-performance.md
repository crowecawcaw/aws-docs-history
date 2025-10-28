# Amazon EBS volume performance

Several factors, including I/O characteristics and the configuration of your instances and
volumes, can affect the performance of Amazon EBS. If you follow the guidance on our Amazon EBS and
Amazon EC2 product detail pages you'll usually achieve good performance. However, there are
some cases where you might need to do some tuning to achieve peak performance. We recommend
that you tune performance with information from your actual workload, in addition to benchmarking,
to determine your optimal configuration. After you learn the basics of working with EBS volumes,
it's a good idea to look at the I/O performance you require and at your options for increasing
Amazon EBS performance to meet those requirements.

AWS updates to the performance of EBS volume types might not
immediately take effect on your existing volumes. To see full performance on an older volume, you
might first need to perform a `ModifyVolume` action on it. For more information, see
[Modify an Amazon EBS volume using Elastic Volumes operations](ebs-modify-volume.md "ebs-modify-volume.md").

###### Contents

- [Amazon EBS performance tips](#tips "#tips")
- [Amazon EBS optimization](ebs-optimization.md "ebs-optimization.md")
- [Initialize Amazon EBS volumes](initalize-volume.md "initalize-volume.md")
- [Configurable instance bandwidth weighting](instance-bandwidth-configuration.md "instance-bandwidth-configuration.md")
- [Amazon EBS I/O characteristics and monitoring](ebs-io-characteristics.md "ebs-io-characteristics.md")
- [Amazon EBS and RAID configuration](raid-config.md "raid-config.md")
- [Benchmark Amazon EBS volumes](benchmark_procedures.md "benchmark_procedures.md")

## Amazon EBS performance tips

These tips represent best practices for getting optimal performance from your EBS volumes
in a variety of user scenarios.

### Use EBS-optimized instances

On instances without support for EBS-optimized throughput, network traffic can contend
with traffic between your instance and your EBS volumes; on EBS-optimized instances, the two
types of traffic are kept separate. Some EBS-optimized instance configurations incur an
extra cost (such as C3, R3, and M3), while others are always EBS-optimized at no extra cost
(such as M4, C4, C5, and D2). For more information, see [Amazon EBS optimization](ebs-optimization.md "ebs-optimization.md").

### Configure instance bandwidth

For supported instance types, you can configure the instance bandwidth weighting to increase
Amazon EBS bandwidth by 25 percent using the `ebs-1` bandwidth weighting. This feature
allows you to optimize your instance's network resource allocation between EBS and VPC networking,
potentially improving EBS performance for I/O-intensive workloads. For more information, see
[Configurable instance bandwidth weighting](instance-bandwidth-configuration.md "instance-bandwidth-configuration.md").

### Understand how performance is calculated

When you measure the performance of your EBS volumes, it is important to understand the
units of measure involved and how performance is calculated. For more information, see [Amazon EBS I/O characteristics and monitoring](ebs-io-characteristics.md "ebs-io-characteristics.md").

### Understand your workload

There is a relationship between the maximum performance of your EBS volumes, the size
and number of I/O operations, and the time it takes for each action to complete. Each of
these factors (performance, I/O, and latency) affects the others, and different applications
are more sensitive to one factor or another. For more information, see
[Benchmark Amazon EBS volumes](benchmark_procedures.md "benchmark_procedures.md").

### Be aware of the performance penalty When initializing volumes

from snapshots

There is a significant increase in latency when you first access each block of data
on a new EBS volume that was created from a snapshot. You can avoid this performance
hit using one of the following options:

- Access each block prior to putting the volume into production. This process is
  called _initialization_ (formerly known as pre-warming). For more
  information, see [Manually initialize the volumes after creation](initalize-volume.md#ebs-initialize "initalize-volume.md#ebs-initialize").
- Enable fast snapshot restore on a snapshot to ensure that the EBS volumes
  created from it are fully-initialized at creation and instantly deliver all
  of their provisioned performance. For more information, see [Amazon EBS fast snapshot restore](ebs-fast-snapshot-restore.md "ebs-fast-snapshot-restore.md").

### Factors that can degrade HDD performance

When you create a snapshot of a Throughput Optimized HDD (`st1`) or Cold HDD (`sc1`) volume,
performance may drop as far as the volume's baseline value while the snapshot is in
progress. This behavior is specific to these volume types. Other factors that can limit
performance include driving more throughput than the instance can support, the performance
penalty encountered while initializing volumes created from a snapshot, and excessive
amounts of small, random I/O on the volume. For more information about calculating
throughput for HDD volumes, see [Amazon EBS volume types](ebs-volume-types.md "ebs-volume-types.md").

Your performance can also be impacted if your application isn’t sending enough I/O
requests. This can be monitored by looking at your volume’s queue length and I/O size. The
queue length is the number of pending I/O requests from your application to your volume. For
maximum consistency, HDD-backed volumes must maintain a queue length (rounded to the nearest
whole number) of 4 or more when performing 1 MiB sequential I/O. For more information about
ensuring consistent performance of your volumes, see [Amazon EBS I/O characteristics and monitoring](ebs-io-characteristics.md "ebs-io-characteristics.md")

### Increase read-ahead for high-throughput, read-heavy workloads on `st1` and `sc1` (_Linux instances only_)

Some workloads are read-heavy and access the block device through the operating system
page cache (for example, from a file system). In this case, to achieve the maximum
throughput, we recommend that you configure the read-ahead setting to 1 MiB. This is a
per-block-device setting that should only be applied to your HDD volumes.

To examine the current value of read-ahead for your block devices, use the following
command:

```
`$` `sudo blockdev --report /dev/`<device>``
```

Block device information is returned in the following format:

```
RO    RA   SSZ   BSZ   StartSec            Size   Device
rw   256   512  4096       4096      8587820544   /dev/<device>
```

The device shown reports a read-ahead value of 256 (the default). Multiply this number
by the sector size (512 bytes) to obtain the size of the read-ahead buffer, which in this
case is 128 KiB. To set the buffer value to 1 MiB, use the following command:

```
`$` `sudo blockdev --setra 2048 /dev/`<device>``
```

Verify that the read-ahead setting now displays 2,048 by running the first command
again.

Only use this setting when your workload consists of large, sequential I/Os. If it
consists mostly of small, random I/Os, this setting will actually degrade your performance.
In general, if your workload consists mostly of small or random I/Os, you should consider
using a General Purpose SSD (`gp2` and `gp3`) volume rather than an `st1` or `sc1` volume.

### Use a modern Linux kernel (_Linux instances only_)

Use a modern Linux kernel with support for indirect descriptors. Any Linux kernel 3.8
and above has this support, as well as any current-generation EC2 instance. If your average
I/O size is at or near 44 KiB, you may be using an instance or kernel without support for
indirect descriptors. For information about deriving the average I/O size from Amazon CloudWatch
metrics, see [Amazon EBS I/O characteristics and monitoring](ebs-io-characteristics.md "ebs-io-characteristics.md").

To achieve maximum throughput on `st1` or `sc1` volumes, we recommend applying a value of
256 to the `xen_blkfront.max` parameter (for Linux kernel versions below 4.6) or
the `xen_blkfront.max_indirect_segments` parameter (for Linux kernel version 4.6
and above). The appropriate parameter can be set in your OS boot command line.

For example, in an Amazon Linux AMI with an earlier kernel, you can add it to the end of the
kernel line in the GRUB configuration found in `/boot/grub/menu.lst`:

```
kernel /boot/vmlinuz-4.4.5-15.26.amzn1.x86_64 root=LABEL=/ console=ttyS0 xen_blkfront.max=256
```

For a later kernel, the command would be similar to the following:

```
kernel /boot/vmlinuz-4.9.20-11.31.amzn1.x86_64 root=LABEL=/ console=tty1 console=ttyS0 xen_blkfront.max_indirect_segments=256
```

Reboot your instance for this setting to take effect.

For more information, see [Configure GRUB for paravirtual AMIs](../../../linux/al2/ug/UserProvidedKernels.md#configuringGRUB "../../../linux/al2/ug/UserProvidedKernels.md#configuringGRUB").
Other Linux distributions, especially those that do not use the GRUB boot loader, may require
a different approach to adjusting the kernel parameters.

For more information about EBS I/O characteristics, see the [Amazon EBS: Designing for
Performance](https://www.youtube.com/watch?v=2wKgha8CZ_w "https://www.youtube.com/watch?v=2wKgha8CZ_w") re:Invent presentation on this topic.

### Use RAID 0 to maximize utilization of instance resources

Some instance types can drive more I/O throughput than what you can provision for a
single EBS volume. You can join multiple volumes together in a RAID 0 configuration to use
the available bandwidth for these instances. For more information, see [Amazon EBS and RAID configuration](raid-config.md "raid-config.md").

### Monitor Amazon EBS volume performance

You can monitor and analyze the performance of your Amazon EBS volumes using Amazon CloudWatch,
status checks, and EBS detailed performance statistics. For more information, see
[Amazon CloudWatch metrics for Amazon EBS](using_cloudwatch_ebs.md "using_cloudwatch_ebs.md") and
[Amazon EBS detailed performance statistics](nvme-detailed-performance-stats.md "nvme-detailed-performance-stats.md").
