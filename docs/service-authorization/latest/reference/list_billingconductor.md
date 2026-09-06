

# Actions, resources, and condition keys for AWS Billing Conductor
<a name="list_billingconductor"></a>

AWS Billing Conductor (service prefix: `billingconductor`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/billingconductor/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/billingconductor/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/billingconductor/latest/userguide/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/billingconductor/billingconductor.json) for this service.

**Topics**
+ [API operations defined by AWS Billing Conductor](#list_billingconductor-operations)
+ [Actions defined by AWS Billing Conductor](#list_billingconductor-actions-as-permissions)
+ [Resource types defined by AWS Billing Conductor](#list_billingconductor-resources-for-iam-policies)
+ [Condition keys for AWS Billing Conductor](#list_billingconductor-policy-keys)

## API operations defined by AWS Billing Conductor
<a name="list_billingconductor-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_billingconductor-actions-as-permissions).




- **   AssociateAccounts  **
  - **IAM action:**  [billingconductor:AssociateAccounts](#list_billingconductor-action-AssociateAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociatePricingRules  **
  - **IAM action:**  [billingconductor:AssociatePricingRules](#list_billingconductor-action-AssociatePricingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateResourcesToCustomLineItem  **
  - **IAM action:**  [billingconductor:BatchAssociateResourcesToCustomLineItem](#list_billingconductor-action-BatchAssociateResourcesToCustomLineItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateResourcesFromCustomLineItem  **
  - **IAM action:**  [billingconductor:BatchDisassociateResourcesFromCustomLineItem](#list_billingconductor-action-BatchDisassociateResourcesFromCustomLineItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBillingGroup  **
  - **IAM action:**  [billingconductor:CreateBillingGroup](#list_billingconductor-action-CreateBillingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billingconductor:TagResource](#list_billingconductor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomLineItem  **
  - **IAM action:**  [billingconductor:CreateCustomLineItem](#list_billingconductor-action-CreateCustomLineItem)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billingconductor:TagResource](#list_billingconductor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePricingPlan  **
  - **IAM action:**  [billingconductor:CreatePricingPlan](#list_billingconductor-action-CreatePricingPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billingconductor:TagResource](#list_billingconductor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePricingRule  **
  - **IAM action:**  [billingconductor:CreatePricingRule](#list_billingconductor-action-CreatePricingRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [billingconductor:TagResource](#list_billingconductor-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteBillingGroup  **
  - **IAM action:**  [billingconductor:DeleteBillingGroup](#list_billingconductor-action-DeleteBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomLineItem  **
  - **IAM action:**  [billingconductor:DeleteCustomLineItem](#list_billingconductor-action-DeleteCustomLineItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePricingPlan  **
  - **IAM action:**  [billingconductor:DeletePricingPlan](#list_billingconductor-action-DeletePricingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePricingRule  **
  - **IAM action:**  [billingconductor:DeletePricingRule](#list_billingconductor-action-DeletePricingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAccounts  **
  - **IAM action:**  [billingconductor:DisassociateAccounts](#list_billingconductor-action-DisassociateAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociatePricingRules  **
  - **IAM action:**  [billingconductor:DisassociatePricingRules](#list_billingconductor-action-DisassociatePricingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBillingGroupCostReport  **
  - **IAM action:**  [billingconductor:GetBillingGroupCostReport](#list_billingconductor-action-GetBillingGroupCostReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountAssociations  **
  - **IAM action:**  [billingconductor:ListAccountAssociations](#list_billingconductor-action-ListAccountAssociations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [organizations:ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListBillingGroupCostReports  **
  - **IAM action:**  [billingconductor:ListBillingGroupCostReports](#list_billingconductor-action-ListBillingGroupCostReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBillingGroups  **
  - **IAM action:**  [billingconductor:ListBillingGroups](#list_billingconductor-action-ListBillingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCustomLineItemVersions  **
  - **IAM action:**  [billingconductor:ListCustomLineItemVersions](#list_billingconductor-action-ListCustomLineItemVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCustomLineItems  **
  - **IAM action:**  [billingconductor:ListCustomLineItems](#list_billingconductor-action-ListCustomLineItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPricingPlans  **
  - **IAM action:**  [billingconductor:ListPricingPlans](#list_billingconductor-action-ListPricingPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPricingPlansAssociatedWithPricingRule  **
  - **IAM action:**  [billingconductor:ListPricingPlansAssociatedWithPricingRule](#list_billingconductor-action-ListPricingPlansAssociatedWithPricingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPricingRules  **
  - **IAM action:**  [billingconductor:ListPricingRules](#list_billingconductor-action-ListPricingRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPricingRulesAssociatedToPricingPlan  **
  - **IAM action:**  [billingconductor:ListPricingRulesAssociatedToPricingPlan](#list_billingconductor-action-ListPricingRulesAssociatedToPricingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourcesAssociatedToCustomLineItem  **
  - **IAM action:**  [billingconductor:ListResourcesAssociatedToCustomLineItem](#list_billingconductor-action-ListResourcesAssociatedToCustomLineItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [billingconductor:ListTagsForResource](#list_billingconductor-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [billingconductor:TagResource](#list_billingconductor-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [billingconductor:UntagResource](#list_billingconductor-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateBillingGroup  **
  - **IAM action:**  [billingconductor:UpdateBillingGroup](#list_billingconductor-action-UpdateBillingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomLineItem  **
  - **IAM action:**  [billingconductor:UpdateCustomLineItem](#list_billingconductor-action-UpdateCustomLineItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePricingPlan  **
  - **IAM action:**  [billingconductor:UpdatePricingPlan](#list_billingconductor-action-UpdatePricingPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePricingRule  **
  - **IAM action:**  [billingconductor:UpdatePricingRule](#list_billingconductor-action-UpdatePricingRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Billing Conductor
<a name="list_billingconductor-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAccounts](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateAccounts.html)  **
  - **Description:** Grants permission to associate between one and 30 accounts to a billing group
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociatePricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociatePricingRules.html)  **
  - **Description:** Grants permission to associate pricing rules
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateResourcesToCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchAssociateResourcesToCustomLineItem.html)  **
  - **Description:** Grants permission to batch associate resources to a percentage custom line item
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateResourcesFromCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BatchDisassociateResourcesFromCustomLineItem.html)  **
  - **Description:** Grants permission to batch disassociate resources from a percentage custom line item
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateBillingGroup.html)  **
  - **Description:** Grants permission to create a billing group
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreateCustomLineItem.html)  **
  - **Description:** Grants permission to create a custom line item
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingPlan.html)  **
  - **Description:** Grants permission to create a pricing plan
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_CreatePricingRule.html)  **
  - **Description:** Grants permission to create a pricing rule
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeleteBillingGroup.html)  **
  - **Description:** Grants permission to delete a billing group
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeleteCustomLineItem.html)  **
  - **Description:** Grants permission to delete a custom line item
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeletePricingPlan.html)  **
  - **Description:** Grants permission to delete a pricing plan
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DeletePricingRule.html)  **
  - **Description:** Grants permission to delete a pricing rule
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAccounts](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociateAccounts.html)  **
  - **Description:** Grants permission to detach between one and 30 accounts from a billing group
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociatePricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociatePricingRules.html)  **
  - **Description:** Grants permission to disassociate pricing rules
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBillingGroupCostReport](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_GetBillingGroupCostReport.html)  **
  - **Description:** Grants permission to view the billing group cost report for the specified billing group
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAccountAssociations](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListAccountAssociations.html)  **
  - **Description:** Grants permission to list the linked accounts of the payer account for the given billing period while also providing the billing group the linked accounts belong to
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBillingGroupCostReports](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroupCostReports.html)  **
  - **Description:** Grants permission to view the billing group cost report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListBillingGroups](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListBillingGroups.html)  **
  - **Description:** Grants permission to view the details of billing groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListCustomLineItemVersions](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItemVersions.html)  **
  - **Description:** Grants permission to view custom line item versions
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCustomLineItems](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListCustomLineItems.html)  **
  - **Description:** Grants permission to view custom line item details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPricingPlans](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlans.html)  **
  - **Description:** Grants permission to view the pricing plans details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPricingPlansAssociatedWithPricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingPlansAssociatedWithPricingRule.html)  **
  - **Description:** Grants permission to list pricing plans associated with a pricing rule
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPricingRules](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRules.html)  **
  - **Description:** Grants permission to view pricing rules details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPricingRulesAssociatedToPricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListPricingRulesAssociatedToPricingPlan.html)  **
  - **Description:** Grants permission to list pricing rules associated to a pricing plan
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourcesAssociatedToCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItem.html)  **
  - **Description:** Grants permission to list resources associated to a percentage custom line item
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags of a resource
  - **Resource types (\*required):** [billinggroup](#list_billingconductor-resource-billinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [customlineitem](#list_billingconductor-resource-customlineitem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingplan](#list_billingconductor-resource-pricingplan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingrule](#list_billingconductor-resource-pricingrule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [billinggroup](#list_billingconductor-resource-billinggroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [customlineitem](#list_billingconductor-resource-customlineitem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingplan](#list_billingconductor-resource-pricingplan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingrule](#list_billingconductor-resource-pricingrule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_billingconductor-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [billinggroup](#list_billingconductor-resource-billinggroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [customlineitem](#list_billingconductor-resource-customlineitem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingplan](#list_billingconductor-resource-pricingplan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Resource types (\*required):** [pricingrule](#list_billingconductor-resource-pricingrule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_billingconductor-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBillingGroup](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateBillingGroup.html)  **
  - **Description:** Grants permission to update a billing group
  - **Resource types (\*required):** [billinggroup\*](#list_billingconductor-resource-billinggroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomLineItem](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdateCustomLineItem.html)  **
  - **Description:** Grants permission to update a custom line item
  - **Resource types (\*required):** [customlineitem\*](#list_billingconductor-resource-customlineitem)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePricingPlan](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdatePricingPlan.html)  **
  - **Description:** Grants permission to update a pricing plan
  - **Resource types (\*required):** [pricingplan\*](#list_billingconductor-resource-pricingplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePricingRule](https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_UpdatePricingRule.html)  **
  - **Description:** Grants permission to update a pricing rule
  - **Resource types (\*required):** [pricingrule\*](#list_billingconductor-resource-pricingrule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Billing Conductor
<a name="list_billingconductor-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [billinggroup](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html)  | arn:${Partition}:billingconductor::${Account}:billinggroup/${BillingGroupId} | [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_) | 
|  [customlineitem](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html)  | arn:${Partition}:billingconductor::${Account}:customlineitem/${CustomLineItemId} | [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_) | 
|  [pricingplan](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html)  | arn:${Partition}:billingconductor::${Account}:pricingplan/${PricingPlanId} | [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_) | 
|  [pricingrule](https://docs.aws.amazon.com/billingconductor/latest/userguide/understanding-abc.html)  | arn:${Partition}:billingconductor::${Account}:pricingrule/${PricingRuleId} | [aws:ResourceTag/${TagKey}](#list_billingconductor-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Billing Conductor
<a name="list_billingconductor-policy-keys"></a>

AWS Billing Conductor defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 