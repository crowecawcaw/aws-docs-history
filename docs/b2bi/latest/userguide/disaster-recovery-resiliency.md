# Resilience in AWS B2B Data Interchange

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

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

AWS B2B Data Interchange supports up to 3 Availability Zones and is backed by an auto scaling, redundant
fleet for your connection and transfer requests.

Note the following:

- Availability Zone-level redundancy is built into the service
- There are redundant fleets for each AZ.
- This redundancy is provided automatically
  For more information about AWS Regions and Availability Zones, see [AWS global
  infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
