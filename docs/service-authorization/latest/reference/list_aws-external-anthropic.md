

# Actions, resources, and condition keys for Claude Platform on AWS
<a name="list_aws-external-anthropic"></a>

Claude Platform on AWS (service prefix: `aws-external-anthropic`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/claude-platform/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/claude-platform/latest/userguide/making-requests.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-external-anthropic/aws-external-anthropic.json) for this service.

**Topics**
+ [Actions defined by Claude Platform on AWS](#list_aws-external-anthropic-actions-as-permissions)
+ [Permission-only actions for Claude Platform on AWS](#list_aws-external-anthropic-permission-only-actions)
+ [Resource types defined by Claude Platform on AWS](#list_aws-external-anthropic-resources-for-iam-policies)
+ [Condition keys for Claude Platform on AWS](#list_aws-external-anthropic-policy-keys)

## Actions defined by Claude Platform on AWS
<a name="list_aws-external-anthropic-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [ArchiveAgent](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a managed agent
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveEnvironment](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a managed agent environment
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveMemoryStore](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a memory store
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveSession](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a managed agent session
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveVault](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a credential vault
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ArchiveWorkspace](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to archive a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssumeConsole](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to assume console access on Claude Platform
  - **Resource types (\*required):** 
  - **Condition keys:** [aws-external-anthropic:Capability](#list_aws-external-anthropic-aws-external-anthropic_Capability)
  - **Access level:** Write

- **   [CancelBatchInference](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to cancel an in-progress batch inference request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CountTokens](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to count tokens for a message request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgent](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a managed agent in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBatchInference](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a batch inference request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEnvironment](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a managed agent environment in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateFile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to upload a file to a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateInference](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a chat completion inference request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMemoryStore](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a managed agent memory store in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a managed agent session in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSkill](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a skill in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserProfile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a user profile in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateUserProfileEnrollmentUrl](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create an enrollment URL for a user profile
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateVault](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a managed agent credential vault in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWebhook](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a webhook in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWorkspace](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create a workspace in an organization
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_aws-external-anthropic-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_aws-external-anthropic-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteBatchInference](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a batch inference request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEnvironment](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a managed agent environment
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a file from a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMemoryStore](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a memory store
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSession](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a managed agent session
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSkill](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a skill from a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVault](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a credential vault
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWebhook](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to delete a webhook
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountStatus](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve the status of account setup and AWS Marketplace registration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgent](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details or versions of a managed agent
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBatchInference](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a batch inference request
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEnvironment](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a managed agent environment
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve a file or its content from a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMemoryStore](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a memory store, its memories, or its memory versions
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetModel](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve information about a specific model
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSession](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details, events, or resources of a managed agent session
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSkill](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a skill or its versions
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUserProfile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a user profile
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVault](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a credential vault or its credentials
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWebhook](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a webhook
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkspace](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to retrieve details of a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAgents](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list managed agents in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBatchInferences](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list batch inference requests in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListEnvironments](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list managed agent environments in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFiles](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list files in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListMemoryStores](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list managed agent memory stores in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListModels](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list available models in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSessions](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list managed agent sessions in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSkills](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list skills in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [workspace](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUserProfiles](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list user profiles in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListVaults](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list managed agent credential vaults in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWebhooks](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list webhooks in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkspaces](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to list workspaces in an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ProcessEnvironmentWork](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to process work items in a self-hosted managed agent environment
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RotateWebhookSecret](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to rotate the signing secret of a webhook
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [workspace](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_aws-external-anthropic-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_aws-external-anthropic-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [workspace](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_aws-external-anthropic-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgent](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a managed agent
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateEnvironment](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a managed agent environment
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMemoryStore](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a memory store, mutate its memories, or redact a memory version
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSession](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a managed agent session, append session events, or manage its resources
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSkill](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to create or delete a skill version
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUserProfile](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a user profile in a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVault](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a credential vault or manage its stored credentials
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWebhook](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a webhook
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkspace](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html#iam-actions)  **
  - **Description:** Grants permission to update a workspace
  - **Resource types (\*required):** [workspace\*](#list_aws-external-anthropic-resource-workspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Claude Platform on AWS
<a name="list_aws-external-anthropic-permission-only-actions"></a>

The following actions are defined by Claude Platform on AWS but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CallWithBearerToken](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-actions.html)  | Grants permission to make API calls using bearer token authentication |  | [aws-external-anthropic:BearerTokenType](#list_aws-external-anthropic-aws-external-anthropic_BearerTokenType) | List | 

## Resource types defined by Claude Platform on AWS
<a name="list_aws-external-anthropic-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [workspace](https://docs.aws.amazon.com/claude-platform/latest/userguide/workspaces.html#workspaces)  | arn:${Partition}:aws-external-anthropic:${Region}:${Account}:workspace/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_aws-external-anthropic-aws_ResourceTag___TagKey_) | 

## Condition keys for Claude Platform on AWS
<a name="list_aws-external-anthropic-policy-keys"></a>

Claude Platform on AWS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws-external-anthropic:BearerTokenType](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-policies.html)  | Filters access by the Short-term or Long-term bearer tokens | String | 
|   [aws-external-anthropic:CalledViaConsole](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-policies.html)  | Filters access by the use of the Claude Platform console | Bool | 
|   [aws-external-anthropic:Capability](https://docs.aws.amazon.com/claude-platform/latest/userguide/iam-policies.html)  | Filters access by the Claude Platform role used for the console session | String | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 