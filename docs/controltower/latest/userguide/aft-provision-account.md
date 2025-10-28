# Provision a new account with AFT

_This section assumes that you've already set up AFT and your AFT management
account, and you are provisioning additional accounts._

To provision a new account with AFT, create an account request Terraform file. This
file contains the input for parameters in the **aft-account-request** repository. After creating an account request
Terraform file, begin processing your account request by running `git push`.
This command invokes the `ct-aft-account-request` operation in the AWS CodePipeline,
which is created in the AFT management account after account provisioning finishes. For
more information, see [AFT account
provisioning pipeline](aft-provisioning-framework.md "aft-provisioning-framework.md").

## Account request Terraform file parameters

You must include the following parameters in your account request Terraform file.
You can view [an example account request Terraform file](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-request "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-request") on GitHub.

- The value of `module name` must be unique per the
  AWS account request.
- The value of `module source` is the path to the account
  request Terraform module that AFT provides.
- The value of `control_tower_parameters` captures the required
  input to create an AWS Control Tower account. The value includes the following input
  fields:
  - `AccountEmail`
  - `AccountName`
  - `ManagedOrganizationalUnit`
  - `SSOUserEmail`
  - `SSOUserFirstName`
  - `SSOUserLastName`

###### Note

The input that you provide for `control_tower_parameters` can't be
changed during the account provisioning.

The supported formats for specifying `ManagedOrganizationalUnit`
in the **aft-account-request** repository include
`OUName` and `OUName (OU-ID)`.

- `account_tags` captures user-defined keys and values, which can
  tag AWS accounts according to business criteria. For more information, see
  [Tagging AWS Organizations
  resources](../../../organizations/latest/userguide/orgs_tagging.md "../../../organizations/latest/userguide/orgs_tagging.md") in the _AWS Organizations User
  Guide_.
- The value of `change_management_parameters` captures
  additional information, such as why an account request was created and who
  initiated the account request. The value includes the following input
  fields:
  - `change_reason`
  - `change_requested_by`

- `custom_fields` captures additional metadata with keys and values
  that deploy as SSM parameters in the vended account under **/aft/account-request/custom-fields/**. You can
  reference this metadata during account customizations to deploy proper
  controls. For example, an account that's subject to regulatory compliance
  might deploy additional AWS Config Rules. The metadata that you collect with
  `custom_fields` can invoke additional processing during
  account provisioning and updating. If a custom field is removed from the
  account request, the custom field is removed from the SSM Parameter Store
  for the vended account.
- (Optional) `account_customizations_name` captures the account
  template folder in the **aft-account-customizations** repository. For more information,
  see [Account customizations](aft-account-customization-options.md "aft-account-customization-options.md").
