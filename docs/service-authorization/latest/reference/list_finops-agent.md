

# Actions, resources, and condition keys for AWS FinOps Agent
<a name="list_finops-agent"></a>

AWS FinOps Agent (service prefix: `finops-agent`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/finops-agent/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/finops-agent/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/finops-agent/) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/finops-agent/finops-agent.json) for this service.

**Topics**
+ [Actions defined by AWS FinOps Agent](#list_finops-agent-actions-as-permissions)
+ [Permission-only actions for AWS FinOps Agent](#list_finops-agent-permission-only-actions)
+ [Resource types defined by AWS FinOps Agent](#list_finops-agent-resources-for-iam-policies)
+ [Condition keys for AWS FinOps Agent](#list_finops-agent-policy-keys)

## Actions defined by AWS FinOps Agent
<a name="list_finops-agent-actions-as-permissions"></a>

AWS FinOps Agent has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS FinOps Agent
<a name="list_finops-agent-permission-only-actions"></a>

The following actions are defined by AWS FinOps Agent but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptAgentRequest](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to accept a pending approval request from the agent |  |   | Write | 
|   [CancelTask](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to cancel a task |  |   | Write | 
|   [CancelTurn](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to cancel an in-progress conversation turn |  |   | Write | 
|   [CreateAgentSpace](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a new FinOps Agent workspace |  |   | Write | 
|   [CreateAutomation](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a reusable automation |  |   | Write | 
|   [CreateConnection](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a connection |  |   | Write | 
|   [CreateConversation](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a new conversation with the FinOps Agent |  |   | Write | 
|   [CreateDocument](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a document |  |   | Write | 
|   [CreateIntegration](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a third-party integration |  |   | Write | 
|   [CreateOneTimeLoginSession](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a one-time login session for the FinOps Agent web application |  |   | Write | 
|   [CreateTask](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a task |  |   | Write | 
|   [CreateTurn](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to create a new turn in a conversation |  |   | Write | 
|   [DeleteAgentSpace](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete a FinOps Agent workspace |  |   | Write | 
|   [DeleteArtifact](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete an artifact and its content |  |   | Write | 
|   [DeleteAutomation](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete an automation |  |   | Write | 
|   [DeleteConnection](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete a connection |  |   | Write | 
|   [DeleteDocument](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete a document |  |   | Write | 
|   [DeleteIntegration](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to delete a third-party integration |  |   | Write | 
|   [GetAgentRequest](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a pending approval request from the agent |  |   | Read | 
|   [GetAgentSpace](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a FinOps Agent workspace |  |   | Read | 
|   [GetArtifactContent](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to download artifact content |  |   | Read | 
|   [GetArtifactMetadata](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view artifact metadata |  |   | Read | 
|   [GetAutomation](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of an automation |  |   | Read | 
|   [GetConnection](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a connection |  |   | Read | 
|   [GetDocumentContent](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to download document content |  |   | Read | 
|   [GetDocumentMetadata](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view document metadata |  |   | Read | 
|   [GetIntegration](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a third-party integration |  |   | Read | 
|   [GetTask](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a task |  |   | Read | 
|   [GetTurn](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to view details of a conversation turn |  |   | Read | 
|   [ListAgentSpaces](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list all FinOps Agent workspaces in the account |  |   | List | 
|   [ListArtifacts](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list artifacts |  |   | List | 
|   [ListAutomations](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list automations |  |   | List | 
|   [ListConnections](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list connections |  |   | List | 
|   [ListConversations](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list conversations |  |   | List | 
|   [ListDocuments](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list documents |  |   | List | 
|   [ListIntegrations](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list third-party integrations |  |   | List | 
|   [ListRecords](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list records for real-time agent activity display |  |   | List | 
|   [ListTasks](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list tasks |  |   | List | 
|   [ListTurns](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to list turns in a conversation |  |   | List | 
|   [RejectAgentRequest](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to reject a pending approval request from the agent |  |   | Write | 
|   [RestoreDocument](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to restore an archived document |  |   | Write | 
|   [SendFeedback](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to submit feedback on agent responses |  |   | Write | 
|   [UpdateAgentSpace](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to update a FinOps Agent workspace configuration |  |   | Write | 
|   [UpdateAutomation](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to update an automation |  |   | Write | 
|   [UpdateConnection](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to update a connection |  |   | Write | 
|   [UpdateDocument](https://docs.aws.amazon.com/finops-agent/)  | Grants permission to update a document's content and metadata |  |   | Write | 

## Resource types defined by AWS FinOps Agent
<a name="list_finops-agent-resources-for-iam-policies"></a>

AWS FinOps Agent does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS FinOps Agent
<a name="list_finops-agent-policy-keys"></a>

AWS FinOps Agent has no service-specific condition keys that can be used in the `Condition` element of policy statements.