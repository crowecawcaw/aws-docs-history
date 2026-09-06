

# Resilience in AWS Backup
<a name="disaster-recovery-resiliency"></a>

 AWS Backup takes its resilience — and your data security — extremely seriously. 

 AWS Backup stores your backups with *at least* as much resilience and durability as your resource’s original AWS service would give you, if you backed it up there. 

AWS Backup is designed to use the AWS global infrastructure to resiliently and redundantly store your backups across multiple Availability Zones for durability of 99.999999999% (11 nines) in any given year, provided that you adhere to the current AWS Backup documentation.

AWS Backup encrypts your backup plans at rest and continuously backs them up. You can also restrict access to your backup plans using AWS Identity and Access Management (IAM) credentials and policies. For more information, see [Authentication](https://docs.aws.amazon.com/aws-backup/latest/devguide/authentication.html), [Access Control](https://docs.aws.amazon.com/aws-backup/latest/devguide/access-control.html), and [ Security Best Practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html).

The AWS global infrastructure is built around AWS Regions and Availability Zones. AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking. AWS Backup stores your backups across Availability Zones. Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures. For more information, see [AWS Backup Service Level Agreement (SLA)](https://aws.amazon.com/backup/sla/).

Furthermore, AWS Backup empowers you to copy your backups across Regions for even greater resilience. For more information about the AWS Backup cross-Region copy feature, see [Creating a Backup Copy](https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-a-copy.html). 

For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).