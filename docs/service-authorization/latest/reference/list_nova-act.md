# Actions, resources, and condition keys for Amazon Nova Act

Amazon Nova Act (service prefix: `nova-act`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../nova-act/latest/userguide/what-is-nova-act.md "../../../nova-act/latest/userguide/what-is-nova-act.md").
- View a list of the [API operations available for
  this service](../../../nova-act/latest/APIReference/API_Operations.md "../../../nova-act/latest/APIReference/API_Operations.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../nova-act/latest/userguide/security-iam-service-with-iam.md "../../../nova-act/latest/userguide/security-iam-service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/nova-act/nova-act.json "https://servicereference.us-east-1.amazonaws.com/v1/nova-act/nova-act.json") for this service.

###### Topics

- [API operations defined by Amazon Nova Act](#list_nova-act-operations "#list_nova-act-operations")
- [Actions defined by Amazon Nova Act](#list_nova-act-actions-as-permissions "#list_nova-act-actions-as-permissions")
- [Resource types defined by Amazon Nova Act](#list_nova-act-resources-for-iam-policies "#list_nova-act-resources-for-iam-policies")
- [Condition keys for Amazon Nova Act](#list_nova-act-policy-keys "#list_nova-act-policy-keys")

## API operations defined by Amazon Nova Act

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_nova-act-actions-as-permissions "#list_nova-act-actions-as-permissions").

| Operation                | IAM action                                                                                                                           | Condition key | Possible value(s) | Access level |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------------- | ------------ |
| CreateAct                | [nova-act:CreateAct](#list_nova-act-action-CreateAct "#list_nova-act-action-CreateAct")                                              |               |                   | Write        |
| CreateSession            | [nova-act:CreateSession](#list_nova-act-action-CreateSession "#list_nova-act-action-CreateSession")                                  |               |                   | Write        |
| CreateWorkflowDefinition | [nova-act:CreateWorkflowDefinition](#list_nova-act-action-CreateWorkflowDefinition "#list_nova-act-action-CreateWorkflowDefinition") |               |                   | Write        |
| CreateWorkflowRun        | [nova-act:CreateWorkflowRun](#list_nova-act-action-CreateWorkflowRun "#list_nova-act-action-CreateWorkflowRun")                      |               |                   | Write        |
| DeleteWorkflowDefinition | [nova-act:DeleteWorkflowDefinition](#list_nova-act-action-DeleteWorkflowDefinition "#list_nova-act-action-DeleteWorkflowDefinition") |               |                   | Write        |
| DeleteWorkflowRun        | [nova-act:DeleteWorkflowRun](#list_nova-act-action-DeleteWorkflowRun "#list_nova-act-action-DeleteWorkflowRun")                      |               |                   | Write        |
| GetWorkflowDefinition    | [nova-act:GetWorkflowDefinition](#list_nova-act-action-GetWorkflowDefinition "#list_nova-act-action-GetWorkflowDefinition")          |               |                   | Read         |
| GetWorkflowRun           | [nova-act:GetWorkflowRun](#list_nova-act-action-GetWorkflowRun "#list_nova-act-action-GetWorkflowRun")                               |               |                   | Read         |
| InvokeActStep            | [nova-act:InvokeActStep](#list_nova-act-action-InvokeActStep "#list_nova-act-action-InvokeActStep")                                  |               |                   | Write        |
| ListActs                 | [nova-act:ListActs](#list_nova-act-action-ListActs "#list_nova-act-action-ListActs")                                                 |               |                   | Read         |
| ListModels               | [nova-act:ListModels](#list_nova-act-action-ListModels "#list_nova-act-action-ListModels")                                           |               |                   | Read         |
| ListSessions             | [nova-act:ListSessions](#list_nova-act-action-ListSessions "#list_nova-act-action-ListSessions")                                     |               |                   | Read         |
| ListWorkflowDefinitions  | [nova-act:ListWorkflowDefinitions](#list_nova-act-action-ListWorkflowDefinitions "#list_nova-act-action-ListWorkflowDefinitions")    |               |                   | List         |
| ListWorkflowRuns         | [nova-act:ListWorkflowRuns](#list_nova-act-action-ListWorkflowRuns "#list_nova-act-action-ListWorkflowRuns")                         |               |                   | List         |
| UpdateAct                | [nova-act:UpdateAct](#list_nova-act-action-UpdateAct "#list_nova-act-action-UpdateAct")                                              |               |                   | Write        |
| UpdateWorkflowRun        | [nova-act:UpdateWorkflowRun](#list_nova-act-action-UpdateWorkflowRun "#list_nova-act-action-UpdateWorkflowRun")                      |               |                   | Write        |

## Actions defined by Amazon Nova Act

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                   | Description                                                                                                                                     | Resource types (\*required)                                                                                        | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | -------------- | ------------ |
| [CreateAct](../../../nova-act/latest/APIReference/API_CreateAct.md "../../../nova-act/latest/APIReference/API_CreateAct.md")                                              | Grants permission to create a new AI task (act) within a session that can interact with tools and perform specific actions                      | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [CreateSession](../../../nova-act/latest/APIReference/API_CreateSession.md "../../../nova-act/latest/APIReference/API_CreateSession.md")                                  | Grants permission to create a new session context within a workflow run to manage conversation state and acts                                   | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [CreateWorkflowDefinition](../../../nova-act/latest/APIReference/API_CreateWorkflowDefinition.md "../../../nova-act/latest/APIReference/API_CreateWorkflowDefinition.md") | Grants permission to create a new workflow definition template that can be used to execute multiple workflow runs                               | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [CreateWorkflowRun](../../../nova-act/latest/APIReference/API_CreateWorkflowRun.md "../../../nova-act/latest/APIReference/API_CreateWorkflowRun.md")                      | Grants permission to create a new execution instance of a workflow definition with specified parameters                                         | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [DeleteWorkflowDefinition](../../../nova-act/latest/APIReference/API_DeleteWorkflowDefinition.md "../../../nova-act/latest/APIReference/API_DeleteWorkflowDefinition.md") | Grants permission to delete a workflow definition and all associated resources                                                                  | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [DeleteWorkflowRun](../../../nova-act/latest/APIReference/API_DeleteWorkflowRun.md "../../../nova-act/latest/APIReference/API_DeleteWorkflowRun.md")                      | Grants permission to terminate and clean up a workflow run, stopping all associated acts and sessions                                           | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [GetWorkflowDefinition](../../../nova-act/latest/APIReference/API_GetWorkflowDefinition.md "../../../nova-act/latest/APIReference/API_GetWorkflowDefinition.md")          | Grants permission to retrieve details and configuration of a specific workflow definition                                                       | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Read         |
| [GetWorkflowRun](../../../nova-act/latest/APIReference/API_GetWorkflowRun.md "../../../nova-act/latest/APIReference/API_GetWorkflowRun.md")                               | Grants permission to retrieve the current state, configuration, and execution details of a workflow run                                         | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Read         |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [InvokeActStep](../../../nova-act/latest/APIReference/API_InvokeActStep.md "../../../nova-act/latest/APIReference/API_InvokeActStep.md")                                  | Grants permission to execute the next step of an act, processing tool call results and returning new tool calls if needed                       | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [ListActs](../../../nova-act/latest/APIReference/API_ListActs.md "../../../nova-act/latest/APIReference/API_ListActs.md")                                                 | Grants permission to list all acts within a specific session with their current status and execution details                                    | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Read         |
| [ListModels](../../../nova-act/latest/APIReference/API_ListModels.md "../../../nova-act/latest/APIReference/API_ListModels.md")                                           | Grants permission to list all available AI models that can be used for workflow execution, including their status and compatibility information |                                                                                                                    |                | Read         |
| [ListSessions](../../../nova-act/latest/APIReference/API_ListSessions.md "../../../nova-act/latest/APIReference/API_ListSessions.md")                                     | Grants permission to list all sessions within a specific workflow run                                                                           | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Read         |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [ListWorkflowDefinitions](../../../nova-act/latest/APIReference/API_ListWorkflowDefinitions.md "../../../nova-act/latest/APIReference/API_ListWorkflowDefinitions.md")    | Grants permission to list all workflow definitions in your account with optional filtering and pagination                                       |                                                                                                                    |                | List         |
| [ListWorkflowRuns](../../../nova-act/latest/APIReference/API_ListWorkflowRuns.md "../../../nova-act/latest/APIReference/API_ListWorkflowRuns.md")                         | Grants permission to list all workflow runs for a specific workflow definition with optional filtering and pagination                           | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | List         |
| [UpdateAct](../../../nova-act/latest/APIReference/API_UpdateAct.md "../../../nova-act/latest/APIReference/API_UpdateAct.md")                                              | Grants permission to update an existing act's configuration, status, or error information                                                       | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |
| [UpdateWorkflowRun](../../../nova-act/latest/APIReference/API_UpdateWorkflowRun.md "../../../nova-act/latest/APIReference/API_UpdateWorkflowRun.md")                      | Grants permission to update the configuration or state of an active workflow run                                                                | [workflow-definition\*](#list_nova-act-resource-workflow-definition "#list_nova-act-resource-workflow-definition") |                | Write        |
| [workflow-run\*](#list_nova-act-resource-workflow-run "#list_nova-act-resource-workflow-run")                                                                             |                                                                                                                                                 |

## Resource types defined by Amazon Nova Act

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                               | ARN                                                                                                                        | Condition keys |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [workflow-definition](../../../nova-act/latest/userguide/workflow-definition.md "../../../nova-act/latest/userguide/workflow-definition.md") | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName}                               |                |
| [workflow-run](../../../nova-act/latest/userguide/workflow-run.md "../../../nova-act/latest/userguide/workflow-run.md")                      | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName}/workflow-run/${WorkflowRunId} |                |

## Condition keys for Amazon Nova Act

Amazon Nova Act has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
