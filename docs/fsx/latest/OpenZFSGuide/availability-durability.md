# Availability and durability for Amazon FSx for OpenZFS

FSx for OpenZFS supports three file system deployment types—Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA)—that offer different levels of availability and durability.
The following sections provide information to help you choose the right deployment type for your workloads. For information on the service's availability SLA (Service Level Agreement),
see [Amazon FSx Service Level Agreement](https://aws.amazon.com/fsx/sla/ "https://aws.amazon.com/fsx/sla/"). For information on which deployment types and storage classes are supported in each AWS Region, see [Availability by AWS Region](available-aws-regions.md "available-aws-regions.md").

###### Topics

- [Choosing a deployment type based on availability and durability](#choosing-single-or-multi "#choosing-single-or-multi")
- [Failover process for FSx for OpenZFS](#multi-az-failover "#multi-az-failover")
- [Working with file system resources](#single-multi-az-resources "#single-multi-az-resources")

## Choosing a deployment type based on availability and durability

FSx for OpenZFS offers two high-availability (HA) deployment options and two non-HA deployment options. Each option provides different levels of availability and durability,
that is described in detail in the following sections. Use this information to help you decide which file system deployment type provides the level of availability and durability
that is best suited for your workload.

### Multi-AZ (HA)

Multi-AZ (HA) file systems are composed of a high-availability pair of file servers spread across two Availability Zones—a preferred Availability Zone and a standby Availability Zone.
Each of the Availability Zones also contains a set of storage volumes. Relative to Single-AZ (non-HA and HA) file systems, Multi-AZ (HA) file systems provide enhanced durability by replicating data
synchronously both within each individual Availability Zone and between the two Availability Zones. Multi-AZ (HA) file systems also offer enhanced availability by automatically failing over to the
standby Availability Zone during planned system maintenance, and in cases of unplanned service disruption, typically within 60 seconds. This allows you to continue accessing your data, and helps to protect your
data against instance failure and Availability Zone disruption.

Multi-AZ (HA) file systems are recommended for business critical production workloads and database workloads that require storage that is highly available and durable across Availability Zones in the same AWS Region.

### Single-AZ (HA)

Single-AZ (HA) file systems are composed of two file servers connected to a single set of storage volumes within a single Availability Zone. During planned maintenance events or unplanned service disruptions, Single-AZ (HA)
file systems fail over from the primary file server to the standby file server, typically within 60 seconds. Amazon FSx continuously monitors the file servers for any hardware failure
and automatically replaces a server in the event of failure while serving data from the standby file server. Once the primary server is restored, the Single-AZ (HA) file systems fail back to the primary server.

Single-AZ (HA) file systems are recommended as a cost-effective solution for workloads that need high availability, but don't need storage redundancy across Availability Zones, including analytics, and EDA workloads.

### Single-AZ (non-HA)

Single-AZ (non-HA) are composed of a single file server instance and a set of storage volumes within one Availability Zone. Amazon FSx continuously
monitors for hardware failures, and automatically recovers from failure events by replacing the
failed infrastructure component. Single-AZ (non-HA) file systems usually experience about 30 minutes of downtime during failure recovery events, and during the planned
maintenance window that you configure for your file system. Single-AZ (non-HA) file systems are designed as a cost-efficient solution for workloads that can tolerate temporary loss of availability in the event of planned file
system maintenance, unplanned service disruption or, in rare cases, the loss of data updates since the most recent backup.

###### Note

For all Single-AZ file systems, file system failure may be unrecoverable in rare cases, such as storage component failures. In these cases, you can recover your file system from the most recent backup.

In addition to differences in availability and durability, different deployment types also offer varying levels of performance that may impact your decision.
Note that both Single-AZ (non-HA and HA) deployment types, FSx for OpenZFS also support Single-AZ 1 and Single-AZ 2. Single-AZ 2 offers higher levels of performance than the maximum offered by Single-AZ 1. For more information on performance differences between deployment types, see
[Performance for Amazon FSx for OpenZFS](performance.md "performance.md").

You can also migrate between deployment types by restoring from a backup, using **rsync**, or using on-demand replication. For more information, see [Migrating between deployment types and storage classes](performance.md#migrating-between-deployments "performance.md#migrating-between-deployments").

## Failover process for FSx for OpenZFS

Multi-AZ (HA) and Single-AZ (HA) file systems automatically fail over from the preferred file server to the standby
file server under the following conditions:

- The preferred file server becomes unavailable.
- The file system's throughput capacity is changed.
- The preferred file server undergoes planned maintenance.

Multi-AZ (HA) file systems will also fail over if an Availability Zone disruption occurs.

When failing over from one file server to another, the new active file server automatically
begins serving all file system read and write requests. A failover typically takes less than 60
seconds from the detection of the failure on the active file server to the promotion of the
standby file server to active status. Upon completion of the failover, you continue to have
access to your data without manual intervention. When the preferred file server is fully recovered and becomes available, Amazon FSx automatically fails back to
it, usually in less than 60 seconds.

### Testing failover on Multi-AZ (HA) and Single-AZ (HA) file systems

You can test failover on your Multi-AZ (HA) or Single-AZ (HA) file system by modifying its throughput capacity. When
you modify your file system's throughput capacity, Amazon FSx switches out the file system's file
servers sequentially. File systems automatically fail over to the secondary server while Amazon FSx
replaces the preferred file server first. After the update, the file system automatically fails
back to the new primary server and Amazon FSx replaces the secondary file server.

You can monitor the progress of the throughput capacity update request in the Amazon FSx
console, the CLI, and the API. For more information about modifying your file system's
throughput capacity and monitoring the progress of the request, see [Modifying throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md").

## Working with file system resources

Each Amazon FSx for OpenZFS file system has a number of resources, including subnets, elastic network interfaces, IP addresses, and backups, that allow Amazon FSx to offer greater availability and durability.
The sections below provide information on how these resources work, as well as recommendations for how to configure and manage them.

### Subnets

When you create a VPC, it spans all the Availability Zones in the region. Availability Zones are distinct
locations that are engineered to be isolated from failures in other
availbility zones. After creating a VPC, you can add one or more subnets in each Availability Zone.
The default VPC has a subnet in each Availability Zone. Each subnet must reside entirely
within one Availability Zone and cannot span zones. When you create a Single-AZ Amazon FSx file
system, you specify a single subnet for the file system. The subnet you choose defines the
Availability Zone in which the file system is created.

When you create a Multi-AZ (HA) file system, you specify two subnets, one for the preferred file
server, and one for the standby file server. The two subnets you choose must be in different
Availability Zones within the same AWS Region. For more information about Amazon VPC, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC user guide_.

For in-AWS applications, we recommend that you launch your clients in the same Availability Zone
as your preferred file server to minimize latency.

### File system elastic network interfaces

For Multi-AZ (HA) file systems, Amazon FSx provisions two ENIs—one in each of the subnets that you associate with your file system.
Clients communicate with your Amazon FSx file system using the elastic network interface that's attached to the file server that serves the data. Network interfaces are considered to be within the service scope of Amazon FSx, despite being part of your account's VPC.
For Single-AZ (HA) file systems, Amazon FSx provisions two ENIs in the subnet that you associate with your file system. For Single-AZ (non-HA) file systems, Amazon FSx provisions one [elastic network interface](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") (ENI) in the subnet that you associate with your file system.

###### Warning

You must not modify or delete the elastic network interfaces associated with your file system.
Modifying or deleting the network interface can cause a permanent loss of connection between
your VPC and your file system.

The following table summarizes the subnet, elastic network interface, and IP address resources for FSx for OpenZFS file system deployment types:

| File system deployment type | Number of subnets | Number of elastic network interfaces | Number of IP addresses |
| --------------------------- | ----------------- | ------------------------------------ | ---------------------- |
| Multi-AZ (HA)               | 2                 | 2                                    | 3                      |
| Single-AZ (HA)              | 1                 | 2                                    | 3                      |
| Single-AZ (non-HA)          | 1                 | 1                                    | 1                      |

Once a file system is created, its IP addresses don't change until the file system is deleted. For Multi-AZ (HA) and Single-AZ (HA) file systems, the number of IP addresses includes a floating IP address, which allows connected clients to transition between the preferred and standby file servers
during a failover event. For more information, see [Accessing your data](accessing-your-data.md "accessing-your-data.md").

###### Important

Amazon FSx doesn't support accessing file systems from, or exposing file systems to the public Internet.
If an Elastic IP address, which is a public IP address reachable from the Internet, is attached to a
file system's elastic network interface, Amazon FSx automatically detaches it.

#### Backups

FSx for OpenZFS offers a native backups feature that's designed to support archival, data
retention, and compliance needs. A backup is a secondary, offline copy of your file system.
Amazon FSx backups are crash-consistent and incremental, which means that only the changes from your
most recent backup are saved. This saves on backup storage costs by not duplicating data. By
default, Amazon FSx takes an automatic daily backup of your file system during a backup window that
you specify. You can create additional backups at any time using the AWS Management Console, AWS Command Line Interface, or
Amazon FSx API. For more information, see [Protecting your data with backups](using-backups.md "using-backups.md").
