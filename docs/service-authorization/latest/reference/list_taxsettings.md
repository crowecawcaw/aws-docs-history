

# Actions, resources, and condition keys for AWS Tax Settings
<a name="list_taxsettings"></a>

AWS Tax Settings (service prefix: `tax`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/control-access-billing.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/tax/tax.json) for this service.

**Topics**
+ [API operations defined by AWS Tax Settings](#list_taxsettings-operations)
+ [Actions defined by AWS Tax Settings](#list_taxsettings-actions-as-permissions)
+ [Permission-only actions for AWS Tax Settings](#list_taxsettings-permission-only-actions)
+ [Resource types defined by AWS Tax Settings](#list_taxsettings-resources-for-iam-policies)
+ [Condition keys for AWS Tax Settings](#list_taxsettings-policy-keys)

## API operations defined by AWS Tax Settings
<a name="list_taxsettings-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_taxsettings-actions-as-permissions).




- **   BatchDeleteTaxRegistration  **
  - **IAM action:**  [tax:BatchDeleteTaxRegistration](#list_taxsettings-action-BatchDeleteTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetTaxExemptions  **
  - **IAM action:**  [tax:GetExemptions](#list_taxsettings-action-GetExemptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutTaxRegistration  **
  - **IAM action:**  [tax:BatchPutTaxRegistration](#list_taxsettings-action-BatchPutTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSupplementalTaxRegistration  **
  - **IAM action:**  [tax:DeleteSupplementalTaxRegistration](#list_taxsettings-action-DeleteSupplementalTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTaxRegistration  **
  - **IAM action:**  [tax:DeleteTaxRegistration](#list_taxsettings-action-DeleteTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetTaxExemptionTypes  **
  - **IAM action:**  [tax:GetExemptions](#list_taxsettings-action-GetExemptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTaxInheritance  **
  - **IAM action:**  [tax:GetTaxInheritance](#list_taxsettings-action-GetTaxInheritance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTaxRegistration  **
  - **IAM action:**  [tax:GetTaxRegistration](#list_taxsettings-action-GetTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTaxRegistrationDocument  **
  - **IAM action:**  [tax:GetTaxRegistrationDocument](#list_taxsettings-action-GetTaxRegistrationDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSupplementalTaxRegistrations  **
  - **IAM action:**  [tax:ListSupplementalTaxRegistrations](#list_taxsettings-action-ListSupplementalTaxRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTaxExemptions  **
  - **IAM action:**  [tax:GetExemptions](#list_taxsettings-action-GetExemptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTaxRegistrations  **
  - **IAM action:**  [tax:ListTaxRegistrations](#list_taxsettings-action-ListTaxRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutSupplementalTaxRegistration  **
  - **IAM action:**  [tax:PutSupplementalTaxRegistration](#list_taxsettings-action-PutSupplementalTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTaxExemption  **
  - **IAM action:**  [tax:UpdateExemptions](#list_taxsettings-action-UpdateExemptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTaxInheritance  **
  - **IAM action:**  [tax:PutTaxInheritance](#list_taxsettings-action-PutTaxInheritance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutTaxRegistration  **
  - **IAM action:**  [tax:PutTaxRegistration](#list_taxsettings-action-PutTaxRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Tax Settings
<a name="list_taxsettings-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [BatchDeleteTaxRegistration](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to batch delete tax registration data |  |   | Write | 
|   [BatchPutTaxRegistration](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to batch update tax registrations |  |   | Write | 
|   [CancelDocument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to cancel documents such as withholding slips |  |   | Write | 
|   [CreateDocument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to upload new documents such as withholding slips |  |   | Write | 
|   [DeleteSupplementalTaxRegistration](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to delete supplemental tax registration data |  |   | Write | 
|   [DeleteTaxRegistration](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to delete tax registration data |  |   | Write | 
|   [GetDocument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to retrieve documents such as withholding slips |  |   | Read | 
|   [GetDocumentUploadUrl](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to retrieve a generated URL to upload documents |  |   | Read | 
|   [GetExemptions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view tax exemptions data |  |   | Read | 
|   [GetTaxInheritance](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view tax inheritance status |  |   | Read | 
|   [GetTaxRegistration](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to view tax registrations data |  |   | Read | 
|   [GetTaxRegistrationDocument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to download tax registration documents |  |   | Read | 
|   [ListDocuments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view documents such as withholding slips |  |   | Read | 
|   [ListSupplementalTaxRegistrations](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to view supplemental tax registrations |  |   | Read | 
|   [ListTaxRegistrations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view tax registrations |  |   | Read | 
|   [ListWithholdingEligibleInvoices](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view eligible withholding invoices |  |   | Read | 
|   [PutSupplementalTaxRegistration](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to update supplemental tax registrations data |  |   | Write | 
|   [PutTaxInheritance](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to set tax inheritance |  |   | Write | 
|   [PutTaxRegistration](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to update tax registrations data |  |   | Write | 
|   [UpdateExemptions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to update tax exemptions data |  |   | Write | 

## Permission-only actions for AWS Tax Settings
<a name="list_taxsettings-permission-only-actions"></a>

The following actions are defined by AWS Tax Settings but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetTaxInfoReportingDocument](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html)  | Grants permission to view/download tax documents/forms |  |   | Read | 
|   [GetTaxInterview](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to retrieve tax interview data |  |   | Read | 
|   [PutTaxInterview](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html)  | Grants permission to update tax interview data |  |   | Write | 

## Resource types defined by AWS Tax Settings
<a name="list_taxsettings-resources-for-iam-policies"></a>

AWS Tax Settings does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Tax Settings
<a name="list_taxsettings-policy-keys"></a>

AWS Tax Settings has no service-specific condition keys that can be used in the `Condition` element of policy statements.