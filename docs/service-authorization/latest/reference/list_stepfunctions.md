

# Actions, resources, and condition keys for AWS Step Functions
<a name="list_stepfunctions"></a>

AWS Step Functions (service prefix: `states`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/step-functions/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-create-iam-role.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/states/states.json) for this service.

**Topics**
+ [API operations defined by AWS Step Functions](#list_stepfunctions-operations)
+ [Actions defined by AWS Step Functions](#list_stepfunctions-actions-as-permissions)
+ [Permission-only actions for AWS Step Functions](#list_stepfunctions-permission-only-actions)
+ [Resource types defined by AWS Step Functions](#list_stepfunctions-resources-for-iam-policies)
+ [Condition keys for AWS Step Functions](#list_stepfunctions-policy-keys)

## API operations defined by AWS Step Functions
<a name="list_stepfunctions-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_stepfunctions-actions-as-permissions).




- **   CreateActivity  **
  - **IAM action:**  [states:CreateActivity](#list_stepfunctions-action-CreateActivity)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [states:TagResource](#list_stepfunctions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStateMachine  **
  - **IAM action:**  [states:CreateStateMachine](#list_stepfunctions-action-CreateStateMachine)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [states:PublishStateMachineVersion](#list_stepfunctions-action-PublishStateMachineVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [states:TagResource](#list_stepfunctions-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** states.amazonaws.com / **Access level:** Write

- **   CreateStateMachineAlias  **
  - **IAM action:**  [states:CreateStateMachineAlias](#list_stepfunctions-action-CreateStateMachineAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteActivity  **
  - **IAM action:**  [states:DeleteActivity](#list_stepfunctions-action-DeleteActivity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStateMachine  **
  - **IAM action:**  [states:DeleteStateMachine](#list_stepfunctions-action-DeleteStateMachine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStateMachineAlias  **
  - **IAM action:**  [states:DeleteStateMachineAlias](#list_stepfunctions-action-DeleteStateMachineAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStateMachineVersion  **
  - **IAM action:**  [states:DeleteStateMachineVersion](#list_stepfunctions-action-DeleteStateMachineVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeActivity  **
  - **IAM action:**  [states:DescribeActivity](#list_stepfunctions-action-DescribeActivity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeExecution  **
  - **IAM action:**  [states:DescribeExecution](#list_stepfunctions-action-DescribeExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeMapRun  **
  - **IAM action:**  [states:DescribeMapRun](#list_stepfunctions-action-DescribeMapRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStateMachine  **
  - **IAM action:**  [states:DescribeStateMachine](#list_stepfunctions-action-DescribeStateMachine) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStateMachineAlias  **
  - **IAM action:**  [states:DescribeStateMachineAlias](#list_stepfunctions-action-DescribeStateMachineAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStateMachineForExecution  **
  - **IAM action:**  [states:DescribeStateMachineForExecution](#list_stepfunctions-action-DescribeStateMachineForExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetActivityTask  **
  - **IAM action:**  [states:GetActivityTask](#list_stepfunctions-action-GetActivityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetExecutionHistory  **
  - **IAM action:**  [states:GetExecutionHistory](#list_stepfunctions-action-GetExecutionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActivities  **
  - **IAM action:**  [states:ListActivities](#list_stepfunctions-action-ListActivities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListExecutions  **
  - **IAM action:**  [states:ListExecutions](#list_stepfunctions-action-ListExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMapRuns  **
  - **IAM action:**  [states:ListMapRuns](#list_stepfunctions-action-ListMapRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStateMachineAliases  **
  - **IAM action:**  [states:ListStateMachineAliases](#list_stepfunctions-action-ListStateMachineAliases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStateMachineVersions  **
  - **IAM action:**  [states:ListStateMachineVersions](#list_stepfunctions-action-ListStateMachineVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListStateMachines  **
  - **IAM action:**  [states:ListStateMachines](#list_stepfunctions-action-ListStateMachines) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [states:ListTagsForResource](#list_stepfunctions-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PublishStateMachineVersion  **
  - **IAM action:**  [states:PublishStateMachineVersion](#list_stepfunctions-action-PublishStateMachineVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RedriveExecution  **
  - **IAM action:**  [states:RedriveExecution](#list_stepfunctions-action-RedriveExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendTaskFailure  **
  - **IAM action:**  [states:SendTaskFailure](#list_stepfunctions-action-SendTaskFailure) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendTaskHeartbeat  **
  - **IAM action:**  [states:SendTaskHeartbeat](#list_stepfunctions-action-SendTaskHeartbeat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendTaskSuccess  **
  - **IAM action:**  [states:SendTaskSuccess](#list_stepfunctions-action-SendTaskSuccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartExecution  **
  - **IAM action:**  [states:DescribeExecution](#list_stepfunctions-action-DescribeExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [states:StartExecution](#list_stepfunctions-action-StartExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartSyncExecution  **
  - **IAM action:**  [states:StartSyncExecution](#list_stepfunctions-action-StartSyncExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopExecution  **
  - **IAM action:**  [states:StopExecution](#list_stepfunctions-action-StopExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [states:TagResource](#list_stepfunctions-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestState  **
  - **IAM action:**  [states:RevealSecrets](#list_stepfunctions-action-RevealSecrets)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [states:TestState](#list_stepfunctions-action-TestState)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** states.amazonaws.com / **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [states:UntagResource](#list_stepfunctions-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateMapRun  **
  - **IAM action:**  [states:UpdateMapRun](#list_stepfunctions-action-UpdateMapRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStateMachine  **
  - **IAM action:**  [states:PublishStateMachineVersion](#list_stepfunctions-action-PublishStateMachineVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [states:UpdateStateMachine](#list_stepfunctions-action-UpdateStateMachine)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** states.amazonaws.com / **Access level:** Write

- **   UpdateStateMachineAlias  **
  - **IAM action:**  [states:UpdateStateMachineAlias](#list_stepfunctions-action-UpdateStateMachineAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateStateMachineDefinition  **
  - **IAM action:**  [states:ValidateStateMachineDefinition](#list_stepfunctions-action-ValidateStateMachineDefinition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Step Functions
<a name="list_stepfunctions-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateActivity.html)  **
  - **Description:** Grants permission to create an activity
  - **Resource types (\*required):** [activity\*](#list_stepfunctions-resource-activity)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_stepfunctions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachine.html)  **
  - **Description:** Grants permission to create a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_stepfunctions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_CreateStateMachineAlias.html)  **
  - **Description:** Grants permission to create a state machine alias
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [DeleteActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteActivity.html)  **
  - **Description:** Grants permission to delete an activity
  - **Resource types (\*required):** [activity\*](#list_stepfunctions-resource-activity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachine.html)  **
  - **Description:** Grants permission to delete a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineAlias.html)  **
  - **Description:** Grants permission to delete a state machine alias
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [DeleteStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DeleteStateMachineVersion.html)  **
  - **Description:** Grants permission to delete a state machine version
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [DescribeActivity](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeActivity.html)  **
  - **Description:** Grants permission to describe an activity
  - **Resource types (\*required):** [activity\*](#list_stepfunctions-resource-activity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeExecution.html)  **
  - **Description:** Grants permission to describe an execution
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [express\*](#list_stepfunctions-resource-express) / **Condition keys:**  
  - **Access level:** Read

- **   [DescribeMapRun](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeMapRun.html)  **
  - **Description:** Grants permission to describe a map run
  - **Resource types (\*required):** [maprun\*](#list_stepfunctions-resource-maprun)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachine.html)  **
  - **Description:** Grants permission to describe a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Read

- **   [DescribeStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineAlias.html)  **
  - **Description:** Grants permission to describe a state machine alias
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Read

- **   [DescribeStateMachineForExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_DescribeStateMachineForExecution.html)  **
  - **Description:** Grants permission to describe the state machine for an execution
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetActivityTask](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetActivityTask.html)  **
  - **Description:** Grants permission to be used by workers to retrieve a task (with the specified activity ARN) which has been scheduled for execution by a running state machine
  - **Resource types (\*required):** [activity\*](#list_stepfunctions-resource-activity)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetExecutionHistory](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetExecutionHistory.html)  **
  - **Description:** Grants permission to return the history of the specified execution as a list of events
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListActivities](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListActivities.html)  **
  - **Description:** Grants permission to list the existing activities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListExecutions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListExecutions.html)  **
  - **Description:** Grants permission to list the executions of a state machine
  - **Resource types (\*required):** [maprun\*](#list_stepfunctions-resource-maprun) / **Condition keys:** [states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** List

- **   [ListMapRuns](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListMapRuns.html)  **
  - **Description:** Grants permission to list the map runs of an execution
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStateMachineAliases](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineAliases.html)  **
  - **Description:** Grants permission to list the aliases of a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** List

- **   [ListStateMachineVersions](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachineVersions.html)  **
  - **Description:** Grants permission to list the versions of a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListStateMachines](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListStateMachines.html)  **
  - **Description:** Grants permission to lists the existing state machines
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an AWS Step Functions resource
  - **Resource types (\*required):** [activity](#list_stepfunctions-resource-activity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [statemachine](#list_stepfunctions-resource-statemachine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PublishStateMachineVersion](https://docs.aws.amazon.com/step-functions/latest/apireference/API_PublishStateMachineVersion.html)  **
  - **Description:** Grants permission to publish a state machine version
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RedriveExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_RedriveExecution.html)  **
  - **Description:** Grants permission to redrive an execution
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendTaskFailure](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskFailure.html)  **
  - **Description:** Grants permission to report that the task identified by the taskToken failed
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendTaskHeartbeat](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskHeartbeat.html)  **
  - **Description:** Grants permission to report to the service that the task represented by the specified taskToken is still making progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendTaskSuccess](https://docs.aws.amazon.com/step-functions/latest/apireference/API_SendTaskSuccess.html)  **
  - **Description:** Grants permission to report that the task identified by the taskToken completed successfully
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html)  **
  - **Description:** Grants permission to start a state machine execution
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html)  **
  - **Description:** Grants permission to start a Synchronous Express state machine execution
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [StopExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StopExecution.html)  **
  - **Description:** Grants permission to stop an execution
  - **Resource types (\*required):** [execution\*](#list_stepfunctions-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS Step Functions resource
  - **Resource types (\*required):** [activity](#list_stepfunctions-resource-activity) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_stepfunctions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Resource types (\*required):** [statemachine](#list_stepfunctions-resource-statemachine) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_stepfunctions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestState](https://docs.aws.amazon.com/step-functions/latest/apireference/API_TestState.html)  **
  - **Description:** Grants permission to test a state machine definition
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an AWS Step Functions resource
  - **Resource types (\*required):** [activity](#list_stepfunctions-resource-activity) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Resource types (\*required):** [statemachine](#list_stepfunctions-resource-statemachine) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateMapRun](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateMapRun.html)  **
  - **Description:** Grants permission to update a map run
  - **Resource types (\*required):** [maprun\*](#list_stepfunctions-resource-maprun)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateStateMachine](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachine.html)  **
  - **Description:** Grants permission to update a state machine
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_stepfunctions-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_stepfunctions-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateStateMachineAlias](https://docs.aws.amazon.com/step-functions/latest/apireference/API_UpdateStateMachineAlias.html)  **
  - **Description:** Grants permission to update a state machine alias
  - **Resource types (\*required):** [statemachine\*](#list_stepfunctions-resource-statemachine)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_)<br />[states:StateMachineQualifier](#list_stepfunctions-states_StateMachineQualifier)
  - **Access level:** Write

- **   [ValidateStateMachineDefinition](https://docs.aws.amazon.com/step-functions/latest/apireference/API_ValidateStateMachineDefinition.html)  **
  - **Description:** Grants permission to validate a state machine definition
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Permission-only actions for AWS Step Functions
<a name="list_stepfunctions-permission-only-actions"></a>

The following actions are defined by AWS Step Functions but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [InvokeHTTPEndpoint](https://docs.aws.amazon.com/step-functions/latest/dg/connect-third-party-apis.html)  | Grants permission to invoke the HTTP Task state |  |   | Write | 
|   [RevealSecrets](https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html)  | Grants permission to reveal sensitive data from an execution |  |   | Read | 

## Resource types defined by AWS Step Functions
<a name="list_stepfunctions-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [activity](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-activities.html)  | arn:${Partition}:states:${Region}:${Account}:activity:${ActivityName} | [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_) | 
|  [execution](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html)  | arn:${Partition}:states:${Region}:${Account}:execution:${StateMachineName}:${ExecutionId} | [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_) | 
|  [express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-executions.html)  | arn:${Partition}:states:${Region}:${Account}:express:${StateMachineName}:${ExecutionId}:${ExpressId} |   | 
|  [labelled execution](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html)  | arn:${Partition}:states:${Region}:${Account}:execution:${StateMachineName}/${MapRunLabel}:${ExecutionId} |   | 
|  [labelled express](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html)  | arn:${Partition}:states:${Region}:${Account}:express:${StateMachineName}/${MapRunLabel}:${ExecutionId}:${ExpressId} |   | 
|  [maprun](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-examine-map-run.html)  | arn:${Partition}:states:${Region}:${Account}:mapRun:${StateMachineName}/${MapRunLabel}:${MapRunId} |   | 
|  [statemachine](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html)  | arn:${Partition}:states:${Region}:${Account}:stateMachine:${StateMachineName} | [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_) | 
|  [statemachinealias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html)  | arn:${Partition}:states:${Region}:${Account}:stateMachine:${StateMachineName}:${StateMachineAliasName} | [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_) | 
|  [statemachineversion](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-cd-aliasing-versioning.html)  | arn:${Partition}:states:${Region}:${Account}:stateMachine:${StateMachineName}:${StateMachineVersionId} | [aws:ResourceTag/${TagKey}](#list_stepfunctions-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Step Functions
<a name="list_stepfunctions-policy-keys"></a>

AWS Step Functions defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 
|   [states:HTTPEndpoint](https://docs.aws.amazon.com/step-functions/latest/dg/connect-third-party-apis.html)  | Filters access by the endpoint that the HTTP Task state allows in the request | String | 
|   [states:HTTPMethod](https://docs.aws.amazon.com/step-functions/latest/dg/connect-third-party-apis.html)  | Filters access by the method that the HTTP Task state allows in the request | String | 
|   [states:StateMachineQualifier](https://docs.aws.amazon.com/step-functions/latest/dg/auth-version-alias.html)  | Filters access by the qualifier of a state machine ARN | ArrayOfString | 