# Security

###### Topics

- [Network isolation](#aurora-features-network-isolation "#aurora-features-network-isolation")
- [Resource-level permissions](#aurora-features-resource-permissions "#aurora-features-resource-permissions")
- [Encryption](#aurora-features-encryption "#aurora-features-encryption")
- [Advanced auditing](#aurora-features-auditing "#aurora-features-auditing")
- [Threat detection](#aurora-features-threat-detection "#aurora-features-threat-detection")

## Network isolation

Aurora runs in [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"), isolating your database in your own virtual network. You can connect to your
on-premises IT infrastructure using industry-standard encrypted IPsec VPNs and configure firewall settings to
control network access to your DB instances.

## Resource-level permissions

Aurora integrates with [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") to give you fine-grained access control over the actions that your IAM
users and groups can take on specific Aurora resources (for example, DB instances, DB snapshots, DB parameter
groups, DB event subscriptions, DB option groups). You can tag your Aurora resources and control actions taken
on groups of resources that have the same tag and tag value. Additional information is available in [IAM
database authentication](../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.md "../../../AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.md") documentation.

## Encryption

Aurora encrypts your data at rest using keys you create and control through [AWS KMS](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). When encryption is
enabled, data stored at rest in the underlying storage is encrypted, as are the automated backups, snapshots,
and replicas in the same cluster. Aurora uses SSL (AES-256) to secure data in transit.

## Advanced auditing

Aurora logs database events with minimal impact on database performance. You can analyze logs for database
management, security, governance, regulatory compliance, and other purposes. You can also monitor activity by
sending audit logs to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/").

## Threat detection

[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") offers threat detection for Aurora to help you identify potential threats to data stored in
Aurora databases. GuardDuty RDS Protection profiles and monitors login activity to existing and new databases
in your account and uses tailored ML models to accurately detect suspicious logins to Aurora databases. If a
potential threat is detected, GuardDuty generates a security finding that includes database details and rich
contextual information on suspicious activity. Aurora integration with GuardDuty provides direct access to
database event logs without requiring you to modify your databases and has no impact on database
performance.
