# Resilience in Deadline Cloud

The AWS global infrastructure is built around AWS Regions and Availability Zones.
 AWS Regions provide multiple physically separated and isolated Availability Zones, which
 are connected with low-latency, high-throughput, and highly redundant networking. With
 Availability Zones, you can design and operate applications and databases that automatically
 fail over between zones without interruption. Availability Zones are more highly available,
 fault tolerant, and scalable than traditional single or multiple data center
 infrastructures. 

For more information about AWS Regions and Availability Zones, see [AWS Global
 Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

AWS Deadline Cloud does not back up data stored in your job attachments S3 bucket. You can
 enable backups of your job attachments data using any standard Amazon S3 backup mechanism, such
 as [S3
 Versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") or [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html "https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html").
