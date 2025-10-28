# Resilience in Amazon Detective

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated
Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and
operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly
available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Detective makes use of the resiliency built
into Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3). For more information, see [resiliency and disaster recovery in Amazon DynamoDB](../../../amazondynamodb/latest/developerguide/disaster-recovery-resiliency.md "../../../amazondynamodb/latest/developerguide/disaster-recovery-resiliency.md") and [Resilience in Amazon Simple Storage Service](../../../AmazonS3/latest/userguide/disaster-recovery-resiliency.md "../../../AmazonS3/latest/userguide/disaster-recovery-resiliency.md").

The Detective architecture is also resilient to the failure of a single Availability Zone.
This resilience is built into Detective, and does not require any configuration.
