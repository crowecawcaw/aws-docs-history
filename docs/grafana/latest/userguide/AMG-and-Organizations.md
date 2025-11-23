# How Amazon Managed Grafana works with AWS Organizations for AWS data

source access

With AWS Organizations, you can centrally manage data source configuration and permission
settings for multiple AWS accounts. In an AWS account with an Amazon Managed Grafana workspace,
you can specify other organizational units to make their AWS data sources available
for viewing in the primary account.

For example, you can use one account in the organization as an Amazon Managed Grafana
_management account_, and give this account access to data
sources in other accounts in the organization. In the management account, list all the
organizational units that have AWS data sources that you want to access with the
management account. This automatically creates the roles and permissions policies that
you need for setting up these data sources, which you can see in the Grafana console in
the Amazon Managed Grafana workspace.

For more information about Organizations, see [What is
AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

Amazon Managed Grafana uses CloudFormation StackSets to automatically create the AWS Identity and Access Management (IAM) roles
necessary for Amazon Managed Grafana to connect to data sources across your AWS organization.
Before Amazon Managed Grafana can manage your IAM policies to access data sources across your
organization, you must enable AWS CloudFormation StackSets in the management account of your
organization. Amazon Managed Grafana automatically enables this the first time that it's
needed.

## Deployment scenarios for

integration with AWS IAM Identity Center and Organizations

If you are using Amazon Managed Grafana with both AWS IAM Identity Center and Organizations, we recommend that you
create an Amazon Managed Grafana workspace in your organization using one of the following three
scenarios. For each scenario, you need to be signed in to an account with sufficient
permissions. For more information, see [Sample policies for
Amazon Managed Grafana](security_iam_id-based-policy-examples.md#security_iam_AMG-id-based-policy-examples "security_iam_id-based-policy-examples.md#security_iam_AMG-id-based-policy-examples").

**Standalone account**

A standalone account is an AWS account that is not a member of an organization
in Organizations. This is a likely scenario if you are trying out AWS for the first
time.

In this scenario, Amazon Managed Grafana automatically enables AWS IAM Identity Center and Organizations when you are
signed in to an account that has the
**AWSGrafanaAccountAdministrator**,
**AWSSSOMemberAccountAdministrator**, and
**AWSSSODirectoryAdministrator** policies. For more
information, see [Create and manage Amazon Managed Grafana workspaces and users in a single standalone
account using IAM Identity Center](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-workspace-standalone "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-workspace-standalone").

**Member account of an existing organization in which IAM Identity Center is
already configured**

To create a workspace in a member account, you must be signed in to an account
that has the **AWSGrafanaAccountAdministrator**,
**AWSSSOMemberAccountAdministrator**, and
**AWSSSODirectoryAdministrator** policies. For more
information, see [Grafana
administrator in a member account using IAM Identity Center](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-admin-member "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-admin-member").

If you create a workspace in a member account and you want that workspace to
access resources from other AWS accounts in your organization, you must use
customer managed permissions in the workspace. For more information, see [Customer-managed permissions](AMG-manage-permissions.md#AMG-customer-managed "AMG-manage-permissions.md#AMG-customer-managed").

To use service-managed permissions to allow a workspace to access resources from
other AWS accounts in the organization, you would have to create the workspace in
the management account of the organization. However, it is not a best practice to
create Amazon Managed Grafana workspaces or other resources in the management account of an
organization. For more information about Organizations best practices, see [Best
practices for the management account](../../../organizations/latest/userguide/orgs_best-practices_mgmt-acct.md "../../../organizations/latest/userguide/orgs_best-practices_mgmt-acct.md").

###### Note

If you enabled AWS IAM Identity Center in the management account before November 25, 2019,
you must also enable IAM Identity Center-integrated applications in the management account.
Optionally, you can also enable IAM Identity Center-integrated applications in the member
accounts after you do so in the management account. To enable these
applications, choose **Enable access** in the IAM Identity Center
**Settings** page in the IAM Identity Center-integrated applications
section. For more information, see [IAM Identity Center-integrated
application enablement](../../../singlesignon/latest/userguide/app-enablement.md "../../../singlesignon/latest/userguide/app-enablement.md").

**Member account of an existing organization in which IAM Identity Center
isn't deployed yet**

In this scenario, sign in as the organization administrator first, and enable
IAM Identity Center in the organization. Then, create the Amazon Managed Grafana workspace in a member account
in the organization.

If you are not an organization administrator, you must contact an administrator
for Organizations and request that they enable IAM Identity Center. After IAM Identity Center is enabled, you can then
create the workspace in a member account.

If you create a workspace in a member account and you want that workspace to
access resources from other AWS accounts in your organization, you must use
customer managed permissions in the workspace. For more information, see [Customer-managed permissions](AMG-manage-permissions.md#AMG-customer-managed "AMG-manage-permissions.md#AMG-customer-managed").

To create a workspace in a member account, you must be signed in to an account
that has the **AWSGrafanaAccountAdministrator**,
**AWSSSOMemberAccountAdministrator**, and
**AWSSSODirectoryAdministrator** policies. For more
information, see [Grafana
administrator in a member account using IAM Identity Center](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-admin-member "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-admin-member").
