# Best practices for FSx for Windows File Server

We recommend that you follow these best practices when working with Amazon FSx for Windows File Server.

###### Topics

- [General best practices](#general-best-practices "#general-best-practices")
- [Security best practices](#security-best-practices "#security-best-practices")
- [Active Directory](#ad-best-practices "#ad-best-practices")
- [Configuring and right-sizing your file system](#configuring-and-right-sizing "#configuring-and-right-sizing")

## General best practices

### Creating a monitoring plan

You can use file system metrics to [monitor](monitoring_overview.md "monitoring_overview.md") your storage and performance usage,
understand your usage patterns, and trigger notifications when your usage approaches
your file system’s storage or performance limits. Monitoring your Amazon FSx file systems
along with the rest of your application environment enables you to quickly debug any
issues that may impact performance.

### Ensuring that your file systems have sufficient resources

Having insufficient resources can result in increased latency and queuing for I/O
requests, which might appear as complete or partial unavailability of your file
system. For more information about monitoring performance and accessing performance
warnings and recommendations, see [Performance warnings and recommendations](monitoring-cloudwatch.md#performance-insights-FSxW "monitoring-cloudwatch.md#performance-insights-FSxW").

## Security best practices

We recommend that you follow these best practices for administering your file system’s
security and access controls. For more detailed information on configuring Amazon FSx to meet
your security and compliance objectives, see [Security in Amazon FSx](security.md "security.md").

### Network security

#### Don't modify or delete the ENI that's associated with your file

system

Your Amazon FSx file system is accessed through an elastic network interface (ENI) that resides in the virtual private cloud
(VPC) that's associated with your file system. Modifying or deleting the network
interface can cause a permanent loss of connection between your VPC and your
file system.

#### Using security groups and network ACLs

You can use security groups and network access control lists (ACLs) to limit
access to your file systems. For [VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups"), the default security group
is already added to your file system in the console. Make sure that the security
group and the network ACLs for the subnets where you create your file system
allow traffic on the ports.

## Active Directory

When you create an Amazon FSx file system, you can join it to your [Microsoft Active Directory domain](aws-ad-integration-fsxW.md "aws-ad-integration-fsxW.md")
to provide user authentication, and share-, file-, and folder-level access control
authorization. Your users can use their existing Active Directory accounts to connect to file
shares and access files and folders within them. In addition, you can migrate the
existing security ACL configuration to Amazon FSx without any modifications. Amazon FSx
provides you with two options for Active Directory: **AWS
managed Microsoft Active Directory** or **self-managed Microsoft Active Directory**.

If you’re using an **AWS managed Microsoft Active Directory**, we
recommend leaving the default settings of your Active Directory security group. If you do modify
these settings, ensure that you maintain a network configuration that satisfies the network requirements.
For more information, see [Networking prerequisites](fsx-aws-managed-ad.md#rfim-networking-requirements "fsx-aws-managed-ad.md#rfim-networking-requirements").

If you’re using a **self-managed Microsoft Active Directory**, you
have additional options for configuring your file system. We recommend the following
best practices for initial configuration when using Amazon FSx with your self-managed
Microsoft Active Directory:

- **Assign subnets to a single Active Directory site**: If
  your Active Directory environment has a large number of domain controllers, use **Active Directory Sites and Services** to assign the
  subnets used by your Amazon FSx file systems to a single Active Directory site with the highest
  availability and reliability. Make sure that the VPC security group, VPC
  network ACL, Windows firewall rules on your DCs, and any other network
  routing controls you have in your Active Directory infrastructure allow communication from
  Amazon FSx on the required ports. This allows Windows to revert to other DCs if it can't use the assigned Active Directory site.
  For more information, see [File system access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").
- **Use a separate Organizational Unit (OU)**:
  Use an OU for your Amazon FSx file systems that’s separate from any other
  organizational units that you might have.
- **Configure your service account with minimum
  privileges required**: Configure or delegate the service
  account that you provide to Amazon FSx with the minimum privileges required. For
  more information, see [Using a self-managed Microsoft Active Directory](self-managed-AD.md "self-managed-AD.md").
- **Continuously verify your Active Directory
  configuration**: Run the [Amazon FSx Active Directory validation
  tool](validate-ad-config.md "validate-ad-config.md") against your Active Directory configuration prior to
  creating your Amazon FSx file system to verify that your configuration is valid
  for use with Amazon FSx, and to discover any warnings and errors that the tool might
  expose.

### Avoid losing availability due to Active Directory misconfiguration

When using Amazon FSx with your self-managed Microsoft Active Directory, it's important to have a
valid Active Directory configuration not only during the creation of your file system, but
also for ongoing operations and availability. During failure recovery events,
routine maintenance events, and throughput capacity update actions, Amazon FSx
rejoins file server resources to your Active Directory. If the Active Directory configuration
is not valid during an event, your file system changes to a status of **Misconfigured**, and is at risk of becoming
unavailable. Here are some ways that you can avoid losing availability:

- **Keep your Active Directory configuration updated with
  Amazon FSx**: If you make changes, such as resetting the
  password of your service account, make sure you update the configuration
  for any file systems using this service account.
- **Monitor for Active Directory misconfiguration**: Set Misconfigured status notifications
  for yourself so that you can reset your file system’s Active Directory configuration, if necessary.
  For an example that uses a Lambda-based solution to achieve this, see
  [Monitoring the health of Amazon FSx file systems using Amazon EventBridge and AWS Lambda](https://aws.amazon.com/blogs/storage/monitoring-the-health-of-amazon-fsx-file-systems-using-amazon-eventbridge-and-aws-lambda/ "https://aws.amazon.com/blogs/storage/monitoring-the-health-of-amazon-fsx-file-systems-using-amazon-eventbridge-and-aws-lambda/").
- **Validate your Active Directory configuration
  regularly**: If you want to proactively detect an Active Directory
  misconfiguration, we recommend that you run the [Active Directory Validation tool](validate-ad-config.md "validate-ad-config.md") against your Active Directory
  configuration on an ongoing basis. If you receive warnings or errors
  when running the validation tool, it means that your file system is at
  risk of becoming misconfigured.
- **Don't move or modify computer objects created by
  FSx**: Amazon FSx creates and manages computer objects in your Active Directory, using the service account and permissions that you provide. Moving
  or modifying these computer objects can result in your file system
  becoming misconfigured.

### Windows ACLs

With Amazon FSx, you use standard Windows access control lists (ACLs) for
fine-grained share-, file-, and folder-level access control. Amazon FSx file systems
automatically verify the credentials of users who access file system data to
enforce these Windows ACLs.

- **Don’t change the NTFS ACL permissions for the
  SYSTEM user**: Amazon FSx requires that the SYSTEM user have
  full control NTFS ACL permissions on all folders within your file
  system. Changing the NTFS ACL permissions for the SYSTEM user may result
  in your file system becoming inaccessible and future file system backups
  may become unusable.

## Configuring and right-sizing your file system

### Selecting a deployment type

Amazon FSx provides two deployment options: Single-AZ and Multi-AZ. We recommend using
**Multi-AZ file systems** for most production
workloads that require high availability to shared Windows file data. For more
information, see [Availability and durability: Single-AZ and Multi-AZ file systems](high-availability-multiAZ.md "high-availability-multiAZ.md").

### Selecting a throughput capacity

Configure your file system with sufficient throughput capacity to meet not only the expected traffic of your
workload, but also additional performance resources required to support the features
you want to enable on your file system. For example, if you’re running data
deduplication, the throughput capacity that you select must provide enough memory to
run deduplication based on the storage that you have. If you’re using shadow copies,
increase throughput capacity to a value that's at least three times the value that's
expected to be driven by your workload to avoid Windows Server deleting your shadow
copies. For more information, see [Impact of throughput capacity on performance](performance.md#impact-throughput-cap-performance "performance.md#impact-throughput-cap-performance").

### Increasing storage capacity and

throughput capacity

Increase the storage capacity of your file system when it’s running low on free
storage, or when you expect your storage requirements to grow larger than the
current storage limit. We recommend maintaining at least 20% of free storage capacity at all times on
your file system. We also recommend increasing throughput capacity by at least 20% before
increasing storage capacity to offset any performance impact during a storage increase.
You can use the _FreeStorageCapacity_ CloudWatch metric to monitor the amount of free
storage available and understand how it trends. For more information, see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity").

You should also increase the throughput capacity of your file system if your
workload is constrained by the current performance limits. You can use the
**Monitoring and performance** page on the FSx console to see
when workload demands have approached or exceeded performance limits to determine
whether your file system is under-provisioned for your workload.

To minimize the duration of storage scaling and avoid reduction in write
performance, we recommend increasing your file system's throughput capacity before
increasing storage capacity and then scaling back
throughput capacity after the storage capacity increase is complete. Most workloads
experience minimal performance impact during storage scaling. However, file systems with
HDD storage type and workloads involving large numbers of end users, high levels of I/O, or
datasets with large numbers of small files could temporarily experience a reduction in performance.
For more information, see [Storage capacity increases
and file system performance](managing-storage-configuration.md#storage-capacity-increase-and-performance "managing-storage-configuration.md#storage-capacity-increase-and-performance").

### Modifying throughput capacity during idle periods

Updating throughput capacity interrupts availability for a few minutes for
Single-AZ file systems and causes failover and failback for Multi-AZ file systems.
For Multi-AZ file systems, if there is ongoing traffic during failover and failback,
any data changes made during this time will need to be synchronized between the file servers.
The data synchronization process can take up to multiple hours for write-heavy and IOPS-heavy workloads.
Although your file system will continue to be available during this time, we recommend scheduling maintenance windows and performing
throughput capacity updates during idle periods when there is minimal load on your
file system to reduce the duration of data synchronization. To learn more, see
[Managing throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").
