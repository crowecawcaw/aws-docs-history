

# AWS Landing Zone and AWS Backup reference architecture
<a name="data-protection-landing-zone"></a>

This reference architecture aligns to the design tenants of a well-architected, secure, and scalable multi-account AWS implementation with the integration of AWS Backup for data protection. You can use or a similar landing zone framework to standardize your data protection strategy.

![Architecture diagram showing AWS Landing Zone and AWS Backup reference architecture.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-protection-aws-backup/images/data-protection-aws-backup-3.png)


1. Use and deploy the Customizations for Control Tower (CfCT) resource template to integrate AWS Backup in your environment.

1. Enable Service Control Policies (SCPs) to set preventive guardrails and backup policies in AWS Organizations.

1. Enable AWS CloudFormation StackSets for your Organization to centrally deploy resources across multiple accounts.

1. Enable AWS Backup in your AWS Organizations environment. Enable cross-account monitoring and cross-account backup management.

1. Centrally manage SSO access to your environment by using . This service integrates with existing corporate identities through federation.

1. Use services such as [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) to maintain audit trails in a centralized manner.

1. Centralize AWS Backup CloudTrail events and AWS Config logs in an S3 bucket owned by the Log Archive account.

1. Securely manage shared resources, such as AWS KMS, to centralize and decouple key ownership by using IAM cross-account roles.

1. Backup policies managed in the management account create backup plans in the target accounts and OUs.

1. Use AWS Backup Audit Manager to monitor backup compliance in each account.

1. Centralize backup copies and AWS Backup Audit Manager reports across your organization in a central backup account.

1. Provide self-service capabilities to end users. They can create or update their backup configuration from a predefined catalog by using AWS Service Catalog.

## Further reading
<a name="landing-zone-further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Backup product page](https://aws.amazon.com/backup/)

## Diagram history
<a name="landing-zone-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](data-protection-cloud-native.md#cloud-native-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-cross-account.md#cross-account-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](#landing-zone-diagram-history) | Reference architecture diagram first published. | July 29, 2022 | 
| [Initial publication](data-protection-vault-lock.md#diagram-history) | Reference architecture diagrams first published. | July 29, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.