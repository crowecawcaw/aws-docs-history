# GuardDuty attack sequence finding

types

GuardDuty detects an attack sequence when a specific sequence of multiple actions aligns with a
potentially suspicious activity. An attack sequence includes **signals** such as API activities and GuardDuty findings. When GuardDuty observes a group of
signals in a specific sequence that indicates an in-progress, ongoing, or a recent security
threat, GuardDuty generates an attack sequence finding. GuardDuty considers individual API activities as
[weak signals](guardduty_concepts.md#guardduty-weak-signals-attack-sequence "guardduty_concepts.md#guardduty-weak-signals-attack-sequence") because they don't present
themselves as potential threat.

The attack sequence detections focus on potential compromise of Amazon S3 data (that can be a part
of a broader ransomware attack), compromised AWS credentials, compromised Amazon EKS clusters,
compromised Amazon ECS clusters, and compromised Amazon EC2 instance groups.
The following sections provide details about each of the attack sequences.

###### Topics

- [AttackSequence:EKS/CompromisedCluster](#attack-sequence-eks-compromised-cluster "#attack-sequence-eks-compromised-cluster")
- [AttackSequence:ECS/CompromisedCluster](#attack-sequence-ecs-compromised-cluster "#attack-sequence-ecs-compromised-cluster")
- [AttackSequence:EC2/CompromisedInstanceGroup](#attack-sequence-ec2-compromised-instance-group "#attack-sequence-ec2-compromised-instance-group")
- [AttackSequence:IAM/CompromisedCredentials](#attack-sequence-iam-compromised-credentials "#attack-sequence-iam-compromised-credentials")
- [AttackSequence:S3/CompromisedData](#attack-sequence-s3-compromised-data "#attack-sequence-s3-compromised-data")

## AttackSequence:EKS/CompromisedCluster

### A sequence of suspicious

actions performed by potentially compromised Amazon EKS cluster.

- Default severity: Critical
- Data sources:
  - [EKS audit log events](kubernetes-protection.md#guardduty_k8s-audit-logs "kubernetes-protection.md#guardduty_k8s-audit-logs")
  - [Runtime Monitoring for Amazon EKS](how-runtime-monitoring-works-eks.md "how-runtime-monitoring-works-eks.md")
  - [Amazon EKS
    malware detection for Amazon EC2](malware-protection.md "malware-protection.md")
  - [AWS CloudTrail data events for S3](s3-protection.md#guardduty_s3dataplane "s3-protection.md#guardduty_s3dataplane")
  - [AWS CloudTrail management events](guardduty_data-sources.md#guardduty_controlplane "guardduty_data-sources.md#guardduty_controlplane")
  - [VPC Flow Logs](guardduty_data-sources.md#guardduty_vpc "guardduty_data-sources.md#guardduty_vpc")
  - [Route53 Resolver DNS query logs](guardduty_data-sources.md#guardduty_dns "guardduty_data-sources.md#guardduty_dns")

This finding informs you that GuardDuty detected a sequence of suspicious actions that indicates
a potentially compromised Amazon EKS cluster in your environment. Multiple suspicious and anomalous
attack behaviors, such as malicious processes or connection with malicious endpoints, were
observed in the same Amazon EKS cluster.

GuardDuty uses its proprietary correlation algorithms to observe and identify the sequence of
actions performed by using the IAM credential. GuardDuty evaluates findings across protection plans
and other signal sources to identify common and emerging attack patterns. GuardDuty uses multiple
factors to surface threats, such as IP reputation, API sequences, user configuration, and
potentially impacted resources.

**Remediation actions**: If this behavior is unexpected in your
environment, then your Amazon EKS cluster may be compromised. For comprehensive remediation guidance, see
[Remediating EKS Protection findings](guardduty-remediate-kubernetes.md "guardduty-remediate-kubernetes.md") and
[Remediating Runtime Monitoring findings](guardduty-remediate-runtime-monitoring.md "guardduty-remediate-runtime-monitoring.md").

Additionally, since AWS credentials may have been compromised through the EKS cluster, see
[Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md"). For steps to remediate other
resources that may have been potentially impacted, see [Remediating detected GuardDuty security findings](guardduty_remediate.md "guardduty_remediate.md").

## AttackSequence:ECS/CompromisedCluster

### A sequence of suspicious

actions performed by potentially compromised Amazon ECS cluster.

- Default severity: Critical
- Data sources:
  - [Runtime Monitoring for Amazon ECS Fargate](how-runtime-monitoring-works-ecs-fargate.md "how-runtime-monitoring-works-ecs-fargate.md")
  - [Runtime Monitoring for EC2 Instances in Amazon ECS](how-runtime-monitoring-works-ec2.md "how-runtime-monitoring-works-ec2.md")
  - [GuardDuty Malware Protection for Amazon EC2](malware-protection.md "malware-protection.md")

This finding informs you that GuardDuty detected a sequence of suspicious signals indicating a potentially compromised
Amazon ECS cluster in your environment. These signals may include malicious processes, communications with malicious endpoints,
or cryptocurrency mining behaviors.

GuardDuty uses proprietary correlation algorithms and multiple detection factors to identify sequences of
suspicious actions within Amazon ECS clusters. Through analysis across protection plans and various signal sources,
GuardDuty identifies common and emerging attack patterns, providing high-confidence detection of potential compromises.

**Remediation actions**: If this behavior is unexpected in your
environment, your Amazon ECS cluster may be compromised. For threat containment recommendations, see
[Remediating a potentially compromised ECS
cluster](compromised-ecs.md "compromised-ecs.md"). Note that the compromise may extend to one or more
ECS tasks or container workloads, which could have been used to create or modify AWS resources.
For comprehensive remediation guidance covering potentially impacted resources, see [Remediating detected GuardDuty security findings](guardduty_remediate.md "guardduty_remediate.md").

## AttackSequence:EC2/CompromisedInstanceGroup

### A sequence of suspicious

actions indicating potentially compromised Amazon EC2 instances.

- Default severity: Critical
- Data sources:
  - [Runtime Monitoring for Amazon EC2](how-runtime-monitoring-works-ec2.md "how-runtime-monitoring-works-ec2.md")
  - [Malware detection for Amazon EC2](malware-protection.md "malware-protection.md")
  - [VPC Flow Logs](guardduty_data-sources.md#guardduty_vpc "guardduty_data-sources.md#guardduty_vpc")
  - [Route53 Resolver DNS query logs](guardduty_data-sources.md#guardduty_dns "guardduty_data-sources.md#guardduty_dns")

This finding indicates GuardDuty detected a sequence of suspicious actions suggesting potential compromise across
a group of Amazon EC2 instances in your environment. Instance groups typically represent applications managed through
infrastructure-as-code, sharing similar configurations such as Auto-scaling group, IAM instance profile role,
AWS CloudFormation stack, Amazon EC2 launch template, AMI or VPC ID. GuardDuty observed multiple suspicious behaviors across one or more instances, including:

- Malicious processes
- Malicious files
- Suspicious network connections
- Cryptocurrency mining activities
- Suspicious usage of Amazon EC2 instance credentials

**Detection Method**: GuardDuty employs proprietary correlation algorithms to identify
suspicious action sequences within Amazon EC2 instances. By evaluating findings across protection plans and various signal sources,
GuardDuty identifies attack patterns using multiple factors such as IP and domain reputation and suspicious running processes.

**Remediation actions**: If this behavior is unexpected in your
environment, your Amazon EC2 instances may be compromised. The compromise could involve:

- Multiple processes
- Instance credentials that may have been used to modify Amazon EC2 instances or other AWS resources

For threat containment recommendations, see [Remediating a potentially compromised Amazon EC2
instance](compromised-ec2.md "compromised-ec2.md").
Note that the compromise may extend to one or more Amazon EC2 instances and involve compromised processes or instance credentials
that could have been used to create or modify Amazon EC2 instances or other AWS resources.
For comprehensive remediation guidance covering potentially impacted resources, see [Remediating detected GuardDuty security findings](guardduty_remediate.md "guardduty_remediate.md").

## AttackSequence:IAM/CompromisedCredentials

### A sequence of API

requests that were invoked by using potentially compromised AWS credentials.

- Default severity: Critical
- Data source: [AWS CloudTrail management events](guardduty_data-sources.md#guardduty_controlplane "guardduty_data-sources.md#guardduty_controlplane")

This finding informs you that GuardDuty detected a sequence of suspicious actions made by using
AWS credentials that impacts one or more resources in your environment. Multiple suspicious and
anomalous attack behaviors were observed by the same credentials, resulting in higher confidence
that the credentials are being misused.

GuardDuty uses its proprietary correlation algorithms to observe and identify the sequence of
actions performed by using the IAM credential. GuardDuty evaluates findings across protection plans
and other signal sources to identify common and emerging attack patterns. GuardDuty uses multiple
factors to surface threats, such as IP reputation, API sequences, user configuration, and
potentially impacted resources.

**Remediation actions**: If this behavior is unexpected in your
environment, then your AWS credentials may have been compromised. For steps to remediate, see
[Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md"). The compromised
credentials may have been used to create or modify additional resources, such as Amazon S3 buckets,
AWS Lambda functions, or Amazon EC2 instances, in your environment. For steps to remediate other
resources that may have been potentially impacted, see [Remediating detected GuardDuty security findings](guardduty_remediate.md "guardduty_remediate.md").

## AttackSequence:S3/CompromisedData

### A sequence of API requests was

invoked in a potential attempt to exfiltrate or destroy data in Amazon S3.

- Default severity: Critical
- Data sources: [AWS CloudTrail data events for S3](s3-protection.md#guardduty_s3dataplane "s3-protection.md#guardduty_s3dataplane") and [AWS CloudTrail management events](guardduty_data-sources.md#guardduty_controlplane "guardduty_data-sources.md#guardduty_controlplane")

This finding informs you that GuardDuty detected a sequence of suspicious actions indicative of
data compromise in one or more Amazon Simple Storage Service (Amazon S3) buckets, by using potentially compromised AWS
credentials. Multiple suspicious and anomalous attack behaviors (API requests) were observed,
resulting in higher confidence of the credentials are being misused.

GuardDuty uses its correlation algorithms to observe and identify the sequence of actions
performed by using the IAM credential. GuardDuty then evaluates findings across protection plans
and other signal sources to identify common and emerging attack patterns. GuardDuty uses multiple
factors to surface threats, such as IP reputation, API sequences, user configuration, and
potentially impacted resources.

**Remediation actions**: If this activity is unexpected in
your environment, your AWS credentials, or Amazon S3 data may have potentially exfiltrated or
destroyed. For steps to remediate, see [Remediating potentially compromised AWS
credentials](compromised-creds.md "compromised-creds.md") and [Remediating a potentially compromised S3 bucket](compromised-s3.md "compromised-s3.md").
