

# Actions, resources, and condition keys for AWS MWAA Serverless
<a name="list_mwaa-serverless"></a>

AWS MWAA Serverless (service prefix: `airflow-serverless`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/airflow-serverless/airflow-serverless.json) for this service.

**Topics**
+ [API operations defined by AWS MWAA Serverless](#list_mwaa-serverless-operations)
+ [Actions defined by AWS MWAA Serverless](#list_mwaa-serverless-actions-as-permissions)
+ [Resource types defined by AWS MWAA Serverless](#list_mwaa-serverless-resources-for-iam-policies)
+ [Condition keys for AWS MWAA Serverless](#list_mwaa-serverless-policy-keys)

## API operations defined by AWS MWAA Serverless
<a name="list_mwaa-serverless-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_mwaa-serverless-actions-as-permissions).




- **   CreateWorkflow  **
  - **IAM action:**  [airflow-serverless:CreateWorkflow](#list_mwaa-serverless-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [airflow-serverless:TagResource](#list_mwaa-serverless-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** airflow-serverless.amazonaws.com / **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [airflow-serverless:DeleteWorkflow](#list_mwaa-serverless-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetTaskInstance  **
  - **IAM action:**  [airflow-serverless:GetTaskInstance](#list_mwaa-serverless-action-GetTaskInstance) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [airflow-serverless:GetWorkflow](#list_mwaa-serverless-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowRun  **
  - **IAM action:**  [airflow-serverless:GetWorkflowRun](#list_mwaa-serverless-action-GetWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [airflow-serverless:ListTagsForResource](#list_mwaa-serverless-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTaskInstances  **
  - **IAM action:**  [airflow-serverless:ListTaskInstances](#list_mwaa-serverless-action-ListTaskInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowRuns  **
  - **IAM action:**  [airflow-serverless:ListWorkflowRuns](#list_mwaa-serverless-action-ListWorkflowRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowVersions  **
  - **IAM action:**  [airflow-serverless:ListWorkflowVersions](#list_mwaa-serverless-action-ListWorkflowVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [airflow-serverless:ListWorkflows](#list_mwaa-serverless-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartWorkflowRun  **
  - **IAM action:**  [airflow-serverless:StartWorkflowRun](#list_mwaa-serverless-action-StartWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopWorkflowRun  **
  - **IAM action:**  [airflow-serverless:StopWorkflowRun](#list_mwaa-serverless-action-StopWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [airflow-serverless:TagResource](#list_mwaa-serverless-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [airflow-serverless:UntagResource](#list_mwaa-serverless-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateWorkflow  **
  - **IAM action:**  [airflow-serverless:UpdateWorkflow](#list_mwaa-serverless-action-UpdateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** airflow-serverless.amazonaws.com / **Access level:** Write



## Actions defined by AWS MWAA Serverless
<a name="list_mwaa-serverless-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html)  **
  - **Description:** Grants permission to create a new workflow
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mwaa-serverless-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-serverless-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to delete a workflow
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetTaskInstance](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetTaskInstance.html)  **
  - **Description:** Grants permission to retrieve the task details for a workflow run
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflow.html)  **
  - **Description:** Grants permission to retrieve details about a workflow
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_GetWorkflowRun.html)  **
  - **Description:** Grants permission to retrieve details about a workflow run
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTaskInstances](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListTaskInstances.html)  **
  - **Description:** Grants permission to list the tasks for a workflow run
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflowRuns](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflowRuns.html)  **
  - **Description:** Grants permission to list the workflow runs of a workflow
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflowVersions](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflowVersions.html)  **
  - **Description:** Grants permission to list the workflow versions
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_ListWorkflows.html)  **
  - **Description:** Grants permission to list the workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StartWorkflowRun.html)  **
  - **Description:** Grants permission to start an on-demand workflow run for the workflow
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopWorkflowRun](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_StopWorkflowRun.html)  **
  - **Description:** Grants permission to stop a workflow run
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag the specified resource
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_mwaa-serverless-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag the specified resource
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_mwaa-serverless-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateWorkflow](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UpdateWorkflow.html)  **
  - **Description:** Grants permission to update an existing workflow
  - **Resource types (\*required):** [Workflow\*](#list_mwaa-serverless-resource-Workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS MWAA Serverless
<a name="list_mwaa-serverless-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Workflow](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/workflows.html)  | arn:${Partition}:airflow-serverless:${Region}:${Account}:workflow/${WorkflowId} | [aws:ResourceTag/${TagKey}](#list_mwaa-serverless-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS MWAA Serverless
<a name="list_mwaa-serverless-policy-keys"></a>

AWS MWAA Serverless defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs that are attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 