

# Actions, resources, and condition keys for AWS Billing
<a name="list_billing"></a>

AWS Billing (service prefix: `billing`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Billing.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/billing/billing.json) for this service.

**Topics**
+ [API operations defined by AWS Billing](#list_billing-operations)
+ [Actions defined by AWS Billing](#list_billing-actions-as-permissions)
+ [Permission-only actions for AWS Billing](#list_billing-permission-only-actions)
+ [Resource types defined by AWS Billing](#list_billing-resources-for-iam-policies)
+ [Condition keys for AWS Billing](#list_billing-policy-keys)

## API operations defined by AWS Billing
<a name="list_billing-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_billing-actions-as-permissions).




- **   AssociateSourceViews  **
  - **IAM action:**  [billing:AssociateSourceViews](#list_billing-action-AssociateSourceViews)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billing:UseSourceView](#list_billing-action-UseSourceView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateBillingView  **
  - **IAM action:**  [billing:CreateBillingView](#list_billing-action-CreateBillingView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billing:TagResource](#list_billing-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [billing:UseSourceView](#list_billing-action-UseSourceView)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DeleteBillingView  **
  - **IAM action:**  [billing:DeleteBillingView](#list_billing-action-DeleteBillingView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateSourceViews  **
  - **IAM action:**  [billing:DisassociateSourceViews](#list_billing-action-DisassociateSourceViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBillingPreferences  **
  - **IAM action:**  [billing:GetBillingPreferences](#list_billing-action-GetBillingPreferences)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetBillingView  **
  - **IAM action:**  [billing:GetBillingView](#list_billing-action-GetBillingView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCreditAllocationHistory  **
  - **IAM action:**  [billing:GetCreditAllocationHistory](#list_billing-action-GetCreditAllocationHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCredits  **
  - **IAM action:**  [billing:GetCredits](#list_billing-action-GetCredits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   GetEnterpriseSupportChargeSummary  **
  - **IAM action:**  [billing:GetEnterpriseSupportChargeSummary](#list_billing-action-GetEnterpriseSupportChargeSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnterpriseSupportContractDetails  **
  - **IAM action:**  [billing:GetEnterpriseSupportContractDetails](#list_billing-action-GetEnterpriseSupportContractDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [billing:GetResourcePolicy](#list_billing-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   ListBillingViews  **
  - **IAM action:**  [billing:ListBillingViews](#list_billing-action-ListBillingViews) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEnterpriseSupportLinkedAccountCharges  **
  - **IAM action:**  [billing:ListEnterpriseSupportLinkedAccountCharges](#list_billing-action-ListEnterpriseSupportLinkedAccountCharges) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSourceViewsForBillingView  **
  - **IAM action:**  [billing:ListSourceViewsForBillingView](#list_billing-action-ListSourceViewsForBillingView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [billing:ListTagsForResource](#list_billing-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RedeemCredits  **
  - **IAM action:**  [billing:RedeemCredits](#list_billing-action-RedeemCredits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [billing:TagResource](#list_billing-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [billing:UntagResource](#list_billing-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBillingPreferences  **
  - **IAM action:**  [billing:UpdateBillingPreferences](#list_billing-action-UpdateBillingPreferences)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateBillingView  **
  - **IAM action:**  [billing:UpdateBillingView](#list_billing-action-UpdateBillingView) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Billing
<a name="list_billing-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateSourceViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AssociateSourceViews.html)  **
  - **Description:** Grants permission to associate source views to a billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreateBillingView.html)  **
  - **Description:** Grants permission to create a billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billing-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billing-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DeleteBillingView.html)  **
  - **Description:** Grants permission to delete a billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateSourceViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DisassociateSourceViews.html)  **
  - **Description:** Grants permission to disassociate source views from a billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBillingPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view billing preferences such as reserved instance, savings plans and credits sharing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetBillingView.html)  **
  - **Description:** Grants permission to get the metadata for a specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCreditAllocationHistory](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view a credit allocation history
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCredits](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view credits that have been redeemed
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnterpriseSupportChargeSummary](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view Enterprise Support charge summary data
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEnterpriseSupportContractDetails](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view Enterprise Support contract details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetResourcePolicy.html)  **
  - **Description:** Grants permission to get the resource policy specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [ListBillingViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBillingViews.html)  **
  - **Description:** Grants permission to get a list of all your available billing views
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEnterpriseSupportLinkedAccountCharges](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view Enterprise Support charges broken down by linked account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSourceViewsForBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListSourceViewsForBillingView.html)  **
  - **Description:** Grants permission to get the list of source views for a specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListTagsForResource.html)  **
  - **Description:** Grants permission to get the list of tags for a specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RedeemCredits](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to redeem an AWS credit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_TagResource.html)  **
  - **Description:** Grants permission to add tags to a specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billing-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billing-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a specified billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billing-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBillingPreferences](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to update billing preferences such as reserved instance, savings plans and credits sharing
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_UpdateBillingView.html)  **
  - **Description:** Grants permission to update a billing view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Billing
<a name="list_billing-permission-only-actions"></a>

The following actions are defined by AWS Billing but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to delete a billing view resource policy
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [GetBillingData](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to perform queries on billing information
  - **Resource types (\*required):** [billingview](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBillingDetails](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view detailed line item billing information
  - **Resource types (\*required):** [billingview](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBillingNotifications](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view notifications sent by AWS related to your accounts billing information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBillingViewData](https://docs.aws.amazon.com/)  **
  - **Description:** Grants permission to get cost and usage data for a specified billng view
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContractInformation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to view the account's contract information including the contract number, end-user organization names, PO numbers and if the account is used to service public-sector customers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIAMAccessPreference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to retrieve the state of the Allow IAM Access billing preference
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSellerOfRecord](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to retrieve the account's default Seller of Record
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutContractInformation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to set the account's contract information end-user organization names and if the account is used to service public-sector customers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_PutResourcePolicy.html)  **
  - **Description:** Grants permission to put a billing view resource policy
  - **Resource types (\*required):** [billingview\*](#list_billing-resource-billingview)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [UpdateIAMAccessPreference](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to update the Allow IAM Access billing preference
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UseSourceView](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  **
  - **Description:** Grants permission to use a billing view as a data source for other billing views
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS Billing
<a name="list_billing-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [billingview](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/)  | arn:${Partition}:billing::${Account}:billingview/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_billing-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Billing
<a name="list_billing-policy-keys"></a>

AWS Billing defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 