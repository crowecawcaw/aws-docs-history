# About the shared accounts

Three special AWS accounts are associated with AWS Control Tower; the management account, the
**audit** account, and the **log
archive** account. These accounts usually are referred to as _shared accounts_, or sometimes as _core accounts_.

- You can select customized names for the audit and log archive accounts when
  you're setting up your landing zone. For information about changing an account
  name, see [Externally changing AWS Control Tower resource names](external-resources.md#changing-names "external-resources.md#changing-names").
- You also can specify an existing AWS account as an AWS Control Tower security or logging account,
  during the initial landing zone setup process. This option eliminates the need
  for AWS Control Tower to create new, shared accounts. (This is a one-time
  selection.)
  For more information about the shared accounts and their associated resources, see
  [Resources created in the shared accounts](shared-account-resources.md "shared-account-resources.md").

## Management account

This AWS account launches AWS Control Tower. By default, the root user for this account
and the IAM user or IAM administrator user for this account have full access to all resources
within your landing zone.

###### Note

As a best practice, we recommend signing in as an IAM Identity Center user with
**Administrator** privileges when performing administrative
functions within the AWS Control Tower console, instead of the signing in as the root user
or IAM administrator user for this account.

For more information about the roles and resources available in the
management account, see [Resources created in the shared accounts](shared-account-resources.md "shared-account-resources.md").

## Log archive account

The log archive shared account is set up automatically when you create your
landing zone, if you do not specifically bring another AWS account.

This account contains a central Amazon S3 bucket for storing a copy of all AWS CloudTrail and
AWS Config log files for all other accounts in your landing zone. As a best practice, we
recommend restricting log archive account access to teams responsible for compliance
and investigations, and their related security or audit tools. This account can be
used for automated security audits, or to host custom AWS Config Rules, such as Lambda
functions, to perform remediation actions.

###### Amazon S3 bucket policy

For AWS Control Tower landing zone version 3.3 and later, accounts must meet an
`aws:SourceOrgID` condition for any write permissions to your
Audit bucket. This condition ensures that CloudTrail only can write logs on behalf of
accounts within your organization to your S3 bucket; it prevents CloudTrail logs
outside your organization from writing to your AWS Control Tower S3 bucket. For more
information, see [AWS Control Tower landing zone version 3.3](2023-all.md#lz-3-3 "2023-all.md#lz-3-3").

For more information about the roles and resources available in the log archive
account, see [Log archive account resources](shared-account-resources.md#log-archive-resources "shared-account-resources.md#log-archive-resources")

###### Note

These logs cannot be changed. All logs are stored for the purposes of audit
and compliance investigations related to account activity.

## Audit account

This shared account is set up automatically when you create your landing zone, if you do not specifically bring another account.

The audit account should be restricted to security and compliance teams with
auditor (read-only) and administrator (full-access) cross-account roles to all
accounts in the landing zone. These roles are intended to be used by security and
compliance teams to:

- Perform audits through AWS mechanisms, such as hosting custom AWS Config rule
  Lambda functions.
- Perform automated security operations, such as remediation actions.

The audit account also receives notifications through the Amazon Simple Notification Service (Amazon SNS)
service. Three categories of notification can be received:

- **All Configuration Events** – This
  topic aggregates all CloudTrail and AWS Config notifications from all accounts in your
  landing zone.
- **Aggregate Security Notifications** –
  This topic aggregates all security notifications from specific CloudWatch events,
  AWS Config Rules compliance status change events, and GuardDuty findings.
- **Drift Notifications** – This topic
  aggregates all the drift warnings discovered across all accounts, users,
  OUs, and SCPs in your landing zone. For more information on drift, see [Detect and resolve drift in AWS Control Tower](drift.md "drift.md").

Audit notifications that are triggered within a member account also can send
alerts to a local Amazon SNS topic. This functionality allows account administrators to
subscribe to audit notifications that are specific to an individual member account.
As a result, administrators can resolve issues that affect an individual account,
while still aggregating all account notifications to your centralized audit account.
For more information, see [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

For more information about the roles and resources available in the audit account,
see [Audit account resources](shared-account-resources.md#audit-account-resources "shared-account-resources.md#audit-account-resources").

For more information about programmatic auditing, see [Programmatic roles and trust relationships for the AWS Control Tower audit account](roles-how.md#stacksets-and-roles "roles-how.md#stacksets-and-roles").

###### Important

The email address you provide for the audit account receives **AWS
Notification - Subscription Confirmation** emails from every
AWS Region supported by AWS Control Tower. To receive compliance emails in your audit
account, you must choose the **Confirm subscription** link
within each email from each AWS Region supported by AWS Control Tower.
