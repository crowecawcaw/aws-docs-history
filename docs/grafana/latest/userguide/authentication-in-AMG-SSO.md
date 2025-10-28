# Use AWS IAM Identity Center with your Amazon Managed Grafana

workspace

Amazon Managed Grafana integrates with AWS IAM Identity Center to provide identity federation for your workforce.
Using Amazon Managed Grafana and IAM Identity Center, users are redirected to their existing company directory
to sign in with their existing credentials. Then, they are seamlessly signed in to their
Amazon Managed Grafana workspace. This ensures that security settings such as password policies and
two-factor authentication are enforced. Using IAM Identity Center does not impact your existing IAM
configuration.

If you do not have an existing user directory or prefer not to federate, IAM Identity Center offers
an integrated user directory that you can use to create users and groups for Amazon Managed Grafana.
Amazon Managed Grafana does not support the use of IAM users and roles to assign permissions within
an Amazon Managed Grafana workspace.

For more information about IAM Identity Center, see [What is AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md"). For more
information about getting started with IAM Identity Center, see [Getting
started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md").

To use IAM Identity Center, you must also have AWS Organizations activated for the account. If needed,
Amazon Managed Grafana can activate Organizations for you when you create your first workspace that is
configured to use IAM Identity Center.

## Required permissions for scenarios using

IAM Identity Center

This section explains the policies that are required for using Amazon Managed Grafana with
IAM Identity Center. The policies needed to administer Amazon Managed Grafana differ based on whether your
AWS account is part of an organization or not.

### Create a Grafana administrator in AWS Organizations

accounts

To grant permissions to create and manage Amazon Managed Grafana workspaces in an
organization, and to allow dependencies such as AWS IAM Identity Center, assign the following
policies to a role.

- Assign the **AWSGrafanaAccountAdministrator** IAM
  policy to allow administering Amazon Managed Grafana workspaces.
- **AWSSSODirectoryAdministrator** allows the role to
  use IAM Identity Center when setting up Amazon Managed Grafana workspaces.
- To allow creating and managing Amazon Managed Grafana workspaces across the entire
  organization, give the role the
  **AWSSSOMasterAccountAdministrator** IAM policy.
  Alternately, give the role the
  **AWSSSOMemberAccountAdministrator** IAM policy
  to allow creating and managing workspaces within a single member account
  of the organization.
- You can also optionally give the role the
  **AWSMarketplaceManageSubscriptions** IAM policy
  (or equivalent permissions) if you want to allow the role to upgrade an
  Amazon Managed Grafana workspace to Grafana enterprise.

If you want to use service-managed permissions when you create an Amazon Managed Grafana
workspace, the role that creates the workspace must also have the
`iam:CreateRole`, `iam:CreatePolicy`, and
`iam:AttachRolePolicy` permissions. These are required to use
AWS CloudFormation StackSets to deploy policies that allow you to read data sources in the
organization's accounts.

###### Important

Granting a user the `iam:CreateRole`,
`iam:CreatePolicy`, and `iam:AttachRolePolicy`
permissions gives that user full administrative access to your AWS
account. For example, a user with these permissions can create a policy that
has full permissions for all resources, and attach that policy to any role.
Be very careful about who you grant these permissions to.

To see the permissions granted to
**AWSGrafanaAccountAdministrator**, see [AWS managed
policy: AWSGrafanaAccountAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")

### Create and manage Amazon Managed Grafana workspaces

and users in a single standalone account

A standalone AWS account is an account that is not a member of an
organization. For more information about AWS Organizations, see [What is
AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md")

To grant permission to create and manage Amazon Managed Grafana workspaces and users in a
standalone account, assign the following IAM policies to a role:

- **AWSGrafanaAccountAdministrator**
- **AWSSSOMasterAccountAdministrator**
- **AWSOrganizationsFullAccess**
- **AWSSSODirectoryAdministrator**

###### Important

Granting a role the **AWSOrganizationsFullAccess** policy
gives that role full administrative access to your AWS account. Be very
careful about who you grant these permissions to.

To see the permissions granted to
**AWSGrafanaAccountAdministrator**, see [AWS managed
policy: AWSGrafanaAccountAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSGrafanaAccountAdministrator")
