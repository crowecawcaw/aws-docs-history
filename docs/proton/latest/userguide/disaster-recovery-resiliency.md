End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Resilience in AWS Proton

The AWS global infrastructure is built around AWS Region and Availability Zones. AWS Regions provide multiple physically separated
and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. With Availability
Zones, you can design and operate applications and databases that automatically fail over between zones without interruption. Availability
Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS
Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, AWS Proton offers features to help support your data resiliency and backup needs.

## AWS Proton backups

AWS Proton maintains a backup of all customer data. In the case of a total outage, this backup can be used to restore AWS Proton and customer data
from a previous valid state.
