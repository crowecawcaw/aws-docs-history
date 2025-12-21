# Appendix: Comparison of SCS-C02 and SCS-C03

## Side-by-side comparison

The following table shows the domains and the percentage of scored questions in each domain for the SCS-C02 exam (in use until December 1, 2025) and the SCS-C03 exam (in use beginning December 2, 2025).

| SCS-C02 Domain                                         | SCS-C03 Domain                                              |
| ------------------------------------------------------ | ----------------------------------------------------------- |
| Domain 1: Threat Detection and Incident Response (14%) | Content Domain 1: Detection (16% of scored content)         |
| Domain 2: Security Logging and Monitoring (18%)        | Content Domain 2: Incident Response (14%)                   |
| Domain 3: Infrastructure Security (20%)                | Content Domain 3: Infrastructure Security (18%)             |
| Domain 4: Identity and Access Management (16%)         | Content Domain 4: Identity and Access Management (20%)      |
| Domain 5: Data Protection (18%)                        | Content Domain 5: Data Protection (18%)                     |
| Domain 6: Management and Security Governance (14%)     | Content Domain 6: Security Foundations and Governance (14%) |

## Additions of content for SCS-C03

In Task 2.2.3, the following content was added:

- 2.2.3 Validate findings from AWS security services to assess the scope and impact of an event.

In Task 3.1.4, the following content was added:

- 3.1.4 Configure integrations with AWS edge services and third-party services (for example, by ingesting data in Open Cybersecurity Schema Framework [OCSF] format, by using third-party WAF rules).

In Task 3.2.7, the following content was added:

- 3.2.7 Implement protections and guardrails for generative AI applications (for example, by applying GenAI OWASP Top 10 for LLM Applications protections).

In Task 5.1.3, the following content was added:

- 5.1.3 Design and configure inter-resource encryption in-transit (for example, inter-node encryption configurations for Amazon EMR, Amazon Elastic Kubernetes Service [Amazon EKS], SageMaker AI, Nitro encryption).

In Task 5.3.3, the following content was added:

- 5.3.3 Describe the differences between imported key material and AWS generated key material.

In Task 5.3.4, the following content was added:

- 5.3.4 Mask sensitive data (for example, CloudWatch Logs data protection policies, Amazon Simple Notification Service [Amazon SNS] message data protection).

In Task 5.3.5, the following content was added:

- 5.3.5 Create and manage encryption keys and certificates across a single AWS Region or multiple Regions (for example, AWS KMS customer managed AWS KMS keys, AWS Private Certificate Authority).

## Deletions of content for SCS-C03

In Task 6.4, the following content was removed:

- Identify security gaps through architectural reviews and cost analysis.

In Task 1.1, the following content was removed:

- AWS Security Finding Format (ASFF)

In Task 1.3, the following content was removed:

- AWS Security Incident Response Guide

In Task 2.5 the following content was removed:

- Log format and components (for example, CloudTrail logs)

In Task 3.3, the following content was removed:

- Host-based security (for example, firewalls, hardening)
- Activating host-based security mechanisms (for example, host-based firewalls)

In Task 3.4, the following content was removed:

- How to analyze reachability (for example, by using VPC Reachability Analyzer and Amazon Inspector)
- Fundamental TCP/IP networking concepts (for example, UDP compared with TCP, ports, Open Systems Interconnection [OSI] model, network operating system utilities)
- Identifying, interpreting, and prioritizing problems in network connectivity (for example, by using Amazon Inspector Network Reachability)

In Task 4.2, the following content was removed:

- Components and impact of a policy (for example, Principal, Action, Resource, Condition)

In Task 5.1, the following content was removed:

- TLS concepts
- Designing cross-Region networking by using private VIFs and public VIFs

In Task 5.2, the following content was removed:

- Configure S3 static website hosting.

## Recategorizations of content for SCS-C03

The following major content reorganizations have occurred in the transition from SCS-C02 to SCS-C03:

SCS-C02 Domains 1 and 2 have been restructured:

- "Threat Detection and Incident Response" and "Security Logging and Monitoring" are now:
  - Domain 1: Detection
  - Domain 2: Incident Response

Domain 6 has been renamed for SCS-C03:

- From "Management and Security Governance" to "Security Foundations and Governance"

The following task statement have been recategorized:

SCS-C02 Task Statement 1.1 is mapped to the following tasks in SCS-C03:

- 1.1 Design and implement monitoring and alerting for an AWS account or organization.
- 1.2 Design and implement logging.
- 2.1 Design and test an incident response plan.
- 2.2 Respond to security events.

SCS-C02 Task Statement 1.2 is mapped to the following tasks in SCS-C03:

- 1.1 Design and implement monitoring and alerting for an AWS account or organization.
- 1.2 Design and implement logging.

SCS-C02 Task Statement 1.3 is mapped to the following tasks in SCS-C03:

- 2.1 Design and test an incident response plan.
- 2.2 Respond to security events.

SCS-C02 Task Statement 2.1 is mapped to the following tasks in SCS-C03:

- 1.1 Design and implement monitoring and alerting for an AWS account or organization.

SCS-C02 Task Statement 2.2 is mapped to the following tasks in SCS-C03:

- 1.1 Design and implement monitoring and alerting for an AWS account or organization.
- 1.2 Design and implement logging.
- 1.3 Troubleshoot security monitoring, logging and alerting.

SCS-C02 Task Statement 2.3 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.

SCS-C02 Task Statement 2.4 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.
- 1.3 Troubleshoot security monitoring, logging and alerting.

SCS-C02 Task Statement 2.5 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.

SCS-C02 Task Statement 3.1 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.
- 3.1 Design, implement, and troubleshoot security controls for network edge services.

SCS-C02 Task Statement 3.2 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.
- 3.3 Design and troubleshoot network security controls.
- 5.1 Design and implement controls for data in transit.
- 6.2 Implement a secure and consistent deployment strategy for cloud resources.

SCS-C02 Task Statement 3.3 is mapped to the following tasks in SCS-C03:

- 3.2 Design, implement, and troubleshoot security controls for compute workloads.
- 5.3 Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials.

SCS-C02 Task Statement 3.4 is mapped to the following tasks in SCS-C03:

- 1.2 Design and implement logging.
- 3.3 Design and troubleshoot network security controls.

SCS-C02 Task Statement 4.1 is mapped to the following tasks in SCS-C03:

- 4.1 Design, implement, and troubleshoot authentication strategies

SCS-C02 Task Statement 4.2 is mapped to the following tasks in SCS-C03:

- 4.2 Design, implement, and troubleshoot authorization strategies

SCS-C02 Task Statement 5.1 is mapped to the following tasks in SCS-C03:

- 3.2 Design, implement, and troubleshoot security controls for compute workloads.
- 3.3 Design and troubleshoot network security controls.
- 5.1 Design and implement controls for data in transit.

SCS-C02 Task Statement 5.2 is mapped to the following tasks in SCS-C03:

- 4.2 Design, implement, and troubleshoot authorization strategies
- 5.2 Design and implement controls for data at rest.

SCS-C02 Task Statement 5.3 is mapped to the following tasks in SCS-C03:

- 5.2 Design and implement controls for data at rest.

SCS-C02 Task Statement 5.4 is mapped to the following tasks in SCS-C03:

- 5.2 Design and implement controls for data at rest.
- 5.3 Design and implement controls to protect confidential data, credentials, secrets, and cryptographic key materials.

SCS-C02 Task Statement 6.1 is mapped to the following tasks in SCS-C03:

- 4.2 Design, implement, and troubleshoot authorization strategies
- 6.1 Develop a strategy to centrally deploy and manage AWS accounts.

SCS-C02 Task Statement 6.2 is mapped to the following tasks in SCS-C03:

- 6.2 Implement a secure and consistent deployment strategy for cloud resources.

SCS-C02 Task Statement 6.3 is mapped to the following tasks in SCS-C03:

- 1.1 Design and implement monitoring and alerting for an AWS account or organization.
- 5.2 Design and implement controls for data at rest.
- 6.3 Evaluate the compliance of AWS resources.

SCS-C02 Task Statement 6.4 is mapped to the following tasks in SCS-C03:

- 2.1 Design and test an incident response plan.
- 1.1 Design and implement monitoring and alerting for an AWS account or organization.
- 6.3 Evaluate the compliance of AWS resources.
