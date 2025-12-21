# Update an existing account

###### Auto Enroll Compatibility

If your organization uses Auto Enroll for automatic account enrollment, be aware that AFT has
limitations with importing these accounts. Accounts enrolled through Auto Enroll lack the
Service Catalog provisioned products required by AFT's import workflow.

**Workaround:** Use the Register OU feature to create provisioned products for automatically
enrolled accounts. This enables the necessary lifecycle events for AFT customizations.

You can update accounts that AFT provisions by editing previously submitted account
requests and running `git push`. This command invokes the account
provisioning workflow and can process account update requests. You can update the input
for `ManagedOrganizationalUnit`, which is part of the required value for
`control_tower_parameters`.

`ManagedOrganizationalUnit` is the only parameter that can be updated,
among all `control_tower_parameters`. However, other parameters that are part
of the account request Terraform file can be updated, such as
`custom_fields`. For more information, see [Provision a new
account with AFT](aft-provision-account.md "aft-provision-account.md").

For example, to update the name or email address of an AFT account, you can define the
specifics as `custom_fields` in the Account Request file. By doing so, you
create SSM parameters, which you can pass into the
`aws_account_alternate_contact` resource during global
customizations.

```
resource "aws_account_alternate_contact" "operations" {

  alternate_contact_type = "OPERATIONS"

  name          = "Example"
  title         = "Example"
  email_address = "someone@example.com"
  phone_number  = "+1234567890"
}
```

You can add similar fields for other contact types, such as operations and security.
In Global Customizations, add data lookups for each custom field, to ensure that you look up all the fields you created in Account Request:

```
data "aws_ssm_parameter" "billing_name" {
            name = "/aft/account-request/custom-fields/billing_name"
            }

            data "aws_ssm_parameter" "billing_title" {
            name = "/aft/account-request/custom-fields/billing_title"
            }

            data "aws_ssm_parameter" "billing_email_address" {
            name = "/aft/account-request/custom-fields/billing_email_address"
            }

            data "aws_ssm_parameter" "billing_phone_number" {
            name = "/aft/account-request/custom-fields/billing_phone_number"
            }
```

Finally, also in the Global Customizations file, create the alternate contact resources. You will need to define one of these blocks for every contact type you created in Account Request:

```
resource "aws_account_alternate_contact" "billing" {

            alternate_contact_type = "BILLING"

            name          = data.aws_ssm_parameter.billing_name.value
            title         = data.aws_ssm_parameter.billing_title.value
            email_address = data.aws_ssm_parameter.billing_email_address.value
            phone_number  = data.aws_ssm_parameter.billing_phone_number.value
            }
```

###### Note

The input that you provide for `control_tower_parameters` can't be
changed during account provisioning.

The supported formats for specifying `ManagedOrganizationalUnit` in
the **aft-account-request** repository include
`OUName` and `OUName (OU-ID)`.

## Update an account that AFT

doesn't provision

You can update AWS Control Tower accounts created outside of AFT by specifying the
account in the **aft-account-request** repository.

###### Note

Make sure that all account details are correct and consistent with the
AWS Control Tower organization and respective AWS Service Catalog provisioned product.

###### Prerequisites for updating an existing AWS account with AFT

- The AWS account must be enrolled in AWS Control Tower.
- The AWS account must be part of the AWS Control Tower organization.
