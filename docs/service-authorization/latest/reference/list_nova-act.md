

# Actions, resources, and condition keys for Amazon Nova Act
<a name="list_nova-act"></a>

Amazon Nova Act (service prefix: `nova-act`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/nova-act/latest/userguide/what-is-nova-act.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/nova-act/latest/userguide/security-iam-service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/nova-act/nova-act.json) for this service.

**Topics**
+ [API operations defined by Amazon Nova Act](#list_nova-act-operations)
+ [Actions defined by Amazon Nova Act](#list_nova-act-actions-as-permissions)
+ [Resource types defined by Amazon Nova Act](#list_nova-act-resources-for-iam-policies)
+ [Condition keys for Amazon Nova Act](#list_nova-act-policy-keys)

## API operations defined by Amazon Nova Act
<a name="list_nova-act-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_nova-act-actions-as-permissions).




- **   CreateAct  **
  - **IAM action:**  [nova-act:CreateAct](#list_nova-act-action-CreateAct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSession  **
  - **IAM action:**  [nova-act:CreateSession](#list_nova-act-action-CreateSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkflowDefinition  **
  - **IAM action:**  [nova-act:CreateWorkflowDefinition](#list_nova-act-action-CreateWorkflowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWorkflowRun  **
  - **IAM action:**  [nova-act:CreateWorkflowRun](#list_nova-act-action-CreateWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowDefinition  **
  - **IAM action:**  [nova-act:DeleteWorkflowDefinition](#list_nova-act-action-DeleteWorkflowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowRun  **
  - **IAM action:**  [nova-act:DeleteWorkflowRun](#list_nova-act-action-DeleteWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWorkflowDefinition  **
  - **IAM action:**  [nova-act:GetWorkflowDefinition](#list_nova-act-action-GetWorkflowDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowRun  **
  - **IAM action:**  [nova-act:GetWorkflowRun](#list_nova-act-action-GetWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InvokeActStep  **
  - **IAM action:**  [nova-act:InvokeActStep](#list_nova-act-action-InvokeActStep) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListActs  **
  - **IAM action:**  [nova-act:ListActs](#list_nova-act-action-ListActs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListModels  **
  - **IAM action:**  [nova-act:ListModels](#list_nova-act-action-ListModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSessions  **
  - **IAM action:**  [nova-act:ListSessions](#list_nova-act-action-ListSessions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWorkflowDefinitions  **
  - **IAM action:**  [nova-act:ListWorkflowDefinitions](#list_nova-act-action-ListWorkflowDefinitions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowRuns  **
  - **IAM action:**  [nova-act:ListWorkflowRuns](#list_nova-act-action-ListWorkflowRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   UpdateAct  **
  - **IAM action:**  [nova-act:UpdateAct](#list_nova-act-action-UpdateAct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflowRun  **
  - **IAM action:**  [nova-act:UpdateWorkflowRun](#list_nova-act-action-UpdateWorkflowRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Nova Act
<a name="list_nova-act-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateAct](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateAct.html)  **
  - **Description:** Grants permission to create a new AI task (act) within a session that can interact with tools and perform specific actions
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateSession](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateSession.html)  **
  - **Description:** Grants permission to create a new session context within a workflow run to manage conversation state and acts
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowDefinition.html)  **
  - **Description:** Grants permission to create a new workflow definition template that can be used to execute multiple workflow runs
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_CreateWorkflowRun.html)  **
  - **Description:** Grants permission to create a new execution instance of a workflow definition with specified parameters
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_DeleteWorkflowDefinition.html)  **
  - **Description:** Grants permission to delete a workflow definition and all associated resources
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_DeleteWorkflowRun.html)  **
  - **Description:** Grants permission to terminate and clean up a workflow run, stopping all associated acts and sessions
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write

- **   [GetWorkflowDefinition](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_GetWorkflowDefinition.html)  **
  - **Description:** Grants permission to retrieve details and configuration of a specific workflow definition
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_GetWorkflowRun.html)  **
  - **Description:** Grants permission to retrieve the current state, configuration, and execution details of a workflow run
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Read

- **   [InvokeActStep](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_InvokeActStep.html)  **
  - **Description:** Grants permission to execute the next step of an act, processing tool call results and returning new tool calls if needed
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write

- **   [ListActs](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListActs.html)  **
  - **Description:** Grants permission to list all acts within a specific session with their current status and execution details
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListModels](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListModels.html)  **
  - **Description:** Grants permission to list all available AI models that can be used for workflow execution, including their status and compatibility information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSessions](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListSessions.html)  **
  - **Description:** Grants permission to list all sessions within a specific workflow run
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Read

- **   [ListWorkflowDefinitions](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListWorkflowDefinitions.html)  **
  - **Description:** Grants permission to list all workflow definitions in your account with optional filtering and pagination
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflowRuns](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_ListWorkflowRuns.html)  **
  - **Description:** Grants permission to list all workflow runs for a specific workflow definition with optional filtering and pagination
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition)
  - **Condition keys:**  
  - **Access level:** List

- **   [UpdateAct](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_UpdateAct.html)  **
  - **Description:** Grants permission to update an existing act's configuration, status, or error information
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateWorkflowRun](https://docs.aws.amazon.com/nova-act/latest/APIReference/API_UpdateWorkflowRun.html)  **
  - **Description:** Grants permission to update the configuration or state of an active workflow run
  - **Resource types (\*required):** [workflow-definition\*](#list_nova-act-resource-workflow-definition) / **Condition keys:**  
  - **Resource types (\*required):** [workflow-run\*](#list_nova-act-resource-workflow-run) / **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Nova Act
<a name="list_nova-act-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [workflow-definition](https://docs.aws.amazon.com/nova-act/latest/userguide/workflow-definition.html)  | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName} |   | 
|  [workflow-run](https://docs.aws.amazon.com/nova-act/latest/userguide/workflow-run.html)  | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName}/workflow-run/${WorkflowRunId} |   | 

## Condition keys for Amazon Nova Act
<a name="list_nova-act-policy-keys"></a>

Amazon Nova Act has no service-specific condition keys that can be used in the `Condition` element of policy statements.