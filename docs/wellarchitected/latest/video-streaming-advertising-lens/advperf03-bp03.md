# ADVPERF03-BP03 Use a cloud file system to store shared data between applications

File storage services (such as Amazon EFS) provide a simple way to
set up and scale file systems and are widely used for big data and
analytics workloads, media processing workflows, and content
management scenarios. They are well-suited for distributed
workloads and applications that need to share files across
multiple EC2 instances.

## Implementation guidance

[Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/")
is a scalable and fully managed cloud file system that provides
a simple, serverless way to share file data across AWS Cloud
services and on-premises resources. In the advertising industry,
Amazon EFS can be used to store and share log files,
configuration files, and other data that needs to be accessed
concurrently by multiple applications or instances. This is
particularly useful for log processing and analysis pipelines,
where data needs to be shared across multiple stages.

- **[Performance
  modes](../../../efs/latest/ug/performance.md#performancemodes "../../../efs/latest/ug/performance.md#performancemodes"):** Amazon EFS offers both General
  Purpose and Max I/O performance modes.
- **[Throughput
  modes](../../../efs/latest/ug/performance.md#throughput-modes "../../../efs/latest/ug/performance.md#throughput-modes"):** Choosing the correct throughput mode for your file system
  depends on your workload's performance requirements.
- **Cost optimization:** Use Amazon EFS lifecycle policies to
  automatically move infrequently accessed files to the [EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/ "https://aws.amazon.com/efs/features/infrequent-access/") storage class,
  reducing stor
- **Mount targets:** Create Amazon EFS mount targets in all
  availability zones to provide high availability and low latency access to your file
  system.
- age costs.

## Resources

- [Encrypting
  data in Amazon EFS](../../../efs/latest/ug/encryption.md "../../../efs/latest/ug/encryption.md")
- [Create an Amazon EFS
  file system and mount it on an Amazon EC2 instance using the AWS CLI](../../../efs/latest/ug/wt1-getting-started.md "../../../efs/latest/ug/wt1-getting-started.md")
- [Mounting
  considerations for Linux](../../../efs/latest/ug/mounting-fs-mount-cmd-general.md "../../../efs/latest/ug/mounting-fs-mount-cmd-general.md")
- [Managing
  automatic backups of Amazon EFS file systems](../../../efs/latest/ug/automatic-backups.md "../../../efs/latest/ug/automatic-backups.md")
