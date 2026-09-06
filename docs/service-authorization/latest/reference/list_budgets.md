

# Actions, resources, and condition keys for AWS Budget Service
<a name="list_budgets"></a>

AWS Budget Service (service prefix: `budgets`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Budgets.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/cost-management/latest/userguide/billing-permissions-ref.html#user-permissions) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/budgets/budgets.json) for this service.

**Topics**
+ [API operations defined by AWS Budget Service](#list_budgets-operations)
+ [Actions defined by AWS Budget Service](#list_budgets-actions-as-permissions)
+ [Resource types defined by AWS Budget Service](#list_budgets-resources-for-iam-policies)
+ [Condition keys for AWS Budget Service](#list_budgets-policy-keys)

## API operations defined by AWS Budget Service
<a name="list_budgets-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_budgets-actions-as-permissions).




- **   CreateBudget  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [budgets:TagResource](#list_budgets-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateBudgetAction  **
  - **IAM action:**  [budgets:CreateBudgetAction](#list_budgets-action-CreateBudgetAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [budgets:TagResource](#list_budgets-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** budgets.amazonaws.com / **Access level:** Write

- **   CreateNotification  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateSubscriber  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBudget  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteBudgetAction  **
  - **IAM action:**  [budgets:DeleteBudgetAction](#list_budgets-action-DeleteBudgetAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteNotification  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteSubscriber  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DescribeBudget  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetAction  **
  - **IAM action:**  [budgets:DescribeBudgetAction](#list_budgets-action-DescribeBudgetAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetActionHistories  **
  - **IAM action:**  [budgets:DescribeBudgetActionHistories](#list_budgets-action-DescribeBudgetActionHistories)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetActionsForAccount  **
  - **IAM action:**  [budgets:DescribeBudgetActionsForAccount](#list_budgets-action-DescribeBudgetActionsForAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetActionsForBudget  **
  - **IAM action:**  [budgets:DescribeBudgetActionsForBudget](#list_budgets-action-DescribeBudgetActionsForBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetNotificationsForAccount  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgetPerformanceHistory  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeBudgets  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeNotificationsForBudget  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeSubscribersForNotification  **
  - **IAM action:**  [budgets:ViewBudget](#list_budgets-action-ViewBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ExecuteBudgetAction  **
  - **IAM action:**  [budgets:ExecuteBudgetAction](#list_budgets-action-ExecuteBudgetAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   ListTagsForResource  **
  - **IAM action:**  [budgets:ListTagsForResource](#list_budgets-action-ListTagsForResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [aws-portal:ViewBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [budgets:TagResource](#list_budgets-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [budgets:UntagResource](#list_budgets-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateBudget  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateBudgetAction  **
  - **IAM action:**  [budgets:UpdateBudgetAction](#list_budgets-action-UpdateBudgetAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** budgets.amazonaws.com / **Access level:** Write

- **   UpdateNotification  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateSubscriber  **
  - **IAM action:**  [budgets:ModifyBudget](#list_budgets-action-ModifyBudget)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aws-portal:ModifyBilling](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-permissions-ref.html#user-permissions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS Budget Service
<a name="list_budgets-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudgetAction.html)  **
  - **Description:** Grants permission to configure a response that executes once your budget exceeds a specific budget threshold. Creating a budget action with tags also requires the 'budgets:TagResource' permission
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteBudgetAction.html)  **
  - **Description:** Grants permission to delete an action that is associated with a specific budget
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Write

- **   [DescribeBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetAction.html)  **
  - **Description:** Grants permission to retrieve the details of a specific budget action associated with a budget
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeBudgetActionHistories](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionHistories.html)  **
  - **Description:** Grants permission to retrieve a historical view of the budget actions statuses associated with a particular budget action. These status include statues such as 'Standby', 'Pending' and 'Executed'
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Read

- **   [DescribeBudgetActionsForAccount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionsForAccount.html)  **
  - **Description:** Grants permission to retrieve the details of all of the budget actions associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeBudgetActionsForBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionsForBudget.html)  **
  - **Description:** Grants permission to retrieve the details of all of the budget actions associated with a budget
  - **Resource types (\*required):** [budget\*](#list_budgets-resource-budget)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Read

- **   [ExecuteBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ExecuteBudgetAction.html)  **
  - **Description:** Grants permission to initiate a pending budget action as well as reverse a previously executed budget action
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Write

- **   [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ListTagsForResource.html)  **
  - **Description:** Grants permission to view resource tags for a budget or budget action
  - **Resource types (\*required):** [budget](#list_budgets-resource-budget) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Resource types (\*required):** [budgetAction](#list_budgets-resource-budgetAction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Read

- **   [ModifyBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Budgets.html)  **
  - **Description:** Grants permission to create and modify budgets, and edit budget details. Creating a budget with tags also requires the 'budgets:TagResource' permission
  - **Resource types (\*required):** [budget\*](#list_budgets-resource-budget)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TagResource.html)  **
  - **Description:** Grants permission to apply resource tags to a budget or budget action. Also needed to create a budget or budget action with tags
  - **Resource types (\*required):** [budget](#list_budgets-resource-budget) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Resource types (\*required):** [budgetAction](#list_budgets-resource-budgetAction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UntagResource.html)  **
  - **Description:** Grants permission to remove resource tags from a budget or budget action
  - **Resource types (\*required):** [budget](#list_budgets-resource-budget) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Resource types (\*required):** [budgetAction](#list_budgets-resource-budgetAction) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudgetAction.html)  **
  - **Description:** Grants permission to update the details of a specific budget action associated with a budget
  - **Resource types (\*required):** [budgetAction\*](#list_budgets-resource-budgetAction)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Write

- **   [ViewBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Operations_AWS_Budgets.html)  **
  - **Description:** Grants permission to view budgets and budget details
  - **Resource types (\*required):** [budget\*](#list_budgets-resource-budget)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys)
  - **Access level:** Read



## Resource types defined by AWS Budget Service
<a name="list_budgets-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)  | arn:${Partition}:budgets::${Account}:budget/${BudgetName} | [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys) | 
|  [budgetAction](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html)  | arn:${Partition}:budgets::${Account}:budget/${BudgetName}/action/${ActionId} | [aws:RequestTag/${TagKey}](#list_budgets-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_budgets-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_budgets-aws_TagKeys) | 

## Condition keys for AWS Budget Service
<a name="list_budgets-policy-keys"></a>

AWS Budget Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 