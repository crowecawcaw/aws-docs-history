# Using AWS managed policies to access Amazon Neptune databases

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. Managed policies grant necessary permissions for common use
cases so you can avoid having to investigate what permissions are needed. For more
information, see [AWS Managed
Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account, are
for using Amazon Neptune management APIs:

- **[NeptuneReadOnlyAccess](read-only-access-iam-managed-policy.md "read-only-access-iam-managed-policy.md")**
  — Grants read-only administrative actions (such as `rds:Describe*` and
  `rds:ListTagsForResource`) and read-only data-access actions
  (`neptune-db:Read*`, `neptune-db:Get*`, and
  `neptune-db:List*`) on all Neptune resources. Use this policy for users
  who need to view cluster configurations and query data without making
  changes.
- **[NeptuneFullAccess](full-access-iam-managed-policy.md "full-access-iam-managed-policy.md")**
  — Grants all administrative actions (`rds:*` on Neptune resources)
  and all data-access actions (`neptune-db:*`). This policy is suitable for
  administrators who manage Neptune clusters through the AWS CLI or SDK but do not need
  AWS Management Console access.
- **[NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md")**
  — Grants all administrative actions on Neptune resources plus additional
  permissions for Amazon EC2 (VPC), IAM, and Neptune Analytics that are needed for
  AWS Management Console workflows. This policy does not include data-access actions
  (`neptune-db:*`). Use this policy for users who manage Neptune through
  the AWS Management Console.
- **NeptuneGraphReadOnlyAccess**
  — This policy is for Neptune Analytics. For details, see [NeptuneGraphReadOnlyAccess
  in Neptune Analytics](../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-graph-read-only.md "../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-graph-read-only.md").
- **AWSServiceRoleForNeptuneGraphPolicy**
  — This policy is for Neptune Analytics. For details, see [AWSServiceRoleForNeptuneGraphPolicy
  in Neptune Analytics](../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-slr-policy.md "../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-slr-policy.md").
  Neptune IAM roles and policies grant some access to Amazon RDS resources, because Neptune
  shares operational technology with Amazon RDS for certain management features. This includes
  administrative API permissions, which is why Neptune administrative actions have an
  `rds:` prefix.

## Creating custom policies

If the AWS managed policies are too broad for your use case, you can create custom
IAM policies that grant only the specific permissions you need. Neptune supports two
categories of custom policies:

- **Administrative policies** — Control
  access to Neptune management operations such as creating, modifying, and deleting
  clusters and instances. These actions use the `rds:` prefix. For examples,
  see [Creating IAM administrative policy statements for Amazon Neptune](iam-admin-policy-examples.md "iam-admin-policy-examples.md").
- **Data-access policies** — Control
  access to the data in your Neptune graph database, including read, write, and delete
  operations. These actions use the `neptune-db:` prefix. For examples, see
  [Creating IAM data-access policies in Amazon Neptune](iam-data-access-examples.md "iam-data-access-examples.md").

By combining administrative and data-access policy statements, you can grant
fine-grained permissions tailored to each user or role in your organization.

## Validating IAM policies

When you create or edit custom IAM policies, we recommend that you validate
them before applying them to users, groups, or roles.

**IAM Access Analyzer policy validation** —
IAM Access Analyzer provides policy checks that validate your IAM policies against
IAM policy grammar and AWS best practices. It identifies errors, security warnings,
and suggestions to help you author policies that are functional and conform to security
best practices. For more information, see [Validating policies with
IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.

**IAM Policy Simulator** — The IAM Policy
Simulator lets you test the effects of IAM policies before committing them to
production. You can simulate API calls to AWS services to verify that your policies
grant or deny the expected access. For more information, see [Testing IAM policies with
the IAM Policy Simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md") in the
_IAM User Guide_.

## Updates to Neptune AWS managed policies

The following table tracks updates to Neptune managed policies starting from
the time Neptune began tracking these changes:

| Policy                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                               | Date       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| AWS managed policies for Amazon Neptune<br>• update to existing policies                                                                                                                                               | The `NeptuneReadOnlyAcess` and `NeptuneFullAccess` managed policies now include<br>`Sid` (statement ID) as an identifier in the policy statement.                                                                                                                                                                                         | 2024-01-22 |
| [NeptuneGraphReadOnlyAccess](../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-graph-read-only.md "../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-graph-read-only.md") (released) | Released to provide read-only access to Neptune Analytics graphs and resources.                                                                                                                                                                                                                                                           | 2023-11-29 |
| [AWSServiceRoleForNeptuneGraphPolicy](../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-slr-policy.md "../../../neptune-analytics/latest/userguide/security-iam-awsmanpol-slr-policy.md") (released)  | Released to allow Neptune Analytics graphs access to CloudWatch to publish operational<br>and usage metrics and logs. See [Using service-linked<br>roles (SLRs) in Neptune Analytics](../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md "../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md"). | 2023-11-29 |
| [NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md") (added permissions)                                                                                  | Added permissions provide all access needed to interact with Neptune Analytics graphs.                                                                                                                                                                                                                                                    | 2023-11/29 |
| [NeptuneFullAccess](full-access-iam-managed-policy.md "full-access-iam-managed-policy.md") (added permissions)                                                                                                         | Added data-access permissions, and permissions for new global database APIs.                                                                                                                                                                                                                                                              | 2022-07-28 |
| [NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md") (added permissions)                                                                                  | Added permissions for new global database APIs.                                                                                                                                                                                                                                                                                           | 2022-07-21 |
| Neptune started tracking changes                                                                                                                                                                                       | Neptune began tracking changes to its AWS managed policies.                                                                                                                                                                                                                                                                               | 2022-07-21 |
