# Resilience and disaster recovery in

Amazon Keyspaces

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

Amazon Keyspaces replicates data automatically three times in multiple AWS Availability Zones within the same AWS Region for durability and high availability.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon Keyspaces offers several features to help
support your data resiliency and backup needs.

**multi-Region replication**

Amazon Keyspaces provides multi-Region replication if you need to replicate your data or applications over
greater geographic distances. You can replicate your Amazon Keyspaces tables across different AWS Regions of your choice.
For more information, see [Multi-Region replication for Amazon Keyspaces (for Apache Cassandra)](multiRegion-replication.md "multiRegion-replication.md").

**Point-in-time recovery (PITR)**
PITR helps protect your Amazon Keyspaces tables from accidental write or delete operations by providing
you continuous backups of your table data. For more information, see [Point-in-time
recovery for Amazon Keyspaces](PointInTimeRecovery.md "PointInTimeRecovery.md").
