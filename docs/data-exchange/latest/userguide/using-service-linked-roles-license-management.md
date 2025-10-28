# Service-linked role for

AWS Data Exchange license management

AWS Data Exchange uses the service-linked role named `AWSServiceRoleForAWSDataExchangeLicenseManagement` –
this role allows AWS Data Exchange to retrieve information about your AWS organization and manage AWS Data Exchange data grants licenses.

The `AWSServiceRoleForAWSDataExchangeLicenseManagement` service-linked role trusts the following services to
assume the role:

- `license-management.dataexchange.amazonaws.com`
  The role permissions policy named `AWSDataExchangeServiceRolePolicyForLicenseManagement` allows AWS Data Exchange
  to complete the following actions on the specified resources:

- Actions:
  - `organizations:DescribeOrganization`
  - `license-manager:ListDistributedGrants`
  - `license-manager:GetGrant`
  - `license-manager:CreateGrantVersion`
  - `license-manager:DeleteGrant`

- Resources:

      + All resources (`*`)

  For more information about the `AWSDataExchangeServiceRolePolicyForLicenseManagement` role, see [AWS managed policy:
  AWSDataExchangeServiceRolePolicyForLicenseManagement](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement "security-iam-awsmanpol.md#security-iam-awsmanpol-awsdataexchangeservicerolepolicyforlicensemanagement").

For more information about using the `AWSServiceRoleForAWSDataExchangeLicenseManagement` service-linked role, see
[Using service-linked roles for
AWS Data Exchange](using-service-linked-roles-adx.md "using-service-linked-roles-adx.md").

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
