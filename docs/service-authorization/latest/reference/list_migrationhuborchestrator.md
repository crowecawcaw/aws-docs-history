

# Actions, resources, and condition keys for AWS Migration Hub Orchestrator
<a name="list_migrationhuborchestrator"></a>

AWS Migration Hub Orchestrator (service prefix: `migrationhub-orchestrator`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/migrationhub-orchestrator/migrationhub-orchestrator.json) for this service.

**Topics**
+ [API operations defined by AWS Migration Hub Orchestrator](#list_migrationhuborchestrator-operations)
+ [Actions defined by AWS Migration Hub Orchestrator](#list_migrationhuborchestrator-actions-as-permissions)
+ [Resource types defined by AWS Migration Hub Orchestrator](#list_migrationhuborchestrator-resources-for-iam-policies)
+ [Condition keys for AWS Migration Hub Orchestrator](#list_migrationhuborchestrator-policy-keys)

## API operations defined by AWS Migration Hub Orchestrator
<a name="list_migrationhuborchestrator-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_migrationhuborchestrator-actions-as-permissions).




- **   CreateTemplate  **
  - **IAM action:**  [migrationhub-orchestrator:CreateTemplate](#list_migrationhuborchestrator-action-CreateTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [migrationhub-orchestrator:TagResource](#list_migrationhuborchestrator-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:CreateWorkflow](#list_migrationhuborchestrator-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [migrationhub-orchestrator:TagResource](#list_migrationhuborchestrator-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWorkflowStep  **
  - **IAM action:**  [migrationhub-orchestrator:CreateWorkflowStep](#list_migrationhuborchestrator-action-CreateWorkflowStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkflowStepGroup  **
  - **IAM action:**  [migrationhub-orchestrator:CreateWorkflowStepGroup](#list_migrationhuborchestrator-action-CreateWorkflowStepGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplate  **
  - **IAM action:**  [migrationhub-orchestrator:DeleteTemplate](#list_migrationhuborchestrator-action-DeleteTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:DeleteWorkflow](#list_migrationhuborchestrator-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowStep  **
  - **IAM action:**  [migrationhub-orchestrator:DeleteWorkflowStep](#list_migrationhuborchestrator-action-DeleteWorkflowStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowStepGroup  **
  - **IAM action:**  [migrationhub-orchestrator:DeleteWorkflowStepGroup](#list_migrationhuborchestrator-action-DeleteWorkflowStepGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetTemplate  **
  - **IAM action:**  [migrationhub-orchestrator:GetTemplate](#list_migrationhuborchestrator-action-GetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateStep  **
  - **IAM action:**  [migrationhub-orchestrator:GetTemplateStep](#list_migrationhuborchestrator-action-GetTemplateStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateStepGroup  **
  - **IAM action:**  [migrationhub-orchestrator:GetTemplateStepGroup](#list_migrationhuborchestrator-action-GetTemplateStepGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:GetWorkflow](#list_migrationhuborchestrator-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowStep  **
  - **IAM action:**  [migrationhub-orchestrator:GetWorkflowStep](#list_migrationhuborchestrator-action-GetWorkflowStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowStepGroup  **
  - **IAM action:**  [migrationhub-orchestrator:GetWorkflowStepGroup](#list_migrationhuborchestrator-action-GetWorkflowStepGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPlugins  **
  - **IAM action:**  [migrationhub-orchestrator:ListPlugins](#list_migrationhuborchestrator-action-ListPlugins) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [migrationhub-orchestrator:ListTagsForResource](#list_migrationhuborchestrator-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateStepGroups  **
  - **IAM action:**  [migrationhub-orchestrator:ListTemplateStepGroups](#list_migrationhuborchestrator-action-ListTemplateStepGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplateSteps  **
  - **IAM action:**  [migrationhub-orchestrator:ListTemplateSteps](#list_migrationhuborchestrator-action-ListTemplateSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplates  **
  - **IAM action:**  [migrationhub-orchestrator:ListTemplates](#list_migrationhuborchestrator-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowStepGroups  **
  - **IAM action:**  [migrationhub-orchestrator:ListWorkflowStepGroups](#list_migrationhuborchestrator-action-ListWorkflowStepGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowSteps  **
  - **IAM action:**  [migrationhub-orchestrator:ListWorkflowSteps](#list_migrationhuborchestrator-action-ListWorkflowSteps) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [migrationhub-orchestrator:ListWorkflows](#list_migrationhuborchestrator-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RetryWorkflowStep  **
  - **IAM action:**  [migrationhub-orchestrator:RetryWorkflowStep](#list_migrationhuborchestrator-action-RetryWorkflowStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:StartWorkflow](#list_migrationhuborchestrator-action-StartWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:StopWorkflow](#list_migrationhuborchestrator-action-StopWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [migrationhub-orchestrator:TagResource](#list_migrationhuborchestrator-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [migrationhub-orchestrator:UntagResource](#list_migrationhuborchestrator-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateWorkflow  **
  - **IAM action:**  [migrationhub-orchestrator:UpdateWorkflow](#list_migrationhuborchestrator-action-UpdateWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflowStep  **
  - **IAM action:**  [migrationhub-orchestrator:UpdateWorkflowStep](#list_migrationhuborchestrator-action-UpdateWorkflowStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflowStepGroup  **
  - **IAM action:**  [migrationhub-orchestrator:UpdateWorkflowStepGroup](#list_migrationhuborchestrator-action-UpdateWorkflowStepGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Migration Hub Orchestrator
<a name="list_migrationhuborchestrator-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateTemplate.html)  **
  - **Description:** Grants permission to create a custom template
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflow.html)  **
  - **Description:** Grants permission to create a workflow based on the selected template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_migrationhuborchestrator-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migrationhuborchestrator-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStep.html)  **
  - **Description:** Grants permission to create a step under a workflow and a specific step group
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStepGroup.html)  **
  - **Description:** Grants permission to to create a custom step group for a given workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteTemplate.html)  **
  - **Description:** Grants permission to delete a custom template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStep.html)  **
  - **Description:** Grants permission to delete a step from a specific step group under a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStepGroup.html)  **
  - **Description:** Grants permission to delete a step group associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetMessage](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetMessage.html)  **
  - **Description:** Grants permission to the plugin to receive information from the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplate.html)  **
  - **Description:** Grants permission to get retrieve metadata for a Template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplateStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStep.html)  **
  - **Description:** Grants permission to retrieve details of a step associated with a template and a step group
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplateStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStepGroup.html)  **
  - **Description:** Grants permission to retrieve metadata of a step group under a template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflow.html)  **
  - **Description:** Grants permission to retrieve metadata asscociated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStep.html)  **
  - **Description:** Grants permission to get details of step associated with a workflow and a step group
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStepGroup.html)  **
  - **Description:** Grants permission to get details of a step group associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPlugins](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListPlugins.html)  **
  - **Description:** Grants permission to get a list all registered Plugins
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get a list of all the tags tied to a resource
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTemplateStepGroups](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateStepGroups.html)  **
  - **Description:** Grants permission to lists step groups of a template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplateSteps](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateSteps.html)  **
  - **Description:** Grants permission to get a list of steps in a step group
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplates](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplates.html)  **
  - **Description:** Grants permission to get a list of all Templates available to customer
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflowStepGroups](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowStepGroups.html)  **
  - **Description:** Grants permission to get list of step groups associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflowSteps](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowSteps.html)  **
  - **Description:** Grants permission to get a list of steps within step group associated with a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflows.html)  **
  - **Description:** Grants permission to list all workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [RegisterPlugin](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_RegisterPlugin.html)  **
  - **Description:** Grants permission to register the plugin to receive an ID and to start receiving messages from the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RetryWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_RetryWorkflowStep.html)  **
  - **Description:** Grants permission to retry a failed step within a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendMessage](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_SendMessage.html)  **
  - **Description:** Grants permission to the plugin to send information to the service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StartWorkflow.html)  **
  - **Description:** Grants permission to start a workflow or resume a stopped workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_StopWorkflow.html)  **
  - **Description:** Grants permission to stop a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [template](#list_migrationhuborchestrator-resource-template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migrationhuborchestrator-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migrationhuborchestrator-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_migrationhuborchestrator-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_migrationhuborchestrator-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migrationhuborchestrator-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [template](#list_migrationhuborchestrator-resource-template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migrationhuborchestrator-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_migrationhuborchestrator-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_migrationhuborchestrator-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateTemplate](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateTemplate.html)  **
  - **Description:** Grants permission to update a custom template
  - **Resource types (\*required):** [template\*](#list_migrationhuborchestrator-resource-template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflow.html)  **
  - **Description:** Grants permission to update the metadata associated with the workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkflowStep](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStep.html)  **
  - **Description:** Grants permission to update metadata and status of a custom step within a workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkflowStepGroup](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStepGroup.html)  **
  - **Description:** Grants permission to update metadata associated with a step group in a given workflow
  - **Resource types (\*required):** [workflow\*](#list_migrationhuborchestrator-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Migration Hub Orchestrator
<a name="list_migrationhuborchestrator-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [template](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/templates.html)  | arn:${Partition}:migrationhub-orchestrator:${Region}:${Account}:template/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_) | 
|  [workflow](https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/workflow.html)  | arn:${Partition}:migrationhub-orchestrator:${Region}:${Account}:workflow/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_migrationhuborchestrator-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Migration Hub Orchestrator
<a name="list_migrationhuborchestrator-policy-keys"></a>

AWS Migration Hub Orchestrator defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 