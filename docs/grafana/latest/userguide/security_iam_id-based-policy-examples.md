# Identity-based policy examples

for Amazon Managed Grafana

By default, users and roles don't have permission to create or modify Amazon Managed Grafana
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon Managed Grafana, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon Managed Grafana](../../../service-authorization/latest/reference/list_amazonmanagedgrafana.md "../../../service-authorization/latest/reference/list_amazonmanagedgrafana.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Amazon Managed Grafana
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Sample policies for
  Amazon Managed Grafana](#security_iam_AMG-id-based-policy-examples "#security_iam_AMG-id-based-policy-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Managed Grafana resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Using the Amazon Managed Grafana

console

To access the console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the resources in your
AWS account. If you create an identity-based policy that is more restrictive than
the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

## Sample policies for

Amazon Managed Grafana

This section contains identity-based policies that are useful for several
Amazon Managed Grafana scenarios.

### Grafana

administrator using SAML

If you use SAML for your user authentication, the administrator who creates
and manages Amazon Managed Grafana needs the following policies:

- **AWSGrafanaAccountAdministrator** or the equivalent
  permissions to create and manage Amazon Managed Grafana workspaces.
- The **AWSMarketplaceManageSubscriptions** policy or
  equivalent permissions, if you want to upgrade an Amazon Managed Grafana workspace to
  Grafana Enterprise.

#### Grafana

administrator in a management account using IAM Identity Center

To grant permissions to create and manage Amazon Managed Grafana workspaces across an
entire organization, and to enable dependencies such as IAM Identity Center, assign the
**AWSGrafanaAccountAdministrator**,
**AWSSSOMasterAccountAdministrator** and the
**AWSSSODirectoryAdministrator** policies to a user.
Additionally, to upgrade an Amazon Managed Grafana workspace to Grafana Enterprise, a
user must have the **AWSMarketplaceManageSubscriptions**
IAM policy or the equivalent permissions.

If you want to use service-managed permissions when you create an
Amazon Managed Grafana workspace, the user who creates the workspace must also have the
`iam:CreateRole`, `iam:CreatePolicy`, and
`iam:AttachRolePolicy` permissions. These are required to use
CloudFormation StackSets to deploy policies that enable you to read data sources in
the organization's accounts.

###### Important

Granting a user the `iam:CreateRole`,
`iam:CreatePolicy`, and `iam:AttachRolePolicy`
permissions gives that user full administrative access to your AWS
account. For example, a user with these permissions can create a policy
that has full permissions for all resources, and attach that policy to
any role. Be very careful about who you grant these permissions to.

To see the permissions granted to
**AWSGrafanaAccountAdministrator**, see [AWS managed
policy: AWSGrafanaAccountAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")

#### Grafana

administrator in a member account using IAM Identity Center

To grant permissions to create and manage Amazon Managed Grafana workspaces in the
member account of an organization, assign the
**AWSGrafanaAccountAdministrator**,
**AWSSSOMemberAccountAdministrator** and the
**AWSSSODirectoryAdministrator** policies to a user.
Additionally, to upgrade an Amazon Managed Grafana workspace to Grafana Enterprise, a
user must have the **AWSMarketplaceManageSubscriptions**
IAM policy or the equivalent permissions.

If you want to use service-managed permissions when you create an
Amazon Managed Grafana workspace, the user who creates the workspace must also have the
`iam:CreateRole`, `iam:CreatePolicy`, and
`iam:AttachRolePolicy` permissions. These are required to
enable the user to read data sources in the account.

###### Important

Granting a user the `iam:CreateRole`,
`iam:CreatePolicy`, and `iam:AttachRolePolicy`
permissions gives that user full administrative access to your AWS
account. For example, a user with these permissions can create a policy
that has full permissions for all resources, and attach that policy to
any role. Be very careful about who you grant these permissions to.

To see the permissions granted to
**AWSGrafanaAccountAdministrator**, see [AWS managed
policy: AWSGrafanaAccountAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")

#### Create and manage Amazon Managed Grafana workspaces and users in a single standalone

account using IAM Identity Center

A standalone AWS account is an account that is not yet a member of an
organization. For more information about organizations, see [What is
AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")

To grant permissions to create and manage Amazon Managed Grafana workspaces and users
in a standalone account, assign the
**AWSGrafanaAccountAdministrator**,
**AWSSSOMasterAccountAdministrator**,
**AWSOrganizationsFullAccess** and
**AWSSSODirectoryAdministrator** policies to a user.
Additionally, to upgrade an Amazon Managed Grafana workspace to Grafana Enterprise, a
user must have the **AWSMarketplaceManageSubscriptions**
IAM policy or the equivalent permissions.

###### Important

Granting a user the `iam:CreateRole`,
`iam:CreatePolicy`, and `iam:AttachRolePolicy`
permissions gives that user full administrative access to your AWS
account. For example, a user with these permissions can create a policy
that has full permissions for all resources, and attach that policy to
any role. Be very careful about who you grant these permissions to.

To see the permissions granted to
**AWSGrafanaAccountAdministrator**, see [AWS managed
policy: AWSGrafanaAccountAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")

#### Assign

and unassign users access to Amazon Managed Grafana

To grant permissions to manage other
users' access to Amazon Managed Grafana workspaces in the account, including granting
Grafana admin permissions to those users for the workspaces,assign the
**AWSGrafanaWorkspacePermissionManagementV2** policy to
that user. If you are using IAM Identity Center to manage users in this workspace, the
user also needs the **AWSSSOReadOnly** and
**AWSSSODirectoryReadOnly** policies.

To see the permissions granted to
**AWSGrafanaWorkspacePermissionManagementV2**, see [AWS
managed policy: AWSGrafanaWorkspacePermissionManagementV2](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2 "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaWorkspacePermissionManagementV2")

#### Amazon Managed Grafana read-only permissions

To grant permissions for read actions,
such as listing and viewing workspaces and opening the Grafana workspace
console, assign the **AWSGrafanaConsoleReadOnlyAccess**,
**AWSSSOReadOnly** and
**AWSSSODirectoryReadOnly** policies to a user
or IAM role.

To see the permissions granted to
**AWSGrafanaConsoleReadOnlyAccess**, see [AWS managed
policy: AWSGrafanaConsoleReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaConsoleReadOnlyAccess") .
