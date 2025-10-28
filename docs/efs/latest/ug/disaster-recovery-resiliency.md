# Resilience in Amazon EFS

The AWS global infrastructure is built around AWS Regions and Availability Zones
(AZs). AWS Regions provide multiple physically separated and isolated
AZs, which are connected with low-latency, high-throughput, and highly
redundant networking. With AZs, you can design and operate applications and
databases that automatically fail over between zones without interruption. AZs
are more highly available, fault tolerant, and scalable than traditional single or multiple
data center infrastructures.

Amazon EFS file systems are resilient to one or more Availability Zone failures within an
AWS Region. Mount targets themselves are designed to be highly available. As you design
for high availability and failover to other AZs, keep in mind that while the
IP addresses and DNS for your mount targets in each AZ are static, they are
redundant components backed by multiple resources. For more information, see [How Amazon EFS works with Amazon EC2](how-it-works.md#how-it-works-ec2 "how-it-works.md#how-it-works-ec2") .

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").
