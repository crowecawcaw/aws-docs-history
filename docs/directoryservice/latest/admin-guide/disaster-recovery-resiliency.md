# Resilience in AWS Directory Service

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between Availability Zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Directory Service offers the ability to take manual
snapshots of data at any point in time to help support your data resiliency and backup
needs. For more information, see [Restoring your AWS Managed Microsoft AD with snapshots](ms_ad_snapshots.md "ms_ad_snapshots.md").
