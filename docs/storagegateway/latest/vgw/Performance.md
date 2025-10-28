# Performance and optimization for

Volume Gateway

This section describes Storage Gateway performance.

###### Topics

- [Optimizing gateway performance](#Optimizing-common "#Optimizing-common")

## Optimizing gateway performance

### Recommended Gateway Server

Configuration

To obtain the best performance out of your gateway, Storage Gateway recommends the following
gateway configuration for your gateway's host server:

- At least 24 dedicated physical CPU cores
- For Volume Gateway, your hardware should dedicate the following
  amounts of RAM:
  - At least 16 GiB of reserved RAM for gateways with cache size up to 16
    TiB
  - At least 32 GiB of reserved RAM for gateways with cache size 16 TiB to
    32 TiB
  - At least 48 GiB of reserved RAM for gateways with cache size 32 TiB to
    64 TiB

- Disk 1, to be used as the gateway cache as follows:
  - SSD using an NVMe controller.

- Disk 2, to be used as the gateway upload buffer as follows:
  - SSD using an NVMe controller.

- Disk 3, to be used as the gateway upload buffer as follows:
  - SSD using an NVMe controller.

- Network adapter 1 configured on VM network 1:
  - Use VM network 1 and add VMXnet3 (10 Gbps) to be used for
    ingestion.

- Network adapter 2 configured on VM network 2:
  - Use VM network 2 and add a VMXnet3 (10 Gbps) to be used to connect to
    AWS.

### Add Resources to Your

Gateway

The following bottlenecks can reduce the performance of your
Volume Gateway below the theoretical maximum sustained
throughput (your bandwidth to AWS cloud):

- CPU core count
- Cache/Upload buffer disk throughput
- Total RAM amount
- Network bandwidth to AWS
- Network bandwidth from initiator to gateway

This section contains steps you can take in order to optimize the performance of your
gateway. This guidance is based on adding resources to your gateway or your application
server.

You can optimize gateway performance by adding resources to your gateway in one or
more of the following ways.

**Use higher-performance disks**

Cache and upload buffer disk throughput can limit your gateway's upload
and download performance. If your gateway is exhibiting performance
significantly below what is expected, consider improving the cache and
upload buffer disk throughput by:

- Using a striped RAID such as RAID 10 to improve disk throughput,
  ideally with a hardware RAID controller.

###### Note

_RAID_ (redundant array of independent
disks) or specifically disk striped RAID configurations like
RAID 10, is the process of dividing a body of data into blocks
and spreading the data blocks across multiple storage devices.
The RAID level you use affects the exact speed and fault
tolerance you can achieve. By striping IO workloads out across
multiple disks, the overall throughput of the RAID device is
much higher than that of any single member disk.

- Using directly attached, high performance disks

To optimize gateway performance, you can add high-performance
disks such as solid-state drives (SSDs) and a NVMe controller. You
can also attach virtual disks to your VM directly from a storage
area network (SAN) instead of the Microsoft Hyper-V NTFS. Improved
disk performance generally results in better throughput and more
input/output operations per second (IOPS).

To measure throughput, use the `ReadBytes` and
`WriteBytes` metrics with the `Samples`
Amazon CloudWatch statistic. For example, the `Samples`
statistic of the `ReadBytes` metric over a sample period
of 5 minutes divided by 300 seconds gives you the IOPS. As a general
rule, when you review these metrics for a gateway, look for low
throughput and low IOPS trends to indicate disk-related bottlenecks.
.

###### Note

CloudWatch metrics are not available for all gateways. For
information about gateway metrics, see [Monitoring Storage Gateway](Main_monitoring-gateways-common.md "Main_monitoring-gateways-common.md").

**Add more upload buffer disks**

To achieve higher write throughput, add at least two upload buffer disks.
When data is written to the gateway, it is written and stored locally on the
upload buffer disks. Afterwards, the stored local data is asynchronously
read from the disks to be processed and uploaded to AWS. Adding more
upload buffer disks may reduce the amount of concurrent I/O operations
performed to each individual disk. This can result in increased write
throughput to the gateway.

**Back gateway virtual disks with separate physical
disks**

When you provision gateway disks, we strongly recommend that you
_don't_ provision local disks for the upload
buffer and cache storage that use the same underlying physical storage disk.
For example, for VMware ESXi, the underlying physical storage resources are
represented as a data store. When you deploy the gateway VM, you choose a
data store on which to store the VM files. When you provision a virtual disk
(for example, as an upload buffer), you can store the virtual disk in the
same data store as the VM or a different data store.

If you have more than one data store, then we strongly recommend that you
choose one data store for each type of local storage you are creating. A
data store that is backed by only one underlying physical disk can lead to
poor performance. An example is when you use such a disk to back both the
cache storage and upload buffer in a gateway setup. Similarly, a data store
that is backed by a less high-performing RAID configuration such as RAID 1
or RAID 6 can lead to poor performance.

**Add CPU resources to your gateway host**

The minimum requirement for a gateway host server is four virtual
processors. To optimize gateway performance, confirm that each virtual
processor that is assigned to the gateway VM is backed by a dedicated CPU
core. In addition, confirm that you are not oversubscribing the CPUs of the
host server.

When you add additional CPUs to your gateway host server, you increase the
processing capability of the gateway. Doing this allows your gateway to deal
with, in parallel, both storing data from your application to your local
storage and uploading this data to Amazon S3. Additional CPUs also help ensure
that your gateway gets enough CPU resources when the host is shared with
other VMs. Providing enough CPU resources has the general effect of
improving throughput.

**Increase bandwidth between your gateway and AWS
cloud**

Increasing your bandwidth to and from AWS will increase the maximum rate
of data ingress to your gateway and egress to AWS cloud. This can improve
your gateway performance if network speed is the limiting factor in your
gateway configuration, rather than other factors like slow disks or poor
gateway-initiator connection bandwidth.

###### Note

Your observed gateway performance will likely be lower than your
network bandwidth due to other limiting factors listed here, such as
cache/upload buffer disk throughput, CPU core count, total RAM amount,
or the bandwidth between your initiator and gateway. Furthermore, your
gateway's normal operation involves many actions taken to protect your
data, which might cause the observed performance to be less than your
network bandwidth.

**Change the volumes configuration**

For Volume Gateways, if you find that adding more volumes to a gateway
reduces the throughput to the gateway, consider adding the volumes to a
separate gateway. In particular, if a volume is used for a high-throughput
application, consider creating a separate gateway for the high-throughput
application. However, as a general rule, you should not use one gateway for
all of your high-throughput applications and another gateway for all of your
low-throughput applications. To measure your volume throughput, use the
`ReadBytes` and `WriteBytes` metrics.

For more information about these metrics, see [Measuring Performance Between Your Application
and Gateway](PerfAppGateway-common.md "PerfAppGateway-common.md").

### Optimize iSCSI Settings

You can optimize iSCSI settings on your iSCSI initiator to achieve higher I/O
performance. We recommend choosing 256 KiB for `MaxReceiveDataSegmentLength`
and `FirstBurstLength`, and 1 MiB for `MaxBurstLength`. For more
information about configuring iSCSI settings, see [Customizing iSCSI Settings](recommendediSCSISettings.md "recommendediSCSISettings.md").

###### Note

These recommended settings can facilitate overall better performance. However, the
specific iSCSI settings that are needed to optimize performance vary depending on
which backup software you use. For details, see your backup software documentation.

### Add Resources to Your

Application Environment

**Increase the bandwidth between your application server
and your gateway**

The connection between your iSCSI initiator and gateway can limit your
upload and download performance. If your gateway is exhibiting performance
significantly worse than expected and you have already improved your CPU
core count and disk throughput, consider:

- Upgrading your network cables to have higher bandwidth between
  your initiator and gateway.

To optimize gateway performance, ensure that the network bandwidth between
your application and the gateway can sustain your application needs. You can
use the `ReadBytes` and `WriteBytes` metrics of the
gateway to measure the total data throughput.

For your application, compare the measured throughput with the desired
throughput. If the measured throughput is less than the desired throughput,
then increasing the bandwidth between your application and gateway can
improve performance if the network is the bottleneck. Similarly, you can
increase the bandwidth between your VM and your local disks, if they're not
direct-attached.

**Add CPU resources to your application
environment**

If your application can use additional CPU resources, then adding more
CPUs can help your application to scale its I/O load.
