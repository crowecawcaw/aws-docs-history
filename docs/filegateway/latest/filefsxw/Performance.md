Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Performance and optimization

This section describes guidance and best practices for optimizing File Gateway
performance.

###### Topics

- [Basic performance guidance for FSx File Gateway](#performance-fgw "#performance-fgw")
- [Optimizing gateway performance](#Optimizing-common "#Optimizing-common")
- [Maximizing S3 File Gateway throughput](Performance-Throughput.md "Performance-Throughput.md")
- [Optimizing S3 File Gateway for SQL Server database
  backups](SQL-Backup-Best-Practices.md "SQL-Backup-Best-Practices.md")

## Basic performance guidance for FSx File Gateway

In this section, you can find guidance for provisioning hardware
for your FSx File Gateway VM. The instance configurations that are listed in the table are
examples, and are provided for reference.

For best performance, the cache disk size must be tuned to the size of the active
working set. Using multiple local disks for the cache increases write performance by
parallelizing access to data and leads to higher IOPS.

###### Note

We don't recommend using ephemeral storage. For information about using ephemeral
storage, see [Using ephemeral storage with EC2 gateways](ephemeral-disk-cache.md "ephemeral-disk-cache.md").

The suggested size limit for individual directories in the file
systems that you connect to File Gateway is 10,000 files per
directory. You can use File Gateway with directories that have more than 10,000
files, but performance might be impacted.

In the following tables, _cache
hit_ read operations are reads from the file data that is served from
cache. _Cache miss_ read operations are reads from the
file data that is served from Amazon FSx for Windows File Server.

The following table shows an example FSx File Gateway
configuration.

### FSx File Gateway performance on Windows

clients

| Example Configuration                                                                                                        | Protocol               | Write throughput (file sizes 1 GB) | Cache hit read throughput | Cache miss read throughput |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ---------------------------------- | ------------------------- | -------------------------- | ---------------------- |
| Root disk: 80 GB, io1 SSD, 4,000 IOPS<br>Cache disks: 2 x 2 TiB NVME<br>Minimum network performance: 10 Gbps<br>CPU: 32 vCPU | RAM: 244 GB            | SMBv3<br>• 1 thread                | 162 MiB/sec (1.4 Gbps)    | 403 MiB/sec (3.4 Gbps)     | 288 MiB/sec (2.4 Gbps) |
| SMBv3<br>• 8 threads                                                                                                         | 511 MiB/sec (4.3 Gbps) | 571 MiB/sec (4.8 Gbps)             | 567 MiB/sec (4.8 Gbps)    |

###### Note

Your performance might vary based on your host platform configuration and network
bandwidth. Write throughput performance decreases with file size, with the highest
achievable throughput for small files (less than 32MiB) being 16 files per
second.

## Optimizing gateway performance

You can find information following about how to optimize the performance of your gateway.
The guidance is based on adding resources to your gateway and adding resources to your
application server.

### Add Resources to Your

Gateway

You can optimize gateway performance by adding resources to your gateway in one or
more of the following ways.

**Use higher-performance disks**

To optimize gateway performance, you can add high-performance disks such
as solid-state drives (SSDs) and a NVMe controller. You can also attach
virtual disks to your VM directly from a storage area network (SAN) instead
of the Microsoft Hyper-V NTFS. Improved disk performance generally results
in better throughput and more input/output operations per second (IOPS). For
information about adding disks, see [Configuring additional cache
storage](ConfiguringLocalDiskStorage.md "ConfiguringLocalDiskStorage.md").

To measure throughput, use the `ReadBytes` and
`WriteBytes` metrics with the `Samples` Amazon
CloudWatch statistic. For example, the `Samples` statistic of the
`ReadBytes` metric over a sample period of 5 minutes divided
by 300 seconds gives you the IOPS. As a general rule, when you review these
metrics for a gateway, look for low throughput and low IOPS trends to
indicate disk-related bottlenecks.

###### Note

CloudWatch metrics are not available for all gateways. For information about
gateway metrics, see [Monitoring your FSx File Gateway](monitoring-file-gateway.md "monitoring-file-gateway.md").

**Add CPU resources to your gateway host**

The minimum requirement for a gateway host server is four virtual
processors. To optimize gateway performance, confirm that the four virtual
processors that are assigned to the gateway VM are backed by four cores. In
addition, confirm that you are not oversubscribing the CPUs of the host
server.

When you add additional CPUs to your gateway host server, you increase the
processing capability of the gateway. Doing this allows your gateway to deal
with, in parallel, both storing data from your application to your local
storage and uploading this data to FSx for Windows File Server.
Additional CPUs also help ensure that your gateway gets enough CPU resources
when the host is shared with other VMs. Providing enough CPU resources has
the general effect of improving throughput.

Storage Gateway supports using 24 CPUs in your gateway host server. You can use 24
CPUs to significantly improve the performance of your gateway. We recommend
the following gateway configuration for your gateway host server:

- 24 CPUs.
- 16 GiB of reserved RAM for File Gateways
  - 16 GiB of reserved RAM for gateways with cache size up to
    16 TiB
  - 32 GiB of reserved RAM for gateways with cache size 16 TiB
    to 32 TiB
  - 48 GiB of reserved RAM for gateways with cache size 32 TiB
    to 64 TiB

- Disk 1 attached to paravirtual controller 1, to be used as the
  gateway cache as follows:
  - SSD using an NVMe controller.

- Network adapter 1 configured on VM network 1:
  - Use VM network 1 and add VMXnet3 (10 Gbps) to be used for
    ingestion.

- Network adapter 2 configured on VM network 2:
  - Use VM network 2 and add a VMXnet3 (10 Gbps) to be used to
    connect to AWS.

**Back gateway virtual disks with separate physical
disks**

When you provision gateway disks, we strongly recommend that you
don't provision local disks for local storage that use the same
underlying physical storage disk. For example, for VMware ESXi, the
underlying physical storage resources are represented as a data store. When
you deploy the gateway VM, you choose a data store on which to store the VM
files. When you provision a virtual disk (for example, as an upload buffer),
you can store the virtual disk in the same data store as the VM or a
different data store.

If you have more than one data store, then we strongly recommend that you
choose one data store for each type of local storage you are creating. A
data store that is backed by only one underlying physical disk can lead to
poor performance. An example is when you use such a disk to back both the
cache storage and upload buffer in a gateway setup. Similarly, a data store
that is backed by a less high-performing RAID configuration such as RAID 1
can lead to poor performance.

### Add Resources to Your

Application Environment

**Increase the bandwidth between your application server
and your gateway**

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

Some file operations on the FSx File Gateway, such as top-level folder renames or permission changes, can result in multiple file operations that lead to a high I/O load on your FSx for Windows File Server file system. If your file system doesn't have enough performance resources for your workload, the file system might delete [shadow copies](../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md "../../../fsx/latest/WindowsGuide/shadow-copies-fsxW.md") because it prioritizes availability for ongoing I/O over historical shadow copy retention.

In the Amazon FSx console, check the **Monitoring and performance** page to see if your file system is under-provisioned. If it is, you can switch to SSD storage, increase throughput capacity, or increase SSD IOPS to handle your workload.
