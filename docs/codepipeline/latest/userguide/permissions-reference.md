

# permissions reference
<a name="permissions-reference"></a>

Use the following table as a reference when you are setting up access control and writing permissions policies that you can attach to an IAM identity (identity-based policies). The table lists each API operation and the corresponding actions for which you can grant permissions to perform the action. For operations that support *resource-level permissions*, the table lists the AWS resource for which you can grant the permissions. You specify the actions in the policy's `Action` field.

*Resource-level permissions* are those that allow you to specify which resources users are allowed to perform actions on. AWS CodePipeline provides partial support for resource-level permissions. This means that for some AWS CodePipeline API calls, you can control when users are allowed to use those actions based on conditions that must be met, or which resources users are allowed to use. For example, you can grant users permission to list pipeline execution information, but only for a specific pipeline or pipelines.

**Note**  
The **Resources** column lists the resource required for API calls that support resource-level permissions. For API calls that do not support resource-level permissions, you can grant users permission to use it, but you have to specify a wildcard (\*) for the resource element of your policy statement.




**API Operations and required permissions for actions**  


- ** [AcknowledgeJob](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_AcknowledgeJob.html) **
  - **Required permissions (API actions):** `codepipeline:AcknowledgeJob`<br />Required to view information about a specified job and whether that job has been received by the job worker. Used for custom actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [AcknowledgeThirdPartyJob](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_AcknowledgeThirdPartyJob.html) **
  - **Required permissions (API actions):** `codepipeline:AcknowledgeThirdPartyJob`<br />Required to confirm a job worker has received the specified job. Used for partner actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [CreateCustomActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreateCustomActionType.html) **
  - **Required permissions (API actions):** `codepipeline:CreateCustomActionType`<br />Required to create a custom action that can be used in all pipelines associated with the AWS account. Used for custom actions only.
  - **Resources:** Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`

- ** [CreatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_CreatePipeline.html) **
  - **Required permissions (API actions):** `codepipeline:CreatePipeline`<br />Required to create a pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [DeleteCustomActionType](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeleteCustomActionType.html) **
  - **Required permissions (API actions):** `codepipeline:DeleteCustomActionType`<br />Required to mark a custom action as deleted. `PollForJobs` for the custom action fails after the action is marked for deletion. Used for custom actions only.
  - **Resources:** Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`

- ** [DeletePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeletePipeline.html) **
  - **Required permissions (API actions):** `codepipeline:DeletePipeline`<br />Required to delete a pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- **[DeleteWebhook](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeleteWebhook.html)**
  - **Required permissions (API actions):** `codepipeline:DeleteWebhook`<br />Required to delete a webhook.
  - **Resources:** Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [DeregisterWebhookWithThirdParty](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DeregisterWebhookWithThirdParty.html) **
  - **Required permissions (API actions):** `codepipeline:DeregisterWebhookWithThirdParty`<br />Before a webhook is deleted, required to remove the connection between the webhook that was created by CodePipeline and the external tool with events to be detected. Currently supported only for webhooks that target an action type of GitHub.
  - **Resources:** Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [DisableStageTransition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_DisableStageTransition.html) **
  - **Required permissions (API actions):** `codepipeline:DisableStageTransition`<br />Required to prevent artifacts in a pipeline from transitioning to the next stage in the pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [EnableStageTransition](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_EnableStageTransition.html) **
  - **Required permissions (API actions):** `codepipeline:EnableStageTransition`<br />Required to enable artifacts in a pipeline to transition to a stage in a pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [GetJobDetails](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetJobDetails.html) **
  - **Required permissions (API actions):** `codepipeline:GetJobDetails`<br />Required to retrieve information about a job. Used for custom actions only.
  - **Resources:** No resource required.

- ** [GetPipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipeline.html) **
  - **Required permissions (API actions):** `codepipeline:GetPipeline`<br />Required to retrieve the structure, stages, actions, and metadata of a pipeline, including the pipeline ARN.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [GetPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipelineExecution.html) **
  - **Required permissions (API actions):** `codepipeline:GetPipelineExecution`<br />Required to retrieve information about an execution of a pipeline, including details about artifacts, the pipeline execution ID, and the name, version, and status of the pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [GetPipelineState](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetPipelineState.html) **
  - **Required permissions (API actions):** `codepipeline:GetPipelineState`<br />Required to retrieve information about the state of a pipeline, including the stages and actions.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [GetThirdPartyJobDetails](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_GetThirdPartyJobDetails.html) **
  - **Required permissions (API actions):** `codepipeline:GetThirdPartyJobDetails`<br />Required to request the details of a job for a third-party action. Used for partner actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- **[ListActionExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListActionExecutions.html)**
  - **Required permissions (API actions):** `codepipeline:ListActionExecutions`<br />Required to generate a summary of all executions for an action.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [ListActionTypes](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListActionTypes.html) **
  - **Required permissions (API actions):** `codepipeline:ListActionTypes`<br />Required to generate a summary of all CodePipeline action types associated with your account.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [ListPipelineExecutions](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelineExecutions.html) **
  - **Required permissions (API actions):** `codepipeline:ListPipelineExecutions`<br />Required to generate a summary of the most recent executions for a pipeline.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [ListPipelines](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListPipelines.html) **
  - **Required permissions (API actions):** `codepipeline:ListPipelines`<br />Required to generate a summary of all of the pipelines associated with your account.
  - **Resources:** Pipeline ARN with wildcard (resource-level permissions at the pipeline name level are not supported)<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{*}}`

- **[ListTagsForResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListTagsForResource.html)**
  - **Required permissions (API actions):** `codepipeline:ListTagsForResource`<br />Required to list tags for a specified resource.<br />Resources are optional.
  - **Resources:**
    - Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`
    - Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`
    - Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- **[ListWebhooks](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ListWebhooks.html)**
  - **Required permissions (API actions):** `codepipeline:ListWebhooks`<br />Required to list all of the webhooks in the account for that Region.
  - **Resources:** Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [PollForJobs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForJobs.html) **
  - **Required permissions (API actions):** `codepipeline:PollForJobs`<br />Required to get a listing of all of the webhooks in this Region for this account.
  - **Resources:** Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`

- ** [PollForThirdPartyJobs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PollForThirdPartyJobs.html) **
  - **Required permissions (API actions):** `codepipeline:PollForThirdPartyJobs`<br />Required to determine whether there are any third-party jobs for a job worker to act on. Used for partner actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [PutActionRevision](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutActionRevision.html) **
  - **Required permissions (API actions):** `codepipeline:PutActionRevision`<br />Required to report information to CodePipeline about new revisions to a source
  - **Resources:** Action<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}/{{stage-name}}/{{action-name}}`

- ** [PutApprovalResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutApprovalResult.html) **
  - **Required permissions (API actions):** `codepipeline:PutApprovalResult`<br />Required to report the response to a manual approval request to CodePipeline. Valid responses are `Approved` and `Rejected`.
  - **Resources:** Action<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}/{{stage-name}}/{{action-name}}` This API call supports resource-level permissions. However, you might encounter an error if you use the IAM console or Policy Generator to create policies with `"codepipeline:PutApprovalResult"` that specify a resource ARN. If you encounter an error, you can use the **JSON** tab in the IAM console or the CLI to create a policy. 

- ** [PutJobFailureResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutJobFailureResult.html) **
  - **Required permissions (API actions):** `codepipeline:PutJobFailureResult`<br />Required to report the failure of a job as returned to the pipeline by a job worker. Used for custom actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [PutJobSuccessResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutJobSuccessResult.html) **
  - **Required permissions (API actions):** `codepipeline:PutJobSuccessResult`<br />Required to report the success of a job as returned to the pipeline by a job worker. Used for custom actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [PutThirdPartyJobFailureResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutThirdPartyJobFailureResult.html) **
  - **Required permissions (API actions):** `codepipeline:PutThirdPartyJobFailureResult`<br />Required to report the failure of a third-party job as returned to the pipeline by a job worker. Used for partner actions only.
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [PutThirdPartyJobSuccessResult](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutThirdPartyJobSuccessResult.html) **
  - **Required permissions (API actions):** `codepipeline:PutThirdPartyJobSuccessResult`<br />Required to report the success of a third-party job as returned to the pipeline by a job worker. Used for partner actions only. 
  - **Resources:** Supports only a wildcard (\*) in the policy Resource element.

- ** [PutWebhook](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_PutWebhook.html) **
  - **Required permissions (API actions):** `codepipeline:PutWebhook`<br />Required to create a webhook.
  - **Resources:**
    - Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`
    - Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [RegisterWebhookWithThirdParty](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RegisterWebhookWithThirdParty.html) **
  - **Required permissions (API actions):** `codepipeline:RegisterWebhookWithThirdParty`<br />After a webhook is created, required to configure supported third parties to call the generated webhook URL.
  - **Resources:** Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [RetryStageExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_RetryStageExecution.html) **
  - **Required permissions (API actions):** `codepipeline:RetryStageExecution`<br />Required to resume the pipeline execution by retrying the last failed actions in a stage.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}/{{stage-name}}`

- ** [StartPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StartPipelineExecution.html) **
  - **Required permissions (API actions):** `codepipeline:StartPipelineExecution`<br />Required to start the specified pipeline (specifically, to start processing the latest commit to the source location specified as part of the pipeline).
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- ** [StopPipelineExecution](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_StopPipelineExecution.html) **
  - **Required permissions (API actions):** `codepipeline:StopPipelineExecution`<br />Required to stop the specified pipeline execution. You choose to either stop the pipeline execution by completing in-progress actions without starting subsequent actions, or by abandoning in-progress actions. 
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

- **[TagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_TagResource.html)**
  - **Required permissions (API actions):** `codepipeline:TagResource`<br />Required to tag the specified resource.<br />Resources are optional.
  - **Resources:**
    - Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`
    - Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`
    - Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- **[UntagResource](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UntagResource.html)**
  - **Required permissions (API actions):** `codepipeline:UntagResource`<br />Required to untag the specified resource.<br />Resources are optional.<br />
  - **Resources:**
    - Action Type<br />`arn:aws:codepipeline:{{region}}:{{account}}:actiontype:{{owner}}/{{category}}/{{provider}}/{{version}}`
    - Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`
    - Webhook<br />`arn:aws:codepipeline:{{region}}:{{account}}:webhook:{{webhook-name}}`

- ** [UpdatePipeline](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_UpdatePipeline.html) **
  - **Required permissions (API actions):** `codepipeline:UpdatePipeline`<br />Required to update a specified pipeline with edits or changes to its structure.
  - **Resources:** Pipeline<br />`arn:aws:codepipeline:{{region}}:{{account}}:{{pipeline-name}}`

