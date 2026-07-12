# Actions, resources, and condition keys for AWS Tax Settings

AWS Tax Settings (service prefix: `tax`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- View a list of the [API operations available for
  this service](../../../awsaccountbilling/latest/aboutv2/api-reference.md "../../../awsaccountbilling/latest/aboutv2/api-reference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2/control-access-billing.md "../../../awsaccountbilling/latest/aboutv2/control-access-billing.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/tax/tax.json "https://servicereference.us-east-1.amazonaws.com/v1/tax/tax.json") for this service.

###### Topics

- [API operations defined by AWS Tax Settings](#list_taxsettings-operations "#list_taxsettings-operations")
- [Actions defined by AWS Tax Settings](#list_taxsettings-actions-as-permissions "#list_taxsettings-actions-as-permissions")
- [Permission-only actions for AWS Tax Settings](#list_taxsettings-permission-only-actions "#list_taxsettings-permission-only-actions")
- [Resource types defined by AWS Tax Settings](#list_taxsettings-resources-for-iam-policies "#list_taxsettings-resources-for-iam-policies")
- [Condition keys for AWS Tax Settings](#list_taxsettings-policy-keys "#list_taxsettings-policy-keys")

## API operations defined by AWS Tax Settings

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_taxsettings-actions-as-permissions "#list_taxsettings-actions-as-permissions").

| Operation                         | IAM action                                                                                                                                                       | Condition key | Possible value(s) | Access level |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| BatchDeleteTaxRegistration        | [tax:BatchDeleteTaxRegistration](#list_taxsettings-action-BatchDeleteTaxRegistration "#list_taxsettings-action-BatchDeleteTaxRegistration")                      |               |                   | Write        |
| BatchGetTaxExemptions             | [tax:GetExemptions](#list_taxsettings-action-GetExemptions "#list_taxsettings-action-GetExemptions")                                                             |               |                   | Read         |
| BatchPutTaxRegistration           | [tax:BatchPutTaxRegistration](#list_taxsettings-action-BatchPutTaxRegistration "#list_taxsettings-action-BatchPutTaxRegistration")                               |               |                   | Write        |
| DeleteSupplementalTaxRegistration | [tax:DeleteSupplementalTaxRegistration](#list_taxsettings-action-DeleteSupplementalTaxRegistration "#list_taxsettings-action-DeleteSupplementalTaxRegistration") |               |                   | Write        |
| DeleteTaxRegistration             | [tax:DeleteTaxRegistration](#list_taxsettings-action-DeleteTaxRegistration "#list_taxsettings-action-DeleteTaxRegistration")                                     |               |                   | Write        |
| GetTaxExemptionTypes              | [tax:GetExemptions](#list_taxsettings-action-GetExemptions "#list_taxsettings-action-GetExemptions")                                                             |               |                   | Read         |
| GetTaxInheritance                 | [tax:GetTaxInheritance](#list_taxsettings-action-GetTaxInheritance "#list_taxsettings-action-GetTaxInheritance")                                                 |               |                   | Read         |
| GetTaxRegistration                | [tax:GetTaxRegistration](#list_taxsettings-action-GetTaxRegistration "#list_taxsettings-action-GetTaxRegistration")                                              |               |                   | Read         |
| GetTaxRegistrationDocument        | [tax:GetTaxRegistrationDocument](#list_taxsettings-action-GetTaxRegistrationDocument "#list_taxsettings-action-GetTaxRegistrationDocument")                      |               |                   | Read         |
| ListSupplementalTaxRegistrations  | [tax:ListSupplementalTaxRegistrations](#list_taxsettings-action-ListSupplementalTaxRegistrations "#list_taxsettings-action-ListSupplementalTaxRegistrations")    |               |                   | Read         |
| ListTaxExemptions                 | [tax:GetExemptions](#list_taxsettings-action-GetExemptions "#list_taxsettings-action-GetExemptions")                                                             |               |                   | Read         |
| ListTaxRegistrations              | [tax:ListTaxRegistrations](#list_taxsettings-action-ListTaxRegistrations "#list_taxsettings-action-ListTaxRegistrations")                                        |               |                   | Read         |
| PutSupplementalTaxRegistration    | [tax:PutSupplementalTaxRegistration](#list_taxsettings-action-PutSupplementalTaxRegistration "#list_taxsettings-action-PutSupplementalTaxRegistration")          |               |                   | Write        |
| PutTaxExemption                   | [tax:UpdateExemptions](#list_taxsettings-action-UpdateExemptions "#list_taxsettings-action-UpdateExemptions")                                                    |               |                   | Write        |
| PutTaxInheritance                 | [tax:PutTaxInheritance](#list_taxsettings-action-PutTaxInheritance "#list_taxsettings-action-PutTaxInheritance")                                                 |               |                   | Write        |
| PutTaxRegistration                | [tax:PutTaxRegistration](#list_taxsettings-action-PutTaxRegistration "#list_taxsettings-action-PutTaxRegistration")                                              |               |                   | Write        |

## Actions defined by AWS Tax Settings

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                | Description                                                         | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [BatchDeleteTaxRegistration](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                              | Grants permission to batch delete tax registration data             |                             |                | Write        |
| [BatchPutTaxRegistration](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                 | Grants permission to batch update tax registrations                 |                             |                | Write        |
| [CancelDocument](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                          | Grants permission to cancel documents such as withholding slips     |                             |                | Write        |
| [CreateDocument](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                          | Grants permission to upload new documents such as withholding slips |                             |                | Write        |
| [DeleteSupplementalTaxRegistration](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md") | Grants permission to delete supplemental tax registration data      |                             |                | Write        |
| [DeleteTaxRegistration](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                   | Grants permission to delete tax registration data                   |                             |                | Write        |
| [GetDocument](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                             | Grants permission to retrieve documents such as withholding slips   |                             |                | Read         |
| [GetDocumentUploadUrl](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                    | Grants permission to retrieve a generated URL to upload documents   |                             |                | Read         |
| [GetExemptions](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                           | Grants permission to view tax exemptions data                       |                             |                | Read         |
| [GetTaxInheritance](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                       | Grants permission to view tax inheritance status                    |                             |                | Read         |
| [GetTaxRegistration](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md")                | Grants permission to view tax registrations data                    |                             |                | Read         |
| [GetTaxRegistrationDocument](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                              | Grants permission to download tax registration documents            |                             |                | Read         |
| [ListDocuments](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                           | Grants permission to view documents such as withholding slips       |                             |                | Read         |
| [ListSupplementalTaxRegistrations](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md")  | Grants permission to view supplemental tax registrations            |                             |                | Read         |
| [ListTaxRegistrations](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                    | Grants permission to view tax registrations                         |                             |                | Read         |
| [ListWithholdingEligibleInvoices](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                         | Grants permission to view eligible withholding invoices             |                             |                | Read         |
| [PutSupplementalTaxRegistration](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md")    | Grants permission to update supplemental tax registrations data     |                             |                | Write        |
| [PutTaxInheritance](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                       | Grants permission to set tax inheritance                            |                             |                | Write        |
| [PutTaxRegistration](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md")                | Grants permission to update tax registrations data                  |                             |                | Write        |
| [UpdateExemptions](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")                                        | Grants permission to update tax exemptions data                     |                             |                | Write        |

## Permission-only actions for AWS Tax Settings

The following actions are defined by AWS Tax Settings but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                              | Description                                            | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ | --------------------------- | -------------- | ------------ |
| [GetTaxInfoReportingDocument](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")           | Grants permission to view/download tax documents/forms |                             |                | Read         |
| [GetTaxInterview](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md") | Grants permission to retrieve tax interview data       |                             |                | Read         |
| [PutTaxInterview](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md") | Grants permission to update tax interview data         |                             |                | Write        |

## Resource types defined by AWS Tax Settings

AWS Tax Settings does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Tax Settings

AWS Tax Settings has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
