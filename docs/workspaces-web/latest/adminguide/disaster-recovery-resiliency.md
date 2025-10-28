# Resilience in Amazon WorkSpaces Secure Browser

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center
infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

The following are currently not supported by WorkSpaces Secure Browser:

- Backing up content across AZs or regions
- Encrypted backups
- Encrypting in-transit content between AZs or regions
- Default or automatic backups
  To configure for high internet availability, you can tune your VPC configuration. For
  high API availability, you can request the right amount of TPS.
