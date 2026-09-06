

# Resilience in AWS Resource Groups
<a name="disaster-recovery-resiliency"></a>

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

In addition to the AWS global infrastructure, AWS Resource Groups offers several features to help support your data resiliency and backup needs.

AWS Resource Groups performs automated backups to internal service resources. These backups are not user-configurable. Backups are encrypted, both at rest and in transit. Resource Groups stores customer data in Amazon DynamoDB.

Even a complete loss of user resource groups would not result in a loss of customer data, because most customer data is replicated across AWS Availability Zones (AZs). If you delete groups accidentally, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/).