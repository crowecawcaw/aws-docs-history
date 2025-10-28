# Service-linked role to share entitlements for AWS Marketplace

To share your AWS Marketplace subscriptions to other accounts in your AWS organization with
AWS License Manager, you must give AWS Marketplace permissions for each account you want to share with. Do
this by using the **AWSServiceRoleForMarketplaceLicenseManagement** role. This role provides
AWS Marketplace with permissions to create and manage licenses in AWS License Manager for the products
that you subscribe to in AWS Marketplace.

The `AWSServiceRoleForMarketplaceLicenseManagement`
service-linked role trusts the following service to perform actions in License Manager on your
behalf:

- `license-management.marketplace.amazonaws.com`
  The `AWSMarketplaceLicenseManagementServiceRolePolicy` allows
  AWS Marketplace to complete the following actions on the specified resources:

- Actions:
  - `"organizations:DescribeOrganization"`
  - `"license-manager:ListReceivedGrants"`
  - `"license-manager:ListDistributedGrants"`
  - `"license-manager:GetGrant"`
  - `"license-manager:CreateGrant"`
  - `"license-manager:CreateGrantVersion"`
  - `"license-manager:DeleteGrant"`
  - `"license-manager:AcceptGrant"`

- Resources:

      + All resources (`"*"`)

  You must configure permissions to allow an IAM entity (such as a user, group, or
  role) to create, edit, or delete a service-linked role. For more information, see
  [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the _IAM User
  Guide_.
