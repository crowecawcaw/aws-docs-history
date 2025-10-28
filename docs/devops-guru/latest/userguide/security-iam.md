# Identity and Access Management for

Amazon DevOps Guru

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use DevOps Guru resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Audience](#security_iam_audience "#security_iam_audience")
- [Authenticating with identities](#security_iam_authentication "#security_iam_authentication")
- [Managing access using policies](#security_iam_access-manage "#security_iam_access-manage")
- [DevOps Guru updates to AWS managed policies
  and service-linked role](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
- [How Amazon DevOps Guru works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Identity-based policies for
  Amazon DevOps Guru](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")
- [Using service-linked roles for
  DevOps Guru](using-service-linked-roles.md "using-service-linked-roles.md")
- [Amazon DevOps Guru permissions
  reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md")
- [Permissions for Amazon SNS topics](sns-required-permissions.md "sns-required-permissions.md")
- [Permissions for AWS KMS–encrypted Amazon SNS
  topics](sns-kms-permissions.md "sns-kms-permissions.md")
- [Troubleshooting Amazon DevOps Guru identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshooting Amazon DevOps Guru identity and
  access](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How Amazon DevOps Guru works with
  IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Identity-based policies for
  Amazon DevOps Guru](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"))

## Authenticating with identities

Authentication is how you sign in to AWS using your identity credentials. You must be authenticated as the AWS account root user, an IAM user, or by assuming an IAM role.

You can sign in as a federated identity using credentials from an identity source like AWS IAM Identity Center (IAM Identity Center), single sign-on authentication, or Google/Facebook credentials. For more information about signing in, see [How to sign in to your AWS account](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User Guide_.

For programmatic access, AWS provides an SDK and CLI to cryptographically sign requests. For more information, see [AWS Signature Version 4 for API requests](../../../IAM/latest/UserGuide/reference_sigv.md "../../../IAM/latest/UserGuide/reference_sigv.md") in the _IAM User Guide_.

### AWS account root user

When you create an AWS account, you begin with one sign-in identity called the AWS account _root user_ that has complete access to all AWS services and resources. We strongly recommend that you don't use the root user for everyday tasks. For tasks that require root user credentials, see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.

### Federated identity

As a best practice, require human users to use federation with an identity provider to access AWS services using temporary credentials.

A _federated identity_ is a user from your enterprise directory, web identity provider, or AWS Directory Service that accesses AWS services using credentials from an identity source. Federated identities assume roles that provide temporary credentials.

For centralized access management, we recommend AWS IAM Identity Center. For more information, see [What is IAM Identity Center?](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") in the _AWS IAM Identity Center User Guide_.

### IAM users and groups

An _[IAM user](../../../IAM/latest/UserGuide/id_users.md "../../../IAM/latest/UserGuide/id_users.md")_ is an identity with specific permissions for a single person or application. We recommend using temporary credentials instead of IAM users with long-term credentials. For more information, see [Require human users to use federation with an identity provider to access AWS using temporary credentials](../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp "../../../IAM/latest/UserGuide/best-practices.md#bp-users-federation-idp") in the _IAM User Guide_.

An [_IAM group_](../../../IAM/latest/UserGuide/id_groups.md "../../../IAM/latest/UserGuide/id_groups.md") specifies a collection of IAM users and makes permissions easier to manage for large sets of users. For more information, see [Use cases for IAM users](../../../IAM/latest/UserGuide/gs-identities-iam-users.md "../../../IAM/latest/UserGuide/gs-identities-iam-users.md") in the _IAM User Guide_.

### IAM roles

An _[IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")_ is an identity with specific permissions that provides temporary credentials. You can assume a role by [switching from a user to an IAM role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") or by calling an AWS CLI or AWS API operation. For more information, see [Methods to assume a role](../../../IAM/latest/UserGuide/id_roles_manage-assume.md "../../../IAM/latest/UserGuide/id_roles_manage-assume.md") in the _IAM User Guide_.

IAM roles are useful for federated user access, temporary IAM user permissions, cross-account access, cross-service access, and applications running on Amazon EC2. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

## Managing access using policies

You control access in AWS by creating policies and attaching them to AWS identities or resources. A policy defines permissions when associated with an identity or resource. AWS evaluates these policies when a principal makes a request. Most policies are stored in AWS as JSON documents. For more information about JSON policy documents, see [Overview of JSON policies](../../../IAM/latest/UserGuide/access_policies.md#access_policies-json "../../../IAM/latest/UserGuide/access_policies.md#access_policies-json") in the _IAM User Guide_.

Using policies, administrators specify who has access to what by defining which **principal** can perform **actions** on what **resources**, and under what **conditions**.

By default, users and roles have no permissions. An IAM administrator creates IAM policies and adds them to roles, which users can then assume. IAM policies define permissions regardless of the method used to perform the operation.

### Identity-based

policies

Identity-based policies are JSON permissions policy documents that you attach to an identity (user, group, or role). These policies control what actions identities can perform, on which resources, and under what conditions. To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.

Identity-based policies can be _inline policies_ (embedded directly into a single identity) or _managed policies_ (standalone policies attached to multiple identities). To learn how to choose between managed and inline policies, see [Choose between managed policies and inline policies](../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md "../../../IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.md") in the _IAM User Guide_.

### Resource-based

policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples include IAM _role trust policies_ and Amazon S3 _bucket policies_. In services that support resource-based policies, service administrators can use them to control access to a specific resource. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy.

Resource-based policies are inline policies that are located in that service. You can't use AWS managed policies from IAM in a resource-based policy.

### Other policy types

AWS supports additional policy types that can set the maximum permissions granted by more common policy types:

- **Permissions boundaries** – Set the maximum permissions that an identity-based policy can grant to an IAM entity. For more information, see [Permissions boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Service control policies (SCPs)** – Specify the maximum permissions for an organization or organizational unit in AWS Organizations. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- **Resource control policies (RCPs)** – Set the maximum available permissions for resources in your accounts. For more information, see [Resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the _AWS Organizations User Guide_.
- **Session policies** – Advanced policies passed as a parameter when creating a temporary session for a role or federated user. For more information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

### Multiple policy

types

When multiple types of policies apply to a request, the resulting permissions are more complicated to understand. To learn how AWS determines whether to allow a request when multiple policy types are involved, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

## DevOps Guru updates to AWS managed policies

and service-linked role

View details about updates to AWS managed policies and service-linked role for DevOps Guru
since this service began tracking these changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the DevOps Guru [Amazon DevOps Guru document history](doc-history.md "doc-history.md").

| Change                                                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                          | Date              |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AmazonDevOpsGuruConsoleFullAccess](security_iam_id-based-policy-examples.md#managed-full-console-access "security_iam_id-based-policy-examples.md#managed-full-console-access") – Update to an existing policy. | The `AmazonDevOpsGuruFullAccess` managed policy now supports Amazon SNS subscriptions.                                                                                                                                                                                               | August 9, 2023    |
| [AmazonDevOpsGuruReadOnlyAccess](security_iam_id-based-policy-examples.md#managed-read-only-access "security_iam_id-based-policy-examples.md#managed-read-only-access") – Update to an existing policy           | The `AmazonDevOpsGuruReadOnlyAccess` managed policy now supports read-only access to Amazon SNS subscription lists.                                                                                                                                                                  | August 9, 2023    |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports access to API Gateway GET actions on REST APIs.                                                                                                                                                                   | January 11, 2023  |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports several Amazon Simple Storage Service and Service Quotas actions.                                                                                                                                                 | October 19, 2022  |
| [AmazonDevOpsGuruFullAccess](security_iam_id-based-policy-examples.md#managed-full-access "security_iam_id-based-policy-examples.md#managed-full-access") – Update to an existing policy                         | The `AmazonDevOpsGuruFullAccess` managed policy now supports access to the CloudWatch `FilterLogEvents` action.                                                                                                                                                                      | August 30, 2022   |
| [AmazonDevOpsGuruConsoleFullAccess](security_iam_id-based-policy-examples.md#managed-full-console-access "security_iam_id-based-policy-examples.md#managed-full-console-access") – Update to an existing policy  | The `AmazonDevOpsGuruConsoleFullAccess` managed policy now supports access to the CloudWatch `FilterLogEvents` action.                                                                                                                                                               | August 30, 2022   |
| [AmazonDevOpsGuruReadOnlyAccess](security_iam_id-based-policy-examples.md#managed-read-only-access "security_iam_id-based-policy-examples.md#managed-read-only-access") – Update to an existing policy           | The `AmazonDevOpsGuruReadOnlyAccess` managed policy now supports read-only access to the CloudWatch `FilterLogEvents` action.                                                                                                                                                        | August 30, 2022   |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports the CloudWatch logs actions `FilterLogEvents`, `DescribeLogGroups`, and `DescribeLogStreams`.                                                                                                                     | July 12, 2022     |
| [Identity-based policies for DevOps Guru](security_iam_id-based-policy-examples.md#managed-full-access "security_iam_id-based-policy-examples.md#managed-full-access") – New managed policy.                     | The `AmazonDevOpsGuruConsoleFullAccess` policy has been added.                                                                                                                                                                                                                       | December 16, 2021 |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports Performance Insights `DescribeMetricsKeys`, and Amazon RDS `DescribeDBInstances` actions.                                                                                                                         | December 1, 2021  |
| [AmazonDevOpsGuruReadOnlyAccess](security_iam_id-based-policy-examples.md#managed-read-only-access "security_iam_id-based-policy-examples.md#managed-read-only-access") – Update to an existing policy           | The `AmazonDevOpsGuruReadOnlyAccess` managed policy now supports read-only access to Amazon RDS `DescribeDBInstances` actions.                                                                                                                                                       | December 1, 2021  |
| [AmazonDevOpsGuruFullAccess](security_iam_id-based-policy-examples.md#managed-full-access "security_iam_id-based-policy-examples.md#managed-full-access") – Update to an existing policy                         | The `AmazonDevOpsGuruFullAccess` managed policy now supports access to Amazon RDS `DescribeDBInstances` actions.                                                                                                                                                                     | December 1, 2021  |
| [Identity-based policies for Amazon DevOps Guru](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md") – New policy added.                                                        | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports access to Amazon RDS `DescribeDBInstances` and Performance Insights `GetResourceMetrics` actions. The `AmazonDevOpsGuruOrganizationsAccess` managed policy provides access to DevOps Guru within an organization. | November 16, 2021 |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now supports AWS Organizations.                                                                                                                                                                                                | November 4, 2021  |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` service-linked role now contains new conditions on the `ssm:CreateOpsItem` and `ssm:AddTagsToResource` actions.                                                                                                                                    | October 11, 2021  |
| [Service-linked role permissions for DevOps Guru](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                 | The `AWSServiceRoleForDevOpsGuru` service-linked role now contains new conditions on the `ssm:CreateOpsItem` and `ssm:AddTagsToResource` actions.                                                                                                                                    | June 14, 2021     |
| [AmazonDevOpsGuruReadOnlyAccess](security_iam_id-based-policy-examples.md#managed-read-only-access "security_iam_id-based-policy-examples.md#managed-read-only-access") – Update to an existing policy           | The `AmazonDevOpsGuruReadOnlyAccess` managed policy now allows read-only access to the AWS Identity and Access Management `GetRole` and the DevOps Guru `DescribeFeedback` actions.                                                                                                  | June 14, 2021     |
| [AmazonDevOpsGuruReadOnlyAccess](security_iam_id-based-policy-examples.md#managed-read-only-access "security_iam_id-based-policy-examples.md#managed-read-only-access") – Update to an existing policy           | The `AmazonDevOpsGuruReadOnlyAccess` managed policy now allows read-only access to the DevOps Guru `GetCostEstimation` and `StartCostEstimation` actions.                                                                                                                            | April 27, 2021    |
| [AmazonDevOpsGuruServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – Update to an existing policy.                                               | The `AWSServiceRoleForDevOpsGuru` role now allows access to the AWS Systems Manager `AddTagsToResource` and Amazon EC2 Auto Scaling `DescribeAutoScalingGroups` actions.                                                                                                             | April 27, 2021    |
| DevOps Guru started tracking changes                                                                                                                                                                             | DevOps Guru started tracking changes for its AWS managed policies.                                                                                                                                                                                                                   | December 10, 2020 |
