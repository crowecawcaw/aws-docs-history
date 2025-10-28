# Resilience in Amazon FSx for NetApp ONTAP

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon FSx offers several features to help support your data resiliency and backup needs.

## Backup and restore

Amazon FSx creates and saves automated backups of the volumes in your Amazon FSx for NetApp ONTAP file system.
Amazon FSx creates automated backups of your volumes during the backup window of your Amazon FSx for NetApp ONTAP file system.
Amazon FSx saves the automated backups of your volumes according to the backup retention period that you specify.
You can also back up your volumes manually, by creating a user-initiated backup. You restore a volume backup
at any time by creating a new volume with the backup specified as the source.

For more information, see [Protecting your data with volume backups](using-backups.md "using-backups.md").

## Snapshots

Amazon FSx creates snapshot copies of the Amazon FSx for NetApp ONTAP volumes. Snapshot copies
offer protection against accidental deletion or modification of files in your volumes by end users. For more
information, see [Protecting your data with snapshots](snapshots-ontap.md "snapshots-ontap.md").

## Availability Zones

Amazon FSx for NetApp ONTAP file systems are designed to provide continuous availability to
data even in the event that a server failure. Each file system is powered by two file
servers in at least one Availability Zone, each with its own storage. Amazon FSx
automatically replicates your data to protect it from component failure, continuously
monitors for hardware failures, and automatically replaces infrastructure components in
the event of a failure. File systems automatically fail over and back as needed
(typically within 60 seconds), and clients automatically fail over and back with the
file system.

### Multi-AZ file systems

Amazon FSx for NetApp ONTAP file systems are highly available and durable across AWS
Availability Zones, and are designed to provide continuous availability to data even
in the event that an Availability Zone is unavailable.

For more information, see [Availability, durability, and deployment options](high-availability-AZ.md "high-availability-AZ.md").

### Single-AZ file systems

Amazon FSx for NetApp ONTAP file systems are highly available and durable within a single AWS
Availability Zone, and are designed to provide continuous availability within that
Availability Zone in the event of an individual file server or disk failure.

For more information, see [Availability, durability, and deployment options](high-availability-AZ.md "high-availability-AZ.md").
