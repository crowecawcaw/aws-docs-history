# AWS account management and

separation

We recommend that you organize workloads in separate accounts and group accounts based on
function, compliance requirements, or a common set of controls rather than mirroring your
organization’s reporting structure. In AWS, accounts are a hard boundary. For example,
account-level separation is strongly recommended for isolating production workloads from
development and test workloads.

**Manage accounts centrally:** AWS Organizations [automates AWS account creation and management](../../../organizations/latest/userguide/orgs_manage_accounts.md "../../../organizations/latest/userguide/orgs_manage_accounts.md"), and control of those accounts after
they are created. When you create an account through AWS Organizations, it is important to consider the
email address you use, as this will be the root user that allows the password to be reset.
Organizations allows you to group accounts into [organizational units (OUs)](../../../organizations/latest/userguide/orgs_manage_ous.md "../../../organizations/latest/userguide/orgs_manage_ous.md"), which can represent different environments based on the
workload’s requirements and purpose.

**Set controls centrally:** Control what your AWS accounts can do
by only allowing specific services, Regions, and service actions at the appropriate level.
AWS Organizations allows you to use service control policies (SCPs) to apply permission guardrails at
the organization, organizational unit, or account level, which apply to all [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) users and roles. For example, you can apply an
SCP that restricts users from launching resources in Regions that you have not explicitly
allowed. AWS Control Tower offers a simplified way to set up and govern multiple accounts. It
automates the setup of accounts in your AWS Organization, automates provisioning, applies
[guardrails](../../../controltower/latest/userguide/guardrails.md "../../../controltower/latest/userguide/guardrails.md") (which include prevention and detection), and provides you with a
dashboard for visibility.

**Configure services and resources centrally:** AWS Organizations helps
you configure [AWS services](https://aws.amazon.com/organizations/features/ "https://aws.amazon.com/organizations/features/") that
apply to all of your accounts. For example, you can configure central logging of all actions
performed across your organization using [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/"), and prevent member accounts from deactivating logging. You can also
centrally aggregate data for rules that you’ve defined using [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/"), allowing you to audit your workloads for compliance and
react quickly to changes. AWS CloudFormation [StackSets](../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md "../../../AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.md") allow you to centrally manage AWS CloudFormation stacks across accounts and OUs in
your organization. This allows you to automatically provision a new account to meet your
security requirements.

Use the delegated administration feature of security services to separate the accounts
used for management from the organizational billing (management) account. Several AWS
services, such as GuardDuty, Security Hub, and AWS Config, support integrations with AWS
Organizations including designating a specific account for administrative functions.

###### Best practices

- [SEC01-BP01 Separate workloads using accounts](sec_securely_operate_multi_accounts.md "sec_securely_operate_multi_accounts.md")
- [SEC01-BP02 Secure account root user and properties](sec_securely_operate_aws_account.md "sec_securely_operate_aws_account.md")
