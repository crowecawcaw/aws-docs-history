# ADVSEC01-BP04 Implement authorization by setting access policies, and implement least privilege access for users to protect programmatic advertising workloads

Address the risk of authenticated advertisers and SSPs access to
data they should not reach.

## Implementation guidance

Implement strong
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam "https://aws.amazon.com/iam") policies when you deploy a global
advertising technology workload. Use the principle of least
privilege, and enforce the separation of duties for good
security posture. Administrative access should only be given to
a small number of secured administrators.

Use [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/ "https://aws.amazon.com/iam/access-analyzer/") to validate IAM policies and verify that
they match IAM best practices and your organization's security
standards.

IAM Access Analyzer can help your organization review and
removed unused or external access across your AWS resources with
continuous monitoring. IAM Access Analyzer can also assist
administrators by validating your IAM policies against IAM
policy grammar and AWS best practices.
