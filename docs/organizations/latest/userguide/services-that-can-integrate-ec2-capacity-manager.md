# EC2 Capacity Manager and

AWS Organizations

EC2 Capacity Manager is a new UI experience with accompanying APIs for you to aggregate, view,
analyze, and manage your capacity usage across EC2 On-Demand, Spot, and Capacity
Reservations. When you grant trusted access for EC2 Capacity Manager to your AWS
Organization, the service gains permission to read organization membership information
across all member accounts. Specifically, Capacity Manager performs the following actions in
member accounts: it collects EC2 usage data (including on-demand instances, spot instances,
and capacity reservations) from all member accounts to aggregate into organization-wide
capacity reports and dashboards. The service does not modify resources or configurations in
member accounts - it only reads usage telemetry data that is already collected by AWS.
This allows organization administrators to view consolidated capacity utilization, forecast
future needs, and optimize resource allocation across their entire organization from a
single dashboard. For more information, see [EC2 Capacity Manager](../../../AWSEC2/latest/UserGuide/capacity-manager.md "../../../AWSEC2/latest/UserGuide/capacity-manager.md") in the
_Amazon EC2 User Guide_.

Use the following information to help you integrate
EC2 Capacity Manager with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows EC2 Capacity Manager to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
EC2 Capacity Manager and Organizations, or if you remove the member account from the organization.

The following service-linked role is created in the management account when you enable
trusted access. This role allows EC2 Capacity Manager to perform tasks in your
organization and its accounts on your behalf.

You can delete or modify this role only if you disable trusted access between
EC2 Capacity Manager and AWS Organizations, or if you remove the member account from the
organization. For more information, see [Using
service-linked roles for EC2 Capacity Manager](../../../AWSEC2/latest/UserGuide/using-service-linked-roles-cm.md "../../../AWSEC2/latest/UserGuide/using-service-linked-roles-cm.md") and [AWS managed policy: AWSEC2CapacityManagerServiceRolePolicy](../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSEC2CapacityManagerServiceRolePolicy "../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol.md#security-iam-awsmanpol-AWSEC2CapacityManagerServiceRolePolicy") in the
_Amazon EC2 User Guide_.

- `AWSServiceRoleForEC2CapacityManager` – Allows
  EC2 Capacity Manager to access AWS services and resources used or managed by
  EC2 Capacity Manager on your behalf.

## Service principals used by

EC2 Capacity Manager

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by EC2 Capacity Manager grant access to the following service
principals:

- `ec2.capacitymanager.amazonaws.com`

## Enabling trusted access with

EC2 Capacity Manager

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

When you grant trusted access for EC2 Capacity Manager to your AWS Organization, the
service gains permission to read organization membership information across all member
accounts. This allows organization administrators to view consolidated capacity
utilization, forecast future needs, and optimize resource allocation across their entire
organization from a single dashboard.

You can enable trusted access using either the EC2 Capacity Manager console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the EC2 Capacity Manager console or
tools to enable integration with Organizations. This lets EC2 Capacity Manager perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by EC2 Capacity Manager. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the EC2 Capacity Manager console or tools then you
don’t need to complete these steps.

To enable trusted access from the EC2 Capacity Manager console, sign in as an
administrator in the management account and open the Amazon EC2 console. Navigate to Capacity
Manager and go to the Settings tab. In the Trusted access section, choose
**Manage trusted access** to enable it.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI
command, or by calling an API operation in one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose
   **Services**.
3. Choose **EC2 Capacity Manager** in the list of
   services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for
   EC2 Capacity Manager** dialog box, type
   **enable** to confirm, and then choose
   **Enable trusted access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of EC2 Capacity Manager that they can now enable that service
   to work with AWS Organizations from the service console.

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable trusted
service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable EC2 Capacity Manager as a trusted
service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal ec2.capacitymanager.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

To disable trusted access from the EC2 Capacity Manager console, navigate to Amazon EC2
Capacity Manager Settings tab. In the Trusted access section, choose **Manage
trusted access** to disable it. Note: All delegated administrators must be
removed prior to disabling trusted access.

You can disable trusted access using either the EC2 Capacity Manager or the AWS Organizations tools.

###### Important

We strongly recommend that whenever possible, you use the EC2 Capacity Manager console or
tools to disable integration with Organizations. This lets EC2 Capacity Manager perform any
clean up that it requires, such as deleting resources or access roles that are no
longer needed by the service. Proceed with these steps only if you can’t disable
integration using the tools provided by EC2 Capacity Manager.

If you disable trusted access by using the EC2 Capacity Manager console or tools then you
don’t need to complete these steps.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable EC2 Capacity Manager as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal ec2.capacitymanager.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for EC2 Capacity Manager

A delegated administrator for EC2 Capacity Manager can manage Capacity Manager for your
organization without using the management account. Delegated administrators have the
ability to enable organization-level capacity management, view capacity data across all
member accounts, modify settings between account-level and organization-level scope, and
manage capacity forecasting for the entire organization. For more information, see
[Delegated
administrators for EC2 Capacity Manager](../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md "../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md") in the
_Amazon EC2 User Guide_.

###### Minimum permissions

Only an administrator in the Organizations management account can configure a delegated
administrator for EC2 Capacity Manager.

You can specify a delegated administrator account using the EC2 Capacity Manager console
by navigating to Settings and managing delegated administrators, or by using the Organizations
`RegisterDelegatedAdministrator` CLI or SDK operation. To configure a
delegated administrator using the EC2 Capacity Manager console, see [Add a delegated administrator](../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md#add-capacity-manager-da "../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md#add-capacity-manager-da") in the
_Amazon EC2 User Guide_.

AWS CLI, AWS API
You can register a delegated administrator account using the AWS CLI or
one of the AWS SDKs:

- AWS CLI: [register-delegated-administrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md")

```
`$` **aws organizations register-delegated-administrator \
 --account-id `ACCOUNT_ID` \
 --service-principal ec2.capacitymanager.amazonaws.com**
```

- AWS API: [RegisterDelegatedAdministrator](../APIReference/API_RegisterDelegatedAdministrator.md "../APIReference/API_RegisterDelegatedAdministrator.md")

## Disabling a delegated administrator

account for EC2 Capacity Manager

Only an administrator in either the Organizations management account or the EC2 Capacity Manager
delegated admin account can remove a delegated administrator account from the
organization. You can remove a delegated administrator using the EC2 Capacity Manager
console by choosing **Remove delegated administrator** in the Settings
tab, or by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation. To remove a delegated administrator using the EC2 Capacity Manager console, see
[Remove a delegated administrator](../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md#remove-capacity-manager-da "../../../AWSEC2/latest/UserGuide/enable-capacity-manager-da.md#remove-capacity-manager-da") in the
_Amazon EC2 User Guide_.

AWS CLI, AWS API
You can remove a delegated administrator account using the AWS CLI or
one of the AWS SDKs:

- AWS CLI: [deregister-delegated-administrator](../../../cli/latest/reference/organizations/deregister-delegated-administrator.md "../../../cli/latest/reference/organizations/deregister-delegated-administrator.md")

```
`$` **aws organizations deregister-delegated-administrator \
 --account-id `ACCOUNT_ID` \
 --service-principal ec2.capacitymanager.amazonaws.com**
```

- AWS API: [DeregisterDelegatedAdministrator](../APIReference/API_DeregisterDelegatedAdministrator.md "../APIReference/API_DeregisterDelegatedAdministrator.md")
