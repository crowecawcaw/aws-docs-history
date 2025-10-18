# Resilience in AWS CloudShell

The AWS global infrastructure is built around AWS Regions and Availability Zones.
 AWS Regions provide multiple physically separated and isolated Availability Zones, which
 are connected with low-latency, high-throughput, and highly redundant networking. With
 Availability Zones, you can design and operate applications and databases that automatically
 fail over between zones without interruption. Availability Zones are more highly available,
 fault tolerant, and scalable than traditional single or multiple data center
 infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global
 Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, AWS CloudShell supports
 the
 following
 feature to
 support your data resiliency and backup
 needs:


* Use AWS CLI calls to specify files in your home directory in AWS CloudShell and add them
 as objects in Amazon S3 buckets. For an example, see the
 [Getting started with
 AWS CloudShell](getting-started.md "getting-started.md").
