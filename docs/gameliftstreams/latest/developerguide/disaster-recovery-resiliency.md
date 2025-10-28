# Resilience in Amazon GameLift Streams

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the data redundancy provided by the AWS global infrastructure, Amazon GameLift Streams is built with a resilient multi-Availability Zone
infrastructure. In the case of an Availability Zone outage, individual existing sessions might be affected, but the service will continue to
load-balance new sessions across healthy Availability Zones.
