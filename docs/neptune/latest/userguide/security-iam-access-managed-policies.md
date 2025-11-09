# Using AWS managed policies to access

Amazon Neptune databases

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. Managed policies grant necessary permissions for common use
cases so you can avoid having to investigate what permissions are needed. For more
information, see [AWS Managed
Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account, are
for using Amazon Neptune management APIs:

- **[NeptuneReadOnlyAccess](read-only-access-iam-managed-policy.md "read-only-access-iam-managed-policy.md")**
  — Grants read-only access to all Neptune resources for both administrative and
  data-access purposes in the root AWS account.
- **[NeptuneFullAccess](full-access-iam-managed-policy.md "full-access-iam-managed-policy.md")**
  — Grants full access to all Neptune resources for both administrative and
  data-access purposes in the root AWS account. This is recommended if you need full
  Neptune access from the AWS CLI or SDK, but not for AWS Management Console access.
- **[NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md")**
  — Grants full access in the root AWS account to all Neptune administrative
  actions and resources, but not to any data-access actions or resources. It also includes
  additional permissions to simplify Neptune access from the console, including limited
  IAM and Amazon EC2 (VPC) permissions.
- **[NeptuneGraphReadOnlyAccess](graph-read-only-access-iam-managed-policy.md "graph-read-only-access-iam-managed-policy.md")**
  — Provides read-only access to all Amazon Neptune Analytics resources along with
  read-only permissions for dependent services
- **[AWSServiceRoleForNeptuneGraphPolicy](aws-service-role-for-neptune-graph-policy.md "aws-service-role-for-neptune-graph-policy.md")**
  — Lets Neptune Analytics graphs to publish CloudWatch operational and usage metrics and logs.
  Neptune IAM roles and policies grant some access to Amazon RDS resources, because Neptune
  shares operational technology with Amazon RDS for certain management features. This includes
  administrative API permissions, which is why Neptune administrative actions have an
  `rds:` prefix.

## Updates to Neptune AWS managed policies

The following table tracks updates to Neptune managed policies starting from
the time Neptune began tracking these changes:

| Policy                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                               | Date       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| AWS managed policies for Amazon Neptune<br>• update to existing policies                                                                      | The `NeptuneReadOnlyAcess` and `NeptuneFullAccess` managed policies now include<br>`Sid` (statement ID) as an identifier in the policy statement.                                                                                                                                                                                         | 2024-01-22 |
| [NeptuneGraphReadOnlyAccess](read-only-access-iam-managed-policy.md "read-only-access-iam-managed-policy.md") (released)                      | Released to provide read-only access to Neptune Analytics graphs and resources.                                                                                                                                                                                                                                                           | 2023-11-29 |
| [AWSServiceRoleForNeptuneGraphPolicy](aws-service-role-for-neptune-graph-policy.md "aws-service-role-for-neptune-graph-policy.md") (released) | Released to allow Neptune Analytics graphs access to CloudWatch to publish operational<br>and usage metrics and logs. See [Using service-linked<br>roles (SLRs) in Neptune Analytics](../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md "../../../neptune-analytics/latest/userguide/nan-service-linked-roles.md"). | 2023-11-29 |
| [NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md") (added permissions)         | Added permissions provide all access needed to interact with Neptune Analytics graphs.                                                                                                                                                                                                                                                    | 2023-11/29 |
| [NeptuneFullAccess](full-access-iam-managed-policy.md "full-access-iam-managed-policy.md") (added permissions)                                | Added data-access permissions, and permissions for new global database APIs.                                                                                                                                                                                                                                                              | 2022-07-28 |
| [NeptuneConsoleFullAccess](console-full-access-iam-managed-policy.md "console-full-access-iam-managed-policy.md") (added permissions)         | Added permissions for new global database APIs.                                                                                                                                                                                                                                                                                           | 2022-07-21 |
| Neptune started tracking changes                                                                                                              | Neptune began tracking changes to its AWS managed policies.                                                                                                                                                                                                                                                                               | 2022-07-21 |
