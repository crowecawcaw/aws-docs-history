

# Actions, resources, and condition keys for Amazon Inspector
<a name="list_inspector"></a>

Amazon Inspector (service prefix: `inspector`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/inspector/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/inspector/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/inspector/latest/userguide/access_permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/inspector/inspector.json) for this service.

**Topics**
+ [API operations defined by Amazon Inspector](#list_inspector-operations)
+ [Actions defined by Amazon Inspector](#list_inspector-actions-as-permissions)
+ [Resource types defined by Amazon Inspector](#list_inspector-resources-for-iam-policies)
+ [Condition keys for Amazon Inspector](#list_inspector-policy-keys)

## API operations defined by Amazon Inspector
<a name="list_inspector-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_inspector-actions-as-permissions).




- **   AddAttributesToFindings  **
  - **IAM action:**  [inspector:AddAttributesToFindings](#list_inspector-action-AddAttributesToFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssessmentTarget  **
  - **IAM action:**  [inspector:CreateAssessmentTarget](#list_inspector-action-CreateAssessmentTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssessmentTemplate  **
  - **IAM action:**  [inspector:CreateAssessmentTemplate](#list_inspector-action-CreateAssessmentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateExclusionsPreview  **
  - **IAM action:**  [inspector:CreateExclusionsPreview](#list_inspector-action-CreateExclusionsPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateResourceGroup  **
  - **IAM action:**  [inspector:CreateResourceGroup](#list_inspector-action-CreateResourceGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentRun  **
  - **IAM action:**  [inspector:DeleteAssessmentRun](#list_inspector-action-DeleteAssessmentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentTarget  **
  - **IAM action:**  [inspector:DeleteAssessmentTarget](#list_inspector-action-DeleteAssessmentTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentTemplate  **
  - **IAM action:**  [inspector:DeleteAssessmentTemplate](#list_inspector-action-DeleteAssessmentTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeAssessmentRuns  **
  - **IAM action:**  [inspector:DescribeAssessmentRuns](#list_inspector-action-DescribeAssessmentRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssessmentTargets  **
  - **IAM action:**  [inspector:DescribeAssessmentTargets](#list_inspector-action-DescribeAssessmentTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeAssessmentTemplates  **
  - **IAM action:**  [inspector:DescribeAssessmentTemplates](#list_inspector-action-DescribeAssessmentTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeCrossAccountAccessRole  **
  - **IAM action:**  [inspector:DescribeCrossAccountAccessRole](#list_inspector-action-DescribeCrossAccountAccessRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExclusions  **
  - **IAM action:**  [inspector:DescribeExclusions](#list_inspector-action-DescribeExclusions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFindings  **
  - **IAM action:**  [inspector:DescribeFindings](#list_inspector-action-DescribeFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourceGroups  **
  - **IAM action:**  [inspector:DescribeResourceGroups](#list_inspector-action-DescribeResourceGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRulesPackages  **
  - **IAM action:**  [inspector:DescribeRulesPackages](#list_inspector-action-DescribeRulesPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssessmentReport  **
  - **IAM action:**  [inspector:GetAssessmentReport](#list_inspector-action-GetAssessmentReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExclusionsPreview  **
  - **IAM action:**  [inspector:GetExclusionsPreview](#list_inspector-action-GetExclusionsPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTelemetryMetadata  **
  - **IAM action:**  [inspector:GetTelemetryMetadata](#list_inspector-action-GetTelemetryMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssessmentRunAgents  **
  - **IAM action:**  [inspector:ListAssessmentRunAgents](#list_inspector-action-ListAssessmentRunAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentRuns  **
  - **IAM action:**  [inspector:ListAssessmentRuns](#list_inspector-action-ListAssessmentRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentTargets  **
  - **IAM action:**  [inspector:ListAssessmentTargets](#list_inspector-action-ListAssessmentTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentTemplates  **
  - **IAM action:**  [inspector:ListAssessmentTemplates](#list_inspector-action-ListAssessmentTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEventSubscriptions  **
  - **IAM action:**  [inspector:ListEventSubscriptions](#list_inspector-action-ListEventSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExclusions  **
  - **IAM action:**  [inspector:ListExclusions](#list_inspector-action-ListExclusions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [inspector:ListFindings](#list_inspector-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRulesPackages  **
  - **IAM action:**  [inspector:ListRulesPackages](#list_inspector-action-ListRulesPackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [inspector:ListTagsForResource](#list_inspector-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PreviewAgents  **
  - **IAM action:**  [inspector:PreviewAgents](#list_inspector-action-PreviewAgents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterCrossAccountAccessRole  **
  - **IAM action:**  [inspector:RegisterCrossAccountAccessRole](#list_inspector-action-RegisterCrossAccountAccessRole)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** inspector.amazonaws.com / **Access level:** Write

- **   RemoveAttributesFromFindings  **
  - **IAM action:**  [inspector:RemoveAttributesFromFindings](#list_inspector-action-RemoveAttributesFromFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTagsForResource  **
  - **IAM action:**  [inspector:SetTagsForResource](#list_inspector-action-SetTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   StartAssessmentRun  **
  - **IAM action:**  [inspector:StartAssessmentRun](#list_inspector-action-StartAssessmentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopAssessmentRun  **
  - **IAM action:**  [inspector:StopAssessmentRun](#list_inspector-action-StopAssessmentRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SubscribeToEvent  **
  - **IAM action:**  [inspector:SubscribeToEvent](#list_inspector-action-SubscribeToEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UnsubscribeFromEvent  **
  - **IAM action:**  [inspector:UnsubscribeFromEvent](#list_inspector-action-UnsubscribeFromEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentTarget  **
  - **IAM action:**  [inspector:UpdateAssessmentTarget](#list_inspector-action-UpdateAssessmentTarget) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Inspector
<a name="list_inspector-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AddAttributesToFindings](https://docs.aws.amazon.com/inspector/latest/APIReference/API_AddAttributesToFindings.html)  | Grants permission to assign attributes (key and value pairs) to the findings that are specified by the ARNs of the findings |  |   | Write | 
|   [CreateAssessmentTarget](https://docs.aws.amazon.com/inspector/latest/APIReference/API_CreateAssessmentTarget.html)  | Grants permission to create a new assessment target using the ARN of the resource group that is generated by CreateResourceGroup |  |   | Write | 
|   [CreateAssessmentTemplate](https://docs.aws.amazon.com/inspector/latest/APIReference/API_CreateAssessmentTemplate.html)  | Grants permission to create an assessment template for the assessment target that is specified by the ARN of the assessment target |  |   | Write | 
|   [CreateExclusionsPreview](https://docs.aws.amazon.com/inspector/latest/APIReference/API_CreateExclusionsPreview.html)  | Grants permission to start the generation of an exclusions preview for the specified assessment template |  |   | Write | 
|   [CreateResourceGroup](https://docs.aws.amazon.com/inspector/latest/APIReference/API_CreateResourceGroup.html)  | Grants permission to create a resource group using the specified set of tags (key and value pairs) that are used to select the EC2 instances to be included in an Amazon Inspector assessment target |  |   | Write | 
|   [DeleteAssessmentRun](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DeleteAssessmentRun.html)  | Grants permission to delete the assessment run that is specified by the ARN of the assessment run |  |   | Write | 
|   [DeleteAssessmentTarget](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DeleteAssessmentTarget.html)  | Grants permission to delete the assessment target that is specified by the ARN of the assessment target |  |   | Write | 
|   [DeleteAssessmentTemplate](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DeleteAssessmentTemplate.html)  | Grants permission to delete the assessment template that is specified by the ARN of the assessment template |  |   | Write | 
|   [DescribeAssessmentRuns](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeAssessmentRuns.html)  | Grants permission to describe the assessment runs that are specified by the ARNs of the assessment runs |  |   | Read | 
|   [DescribeAssessmentTargets](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeAssessmentTargets.html)  | Grants permission to describe the assessment targets that are specified by the ARNs of the assessment targets |  |   | Read | 
|   [DescribeAssessmentTemplates](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeAssessmentTemplates.html)  | Grants permission to describe the assessment templates that are specified by the ARNs of the assessment templates |  |   | Read | 
|   [DescribeCrossAccountAccessRole](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeCrossAccountAccessRole.html)  | Grants permission to describe the IAM role that enables Amazon Inspector to access your AWS account |  |   | Read | 
|   [DescribeExclusions](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeExclusions.html)  | Grants permission to describe the exclusions that are specified by the exclusions' ARNs |  |   | Read | 
|   [DescribeFindings](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeFindings.html)  | Grants permission to describe the findings that are specified by the ARNs of the findings |  |   | Read | 
|   [DescribeResourceGroups](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeResourceGroups.html)  | Grants permission to describe the resource groups that are specified by the ARNs of the resource groups |  |   | Read | 
|   [DescribeRulesPackages](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DescribeRulesPackages.html)  | Grants permission to describe the rules packages that are specified by the ARNs of the rules packages |  |   | Read | 
|   [GetAssessmentReport](https://docs.aws.amazon.com/inspector/latest/APIReference/API_GetAssessmentReport.html)  | Grants permission to produce an assessment report that includes detailed and comprehensive results of a specified assessment run |  |   | Read | 
|   [GetExclusionsPreview](https://docs.aws.amazon.com/inspector/latest/APIReference/API_GetExclusionsPreview.html)  | Grants permission to retrieve the exclusions preview (a list of ExclusionPreview objects) specified by the preview token |  |   | Read | 
|   [GetTelemetryMetadata](https://docs.aws.amazon.com/inspector/latest/APIReference/API_GetTelemetryMetadata.html)  | Grants permission to get information about the data that is collected for the specified assessment run |  |   | Read | 
|   [ListAssessmentRunAgents](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListAssessmentRunAgents.html)  | Grants permission to list the agents of the assessment runs that are specified by the ARNs of the assessment runs |  |   | List | 
|   [ListAssessmentRuns](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListAssessmentRuns.html)  | Grants permission to list the assessment runs that correspond to the assessment templates that are specified by the ARNs of the assessment templates |  |   | List | 
|   [ListAssessmentTargets](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListAssessmentTargets.html)  | Grants permission to list the ARNs of the assessment targets within this AWS account |  |   | List | 
|   [ListAssessmentTemplates](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListAssessmentTemplates.html)  | Grants permission to list the assessment templates that correspond to the assessment targets that are specified by the ARNs of the assessment targets |  |   | List | 
|   [ListEventSubscriptions](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListEventSubscriptions.html)  | Grants permission to list all the event subscriptions for the assessment template that is specified by the ARN of the assessment template |  |   | List | 
|   [ListExclusions](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListExclusions.html)  | Grants permission to list exclusions that are generated by the assessment run |  |   | List | 
|   [ListFindings](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListFindings.html)  | Grants permission to list findings that are generated by the assessment runs that are specified by the ARNs of the assessment runs |  |   | List | 
|   [ListRulesPackages](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListRulesPackages.html)  | Grants permission to list all available Amazon Inspector rules packages |  |   | List | 
|   [ListTagsForResource](https://docs.aws.amazon.com/inspector/latest/APIReference/API_ListTagsForResource.html)  | Grants permission to list all tags associated with an assessment template |  |   | Read | 
|   [PreviewAgents](https://docs.aws.amazon.com/inspector/latest/APIReference/API_PreviewAgents.html)  | Grants permission to preview the agents installed on the EC2 instances that are part of the specified assessment target |  |   | Read | 
|   [RegisterCrossAccountAccessRole](https://docs.aws.amazon.com/inspector/latest/APIReference/API_RegisterCrossAccountAccessRole.html)  | Grants permission to register the IAM role that Amazon Inspector uses to list your EC2 instances at the start of the assessment run or when you call the PreviewAgents action |  |   | Write | 
|   [RemoveAttributesFromFindings](https://docs.aws.amazon.com/inspector/latest/APIReference/API_RemoveAttributesFromFindings.html)  | Grants permission to remove entire attributes (key and value pairs) from the findings that are specified by the ARNs of the findings where an attribute with the specified key exists |  |   | Write | 
|   [SetTagsForResource](https://docs.aws.amazon.com/inspector/latest/APIReference/API_SetTagsForResource.html)  | Grants permission to set tags (key and value pairs) to the assessment template that is specified by the ARN of the assessment template |  |   | Tagging, Write | 
|   [StartAssessmentRun](https://docs.aws.amazon.com/inspector/latest/APIReference/API_StartAssessmentRun.html)  | Grants permission to start the assessment run specified by the ARN of the assessment template |  |   | Write | 
|   [StopAssessmentRun](https://docs.aws.amazon.com/inspector/latest/APIReference/API_StopAssessmentRun.html)  | Grants permission to stop the assessment run that is specified by the ARN of the assessment run |  |   | Write | 
|   [SubscribeToEvent](https://docs.aws.amazon.com/inspector/latest/APIReference/API_SubscribeToEvent.html)  | Grants permission to enable the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic |  |   | Write | 
|   [UnsubscribeFromEvent](https://docs.aws.amazon.com/inspector/latest/APIReference/API_UnsubscribeFromEvent.html)  | Grants permission to disable the process of sending Amazon Simple Notification Service (SNS) notifications about a specified event to a specified SNS topic |  |   | Write | 
|   [UpdateAssessmentTarget](https://docs.aws.amazon.com/inspector/latest/APIReference/API_UpdateAssessmentTarget.html)  | Grants permission to update the assessment target that is specified by the ARN of the assessment target |  |   | Write | 

## Resource types defined by Amazon Inspector
<a name="list_inspector-resources-for-iam-policies"></a>

Amazon Inspector does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon Inspector
<a name="list_inspector-policy-keys"></a>

Amazon Inspector has no service-specific condition keys that can be used in the `Condition` element of policy statements.