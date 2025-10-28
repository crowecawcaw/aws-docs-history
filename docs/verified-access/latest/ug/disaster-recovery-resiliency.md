# Resilience in Verified Access

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center
infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Verified Access offers the following feature to help
support your high availability needs.

## Multiple subnets for high availability

When you create a load balancer type Verified Access endpoint, you can associate multiple
subnets to the endpoint. Each subnet that you associate with the endpoint must belong to
a different Availability Zone. By associating multiple subnets you can ensure high
availability by using multiple Availability Zones.
