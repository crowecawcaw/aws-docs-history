

# AMS for Backup
<a name="ams-backup"></a>

Use this reference architecture to understand how AWS Managed Services (AMS) manages data availability and continuity. AMS takes complete ownership of backup monitoring, alerting, restoration, and reporting.

This reference architecture was validated by the AWS Managed Services team for technical accuracy on September 20, 2022.

![Reference architecture diagram showing how AWS Managed Services manages backup by using AWS Backup, , and Amazon CloudWatch.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aws-managed-services-operational-excellence/images/aws-managed-services-operational-excellence-6.png)


The following steps describe the architecture:

1. The backup capability primarily falls under the architecture and governance teams. They define policies, provide guidelines, and requirements.

1. Your application and DevOps teams follow the guidelines and ensure regular backup at the application and OS levels. Your application teams are responsible for defining backup windows, backup plans, and disaster recovery (DR) testing.

1. AMS uses AWS Backup to perform backup and restore for all AWS services it supports. AMS sets up backup automation and vaults as part of AWS account onboarding.

1. AMS offers multiple backup plans to suit different needs. You set up custom backup plans or vaults based on environment, tier, recovery point objective (RPO), and applications by using AWS tags.

1. With AMS, you get daily backup coverage reporting based on account, plan, and resources. Backup reports are available to consume and export through the AMS Console.

1. AMS implements backup alerting and monitoring by using rules and Amazon CloudWatch.

1. The AMS internal service account runs backup orchestration and automation. receives all backup-related events to perform backup deployment, monitoring, alerting, reporting, and failure remediations.

## Deploy the architecture
<a name="ams-backup-deploy"></a>

AWS Managed Services deploys and manages this architecture on your behalf as part of the AMS operations plan. You do not need to deploy CloudFormation templates or write custom code. To get started with AMS, see the [What is AWS Managed Services?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html) section in the AMS User Guide.

For onboarding details and account setup, see [AMS onboarding](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-onboarding.html).

## Further reading
<a name="backup-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Managed Services product page](https://aws.amazon.com/managed-services/)

## Diagram history
<a name="backup-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](ams-helpdesk.md#helpdesk-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-proactive-monitoring.md#monitoring-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-security-operations.md#security-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-logging.md#logging-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-patching.md#patching-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](#backup-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.