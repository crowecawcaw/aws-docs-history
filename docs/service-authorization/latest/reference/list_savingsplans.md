

# Actions, resources, and condition keys for AWS Savings Plans
<a name="list_savingsplans"></a>

AWS Savings Plans (service prefix: `savingsplans`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/savingsplans/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/savingsplans/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/savingsplans/latest/userguide/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/savingsplans/savingsplans.json) for this service.

**Topics**
+ [API operations defined by AWS Savings Plans](#list_savingsplans-operations)
+ [Actions defined by AWS Savings Plans](#list_savingsplans-actions-as-permissions)
+ [Resource types defined by AWS Savings Plans](#list_savingsplans-resources-for-iam-policies)
+ [Condition keys for AWS Savings Plans](#list_savingsplans-policy-keys)

## API operations defined by AWS Savings Plans
<a name="list_savingsplans-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_savingsplans-actions-as-permissions).




- **   CreateSavingsPlan  **
  - **IAM action:**  [savingsplans:CreateSavingsPlan](#list_savingsplans-action-CreateSavingsPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [savingsplans:TagResource](#list_savingsplans-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteQueuedSavingsPlan  **
  - **IAM action:**  [savingsplans:DeleteQueuedSavingsPlan](#list_savingsplans-action-DeleteQueuedSavingsPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeSavingsPlanRates  **
  - **IAM action:**  [savingsplans:DescribeSavingsPlanRates](#list_savingsplans-action-DescribeSavingsPlanRates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSavingsPlans  **
  - **IAM action:**  [savingsplans:DescribeSavingsPlans](#list_savingsplans-action-DescribeSavingsPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSavingsPlansOfferingRates  **
  - **IAM action:**  [savingsplans:DescribeSavingsPlansOfferingRates](#list_savingsplans-action-DescribeSavingsPlansOfferingRates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSavingsPlansOfferings  **
  - **IAM action:**  [savingsplans:DescribeSavingsPlansOfferings](#list_savingsplans-action-DescribeSavingsPlansOfferings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [savingsplans:ListTagsForResource](#list_savingsplans-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ReturnSavingsPlan  **
  - **IAM action:**  [savingsplans:ReturnSavingsPlan](#list_savingsplans-action-ReturnSavingsPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [savingsplans:TagResource](#list_savingsplans-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [savingsplans:UntagResource](#list_savingsplans-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Savings Plans
<a name="list_savingsplans-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSavingsPlan](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_CreateSavingsPlan.html)  **
  - **Description:** Grants permission to create a savings plan
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_savingsplans-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_savingsplans-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteQueuedSavingsPlan](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DeleteQueuedSavingsPlan.html)  **
  - **Description:** Grants permission to delete the queued savings plan associated with customers account
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeSavingsPlanRates](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlanRates.html)  **
  - **Description:** Grants permission to describe the rates associated with customers savings plan
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSavingsPlans](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlans.html)  **
  - **Description:** Grants permission to describe the savings plans associated with customers account
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSavingsPlansOfferingRates](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferingRates.html)  **
  - **Description:** Grants permission to describe the rates assciated with savings plans offerings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSavingsPlansOfferings](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_DescribeSavingsPlansOfferings.html)  **
  - **Description:** Grants permission to describe the savings plans offerings that customer is eligible to purchase
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a savings plan
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ReturnSavingsPlan](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_ReturnSavingsPlan.html)  **
  - **Description:** Grants permission to return a savings plan
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a savings plan
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_savingsplans-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_savingsplans-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/savingsplans/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a savings plan
  - **Resource types (\*required):** [savingsplan\*](#list_savingsplans-resource-savingsplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_savingsplans-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Savings Plans
<a name="list_savingsplans-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [savingsplan](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)  | arn:${Partition}:savingsplans::${Account}:savingsplan/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_savingsplans-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Savings Plans
<a name="list_savingsplans-policy-keys"></a>

AWS Savings Plans defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 