

# Actions, resources, and condition keys for AWS CodePipeline
<a name="list_codepipeline"></a>

AWS CodePipeline (service prefix: `codepipeline`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codepipeline/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codepipeline/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codepipeline/codepipeline.json) for this service.

**Topics**
+ [API operations defined by AWS CodePipeline](#list_codepipeline-operations)
+ [Actions defined by AWS CodePipeline](#list_codepipeline-actions-as-permissions)
+ [Resource types defined by AWS CodePipeline](#list_codepipeline-resources-for-iam-policies)
+ [Condition keys for AWS CodePipeline](#list_codepipeline-policy-keys)

## API operations defined by AWS CodePipeline
<a name="list_codepipeline-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codepipeline-actions-as-permissions).




- **   AcknowledgeJob  **
  - **IAM action:**  [codepipeline:AcknowledgeJob](#list_codepipeline-action-AcknowledgeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcknowledgeThirdPartyJob  **
  - **IAM action:**  [codepipeline:AcknowledgeThirdPartyJob](#list_codepipeline-action-AcknowledgeThirdPartyJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomActionType  **
  - **IAM action:**  [codepipeline:CreateCustomActionType](#list_codepipeline-action-CreateCustomActionType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codepipeline:TagResource](#list_codepipeline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePipeline  **
  - **IAM action:**  [codepipeline:CreatePipeline](#list_codepipeline-action-CreatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codepipeline:TagResource](#list_codepipeline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, codebuild.amazonaws.com, codepipeline.amazonaws.com / **Access level:** Write

- **   DeleteCustomActionType  **
  - **IAM action:**  [codepipeline:DeleteCustomActionType](#list_codepipeline-action-DeleteCustomActionType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePipeline  **
  - **IAM action:**  [codepipeline:DeletePipeline](#list_codepipeline-action-DeletePipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWebhook  **
  - **IAM action:**  [codepipeline:DeleteWebhook](#list_codepipeline-action-DeleteWebhook) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterWebhookWithThirdParty  **
  - **IAM action:**  [codepipeline:DeregisterWebhookWithThirdParty](#list_codepipeline-action-DeregisterWebhookWithThirdParty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableStageTransition  **
  - **IAM action:**  [codepipeline:DisableStageTransition](#list_codepipeline-action-DisableStageTransition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableStageTransition  **
  - **IAM action:**  [codepipeline:EnableStageTransition](#list_codepipeline-action-EnableStageTransition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetActionType  **
  - **IAM action:**  [codepipeline:GetActionType](#list_codepipeline-action-GetActionType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJobDetails  **
  - **IAM action:**  [codepipeline:GetJobDetails](#list_codepipeline-action-GetJobDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipeline  **
  - **IAM action:**  [codepipeline:GetPipeline](#list_codepipeline-action-GetPipeline) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipelineExecution  **
  - **IAM action:**  [codepipeline:GetPipelineExecution](#list_codepipeline-action-GetPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPipelineState  **
  - **IAM action:**  [codepipeline:GetPipelineState](#list_codepipeline-action-GetPipelineState) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThirdPartyJobDetails  **
  - **IAM action:**  [codepipeline:GetThirdPartyJobDetails](#list_codepipeline-action-GetThirdPartyJobDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActionExecutions  **
  - **IAM action:**  [codepipeline:ListActionExecutions](#list_codepipeline-action-ListActionExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActionTypes  **
  - **IAM action:**  [codepipeline:ListActionTypes](#list_codepipeline-action-ListActionTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeployActionExecutionTargets  **
  - **IAM action:**  [codepipeline:ListDeployActionExecutionTargets](#list_codepipeline-action-ListDeployActionExecutionTargets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPipelineExecutions  **
  - **IAM action:**  [codepipeline:ListPipelineExecutions](#list_codepipeline-action-ListPipelineExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPipelines  **
  - **IAM action:**  [codepipeline:ListPipelines](#list_codepipeline-action-ListPipelines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuleExecutions  **
  - **IAM action:**  [codepipeline:ListRuleExecutions](#list_codepipeline-action-ListRuleExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRuleTypes  **
  - **IAM action:**  [codepipeline:ListRuleTypes](#list_codepipeline-action-ListRuleTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [codepipeline:ListTagsForResource](#list_codepipeline-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebhooks  **
  - **IAM action:**  [codepipeline:ListWebhooks](#list_codepipeline-action-ListWebhooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   OverrideStageCondition  **
  - **IAM action:**  [codepipeline:OverrideStageCondition](#list_codepipeline-action-OverrideStageCondition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PollForJobs  **
  - **IAM action:**  [codepipeline:PollForJobs](#list_codepipeline-action-PollForJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PollForThirdPartyJobs  **
  - **IAM action:**  [codepipeline:PollForThirdPartyJobs](#list_codepipeline-action-PollForThirdPartyJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutActionRevision  **
  - **IAM action:**  [codepipeline:PutActionRevision](#list_codepipeline-action-PutActionRevision) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutApprovalResult  **
  - **IAM action:**  [codepipeline:PutApprovalResult](#list_codepipeline-action-PutApprovalResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutJobFailureResult  **
  - **IAM action:**  [codepipeline:PutJobFailureResult](#list_codepipeline-action-PutJobFailureResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutJobSuccessResult  **
  - **IAM action:**  [codepipeline:PutJobSuccessResult](#list_codepipeline-action-PutJobSuccessResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutThirdPartyJobFailureResult  **
  - **IAM action:**  [codepipeline:PutThirdPartyJobFailureResult](#list_codepipeline-action-PutThirdPartyJobFailureResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutThirdPartyJobSuccessResult  **
  - **IAM action:**  [codepipeline:PutThirdPartyJobSuccessResult](#list_codepipeline-action-PutThirdPartyJobSuccessResult) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutWebhook  **
  - **IAM action:**  [codepipeline:PutWebhook](#list_codepipeline-action-PutWebhook)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codepipeline:TagResource](#list_codepipeline-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codepipeline:UntagResource](#list_codepipeline-action-UntagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RegisterWebhookWithThirdParty  **
  - **IAM action:**  [codepipeline:RegisterWebhookWithThirdParty](#list_codepipeline-action-RegisterWebhookWithThirdParty) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RetryStageExecution  **
  - **IAM action:**  [codepipeline:RetryStageExecution](#list_codepipeline-action-RetryStageExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RollbackStage  **
  - **IAM action:**  [codepipeline:RollbackStage](#list_codepipeline-action-RollbackStage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPipelineExecution  **
  - **IAM action:**  [codepipeline:StartPipelineExecution](#list_codepipeline-action-StartPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPipelineExecution  **
  - **IAM action:**  [codepipeline:StopPipelineExecution](#list_codepipeline-action-StopPipelineExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codepipeline:TagResource](#list_codepipeline-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codepipeline:UntagResource](#list_codepipeline-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateActionType  **
  - **IAM action:**  [codepipeline:UpdateActionType](#list_codepipeline-action-UpdateActionType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePipeline  **
  - **IAM action:**  [codepipeline:UpdatePipeline](#list_codepipeline-action-UpdatePipeline)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codestar-connections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** cloudformation.amazonaws.com, codebuild.amazonaws.com, codepipeline.amazonaws.com / **Access level:** Write



## Actions defined by AWS CodePipeline
<a name="list_codepipeline-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcknowledgeJob](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_AcknowledgeJob.html)  **
  - **Description:** Grants permission to view information about a specified job and whether that job has been received by the job worker
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AcknowledgeThirdPartyJob](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_AcknowledgeThirdPartyJob.html)  **
  - **Description:** Grants permission to confirm that a job worker has received the specified job (partner actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCustomActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreateCustomActionType.html)  **
  - **Description:** Grants permission to create a custom action that you can use in the pipelines associated with your AWS account
  - **Resource types (\*required):** [actiontype\*](#list_codepipeline-resource-actiontype)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html)  **
  - **Description:** Grants permission to create a uniquely named pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCustomActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeleteCustomActionType.html)  **
  - **Description:** Grants permission to delete a custom action
  - **Resource types (\*required):** [actiontype\*](#list_codepipeline-resource-actiontype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeletePipeline.html)  **
  - **Description:** Grants permission to delete a specified pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebhook](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeleteWebhook.html)  **
  - **Description:** Grants permission to delete a specified webhook
  - **Resource types (\*required):** [webhook\*](#list_codepipeline-resource-webhook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterWebhookWithThirdParty](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeregisterWebhookWithThirdParty.html)  **
  - **Description:** Grants permission to remove the registration of a webhook with the third party specified in its configuration
  - **Resource types (\*required):** [webhook\*](#list_codepipeline-resource-webhook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableStageTransition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DisableStageTransition.html)  **
  - **Description:** Grants permission to prevent revisions from transitioning to the next stage in a pipeline
  - **Resource types (\*required):** [stage\*](#list_codepipeline-resource-stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableStageTransition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_EnableStageTransition.html)  **
  - **Description:** Grants permission to allow revisions to transition to the next stage in a pipeline
  - **Resource types (\*required):** [stage\*](#list_codepipeline-resource-stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetActionType.html)  **
  - **Description:** Grants permission to view information about an action type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJobDetails](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetJobDetails.html)  **
  - **Description:** Grants permission to view information about a job (custom actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipeline.html)  **
  - **Description:** Grants permission to retrieve information about a pipeline structure
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipelineExecution.html)  **
  - **Description:** Grants permission to view information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPipelineState](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipelineState.html)  **
  - **Description:** Grants permission to view information about the current state of the stages and actions of a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetThirdPartyJobDetails](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetThirdPartyJobDetails.html)  **
  - **Description:** Grants permission to view the details of a job for a third-party action (partner actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListActionExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListActionExecutions.html)  **
  - **Description:** Grants permission to list the action executions that have occurred in a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListActionTypes](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListActionTypes.html)  **
  - **Description:** Grants permission to list a summary of all the action types available for pipelines in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDeployActionExecutionTargets](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListDeployActionExecutionTargets.html)  **
  - **Description:** Grants permission to list the deployment details for deploy action executions that have occurred in a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPipelineExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelineExecutions.html)  **
  - **Description:** Grants permission to list a summary of the most recent executions for a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPipelines](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelines.html)  **
  - **Description:** Grants permission to list a summary of all the pipelines associated with your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRuleExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListRuleExecutions.html)  **
  - **Description:** Grants permission to list the rule executions that have occurred in a pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListRuleTypes](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListRuleTypes.html)  **
  - **Description:** Grants permission to list a summary of all the rule types available for pipelines in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a CodePipeline resource
  - **Resource types (\*required):** [actiontype](#list_codepipeline-resource-actiontype) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pipeline](#list_codepipeline-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [webhook](#list_codepipeline-resource-webhook) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWebhooks](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListWebhooks.html)  **
  - **Description:** Grants permission to list all of the webhooks associated with your AWS account
  - **Resource types (\*required):** [webhook\*](#list_codepipeline-resource-webhook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [OverrideStageCondition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_OverrideStageCondition.html)  **
  - **Description:** Grants permission to resume the pipeline execution by overriding a condition in a stage
  - **Resource types (\*required):** [stage\*](#list_codepipeline-resource-stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PollForJobs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForJobs.html)  **
  - **Description:** Grants permission to view information about any jobs for CodePipeline to act on
  - **Resource types (\*required):** [actiontype\*](#list_codepipeline-resource-actiontype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PollForThirdPartyJobs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForThirdPartyJobs.html)  **
  - **Description:** Grants permission to determine whether there are any third-party jobs for a job worker to act on (partner actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutActionRevision](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutActionRevision.html)  **
  - **Description:** Grants permission to edit actions in a pipeline
  - **Resource types (\*required):** [action\*](#list_codepipeline-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutApprovalResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutApprovalResult.html)  **
  - **Description:** Grants permission to provide a response (Approved or Rejected) to a manual approval request in CodePipeline
  - **Resource types (\*required):** [action\*](#list_codepipeline-resource-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutJobFailureResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutJobFailureResult.html)  **
  - **Description:** Grants permission to represent the failure of a job as returned to the pipeline by a job worker (custom actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutJobSuccessResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutJobSuccessResult.html)  **
  - **Description:** Grants permission to represent the success of a job as returned to the pipeline by a job worker (custom actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutThirdPartyJobFailureResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutThirdPartyJobFailureResult.html)  **
  - **Description:** Grants permission to represent the failure of a third-party job as returned to the pipeline by a job worker (partner actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutThirdPartyJobSuccessResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutThirdPartyJobSuccessResult.html)  **
  - **Description:** Grants permission to represent the success of a third-party job as returned to the pipeline by a job worker (partner actions only)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutWebhook](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutWebhook.html)  **
  - **Description:** Grants permission to create or update a webhook
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Resource types (\*required):** [webhook\*](#list_codepipeline-resource-webhook) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Access level:** Write

- **   [RegisterWebhookWithThirdParty](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RegisterWebhookWithThirdParty.html)  **
  - **Description:** Grants permission to register a webhook with the third party specified in its configuration
  - **Resource types (\*required):** [webhook\*](#list_codepipeline-resource-webhook)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RetryStageExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RetryStageExecution.html)  **
  - **Description:** Grants permission to resume the pipeline execution by retrying the last failed actions in a stage
  - **Resource types (\*required):** [stage\*](#list_codepipeline-resource-stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RollbackStage](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RollbackStage.html)  **
  - **Description:** Grants permission to rollback the stage to a previous successful execution
  - **Resource types (\*required):** [stage\*](#list_codepipeline-resource-stage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html)  **
  - **Description:** Grants permission to run the most recent revision through the pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StopPipelineExecution.html)  **
  - **Description:** Grants permission to stop an in-progress pipeline execution
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a CodePipeline resource
  - **Resource types (\*required):** [actiontype](#list_codepipeline-resource-actiontype) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Resource types (\*required):** [pipeline](#list_codepipeline-resource-pipeline) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Resource types (\*required):** [webhook](#list_codepipeline-resource-webhook) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_codepipeline-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a CodePipeline resource
  - **Resource types (\*required):** [actiontype](#list_codepipeline-resource-actiontype) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Resource types (\*required):** [pipeline](#list_codepipeline-resource-pipeline) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Resource types (\*required):** [webhook](#list_codepipeline-resource-webhook) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codepipeline-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UpdateActionType.html)  **
  - **Description:** Grants permission to update an action type
  - **Resource types (\*required):** [actiontype\*](#list_codepipeline-resource-actiontype)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UpdatePipeline.html)  **
  - **Description:** Grants permission to update a pipeline with changes to the structure of the pipeline
  - **Resource types (\*required):** [pipeline\*](#list_codepipeline-resource-pipeline)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS CodePipeline
<a name="list_codepipeline-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [action](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format)  | arn:${Partition}:codepipeline:${Region}:${Account}:${PipelineName}/${StageName}/${ActionName} | [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_) | 
|  [actiontype](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format)  | arn:${Partition}:codepipeline:${Region}:${Account}:actiontype:${Owner}/${Category}/${Provider}/${Version} | [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_) | 
|  [pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format)  | arn:${Partition}:codepipeline:${Region}:${Account}:${PipelineName} | [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_) | 
|  [stage](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format)  | arn:${Partition}:codepipeline:${Region}:${Account}:${PipelineName}/${StageName} | [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_) | 
|  [webhook](https://docs.aws.amazon.com/codepipeline/latest/userguide/iam-access-control-identity-based.html#ACP_ARN_Format)  | arn:${Partition}:codepipeline:${Region}:${Account}:webhook:${WebhookName} | [aws:ResourceTag/${TagKey}](#list_codepipeline-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS CodePipeline
<a name="list_codepipeline-policy-keys"></a>

AWS CodePipeline defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters actions based on the presence of tag keys in the request | ArrayOfString | 