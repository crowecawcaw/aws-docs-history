# Service-linked roles for AWS

Organization discovery in AWS Data Exchange

AWS Data Exchange uses the service-linked role named `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` –
this role allows AWS Data Exchange to retrieve information about your AWS organization to determine eligibility for AWS Data Exchange data grants license distribution.

###### Note

This role is only needed in the AWS Organization's management account.

The `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` service-linked role trusts the following services to
assume the role:

- `organization-discovery.dataexchange.amazonaws.com`
  The role permissions policy named `AWSDataExchangeServiceRolePolicyForOrganizationDiscovery` allows AWS Data Exchange
  to complete the following actions on the specified resources:

- Actions:
  - `organizations:DescribeOrganization`
  - `organizations:DescribeAccount`
  - `organizations:ListAccounts`

- Resources:

      + All resources (`*`)

  For more information about the `AWSDataExchangeServiceRolePolicyForOrganizationDiscovery` role, see [AWS managed policy:
  AWSDataExchangeServiceRolePolicyForOrganizationDiscovery](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery").

For more information about using the `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` service-linked role, see
[Using service-linked roles for
AWS Data Exchange](using-service-linked-roles-adx.md "using-service-linked-roles-adx.md") earlier in this section.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
