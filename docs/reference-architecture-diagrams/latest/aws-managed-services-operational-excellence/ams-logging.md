

# AMS for Logging
<a name="ams-logging"></a>

Use this reference architecture to understand how AWS Managed Services (AMS) provides centralized observability with logging and tracing. AMS enables and aggregates multiple logs as part of account onboarding.

This reference architecture was validated by the AWS Managed Services team for technical accuracy on September 20, 2022.

![Reference architecture diagram showing how AWS Managed Services provides centralized logging by using Amazon CloudWatch, AWS CloudTrail, VPC Flow Logs, and .](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/aws-managed-services-operational-excellence/images/aws-managed-services-operational-excellence-4.png)


The following steps describe the architecture:

1. The logging capability primarily falls under the security and governance teams. They define policies, provide guidelines, requirements, and tooling.

1. Architecture and DevOps teams follow the guidelines and ensure logging is enabled at application, OS, and infrastructure (API, firewall, network) levels.

1. AMS improves the logging posture by enabling 5 of 6 essential log types. Cloud infrastructure API (through AWS CloudTrail), OS and application (through CloudWatch OS agent), and network (VPC Flow Logs) are enabled as part of account onboarding.

1. All essential logs are locally available in CloudWatch Logs for local log search, alerting, or troubleshooting through built-in CloudWatch Insights. You can choose required retention periods for local logs.

1. AMS further improves the logging posture by enabling local events from 200\+ rules and findings as part of onboarding. AMS Ops monitor these findings 24x7 and remediate as needed.

1. You can aggregate all security-related events into a dedicated centralized security account for , , or AWS Security Hub with help from AMS operations.

1. Push consolidated event logs by using and local CloudWatch log groups into a dedicated centralized logging account. Use Kinesis to collect, filter, and transform all logs and event streams at high scale. Then index into for operational alerting, reporting, and dashboards.

## Deploy the architecture
<a name="ams-logging-deploy"></a>

AWS Managed Services deploys and manages this architecture on your behalf as part of the AMS operations plan. You do not need to deploy CloudFormation templates or write custom code. To get started with AMS, see the [What is AWS Managed Services?](https://docs.aws.amazon.com/managedservices/latest/userguide/what-is-ams.html) section in the AMS User Guide.

For onboarding details and account setup, see [AMS onboarding](https://docs.aws.amazon.com/managedservices/latest/userguide/ams-onboarding.html).

## Further reading
<a name="logging-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Managed Services product page](https://aws.amazon.com/managed-services/)

## Diagram history
<a name="logging-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](ams-helpdesk.md#helpdesk-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-proactive-monitoring.md#monitoring-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-security-operations.md#security-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](#logging-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-patching.md#patching-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 
| [Initial publication](ams-backup.md#backup-diagram-history) | Reference architecture diagrams first published. | September 20, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.