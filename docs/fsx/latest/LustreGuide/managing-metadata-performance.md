# Managing metadata performance

You can update the metadata configuration of your FSx for Lustre file system without
any disruption to your end users or applications by using the Amazon FSx console, Amazon FSx API,
or AWS Command Line Interface (AWS CLI). The update procedure increases the number of provisioned Metadata
IOPS for your file system.

###### Note

Enhanced metadata is available only for 2.15 file systems. You can increase metadata performance only
on FSx for Lustre file systems created with the Persistent 2 deployment type and a metadata configuration
specified. You cannot add or update the metadata configuration for an FSx for Lustre file system if the metadata
configuration is not specified at the time of file system creation. This also applies to file systems
restored from backups of 2.12 file systems which did not support enhanced metadata performance, or from
2.15 file systems which had no metadata configuration specified.

The increased metadata performance of your file system is available for use within
minutes. You can update the metadata performance at anytime, as long as metadata performance
increase requests are at least 6 hours apart. While scaling metadata performance, the
file system may be unavailable for a few minutes. File operations issued by clients while
the file system is unavailable will transparently retry and eventually succeed after metadata
performance scaling is complete. You will be billed for the new metadata performance increase
after it becomes available to you.

You can track the progress of a metadata performance increase at any time by using the
Amazon FSx console, CLI, and API. For more information, see
[Monitoring metadata configuration updates](monitoring-metadata-performance-increase.md "monitoring-metadata-performance-increase.md").

###### Topics

- [Lustre metadata performance configuration](#metadata-configuration "#metadata-configuration")
- [Considerations when increasing
  metadata performance](#metadata-scaling-considerations "#metadata-scaling-considerations")
- [When to increase metadata performance](#when-to-modify-metadata-performance "#when-to-modify-metadata-performance")
- [Increasing metadata performance](modify-metadata-performance.md "modify-metadata-performance.md")
- [Changing the metadata configuration mode](switch-provisioning-mode.md "switch-provisioning-mode.md")
- [Monitoring metadata configuration updates](monitoring-metadata-performance-increase.md "monitoring-metadata-performance-increase.md")

## Lustre metadata performance configuration

The number of provisioned Metadata IOPS determines the maximum rate of metadata
operations that can be supported by the file system.

When you create the file system, you choose a metadata configuration mode:

- For SSD file systems, you can choose Automatic mode if you want Amazon FSx to automatically
  provision and scale the Metadata IOPS on your file system based on your file system's storage
  capacity. Note that Intelligent-Tiering file systems don't support Automatic mode.
- For SSD file systems, you can choose User-provisioned if you want to specify the number of Metadata IOPS
  to provision for your file system.
- For Intelligent-Tiering file systems, you must choose User-provisioned mode. With User-provisioned mode,
  you can specify the number of Metadata IOPS to provision for your file system.

On SSD file systems, you can switch from Automatic mode to User-provisioned mode
at any time. You can also switch from User-provisioned to Automatic mode if the number of Metadata IOPS
provisioned on your file system matches the default number of Metadata IOPS provisioned in Automatic mode.
Intelligent-Tiering file systems only support User-provisioned mode, so you can't switch metadata
configuration modes.

Valid Metadata IOPS values are as follows:

- For SSD file systems, valid Metadata IOPS values are 1500, 3000, 6000, and multiples
  of 12000 up to a maximum of 192000.
- For Intelligent-Tiering file systems, valid Metadata IOPS values are 6000 and

12000.

If the metadata performance of your workload exceeds the number of Metadata IOPS
provisioned in Automatic mode, you can use User-provisioned mode to increase the
Metadata IOPS value for your file system.

You can view the current value of the file system's metadata server configuration
as follows:

- Using the console – On the **Summary** panel of the
  file system details page, the **Metadata IOPS**
  field shows the current value of the provisioned Metadata IOPS and the
  current metadata configuration mode of the file system.
- Using the CLI or API – Use the
  [describe-file-systems](../../../cli/latest/reference/fsx/describe-file-systems.md "../../../cli/latest/reference/fsx/describe-file-systems.md") CLI command or the [DescribeFileSystems](../APIReference/API_DescribeFileSystems.md "../APIReference/API_DescribeFileSystems.md") API operation, and look for
  the `MetadataConfiguration` property.

## Considerations when increasing

metadata performance

Here are a few important considerations when increasing your metadata performance:

- **Metadata performance increase only** – You can
  only _increase_ the number of Metadata IOPS for a file system; you cannot
  decrease the number of Metadata IOPS.
- **Specifying Metadata IOPS in Automatic mode not supported** –
  You can't specify the number of Metadata IOPS on a file system that is in Automatic mode.
  You'll have to switch to User-provisioned mode and then make the request. For more information,
  see [Changing the metadata configuration mode](switch-provisioning-mode.md "switch-provisioning-mode.md").
- **Metadata IOPS for data written before scaling** – When scaling
  Metadata IOPS beyond 12000, FSx for Lustre adds new metadata servers to your file system. New metadata is automatically
  distributed across all servers for improved performance. However, existing metadata and subdirectories created before
  scaling remain on original servers, with no increase in Metadata IOPS.
- **Time between increases** – You can't make further
  metadata performance increases on a file system until 6 hours after the last increase was requested.
- **Concurrent metadata performance and SSD storage increases** – You
  cannot scale metadata performance and file system storage capacity concurrently.

## When to increase metadata performance

Increase the number of Metadata IOPS when you need to run workloads that require higher levels of metadata
performance than is provisioned by default on your file system. You can monitor your metadata performance
on the AWS Management Console by using the `Metadata IOPS Utilization` graph which provides the
percentage of provisioned metadata server performance you are consuming on your file system.

You can also monitor your metadata performance using more granular CloudWatch metrics. CloudWatch metrics include
`DiskReadOperations` and `DiskWriteOperations`, which provide the volume of metadata
server operations that require disk IO, as well as granular metrics for metadata operations
including file and directory creation, stats, reads, and deletes. For more
information, see [FSx for Lustre metadata metrics](fs-metrics.md#fs-metadata-metrics "fs-metrics.md#fs-metadata-metrics").
