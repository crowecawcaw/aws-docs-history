# Provision and manage accounts in

AWS Control Tower

This chapter includes:

- an overview and procedures for provisioning and managing new member
  accounts in AWS Control Tower.
- an overview and procedures for enrolling an existing AWS account into
  AWS Control Tower.
  For general information about accounts in AWS Control Tower, see
  [About AWS accounts in AWS Control Tower](accounts.md "accounts.md"). For information about enrolling
  multiple acounts into AWS Control Tower, see [Register an existing organizational unit with
  AWS Control Tower](importing-existing.md "importing-existing.md").

###### Note

You can perform up to five (5) account-related operations concurrently, including
provisioning, updating, and enrolling.

## Permissions required for provisioning accounts

With the appropriate user group permissions,
provisioners can specify standardized baselines and network configurations for any
accounts in their organization.

When you create accounts from the AWS Control Tower console with Account Factory, you must be signed
into an account with an IAM user that has the
`AWSServiceCatalogEndUserFullAccess` policy enabled, along with
permissions to use the AWS Control Tower console, and you cannot be signed in as the
**Root** user.

###### Note

When provisioning an account, the account requester always must have the
`CreateAccount` and the `DescribeCreateAccountStatus`
permissions. This permission set is part of the **Admin** role, and it is given
automatically when a requester assumes the **Admin** role. If you delegate permission to
provision accounts, you may need to add these permissions directly for the account
requestors.

For general information about permissions required in AWS Control Tower, see [Using identity-based policies (IAM
policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md"). For information about roles
and accounts in AWS Control Tower, see [Roles and accounts](roles.md "roles.md").
