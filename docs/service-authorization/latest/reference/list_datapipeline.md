

# Actions, resources, and condition keys for AWS Data Pipeline
<a name="list_datapipeline"></a>

AWS Data Pipeline (service prefix: `datapipeline`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/datapipeline/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-control-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/datapipeline/datapipeline.json) for this service.

**Topics**
+ [API operations defined by AWS Data Pipeline](#list_datapipeline-operations)
+ [Actions defined by AWS Data Pipeline](#list_datapipeline-actions-as-permissions)
+ [Permission-only actions for AWS Data Pipeline](#list_datapipeline-permission-only-actions)
+ [Resource types defined by AWS Data Pipeline](#list_datapipeline-resources-for-iam-policies)
+ [Condition keys for AWS Data Pipeline](#list_datapipeline-policy-keys)

## API operations defined by AWS Data Pipeline
<a name="list_datapipeline-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_datapipeline-actions-as-permissions).




- **   ActivatePipeline  **
  - **IAM action:**  [datapipeline:ActivatePipeline](#list_datapipeline-action-ActivatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datapipeline.amazonaws.com, ec2.amazonaws.com, elasticmapreduce.amazonaws.com / **Access level:** Write

- **   AddTags  **
  - **IAM action:**  [datapipeline:AddTags](#list_datapipeline-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CreatePipeline  **
  - **IAM action:**  [datapipeline:AddTags](#list_datapipeline-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [datapipeline:CreatePipeline](#list_datapipeline-action-CreatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeactivatePipeline  **
  - **IAM action:**  [datapipeline:DeactivatePipeline](#list_datapipeline-action-DeactivatePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipeline  **
  - **IAM action:**  [datapipeline:DeletePipeline](#list_datapipeline-action-DeletePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeObjects  **
  - **IAM action:**  [datapipeline:DescribeObjects](#list_datapipeline-action-DescribeObjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePipelines  **
  - **IAM action:**  [datapipeline:DescribePipelines](#list_datapipeline-action-DescribePipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   EvaluateExpression  **
  - **IAM action:**  [datapipeline:EvaluateExpression](#list_datapipeline-action-EvaluateExpression) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipelineDefinition  **
  - **IAM action:**  [datapipeline:GetPipelineDefinition](#list_datapipeline-action-GetPipelineDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPipelines  **
  - **IAM action:**  [datapipeline:ListPipelines](#list_datapipeline-action-ListPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PollForTask  **
  - **IAM action:**  [datapipeline:PollForTask](#list_datapipeline-action-PollForTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPipelineDefinition  **
  - **IAM action:**  [datapipeline:PutPipelineDefinition](#list_datapipeline-action-PutPipelineDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datapipeline.amazonaws.com, ec2.amazonaws.com, elasticmapreduce.amazonaws.com / **Access level:** Write

- **   QueryObjects  **
  - **IAM action:**  [datapipeline:QueryObjects](#list_datapipeline-action-QueryObjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RemoveTags  **
  - **IAM action:**  [datapipeline:RemoveTags](#list_datapipeline-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   ReportTaskProgress  **
  - **IAM action:**  [datapipeline:ReportTaskProgress](#list_datapipeline-action-ReportTaskProgress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReportTaskRunnerHeartbeat  **
  - **IAM action:**  [datapipeline:ReportTaskRunnerHeartbeat](#list_datapipeline-action-ReportTaskRunnerHeartbeat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetStatus  **
  - **IAM action:**  [datapipeline:SetStatus](#list_datapipeline-action-SetStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetTaskStatus  **
  - **IAM action:**  [datapipeline:SetTaskStatus](#list_datapipeline-action-SetTaskStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidatePipelineDefinition  **
  - **IAM action:**  [datapipeline:ValidatePipelineDefinition](#list_datapipeline-action-ValidatePipelineDefinition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** datapipeline.amazonaws.com, ec2.amazonaws.com, elasticmapreduce.amazonaws.com / **Access level:** Write



## Actions defined by AWS Data Pipeline
<a name="list_datapipeline-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ActivatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ActivatePipeline.html)  **
  - **Description:** Grants permission to validate the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)<br />[datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to add or modify tags for the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datapipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datapipeline-aws_TagKeys)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Tagging, Write

- **   [CreatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_CreatePipeline.html)  **
  - **Description:** Grants permission to create a new, empty pipeline
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datapipeline-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_datapipeline-aws_TagKeys)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Write

- **   [DeactivatePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DeactivatePipeline.html)  **
  - **Description:** Grants permission to Deactivate the specified running pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)<br />[datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DeletePipeline.html)  **
  - **Description:** Grants permission to delete a pipeline, its pipeline definition, and its run history
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Write

- **   [DescribeObjects](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribeObjects.html)  **
  - **Description:** Grants permission to get the object definitions for a set of objects associated with the pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Read

- **   [DescribePipelines](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_DescribePipelines.html)  **
  - **Description:** Grants permission to retrieves metadata about one or more pipelines
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Read

- **   [EvaluateExpression](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_EvaluateExpression.html)  **
  - **Description:** Grants permission to task runners to call EvaluateExpression, to evaluate a string in the context of the specified object
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Read

- **   [GetPipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_GetPipelineDefinition.html)  **
  - **Description:** Grants permission to gets the definition of the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)<br />[datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Read

- **   [ListPipelines](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ListPipelines.html)  **
  - **Description:** Grants permission to list the pipeline identifiers for all active pipelines that you have permission to access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PollForTask](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PollForTask.html)  **
  - **Description:** Grants permission to task runners to call PollForTask, to receive a task to perform from AWS Data Pipeline
  - **Resource types (\*required):** 
  - **Condition keys:** [datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Write

- **   [PutPipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutPipelineDefinition.html)  **
  - **Description:** Grants permission to add tasks, schedules, and preconditions to the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)<br />[datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Write

- **   [QueryObjects](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_QueryObjects.html)  **
  - **Description:** Grants permission to query the specified pipeline for the names of objects that match the specified set of conditions
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Read

- **   [RemoveTags](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove existing tags from the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_datapipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_datapipeline-aws_TagKeys)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Tagging, Write

- **   [ReportTaskProgress](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskProgress.html)  **
  - **Description:** Grants permission to task runners to call ReportTaskProgress, when they are assigned a task to acknowledge that it has the task
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReportTaskRunnerHeartbeat](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ReportTaskRunnerHeartbeat.html)  **
  - **Description:** Grants permission to task runners to call ReportTaskRunnerHeartbeat every 15 minutes to indicate that they are operational
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetStatus](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetStatus.html)  **
  - **Description:** Grants permission to requests that the status of the specified physical or logical pipeline objects be updated in the specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)
  - **Access level:** Write

- **   [SetTaskStatus](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_SetTaskStatus.html)  **
  - **Description:** Grants permission to task runners to call SetTaskStatus to notify AWS Data Pipeline that a task is completed and provide information about the final status
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidatePipelineDefinition](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ValidatePipelineDefinition.html)  **
  - **Description:** Grants permission to validate the specified pipeline definition to ensure that it is well formed and can be run without error
  - **Resource types (\*required):** [pipeline\*](#list_datapipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_)<br />[datapipeline:PipelineCreator](#list_datapipeline-datapipeline_PipelineCreator)<br />[datapipeline:Tag/${TagKey}](#list_datapipeline-datapipeline_Tag___TagKey_)<br />[datapipeline:workerGroup](#list_datapipeline-datapipeline_workerGroup)
  - **Access level:** Read



## Permission-only actions for AWS Data Pipeline
<a name="list_datapipeline-permission-only-actions"></a>

The following actions are defined by AWS Data Pipeline but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [GetAccountLimits](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_GetAccountLimits.html)  | Grants permission to call GetAccountLimits |  |   | List | 
|   [PutAccountLimits](https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutAccountLimits.html)  | Grants permission to call PutAccountLimits |  |   | Write | 

## Resource types defined by AWS Data Pipeline
<a name="list_datapipeline-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [pipeline](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatapipeline.html)  | arn:${Partition}:datapipeline:${Region}:${Account}:pipeline/${PipelineId} | [aws:ResourceTag/${TagKey}](#list_datapipeline-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Data Pipeline
<a name="list_datapipeline-policy-keys"></a>

AWS Data Pipeline defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 
|   [datapipeline:PipelineCreator](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-example-tag-policies.html#ex3)  | Filters access by the IAM user that created the pipeline | ArrayOfString | 
|   [datapipeline:Tag/${TagKey}](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-resourcebased-access.html#dp-control-access-tags)  | Filters access by customer-specified key/value pair that can be attached to a resource | String | 
|   [datapipeline:workerGroup](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-resourcebased-access.html#dp-control-access-workergroup)  | Filters access by the name of a worker group for which a Task Runner retrieves work | ArrayOfString | 