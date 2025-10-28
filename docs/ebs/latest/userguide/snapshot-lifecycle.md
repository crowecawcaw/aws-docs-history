# Automate backups with Amazon Data Lifecycle Manager

You can use Amazon Data Lifecycle Manager to automate the creation, retention, and deletion of EBS snapshots and
EBS-backed AMIs. When you automate snapshot and AMI management, it helps you to:

- Protect valuable data by enforcing a regular backup schedule.
- Create standardized AMIs that can be refreshed at regular intervals.
- Retain backups as required by auditors or internal compliance.
- Reduce storage costs by deleting outdated backups.
- Create disaster recovery backup policies that back up data to isolated Regions
  or accounts.
  When combined with the monitoring features of Amazon EventBridge and AWS CloudTrail, Amazon Data Lifecycle Manager provides
  a complete backup solution for Amazon EC2 instances and individual EBS volumes at no additional
  cost.

###### Important

- Amazon Data Lifecycle Manager can't manage snapshots or AMIs created by any other means.
- Amazon Data Lifecycle Manager can't automate the creation, retention, and deletion of instance
  store-backed AMIs.
  Amazon Data Lifecycle Manager is assessed as a service capability of Amazon Elastic Block Store (Amazon EBS). Any [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/") (FedRAMP,
  HIPAA BAA, SOC, etc) which lists Amazon EBS will also apply to Amazon Data Lifecycle Manager.

###### Contents

- [Quotas](#dlm-quotas "#dlm-quotas")
- [How it works](dlm-elements.md "dlm-elements.md")
- [Default vs custom policies](policy-differences.md "policy-differences.md")
- [Create default policies](default-policies.md "default-policies.md")
- [Create custom policy for snapshots](snapshot-ami-policy.md "snapshot-ami-policy.md")
- [Create custom policy for AMIs](ami-policy.md "ami-policy.md")
- [Automate cross-account snapshot copies](event-policy.md "event-policy.md")
- [Modify policies](modify.md "modify.md")
- [Delete policies](delete.md "delete.md")
- [Control access](dlm-prerequisites.md "dlm-prerequisites.md")
- [Monitor policies](dlm-monitor-lifecycle.md "dlm-monitor-lifecycle.md")
- [Service endpoints](dlm-service-endpoints.md "dlm-service-endpoints.md")
- [Interface VPC endpoints](dlm-vpc-endpoints.md "dlm-vpc-endpoints.md")
- [Troubleshoot](dlm-troubleshooting.md "dlm-troubleshooting.md")

## Quotas

Your AWS account has the following quotas related to Amazon Data Lifecycle Manager:

| Description                                     | Quota |
| ----------------------------------------------- | ----- |
| Custom lifecycle policies per Region            | 100   |
| Default policies for EBS snapshots per Region   | 1     |
| Default policies for EBS-backed AMIs per Region | 1     |
| Tags per resource                               | 45    |
