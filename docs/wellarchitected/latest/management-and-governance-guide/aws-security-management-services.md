# AWS security management services

The following AWS services can be used to help you meet the
prescribed benefits of the M&G Guide:

[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") is a cloud security posture management service
that performs security best practice checks, aggregates alerts,
and enables automated remediation. AWS Security Hub CSPM aggregates,
organizes, and prioritizes your findings from multiple AWS
services as well as from AWS Partner solutions, enabling you to
quickly assess the security posture across your AWS accounts. AWS Security Hub CSPM runs automated configurations and compliance checks
based on open standards, such as CIS Benchmarks, NIST frameworks,
and AWS Foundational Security Best Practices.

[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") is a threat detection service that continually
monitors for malicious activity and unintended behavior to protect
your AWS accounts, workloads, and data stored in Amazon S3. Amazon GuardDuty uses machine learning, anomaly detection, and integrated
threat intelligence to identify and prioritize potential threats.
GuardDuty analyzes tens of billions of events across multiple AWS
data sources, such as AWS CloudTrail event logs, Amazon VPC Flow
Logs, and DNS logs.

Both AWS Security Hub CSPM and Amazon GuardDuty have the concept of an
_administrator_ and _member_
account. The administrator account can view the aggregated
findings of all member accounts within a Region. You should
delegate administration of Security Hub CSPM and GuardDuty to the
security audit account provisioned by AWS Control Tower.

[AWS Security Hub CSPM Automated Response and Remediation](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/ "https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/") is a solution
that uses AWS Security Hub CSPM to provide a ready-to-deploy
architecture and a library of automated playbooks. The solution
creates an Service Catalog portfolio of predefined security
response and remediation actions called playbooks. Individual
playbooks are deployed in the Security Hub CSPM primary account. Each
playbook contains the necessary custom actions, AWS Identity and Access Management (IAM) roles, Amazon CloudWatch Events, Systems
Manager automation documents, AWS Lambda functions, and AWS Step Functions needed to start a remediation workflow within a single
AWS account, or across multiple accounts.

[Amazon
Detective](https://aws.amazon.com/detective/ "https://aws.amazon.com/detective/") automatically collects log data from your AWS
resources and uses machine learning, statistical analysis, and
graph theory to build a linked set of data that enables you to
easily conduct faster and more efficient security investigations.

[AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") implements centralized logging and audit
accounts that use AWS CloudTrail and Amazon CloudWatch. This is
done using AWS Config for detective guardrail enablement, and SCPs
from AWS Organizations for preventive controls.

[AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") allows you to create automated responses to
security misconfigurations via specific automation documents, with
patch management functions.

Using
[automated
reasoning technology](https://aws.amazon.com/security/provable-security/ "https://aws.amazon.com/security/provable-security/") (the application of mathematical logic
to help answer critical questions about your infrastructure), AWS
is able to identify opportunities to improve your security
posture. We call this _provable security_
providing higher assurance in security of the cloud and in the
cloud. Automated reasoning capabilities include
[IAM
Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/ "https://aws.amazon.com/iam/features/analyze-access/"),
[VPC
Reachability Analyzer](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md"),
[Amazon
CodeGuru](https://aws.amazon.com/codeguru/ "https://aws.amazon.com/codeguru/"),
[Amazon S3 Block Public Access](https://aws.amazon.com/s3/features/block-public-access/ "https://aws.amazon.com/s3/features/block-public-access/"), and Amazon Inspector network
reachability.

If you would like support implementing this guidance, or assisting
you with building the foundational elements prescribed by the
M&G Guide, we recommend you review the offerings provided by
[AWS Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/") or the AWS Partners in the
[Built
on Control Tower program](https://aws.amazon.com/controltower/partners/ "https://aws.amazon.com/controltower/partners/").

If you are seeking help to operate your workloads in AWS following
this guidance,
[AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/") can augment your operational
capabilities as a short-term accelerator or a long-term solution,
letting you focus on transforming your applications and businesses
in the cloud.
