# Amazon VPC IP Address Manager (IPAM) and AWS Organizations

Amazon VPC IP Address Manager (IPAM) is a VPC feature that makes it easier for you to plan, track, and monitor IP
addresses for your AWS workloads.

Using AWS Organizations allows you to monitor IP address usage throughout your organization and
share IP address pools across member accounts.

For more information, see
[Integrate IPAM
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Amazon VPC IPAM User Guide_.

Use the following information to help you integrate Amazon VPC IP Address Manager (IPAM) with AWS Organizations.

## Service-linked roles created when

you enable integration

The following service-linked role is automatically created in your organization's
management account and each member account when you integrate IPAM with AWS Organizations
either by using the IPAM console or using IPAM's
`EnableIpamOrganizationAdminAccount` API.

- `AWSServiceRoleForIPAM`

For more information, see [Service-linked roles for IPAM](../../../vpc/latest/ipam/iam-ipam-slr.md "../../../vpc/latest/ipam/iam-ipam-slr.md") in
the _Amazon VPC IPAM User Guide_.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by IPAM grant access to the following service
principals:

- `ipam.amazonaws.com`

## To enable trusted access with

IPAM

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

###### Note

When you designate a delegated administrator for IPAM it automatically enables
trusted access for IPAM for your organization.

IPAM requires trusted access to AWS Organizations before you can designate a member
account to be the delegated administrator for this service for your
organization.

You can enable trusted access using only Amazon VPC IP Address Manager (IPAM) tools.

If you integrate IPAM with AWS Organizations using the IPAM console or using the IPAM
`EnableIpamOrganizationAdminAccount` API, you automatically grant trusted
access to IPAM. Granting trusted access creates the service-linked role `AWSServiceRoleForIPAM` in the management account and in all of the member
accounts in the organization. IPAM uses the service-linked role to monitor CIDRs
associated with EC2 networking resources in your organization and to store metrics
related to IPAM in Amazon CloudWatch. For more information, see [Service-linked roles for IPAM](../../../vpc/latest/ipam/iam-ipam-slr.md "../../../vpc/latest/ipam/iam-ipam-slr.md") in
the _Amazon VPC IPAM User Guide_.

For instructions about enabling trusted access, see [Integrate IPAM with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md")
in the _Amazon VPC IPAM User Guide_.

###### Note

You can't enable trusted access with IPAM using the AWS Organizations console or with
the [`EnableAWSServiceAccess`](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md") API.

## To disable trusted access with

IPAM

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Only an administrator in the AWS Organizations management account can disable trusted access
with IPAM using the AWS Organizations `disable-aws-service-access` API.

For information about disabling IPAM account permissions and deleting the
service-linked role, see [Service-linked roles for IPAM](../../../vpc/latest/ipam/iam-ipam-slr.md "../../../vpc/latest/ipam/iam-ipam-slr.md") in
the _Amazon VPC IPAM User Guide_.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable Amazon VPC IP Address Manager (IPAM) as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal ipam.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for IPAM

The delegated administrator account for IPAM is responsible for creating the IPAM
and IP address pools, managing and monitoring IP address usage in the organization, and
sharing IP address pools across member accounts. For more information, see [Integrate IPAM
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Amazon VPC IPAM User Guide_.

Only an administrator in the organization management account can configure a delegated
administrator for IPAM.

You can specify a delegated administrator account from the IPAM console, or by using
the `enable-ipam-organization-admin-account` API. For more information, see
[enable-ipam-organization-admin-account](../../../cli/latest/reference/ec2/enable-ipam-organization-admin-account.md "../../../cli/latest/reference/ec2/enable-ipam-organization-admin-account.md") in the _AWS AWS CLI Command
Reference_.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for IPAM in the organization

To configure a delegated administrator using the IPAM console, see [Integrate IPAM
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Amazon VPC IPAM User Guide_.

## Disabling a delegated administrator

for IPAM

Only an administrator in the organization management account can configure a delegated
administrator for IPAM.

To remove a delegated administrator using the AWS AWS CLI, see [disable-ipam-organization-admin-account](../../../cli/latest/reference/ec2/disable-ipam-organization-admin-account.md "../../../cli/latest/reference/ec2/disable-ipam-organization-admin-account.md") in the _AWS AWS CLI Command
Reference_.

To disable the delegated admin IPAM account using the IPAM console, see [Integrate IPAM
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Amazon VPC IPAM User Guide_.
