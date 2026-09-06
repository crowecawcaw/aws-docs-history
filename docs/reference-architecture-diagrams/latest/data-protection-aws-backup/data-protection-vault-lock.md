

# Creating immutable backups with AWS Backup Vault Lock
<a name="data-protection-vault-lock"></a>

This architecture details the key steps involved in setting up a central immutable backup data bunker that follows the principle of least privilege in a multi-account AWS Organization.

![Architecture diagram showing how to create immutable backups with AWS Backup Vault Lock.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-protection-aws-backup/images/data-protection-aws-backup-4.png)


1. Create a resource policy that limits CopyFromBackupVault to the Backup Data Bunker Account. Apply it to the AWS Backup vaults in each member account. Create a customer-managed KMS key for each vault.

1. Set up a Backup Data Bunker account, create an AWS Backup Vault, and apply Vault Lock. Create a resource policy that limits CopyIntoBackupVault actions from specific OUs or accounts.

1. Create a customer-managed KMS key in a separate Key Vault account and share it with the Central Vault Account. Implement additional security controls, including MFA on critical KMS API calls.

1. Create a Service Control Policy that restricts access to appropriate IAM roles for backup operations into the Backup Data Bunker account.

1. Create an AWS Backup policy with a copy operation into the Backup Data Bunker account. Apply it to the member accounts.

1. Restrict access to the Backup Data Bunker account to specific users through AWS SSO and MFA, following a Break Glass workflow.

1. The authenticated user receives AWS STS temporary credentials through federation. These credentials provide specific access to the Backup Data Bunker.

1. Create audit reporting by using AWS Backup Audit Manager (BAM).

1. Create an organizational CloudTrail for recording and monitoring policy changes and Central Backup Vault access patterns.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Backup product page](https://aws.amazon.com/backup/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](data-protection-cloud-native.md#cloud-native-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-cross-account.md#cross-account-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-landing-zone.md#landing-zone-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](#diagram-history) | Reference architecture diagrams first published. | July 29, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.