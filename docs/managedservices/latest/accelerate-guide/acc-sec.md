# Security management in AMS Accelerate

AWS Managed Services uses multiple controls to protect your information assets and to help you keep your AWS infrastructure secure. AMS Accelerate maintains a library of AWS Config Rules and remediation actions to ensure that all your accounts comply with
industry standards for security and operational integrity. AWS Config Rules continuously tracks the configuration change among your recorded resources. If a change
violates any rule conditions, AMS reports its findings, and allows you to remediate violations
automatically or by request, according to the severity of the violation. AWS Config Rules facilitate compliance with standards set by:
the Center for Internet Security (CIS),
the National Institute of Standards and Technology (NIST) Cloud Security Framework (CSF),
the Health Insurance Portability and Accountability Act (HIPAA),
and the Payment Card Industry (PCI) Data Security Standard (DSS).

In addition, AMS leverages Amazon GuardDuty to identify potentially unauthorized or malicious activity in your AWS environment. AMS monitors GuardDuty findings 24x7.
AMS collaborates with you to understand the impact of the findings and identify remediation based on best practice recommendations.
AMS also uses Amazon Macie to protect your sensitive data such as personal health information (PHI), personally identifiable information (PII) and financial data.

###### Note

Amazon Macie is an optional service and is not enabled by default.

AMS Accelerate provides a range of operational services to help you achieve operational excellence on AWS.
To learn more about how AMS helps your teams achieve overall operational excellence in AWS Cloud with AMS key operational
capabilities including 24x7 helpdesk, proactive monitoring, security, patching, logging, and backup, see
[AMS Reference Architecture Diagrams](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf").

###### Topics

- [Use the Log4j SSM Document to discover occurrences in Accelerate](acc-lm-log4j.md "acc-lm-log4j.md")
- [Infrastructure security monitoring in AMS](acc-sec-infra-sec.md "acc-sec-infra-sec.md")
- [Data protection in Accelerate](acc-sec-data-protect.md "acc-sec-data-protect.md")
- [AWS Identity and Access Management in AMS Accelerate](acc-sec-iam.md "acc-sec-iam.md")
- [Security Incident Response in AMS](security-incident-response.md "security-incident-response.md")
- [Security event logging and monitoring in Accelerate](acc-sec-log-mon.md "acc-sec-log-mon.md")
- [Configuration compliance in Accelerate](acc-sec-compliance.md "acc-sec-compliance.md")
- [Incident response in Accelerate](acc-sec-incident.md "acc-sec-incident.md")
- [Resilience in Accelerate](acc-sec-resilience.md "acc-sec-resilience.md")
- [Security control for end-of-support operating systems](ams-eos-sec-controls-os.md "ams-eos-sec-controls-os.md")
- [Security best practices in Accelerate](acc-sec-best-practice.md "acc-sec-best-practice.md")
- [Change request security reviews](acc-sec-change-request-review.md "acc-sec-change-request-review.md")
- [Security FAQ](security-access-faq.md "security-access-faq.md")
