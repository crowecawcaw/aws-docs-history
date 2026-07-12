# Actions, resources, and condition keys for AWS FinOps Agent

AWS FinOps Agent (service prefix: `finops-agent`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../finops-agent/latest/userguide.md "../../../finops-agent/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../finops-agent.md "../../../finops-agent.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../finops-agent.md "../../../finops-agent.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/finops-agent/finops-agent.json "https://servicereference.us-east-1.amazonaws.com/v1/finops-agent/finops-agent.json") for this service.

###### Topics

- [Actions defined by AWS FinOps Agent](#list_finops-agent-actions-as-permissions "#list_finops-agent-actions-as-permissions")
- [Permission-only actions for AWS FinOps Agent](#list_finops-agent-permission-only-actions "#list_finops-agent-permission-only-actions")
- [Resource types defined by AWS FinOps Agent](#list_finops-agent-resources-for-iam-policies "#list_finops-agent-resources-for-iam-policies")
- [Condition keys for AWS FinOps Agent](#list_finops-agent-policy-keys "#list_finops-agent-policy-keys")

## Actions defined by AWS FinOps Agent

AWS FinOps Agent has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS FinOps Agent

The following actions are defined by AWS FinOps Agent but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                          | Description                                                                               | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AcceptAgentRequest](../../../finops-agent.md "../../../finops-agent.md")        | Grants permission to accept a pending approval request from the agent                     |                             |                | Write        |
| [CancelTask](../../../finops-agent.md "../../../finops-agent.md")                | Grants permission to cancel a task                                                        |                             |                | Write        |
| [CancelTurn](../../../finops-agent.md "../../../finops-agent.md")                | Grants permission to cancel an in-progress conversation turn                              |                             |                | Write        |
| [CreateAgentSpace](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to create a new FinOps Agent workspace                                  |                             |                | Write        |
| [CreateAutomation](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to create a reusable automation                                         |                             |                | Write        |
| [CreateConnection](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to create a connection                                                  |                             |                | Write        |
| [CreateConversation](../../../finops-agent.md "../../../finops-agent.md")        | Grants permission to create a new conversation with the FinOps Agent                      |                             |                | Write        |
| [CreateDocument](../../../finops-agent.md "../../../finops-agent.md")            | Grants permission to create a document                                                    |                             |                | Write        |
| [CreateIntegration](../../../finops-agent.md "../../../finops-agent.md")         | Grants permission to create a third-party integration                                     |                             |                | Write        |
| [CreateOneTimeLoginSession](../../../finops-agent.md "../../../finops-agent.md") | Grants permission to create a one-time login session for the FinOps Agent web application |                             |                | Write        |
| [CreateTask](../../../finops-agent.md "../../../finops-agent.md")                | Grants permission to create a task                                                        |                             |                | Write        |
| [CreateTurn](../../../finops-agent.md "../../../finops-agent.md")                | Grants permission to create a new turn in a conversation                                  |                             |                | Write        |
| [DeleteAgentSpace](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to delete a FinOps Agent workspace                                      |                             |                | Write        |
| [DeleteArtifact](../../../finops-agent.md "../../../finops-agent.md")            | Grants permission to delete an artifact and its content                                   |                             |                | Write        |
| [DeleteAutomation](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to delete an automation                                                 |                             |                | Write        |
| [DeleteConnection](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to delete a connection                                                  |                             |                | Write        |
| [DeleteDocument](../../../finops-agent.md "../../../finops-agent.md")            | Grants permission to delete a document                                                    |                             |                | Write        |
| [DeleteIntegration](../../../finops-agent.md "../../../finops-agent.md")         | Grants permission to delete a third-party integration                                     |                             |                | Write        |
| [GetAgentRequest](../../../finops-agent.md "../../../finops-agent.md")           | Grants permission to view details of a pending approval request from the agent            |                             |                | Read         |
| [GetAgentSpace](../../../finops-agent.md "../../../finops-agent.md")             | Grants permission to view details of a FinOps Agent workspace                             |                             |                | Read         |
| [GetArtifactContent](../../../finops-agent.md "../../../finops-agent.md")        | Grants permission to download artifact content                                            |                             |                | Read         |
| [GetArtifactMetadata](../../../finops-agent.md "../../../finops-agent.md")       | Grants permission to view artifact metadata                                               |                             |                | Read         |
| [GetAutomation](../../../finops-agent.md "../../../finops-agent.md")             | Grants permission to view details of an automation                                        |                             |                | Read         |
| [GetConnection](../../../finops-agent.md "../../../finops-agent.md")             | Grants permission to view details of a connection                                         |                             |                | Read         |
| [GetDocumentContent](../../../finops-agent.md "../../../finops-agent.md")        | Grants permission to download document content                                            |                             |                | Read         |
| [GetDocumentMetadata](../../../finops-agent.md "../../../finops-agent.md")       | Grants permission to view document metadata                                               |                             |                | Read         |
| [GetIntegration](../../../finops-agent.md "../../../finops-agent.md")            | Grants permission to view details of a third-party integration                            |                             |                | Read         |
| [GetTask](../../../finops-agent.md "../../../finops-agent.md")                   | Grants permission to view details of a task                                               |                             |                | Read         |
| [GetTurn](../../../finops-agent.md "../../../finops-agent.md")                   | Grants permission to view details of a conversation turn                                  |                             |                | Read         |
| [ListAgentSpaces](../../../finops-agent.md "../../../finops-agent.md")           | Grants permission to list all FinOps Agent workspaces in the account                      |                             |                | List         |
| [ListArtifacts](../../../finops-agent.md "../../../finops-agent.md")             | Grants permission to list artifacts                                                       |                             |                | List         |
| [ListAutomations](../../../finops-agent.md "../../../finops-agent.md")           | Grants permission to list automations                                                     |                             |                | List         |
| [ListConnections](../../../finops-agent.md "../../../finops-agent.md")           | Grants permission to list connections                                                     |                             |                | List         |
| [ListConversations](../../../finops-agent.md "../../../finops-agent.md")         | Grants permission to list conversations                                                   |                             |                | List         |
| [ListDocuments](../../../finops-agent.md "../../../finops-agent.md")             | Grants permission to list documents                                                       |                             |                | List         |
| [ListIntegrations](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to list third-party integrations                                        |                             |                | List         |
| [ListRecords](../../../finops-agent.md "../../../finops-agent.md")               | Grants permission to list records for real-time agent activity display                    |                             |                | List         |
| [ListTasks](../../../finops-agent.md "../../../finops-agent.md")                 | Grants permission to list tasks                                                           |                             |                | List         |
| [ListTurns](../../../finops-agent.md "../../../finops-agent.md")                 | Grants permission to list turns in a conversation                                         |                             |                | List         |
| [RejectAgentRequest](../../../finops-agent.md "../../../finops-agent.md")        | Grants permission to reject a pending approval request from the agent                     |                             |                | Write        |
| [RestoreDocument](../../../finops-agent.md "../../../finops-agent.md")           | Grants permission to restore an archived document                                         |                             |                | Write        |
| [SendFeedback](../../../finops-agent.md "../../../finops-agent.md")              | Grants permission to submit feedback on agent responses                                   |                             |                | Write        |
| [UpdateAgentSpace](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to update a FinOps Agent workspace configuration                        |                             |                | Write        |
| [UpdateAutomation](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to update an automation                                                 |                             |                | Write        |
| [UpdateConnection](../../../finops-agent.md "../../../finops-agent.md")          | Grants permission to update a connection                                                  |                             |                | Write        |
| [UpdateDocument](../../../finops-agent.md "../../../finops-agent.md")            | Grants permission to update a document's content and metadata                             |                             |                | Write        |

## Resource types defined by AWS FinOps Agent

AWS FinOps Agent does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS FinOps Agent

AWS FinOps Agent has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
