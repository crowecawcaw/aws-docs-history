# Resilience and disaster recovery in

Amazon DynamoDB

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between Availability Zones without interruption. Availability Zones are more
highly available, fault tolerant, and scalable than traditional single or multiple data
center infrastructures.

If you need to replicate your data or applications over greater geographic distances, use
AWS Local Regions. An AWS Local Region is a single data center designed to complement an
existing AWS Region. Like all AWS Regions, AWS Local Regions are completely isolated
from other AWS Regions.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon DynamoDB offers several features to help
support your data resiliency and backup needs.

**On-demand backup and restore**

DynamoDB provides on-demand backup capability. It allows you to create full
backups of your tables for long-term retention and archival. For more
information, see [On-Demand
backup and restore for DynamoDB](Backup-and-Restore.md "Backup-and-Restore.md").

**Point-in-time recovery**

Point-in-time recovery helps protect your DynamoDB tables from accidental write
or delete operations. With point in time recovery, you don't have to worry about
creating, maintaining, or scheduling on-demand backups. For more information,
see [Point-in-time recovery for DynamoDB](Point-in-time-recovery.md "Point-in-time-recovery.md").

**Global tables that sync across AWS
regions**

DynamoDB automatically spreads the data and traffic for your tables over a
sufficient number of servers to handle your throughput and storage requirements,
while maintaining consistent and fast performance. All of your data is stored on
solid-state disks (SSDs) and is automatically replicated across multiple
Availability Zones in an AWS Region, providing built-in high availability and
data durability. You can use global tables to keep DynamoDB tables in sync
across AWS Regions.
