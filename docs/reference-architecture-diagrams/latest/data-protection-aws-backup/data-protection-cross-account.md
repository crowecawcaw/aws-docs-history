

# Cross-account and Region data protection with AWS Backup and AWS Organizations
<a name="data-protection-cross-account"></a>

This reference architecture shows how to implement a consistent backup strategy through multiple AWS accounts and Regions, and copy backups between them through an automated, policy-driven approach.

![Architecture diagram showing cross-account and Region data protection with AWS Backup and AWS Organizations.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-protection-aws-backup/images/data-protection-aws-backup-2.png)


1. Use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) StackSets to create [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) resources such as an [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) role, backup vault, [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) key, and access policies.

1. Create a backup policy. Define the frequency, retention, lifecycle, backup copy settings, and resource assignment tag values. Then attach the policy to a target.

1. StackSets and backup policies support both organizational units (OUs) or specific AWS accounts as targets.

1. Use Service Control Policies (SCPs) to protect your AWS Backup resources from unwanted modification, deletion, or use.

1. After configuration and attachment to a target, AWS Backup creates a backup plan in all member accounts that belong to the OU.

1. Based on the plan schedule, backup jobs run and recovery points appear in the backup vault.

1. For cross-account backup copies, use a customer-managed AWS KMS key on the originating resource and source backup vault. Then provide the necessary permissions to the key and target vault.

1. Cross-Region backups can occur within the same account or to a different account in a single step. The backup policy defines the vault name and destination account.

1. Forward backup events through an [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rule to a central custom event bus for centralized monitoring. Then trigger email notifications by using [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

1. Monitor cross-account and Region activities through the AWS Backup console in the AWS Organizations management account.

## Further reading
<a name="cross-account-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Backup product page](https://aws.amazon.com/backup/)

## Diagram history
<a name="cross-account-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](data-protection-cloud-native.md#cloud-native-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](#cross-account-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-landing-zone.md#landing-zone-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-vault-lock.md#diagram-history) | Reference architecture diagrams first published. | July 29, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.