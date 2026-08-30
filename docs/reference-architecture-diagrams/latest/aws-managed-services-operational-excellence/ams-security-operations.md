# AMS for Security Operations

Use this reference architecture to understand how AWS Managed Services (AMS) accelerates security and compliance in an AWS environment. AMS enables numerous security guardrails as part of account onboarding, providing a well-monitored and secure environment from day one.

This reference architecture was validated by the AWS Managed Services team for technical accuracy on September 20, 2022.

![Reference architecture diagram showing how AWS Managed Services accelerates security and compliance by using , , AWS CloudTrail, and AWS Security Hub.](images/aws-managed-services-operational-excellence-3.png)
The following steps describe the architecture:

1. Security and governance teams define high-level policies, requirements, and tooling. Your application and operations teams follow the guidelines to ensure security best practices are implemented.
2. As part of account onboarding, AMS enables essential AWS services and logs to achieve the desired security posture at OS, infrastructure, and account levels.
3. AMS uses to continuously monitor threats and potential malicious activities. AMS also implements custom rules for PCI, NIST, CIS, and HIPAA compliance. Optionally, AMS can monitor for sensitive data by using AWS Macie.
4. All threat findings and non-compliant rules generate monitoring events. These events go into an AMS internal service account for investigation, noise reduction, and remediation.
5. AMS uses AWS Systems Manager to create and remediate incidents. AMS also helps restore services and data by using AWS Backup.
6. You can collate and ingest security events from multiple third-party security tools and monitor them by using AWS Security Hub.

## Deploy the architecture

AWS Managed Services deploys and manages this architecture on your behalf as part of the AMS operations plan. You do not need to deploy CloudFormation templates or write custom code. To get started with AMS, see the [What is AWS Managed Services?](../../../managedservices/latest/userguide/what-is-ams.md "../../../managedservices/latest/userguide/what-is-ams.md") section in the AMS User Guide.

For onboarding details and account setup, see [AMS onboarding](../../../managedservices/latest/userguide/ams-onboarding.md "../../../managedservices/latest/userguide/ams-onboarding.md").

## Further reading

For additional information, refer to the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [AWS Managed Services product page](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change                                                                                                                                 | Description                                      | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------ |
| [Initial publication](ams-helpdesk.md#helpdesk-diagram-history "ams-helpdesk.md#helpdesk-diagram-history")                             | Reference architecture diagrams first published. | September 20, 2022 |
| [Initial publication](ams-proactive-monitoring.md#monitoring-diagram-history "ams-proactive-monitoring.md#monitoring-diagram-history") | Reference architecture diagrams first published. | September 20, 2022 |
| Initial publication                                                                                                                    | Reference architecture diagrams first published. | September 20, 2022 |
| [Initial publication](ams-logging.md#logging-diagram-history "ams-logging.md#logging-diagram-history")                                 | Reference architecture diagrams first published. | September 20, 2022 |
| [Initial publication](ams-patching.md#patching-diagram-history "ams-patching.md#patching-diagram-history")                             | Reference architecture diagrams first published. | September 20, 2022 |
| [Initial publication](ams-backup.md#backup-diagram-history "ams-backup.md#backup-diagram-history")                                     | Reference architecture diagrams first published. | September 20, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
