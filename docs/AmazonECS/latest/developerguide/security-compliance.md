# Compliance and security best practices for Amazon ECS

Your compliance responsibility when using Amazon ECS is determined by the sensitivity of your
data, the compliance objectives of your company, and applicable laws and regulations.

## Payment Card Industry Data Security Standards (PCI DSS)

It's important that you understand the complete flow of cardholder data (CHD)
within the environment when adhering to PCI DSS. The CHD flow determines the
applicability of the PCI DSS, defines the boundaries and components of a
cardholder data environment (CDE), and therefore the scope of a PCI DSS
assessment. Accurate determination of the PCI DSS scope is key to defining the
security posture and ultimately a successful assessment. Customers must have a
procedure for scope determination that assures its completeness and detects changes
or deviations from the scope.

The temporary nature of containerized applications provides additional
complexities when auditing configurations. As a result, customers need to maintain
an awareness of all container configuration parameters to ensure compliance
requirements are addressed throughout all phases of a container lifecycle.

For additional information on achieving PCI DSS compliance on Amazon ECS, refer
to the following whitepapers.

- [Architecting on Amazon ECS for PCI DSS compliance](https://d1.awsstatic.com/whitepapers/compliance/architecting-on-amazon-ecs-for-pci-dss-compliance.pdf "                     https://d1.awsstatic.com/whitepapers/compliance/architecting-on-amazon-ecs-for-pci-dss-compliance.pdf")

## HIPAA (U.S. Health Insurance Portability and Accountability Act)

Using Amazon ECS with workloads that process protected health information (PHI)
requires no additional configuration. Amazon ECS acts as an orchestration service that
coordinates the launch of containers on Amazon EC2. It doesn't operate with or upon data
within the workload being orchestrated. Consistent with HIPAA regulations and the
AWS Business Associate Addendum, PHI should be encrypted in transit and at-rest
when accessed by containers launched with Amazon ECS.

Various mechanisms for encrypting at-rest are available with each AWS storage
option, such as Amazon S3, Amazon EBS, and AWS KMS. You can deploy an overlay network (such as VNS3
or Weave Net) to ensure complete encryption of PHI transferred between containers or to
provide a redundant layer of encryption. You should also use complete logging, and
direct all container logs to Amazon CloudWatch. For information about using the best practices
for infrastructure security, see [Infrastructure Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS
Well‐Architected Framework_.

## AWS Security Hub CSPM

Use AWS Security Hub CSPM. This AWS service provides a comprehensive
view of your security state within AWS. Security Hub CSPM uses security controls to evaluate your
AWS resources and to check your compliance against security industry standards and
best practices. For a list of supported services and controls, see [Security Hub CSPM
controls reference](../../../securityhub/latest/userguide/securityhub-controls-reference.md "../../../securityhub/latest/userguide/securityhub-controls-reference.md").

## Amazon GuardDuty with Amazon ECS Runtime Monitoring

Amazon GuardDuty is a threat detection service that helps protect your accounts,
containers, workloads, and the data within your AWS environment. Using machine
learning (ML) models, and anomaly and threat detection capabilities, GuardDuty
continuously monitors different log sources and runtime activity to identify and
prioritize potential security risks and malicious activities in your
environment.

Use Runtime Monitoring in GuardDuty to identify malicious or unauthorized behavior.
Runtime Monitoring protects workloads running on Fargate and EC2 by continuously
monitoring AWS log and networking activity to identify malicious or unauthorized
behavior. Runtime Monitoring uses a lightweight, fully managed GuardDuty security agent that
analyzes on-host behavior, such as file access, process execution, and network
connections. This covers issues including escalation of privileges, use of exposed
credentials, or communication with malicious IP addresses, domains, and the presence
of malware on your Amazon EC2 instances and container workloads. For more information,
see [GuardDuty Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") in the _GuardDuty User
Guide_.

## Compliance recommendations

We recommend that you engage the compliance program owners within your business early
and use the AWS shared responsibility model to identify compliance control ownership
for success with the relevant compliance programs. For more information, see [AWS shared responsibility model for Amazon ECS](security-shared-model.md "security-shared-model.md").
