

# Actions, resources, and condition keys for AWS Invoicing Service
<a name="list_invoicing"></a>

AWS Invoicing Service (service prefix: `invoicing`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/invoicing/invoicing.json) for this service.

**Topics**
+ [API operations defined by AWS Invoicing Service](#list_invoicing-operations)
+ [Actions defined by AWS Invoicing Service](#list_invoicing-actions-as-permissions)
+ [Permission-only actions for AWS Invoicing Service](#list_invoicing-permission-only-actions)
+ [Resource types defined by AWS Invoicing Service](#list_invoicing-resources-for-iam-policies)
+ [Condition keys for AWS Invoicing Service](#list_invoicing-policy-keys)

## API operations defined by AWS Invoicing Service
<a name="list_invoicing-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_invoicing-actions-as-permissions).




- **   BatchGetInvoiceProfile  **
  - **IAM action:**  [invoicing:BatchGetInvoiceProfile](#list_invoicing-action-BatchGetInvoiceProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateInvoiceUnit  **
  - **IAM action:**  [invoicing:CreateInvoiceUnit](#list_invoicing-action-CreateInvoiceUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [invoicing:TagResource](#list_invoicing-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateProcurementPortalPreference  **
  - **IAM action:**  [invoicing:CreateProcurementPortalPreference](#list_invoicing-action-CreateProcurementPortalPreference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [invoicing:TagResource](#list_invoicing-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteInvoiceUnit  **
  - **IAM action:**  [invoicing:DeleteInvoiceUnit](#list_invoicing-action-DeleteInvoiceUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DeleteProcurementPortalPreference  **
  - **IAM action:**  [invoicing:DeleteProcurementPortalPreference](#list_invoicing-action-DeleteProcurementPortalPreference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetInvoicePDF  **
  - **IAM action:**  [invoicing:GetInvoicePDF](#list_invoicing-action-GetInvoicePDF)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetInvoiceUnit  **
  - **IAM action:**  [invoicing:GetInvoiceUnit](#list_invoicing-action-GetInvoiceUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetProcurementPortalPreference  **
  - **IAM action:**  [invoicing:GetProcurementPortalPreference](#list_invoicing-action-GetProcurementPortalPreference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListInvoiceSummaries  **
  - **IAM action:**  [invoicing:ListInvoiceSummaries](#list_invoicing-action-ListInvoiceSummaries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListInvoiceUnits  **
  - **IAM action:**  [invoicing:ListInvoiceUnits](#list_invoicing-action-ListInvoiceUnits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListProcurementPortalPreferences  **
  - **IAM action:**  [invoicing:ListProcurementPortalPreferences](#list_invoicing-action-ListProcurementPortalPreferences)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [invoicing:ListTagsForResource](#list_invoicing-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   PutProcurementPortalPreference  **
  - **IAM action:**  [invoicing:PutProcurementPortalPreference](#list_invoicing-action-PutProcurementPortalPreference)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   SendProcurementPortalValidation  **
  - **IAM action:**  [invoicing:SendProcurementPortalValidation](#list_invoicing-action-SendProcurementPortalValidation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [invoicing:TagResource](#list_invoicing-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [invoicing:UntagResource](#list_invoicing-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateInvoiceUnit  **
  - **IAM action:**  [invoicing:UpdateInvoiceUnit](#list_invoicing-action-UpdateInvoiceUnit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   UpdateProcurementPortalPreferenceStatus  **
  - **IAM action:**  [invoicing:UpdateProcurementPortalPreferenceStatus](#list_invoicing-action-UpdateProcurementPortalPreferenceStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   VerifyProcurementPortalValidation  **
  - **IAM action:**  [invoicing:VerifyProcurementPortalValidation](#list_invoicing-action-VerifyProcurementPortalValidation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Invoicing Service
<a name="list_invoicing-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetInvoiceProfile](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_BatchGetInvoiceProfile.html)  **
  - **Description:** Grants permission to get invoice profile details for an account in your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateInvoiceUnit.html)  **
  - **Description:** Grants permission to create an invoice unit for your organization
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_invoicing-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_invoicing-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateProcurementPortalPreference.html)  **
  - **Description:** Grants permission to create a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DeleteInvoiceUnit.html)  **
  - **Description:** Grants permission to update an invoice unit for your organization
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DeleteProcurementPortalPreference.html)  **
  - **Description:** Grants permission to delete a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetInvoicePDF](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoicePDF.html)  **
  - **Description:** Grants permission to get downloadable Invoice document pre-signed URL with supplemental documents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoiceUnit.html)  **
  - **Description:** Grants permission to get invoice units for your organization
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetProcurementPortalPreference.html)  **
  - **Description:** Grants permission to get a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListInvoiceSummaries](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceSummaries.html)  **
  - **Description:** Grants permission to get Invoice summary information for your account or linked account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListInvoiceUnits](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceUnits.html)  **
  - **Description:** Grants permission to list invoice units for your organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProcurementPortalPreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortalPreferences.html)  **
  - **Description:** Grants permission to list procurement portal preferences for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProcurementPortalSuppliers](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortalSuppliers.html)  **
  - **Description:** Grants permission to list suppliers for a procurement portal
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProcurementPortals](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortals.html)  **
  - **Description:** Grants permission to list procurement portals for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [procurement-portal-preference\*](#list_invoicing-resource-procurement-portal-preference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_PutProcurementPortalPreference.html)  **
  - **Description:** Grants permission to update a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendProcurementPortalValidation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_SendProcurementPortalValidation.html)  **
  - **Description:** Grants permission to send a one-time passcode (OTP) to validate a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_invoicing-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_invoicing-aws_TagKeys)
  - **Resource types (\*required):** [procurement-portal-preference\*](#list_invoicing-resource-procurement-portal-preference) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_invoicing-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_invoicing-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_invoicing-aws_TagKeys)
  - **Resource types (\*required):** [procurement-portal-preference\*](#list_invoicing-resource-procurement-portal-preference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_invoicing-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateInvoiceUnit.html)  **
  - **Description:** Grants permission to update an invoice unit for your organization
  - **Resource types (\*required):** [invoice-unit\*](#list_invoicing-resource-invoice-unit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProcurementPortalPreferenceStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateProcurementPortalPreferenceStatus.html)  **
  - **Description:** Grants permission to update the status for a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyProcurementPortalValidation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_VerifyProcurementPortalValidation.html)  **
  - **Description:** Grants permission to verify the one-time passcode (OTP) to validate a procurement portal preference
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Invoicing Service
<a name="list_invoicing-permission-only-actions"></a>

The following actions are defined by AWS Invoicing Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetInvoiceCorrection](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoiceCorrection.html)  | Grants permission to get Invoice Correction |  |   | Read | 
|   [GetInvoiceEmailDeliveryPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  | Grants permission to get Invoice Email Delivery Preferences |  |   | Read | 
|   [ListInvoiceCorrections](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceCorrections.html)  | Grants permission to list Invoice Corrections |  |   | List | 
|   [PutInvoiceEmailDeliveryPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_id-based-policy-examples.html#billing-permissions-ref)  | Grants permission to put Invoice Email Delivery Preferences |  |   | Write | 
|   [StartInvoiceCorrection](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_StartInvoiceCorrection.html)  | Grants permission to start Invoice Correction |  |   | Write | 

## Resource types defined by AWS Invoicing Service
<a name="list_invoicing-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [invoice-unit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceUnit.html)  | arn:${Partition}:invoicing::${Account}:invoice-unit/${Identifier} | [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_) | 
|  [procurement-portal-preference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreference.html)  | arn:${Partition}:invoicing::${Account}:procurement-portal-preference/${Identifier} | [aws:ResourceTag/${TagKey}](#list_invoicing-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Invoicing Service
<a name="list_invoicing-policy-keys"></a>

AWS Invoicing Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of mandatory tags in the request | ArrayOfString | 