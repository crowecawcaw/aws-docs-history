

# Actions, resources, and condition keys for AWS Compute Optimizer Automation
<a name="list_compute-optimizer-automation"></a>

AWS Compute Optimizer Automation (service prefix: `aco-automation`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Operations_Compute_Optimizer_Automation.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aco-automation/aco-automation.json) for this service.

**Topics**
+ [API operations defined by AWS Compute Optimizer Automation](#list_compute-optimizer-automation-operations)
+ [Actions defined by AWS Compute Optimizer Automation](#list_compute-optimizer-automation-actions-as-permissions)
+ [Resource types defined by AWS Compute Optimizer Automation](#list_compute-optimizer-automation-resources-for-iam-policies)
+ [Condition keys for AWS Compute Optimizer Automation](#list_compute-optimizer-automation-policy-keys)

## API operations defined by AWS Compute Optimizer Automation
<a name="list_compute-optimizer-automation-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_compute-optimizer-automation-actions-as-permissions).




- **   AssociateAccounts  **
  - **IAM action:**  [aco-automation:AssociateAccounts](#list_compute-optimizer-automation-action-AssociateAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAutomationRule  **
  - **IAM action:**  [aco-automation:CreateAutomationRule](#list_compute-optimizer-automation-action-CreateAutomationRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aco-automation:TagResource](#list_compute-optimizer-automation-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAutomationRule  **
  - **IAM action:**  [aco-automation:DeleteAutomationRule](#list_compute-optimizer-automation-action-DeleteAutomationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAccounts  **
  - **IAM action:**  [aco-automation:DisassociateAccounts](#list_compute-optimizer-automation-action-DisassociateAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAutomationEvent  **
  - **IAM action:**  [aco-automation:GetAutomationEvent](#list_compute-optimizer-automation-action-GetAutomationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomationRule  **
  - **IAM action:**  [aco-automation:GetAutomationRule](#list_compute-optimizer-automation-action-GetAutomationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEnrollmentConfiguration  **
  - **IAM action:**  [aco-automation:GetEnrollmentConfiguration](#list_compute-optimizer-automation-action-GetEnrollmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccounts  **
  - **IAM action:**  [aco-automation:ListAccounts](#list_compute-optimizer-automation-action-ListAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationEventSteps  **
  - **IAM action:**  [aco-automation:ListAutomationEventSteps](#list_compute-optimizer-automation-action-ListAutomationEventSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationEventSummaries  **
  - **IAM action:**  [aco-automation:ListAutomationEventSummaries](#list_compute-optimizer-automation-action-ListAutomationEventSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationEvents  **
  - **IAM action:**  [aco-automation:ListAutomationEvents](#list_compute-optimizer-automation-action-ListAutomationEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationRulePreview  **
  - **IAM action:**  [aco-automation:ListAutomationRulePreview](#list_compute-optimizer-automation-action-ListAutomationRulePreview)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListAutomationRulePreviewSummaries  **
  - **IAM action:**  [aco-automation:ListAutomationRulePreviewSummaries](#list_compute-optimizer-automation-action-ListAutomationRulePreviewSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomationRules  **
  - **IAM action:**  [aco-automation:ListAutomationRules](#list_compute-optimizer-automation-action-ListAutomationRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendedActionSummaries  **
  - **IAM action:**  [aco-automation:ListRecommendedActionSummaries](#list_compute-optimizer-automation-action-ListRecommendedActionSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRecommendedActions  **
  - **IAM action:**  [aco-automation:ListRecommendedActions](#list_compute-optimizer-automation-action-ListRecommendedActions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aco-automation:ListTagsForResource](#list_compute-optimizer-automation-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RollbackAutomationEvent  **
  - **IAM action:**  [aco-automation:RollbackAutomationEvent](#list_compute-optimizer-automation-action-RollbackAutomationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAutomationEvent  **
  - **IAM action:**  [aco-automation:StartAutomationEvent](#list_compute-optimizer-automation-action-StartAutomationEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [aco-automation:TagResource](#list_compute-optimizer-automation-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aco-automation:UntagResource](#list_compute-optimizer-automation-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAutomationRule  **
  - **IAM action:**  [aco-automation:UpdateAutomationRule](#list_compute-optimizer-automation-action-UpdateAutomationRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEnrollmentConfiguration  **
  - **IAM action:**  [aco-automation:UpdateEnrollmentConfiguration](#list_compute-optimizer-automation-action-UpdateEnrollmentConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Compute Optimizer Automation
<a name="list_compute-optimizer-automation-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AssociateAccounts.html)  **
  - **Description:** Grants permission to associate member accounts with the management account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_CreateAutomationRule.html)  **
  - **Description:** Grants permission to create automation rule
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_compute-optimizer-automation-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_compute-optimizer-automation-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DeleteAutomationRule.html)  **
  - **Description:** Grants permission to delete automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DisassociateAccounts.html)  **
  - **Description:** Grants permission to disassociate member accounts from the management account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationEvent.html)  **
  - **Description:** Grants permission to get automation event details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationRule.html)  **
  - **Description:** Grants permission to get automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnrollmentConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetEnrollmentConfiguration.html)  **
  - **Description:** Grants permission to get enrollment configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAccounts.html)  **
  - **Description:** Grants permission to list the accounts in your organization that are enrolled in Compute Optimizer and whether they have enabled the Automation feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationEventSteps](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEventSteps.html)  **
  - **Description:** Grants permission to list automation event steps
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationEventSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEventSummaries.html)  **
  - **Description:** Grants permission to list automation event summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationEvents](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEvents.html)  **
  - **Description:** Grants permission to list automation events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRulePreview](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreview.html)  **
  - **Description:** Grants permission to list automation rule preview results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRulePreviewSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreviewSummaries.html)  **
  - **Description:** Grants permission to list automation rule preview summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomationRules](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRules.html)  **
  - **Description:** Grants permission to list automation rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendedActionSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListRecommendedActionSummaries.html)  **
  - **Description:** Grants permission to list recommended action summaries
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendedActions](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListRecommendedActions.html)  **
  - **Description:** Grants permission to list recommended actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RollbackAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RollbackAutomationEvent.html)  **
  - **Description:** Grants permission to initiate a rollback for an automation event
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_StartAutomationEvent.html)  **
  - **Description:** Grants permission to initiate an on-demand automation for a recommended action
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_TagResource.html)  **
  - **Description:** Grants permission to add tags to automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_compute-optimizer-automation-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_compute-optimizer-automation-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_compute-optimizer-automation-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateAutomationRule.html)  **
  - **Description:** Grants permission to update automation rule
  - **Resource types (\*required):** [AutomationRule\*](#list_compute-optimizer-automation-resource-AutomationRule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnrollmentConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateEnrollmentConfiguration.html)  **
  - **Description:** Grants permission to update enrollment configuration for the Compute Optimizer automation feature
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Compute Optimizer Automation
<a name="list_compute-optimizer-automation-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html)  | arn:${Partition}:compute-optimizer::${Account}:automation-rule/${RuleId} | [aws:ResourceTag/${TagKey}](#list_compute-optimizer-automation-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Compute Optimizer Automation
<a name="list_compute-optimizer-automation-policy-keys"></a>

AWS Compute Optimizer Automation defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](API_automation_Tag.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](API_automation_TagResource.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](API_automation_Tag.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 