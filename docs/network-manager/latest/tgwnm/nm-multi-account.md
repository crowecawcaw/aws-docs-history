# Multi-account in AWS Global Networks for Transit Gateways

With AWS Global Networks for Transit Gateways, you can manage, monitor, and view dashboards of global network resources
from multiple AWS accounts associated with a single organization using AWS Network Manager. For more
information about setting up multi-account, see [Manage multiple accounts in global networks using AWS Organizations](#tgw-nm-multi "#tgw-nm-multi") below.

###### Important

- We strongly recommended that you use the global networks console for enabling multi-account
  settings with global networks, because the console automatically creates all required
  roles and permissions for multi-account access. Choosing an alternative approach requires
  an advanced level of expertise, and opens the multi-account set up for your global network
  to be more prone to error.
- Multi-account is not available in the AWS GovCloud (US-West) and the
  AWS GovCloud (US-East) Regions.

## Prerequisites

To enable multi-account, you first set up an account in AWS Organizations. This first account
becomes the management account. Using this account, you can then add other accounts as member
accounts to your organization. For more information about how multi-account support works, see
[Creating and managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User
Guide_.

## Manage multiple accounts in global networks using AWS Organizations

AWS Global Networks for Transit Gateways allows you to centrally manage, monitor, and visualize network resources from
multiple accounts within an organization in a single global network. To manage resources
from multiple accounts in global networks, you first set up an organization using AWS Organizations. The first
account that you use to create an organization becomes the management account. Using this
account, you can add other accounts as member accounts to your organization. From the
management account, you can designate one or more accounts within the orgaization as
delegated administrator accounts by registering them using the global networks console. For more
information about setting up an organization, see [Creating and managing an
organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md") in the _AWS Organizations User Guide_.

To enable multi-account access in the global networks console, you first enable trusted access for
the Network Manager service, and then register a delegated administrator account for your
organization.

###### Important

- We strongly recommended that you use the global networks console for enabling multi-account
  settings with global networks, because the console automatically creates all required
  roles and permissions for multi-account access. Choosing an alternative approach requires
  an advanced level of expertise, and opens the multi-account set up for your global network
  to be more prone to error.
- Multi-account is not available in the AWS GovCloud (US-West) and the
  AWS GovCloud (US-East) Regions.

With multi-account support, you can create a single global network for any of your
AWS accounts, and then register transit gateways from those accounts using the global networks console.
Multi-account is supported in all AWS Regions where global networks is supported. For more
information about multi-account, see [Multi-account in AWS Global Networks for Transit Gateways](nm-multi-account.md "nm-multi-account.md").

### Trusted access

Trusted access creates `AWSServiceAccess` for global networks and AWS CloudFormation StackSets
with AWS Organizations. Enabling trusted access provides required permissions for AWS Organizations to
deploy service-linked roles (SLRs) to all member accounts within your organization.

#### Enable trusted access

When you enable trusted access from the global networks console, you select a one-time
permission level
(`IAMRoleForAWSNetworkManagerCrossAccountResourceAccess`) as either
administrator or read-only for each of the management and delegated administrator
accounts.

- **Admin** — Assign this permission if the delegated
  administrator and management accounts need to be able to modify resources
  from other accounts in the global network while using the global networks console
  switch role.
- **Read-only** — Assign this permission if the delegated
  administrator and management accounts only need to review information about
  resources from other accounts in the global network while using the
  global networks console switch role, but don't need to make any changes.

The global networks console manages all of this when calling the Network Manager API.

When you enable trusted access, the following roles are deployed in your
organization using AWS CloudFormation StackSets and AWS Identity and Access Management (IAM) services:

- The Network Manager SLR (`AWSServiceRoleForNetworkManager`) to
  all member accounts
- The AWS CloudFormation StackSets member SLR
  (`AWSServiceRoleForCloudFormationStackSetsOrgMember`) to all
  member accounts
- The Network Manager SLR (`AWSServiceRoleForNetworkManager`) to
  the management account
- The AWS CloudFormation StackSets admin
  (`AWSServiceRoleForCloudFormationStackSetsOrgAdmin`) SLR to
  the management account
- The Amazon CloudWatch sharing role
  (`CloudWatch-CrossAccountSharingRole`) to all member
  accounts
- The global networks console switch role
  (`IAMRoleForAWSNetworkManagerCrossAccountResourceAccess`) to
  all member accounts
- The Amazon CloudWatch monitoring role
  (`AWSServiceRoleForCloudWatchCrossAccount`) to the management
  account

For more information about enabling trusted access, see [Enable trusted access in an AWS global network](nm-enable-trusted.md "nm-enable-trusted.md").

##### Disable trusted access

###### Note

Disabling trusted access through the global networks console removes
`AWSServiceAccess` for global networks with AWS Organizations. Disabling
trusted access removes global networks access to perform tasks within your
organization. AWS Organizations won't allow you to disable an organization's trusted
access for the Network Manager service if there are any delegated administrators
that haven't been deregistered from that organization.

- Disabling trusted access through the global networks console won't remove
  `AWSServiceAccess` for AWS CloudFormation StackSets with AWS Organizations. You
  can manually remove the service access for AWS CloudFormation StackSets by using the
  AWS CloudFormation StackSet console or by using the Organizations API/CLI. For more
  information on disabling trusted access for AWS CloudFormation StackSets, see [Disable trusted access with AWS CloudFormation StackSets](../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md#integrate-disable-ta-cloudformation "../../../organizations/latest/userguide/services-that-can-integrate-cloudformation.md#integrate-disable-ta-cloudformation") in the
  _AWS Organizations User Guide_.
- Disabling trusted access won't remove any SLRs that were deployed when
  enabling trusted access.

When you disable trusted access, the following are affected in global networks:

- All transit gateways owned by other accounts in your organization. You won't be
  able to see transit gateways or their attached resources from other accounts in
  your organization that were registered to your global network.
- IAM roles deployed in all member accounts managed by the Network Manager
  service. Disabling trusted access doesn't remove accounts, transit gateways, or
  resources but does deregister them from other delegated administrator's
  global networks. These can be added back in as needed by re-enabling
  trusted access. For more information about the
  `DeleteStackSet` API, see [`DeleteStackSet`](../../../AWSCloudFormation/latest/APIReference/API_DeleteStackSet.md "../../../AWSCloudFormation/latest/APIReference/API_DeleteStackSet.md") in the _AWS CloudFormation
  API Reference_.

For more information about disabling trusted access, see [Disable trusted access in an AWS global network](nm-multi-disable.md "nm-multi-disable.md").

### Delegated administrators

Member accounts in your organization with delegated administrator access are able to
leverage service-linked roles and assume IAM roles for access across multiple
accounts. Only member accounts that are part of your AWS Organizations can be registered as
delegated administrators. Your organization can have up to ten registered delegated
administrators. Before you register a delegated administrator, you must enable global networks trusted
access for your organization. For more information, see [Enable trusted access in an AWS global network](nm-enable-trusted.md "nm-enable-trusted.md").

###### Important

Using your AWS Organizations management account to manage your global
network in global networks is not recommended because the required service-linked roles are
not propagated to this account. For more information on service-linked roles, see
[AWS Global Networks for Transit Gateways service-linked roles](nm-service-linked-roles.md "nm-service-linked-roles.md").

#### Register delegated administrators

After it's registered, a delegated administrator has the same permissions as the
management account. A delegated administrator for the Network Manager service can leverage
the SLRs in the member accounts that were deployed when trusted access was enabled
and can view transit gateways from other member accounts and can register them to your global
network. This allows transit gateways and associated resources to appear in your global
network topology. In addition AWS CloudFormation StackSets is updated to include the delegated
administrator accounts in the trusted relationship of the deployed IAM roles in
the member accounts.

For information about registering a delegated administrator, see [Register an administrator for multi-account in an AWS global
network](nm-delegate-admin.md "nm-delegate-admin.md").

#### Deregister delegated

administrators

Deregistering a delegated administrator removes that account's permission to
leverage SLRs and assume IAM roles in other member accounts that were set up using
AWS Organizations.

After it's deregistered, the delegated administrator no longer has the same
permissions as the management account. The following occurs:

- A delegated administrator is no longer able to leverage the deployed SLRs
  in the member accounts that were deployed when trusted access was
  enabled.
- All registered transit gateways from other member accounts are deregistered from any
  global network for the specific delegated administrator. The network
  topology is updated to no longer show resources from other member
  accounts.
- AWS CloudFormation StackSets are updated with the removal of the delegated
  administrator account. That account is no longer able to assume any IAM
  roles deployed in other member accounts.

For information about deregistering a delegated administrator, see [Deregister an administrator from multi-account in an AWS
global network](nm-deregister-admin.md "nm-deregister-admin.md").

###### Multi-account tasks

- [Enable trusted access](nm-enable-trusted.md "nm-enable-trusted.md")
- [Disabled trusted access](nm-multi-disable.md "nm-multi-disable.md")
- [Register a delegated administrator](nm-delegate-admin.md "nm-delegate-admin.md")
- [Deregister a delegated administrator](nm-deregister-admin.md "nm-deregister-admin.md")
- [Manage IAM role deployments](nm-multi-manage-iam.md "nm-multi-manage-iam.md")
- [Troubleshoot self-managed roles](nm-multi-account-troubleshooting.md "nm-multi-account-troubleshooting.md")
