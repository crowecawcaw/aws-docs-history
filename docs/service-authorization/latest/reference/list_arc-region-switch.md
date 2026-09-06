

# Actions, resources, and condition keys for Amazon ARC Region switch
<a name="list_arc-region-switch"></a>

Amazon ARC Region switch (service prefix: `arc-region-switch`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/r53recovery/latest/dg/region-switch.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/arc-region-switch/latest/api/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/r53recovery/latest/dg/security-iam-region-switch.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/arc-region-switch/arc-region-switch.json) for this service.

**Topics**
+ [API operations defined by Amazon ARC Region switch](#list_arc-region-switch-operations)
+ [Actions defined by Amazon ARC Region switch](#list_arc-region-switch-actions-as-permissions)
+ [Permission-only actions for Amazon ARC Region switch](#list_arc-region-switch-permission-only-actions)
+ [Resource types defined by Amazon ARC Region switch](#list_arc-region-switch-resources-for-iam-policies)
+ [Condition keys for Amazon ARC Region switch](#list_arc-region-switch-policy-keys)

## API operations defined by Amazon ARC Region switch
<a name="list_arc-region-switch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_arc-region-switch-actions-as-permissions).




- **   ApprovePlanExecutionStep  **
  - **IAM action:**  [arc-region-switch:ApprovePlanExecutionStep](#list_arc-region-switch-action-ApprovePlanExecutionStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelPlanExecution  **
  - **IAM action:**  [arc-region-switch:CancelPlanExecution](#list_arc-region-switch-action-CancelPlanExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePlan  **
  - **IAM action:**  [arc-region-switch:CreatePlan](#list_arc-region-switch-action-CreatePlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [arc-region-switch:GetPlan](#list_arc-region-switch-action-GetPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [arc-region-switch:TagResource](#list_arc-region-switch-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** arc-region-switch.amazonaws.com / **Access level:** Write

- **   DeletePlan  **
  - **IAM action:**  [arc-region-switch:DeletePlan](#list_arc-region-switch-action-DeletePlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetPlan  **
  - **IAM action:**  [arc-region-switch:GetPlan](#list_arc-region-switch-action-GetPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlanEvaluationStatus  **
  - **IAM action:**  [arc-region-switch:GetPlanEvaluationStatus](#list_arc-region-switch-action-GetPlanEvaluationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlanExecution  **
  - **IAM action:**  [arc-region-switch:GetPlanExecution](#list_arc-region-switch-action-GetPlanExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlanInRegion  **
  - **IAM action:**  [arc-region-switch:GetPlanInRegion](#list_arc-region-switch-action-GetPlanInRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPlanExecutionEvents  **
  - **IAM action:**  [arc-region-switch:ListPlanExecutionEvents](#list_arc-region-switch-action-ListPlanExecutionEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlanExecutions  **
  - **IAM action:**  [arc-region-switch:ListPlanExecutions](#list_arc-region-switch-action-ListPlanExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlans  **
  - **IAM action:**  [arc-region-switch:ListPlans](#list_arc-region-switch-action-ListPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPlansInRegion  **
  - **IAM action:**  [arc-region-switch:ListPlansInRegion](#list_arc-region-switch-action-ListPlansInRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoute53HealthChecks  **
  - **IAM action:**  [arc-region-switch:ListRoute53HealthChecks](#list_arc-region-switch-action-ListRoute53HealthChecks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRoute53HealthChecksInRegion  **
  - **IAM action:**  [arc-region-switch:ListRoute53HealthChecksInRegion](#list_arc-region-switch-action-ListRoute53HealthChecksInRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [arc-region-switch:ListTagsForResource](#list_arc-region-switch-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartPlanExecution  **
  - **IAM action:**  [arc-region-switch:StartPlanExecution](#list_arc-region-switch-action-StartPlanExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [arc-region-switch:TagResource](#list_arc-region-switch-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [arc-region-switch:UntagResource](#list_arc-region-switch-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePlan  **
  - **IAM action:**  [arc-region-switch:GetPlan](#list_arc-region-switch-action-GetPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [arc-region-switch:UpdatePlan](#list_arc-region-switch-action-UpdatePlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** arc-region-switch.amazonaws.com / **Access level:** Write

- **   UpdatePlanExecution  **
  - **IAM action:**  [arc-region-switch:UpdatePlanExecution](#list_arc-region-switch-action-UpdatePlanExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePlanExecutionStep  **
  - **IAM action:**  [arc-region-switch:UpdatePlanExecutionStep](#list_arc-region-switch-action-UpdatePlanExecutionStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon ARC Region switch
<a name="list_arc-region-switch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ApprovePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ApprovePlanExecutionStep.html)  **
  - **Description:** Grants permission to approve a plan execution step
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CancelPlanExecution.html)  **
  - **Description:** Grants permission to cancel a plan execution
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CreatePlan.html)  **
  - **Description:** Grants permission to create a plan
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_arc-region-switch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_arc-region-switch-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DeletePlan.html)  **
  - **Description:** Grants permission to delete a plan
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlan.html)  **
  - **Description:** Grants permission to get information about plans in all AWS Regions using a control plane
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html)  **
  - **Description:** Grants permission to get a plan's evaluation status
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html)  **
  - **Description:** Grants permission to get plan execution details and setup information
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanInRegion.html)  **
  - **Description:** Grants permission to get information about a plan in a specific AWS Region using the Region switch Regional data plane
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPlanExecutionEvents](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutionEvents.html)  **
  - **Description:** Grants permission to list plan execution events
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPlanExecutions](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutions.html)  **
  - **Description:** Grants permission to list plan executions
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPlans](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlans.html)  **
  - **Description:** Grants permission to list plans in all AWS Regions using a control plane
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPlansInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlansInRegion.html)  **
  - **Description:** Grants permission to list plans in a specific AWS Region using the Region switch Regional data plane
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRoute53HealthChecks](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecks.html)  **
  - **Description:** Grants permission to list Route 53 health checks
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRoute53HealthChecksInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecksInRegion.html)  **
  - **Description:** Grants permission to list Route 53 health checks in a specific AWS Region using the Region switch Regional data plane
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StartPlanExecution.html)  **
  - **Description:** Grants permission to start a plan execution
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_arc-region-switch-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_arc-region-switch-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_arc-region-switch-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html)  **
  - **Description:** Grants permission to update a plan
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecution.html)  **
  - **Description:** Grants permission to update a plan execution
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecutionStep.html)  **
  - **Description:** Grants permission to update a plan execution step
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon ARC Region switch
<a name="list_arc-region-switch-permission-only-actions"></a>

The following actions are defined by Amazon ARC Region switch but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-region-switch.region-switch-different-accounts.html)  **
  - **Description:** Grants permission to delete the RAM access control policy for a plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [GetResourcePolicy](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-region-switch.region-switch-different-accounts.html)  **
  - **Description:** Grants permission to get the resource policy of a plan
  - **Resource types (\*required):** [plan\*](#list_arc-region-switch-resource-plan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-region-switch.region-switch-different-accounts.html)  **
  - **Description:** Grants permission to define the RAM access control policy for a plan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon ARC Region switch
<a name="list_arc-region-switch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [plan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Plan.html)  | arn:${Partition}:arc-region-switch::${Account}:plan/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_arc-region-switch-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon ARC Region switch
<a name="list_arc-region-switch-policy-keys"></a>

Amazon ARC Region switch defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 