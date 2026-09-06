

# Cloud-native data protection with AWS Backup
<a name="data-protection-cloud-native"></a>

This reference architecture describes how [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is implemented in a single AWS account to protect multiple services in an automated way.

![Architecture diagram showing cloud-native data protection with AWS Backup.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-protection-aws-backup/images/data-protection-aws-backup-1.png)


1. Use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to create the components that AWS Backup uses in this architecture.

1. The AWS Backup plan defines the frequency, retention period, lifecycle, backup copy destination, and resources to protect.

1. The AWS Backup vault is a logical container that stores and organizes your backups. A defined [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key enforces encryption.

1. A backup job runs within the backup window defined in the backup plan. After the job completes, a recovery point appears in the vault for restore.

1. Secure access to your resources through [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) by using AWS-managed policies as a starting point. At the vault level, access policies protect the vault and its contents.

1. AWS Backup actions record in [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) as events.

1. Monitor AWS Backup service metrics through [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

1. Use [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to monitor AWS Backup events, such as when a backup fails or gets deleted.

1. Audit backups and automate reports through AWS Backup Audit Manager. With this service, you can continuously monitor compliance of your backups.

## Further reading
<a name="cloud-native-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Backup product page](https://aws.amazon.com/backup/)

## Diagram history
<a name="cloud-native-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#cloud-native-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-cross-account.md#cross-account-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-landing-zone.md#landing-zone-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-vault-lock.md#diagram-history) | Reference architecture diagrams first published. | July 29, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.