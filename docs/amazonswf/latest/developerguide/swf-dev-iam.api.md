

# API Summary
<a name="swf-dev-iam.api"></a>

This section briefly describes how you can use IAM policies to control how an actor can use each API and pseudo API to access Amazon SWF resources.
+ For all actions except `RegisterDomain` and `ListDomains`, you can allow or deny access to any or all of an account's domains by expressing permissions for the domain resource. 
+ You can allow or deny permission for any member of the regular API and, if you grant permission to call `[RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)`, any member of the pseudo API. 
+ You can use a Condition to constrain some parameters' allowable values.

The following sections list the parameters that can be constrained for each member of the regular and pseudo API and provide the associated key, and note any limitations on how you can control domain access. 

## Regular API
<a name="swf-dev-iam.api.regular"></a>

This section lists the regular API members, and briefly describes the parameters that can be constrained and the associated keys. It also notes any limitations on how you can control domain access.

`[CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html)`
+ `tagFilter.tag` – String constraint. The key is `swf:tagFilter.tag`
+ `typeFilter.name` – String constraint. The key is `swf:typeFilter.name`.
+ `typeFilter.version` – String constraint. The key is `swf:typeFilter.version`. 

**Note**  
`CountClosedWorkflowExecutions` requires `typeFilter` and `tagFilter` to be mutually exclusive.

`[CountOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountOpenWorkflowExecutions.html)`
+ `tagFilter.tag` – String constraint. The key is `swf:tagFilter.tag`
+ `typeFilter.name` – String constraint. The key is `swf:typeFilter.name`.
+ `typeFilter.version` – String constraint. The key is `swf:typeFilter.version`. 

**Note**  
`CountOpenWorkflowExecutions` requires `typeFilter` and `tagFilter` to be mutually exclusive.

`[CountPendingActivityTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingActivityTasks.html)`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.

`[CountPendingDecisionTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingDecisionTasks.html)`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.

`[DeleteActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteActivityType.html)`
+ `activityType.name` – String constraint. The key is `swf:activityType.name`.
+ `activityType.version` – String constraint. The key is `swf:activityType.version`.

`[DeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateActivityType.html)`
+ `activityType.name` – String constraint. The key is `swf:activityType.name`.
+ `activityType.version` – String constraint. The key is `swf:activityType.version`.

`[DeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html)`
+ You can't constrain this action's parameters.

`[DeleteWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteWorkflowType.html)`
+ `workflowType.name` – String constraint. The key is `swf:workflowType.name`.
+ `workflowType.version` – String constraint. The key is `swf:workflowType.version`. 

`[DeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateWorkflowType.html)`
+ `workflowType.name` – String constraint. The key is `swf:workflowType.name`.
+ `workflowType.version` – String constraint. The key is `swf:workflowType.version`. 

`[DescribeActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html)`
+ `activityType.name` – String constraint. The key is `swf:activityType.name`.
+ `activityType.version` – String constraint. The key is `swf:activityType.version`.

`[DescribeDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html)`
+ You can't constrain this action's parameters.

`[DescribeWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowExecution.html)`
+ You can't constrain this action's parameters.

`[DescribeWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html)`
+ `workflowType.name` – String constraint. The key is `swf:workflowType.name`.
+ `workflowType.version` – String constraint. The key is `swf:workflowType.version`.

`[GetWorkflowExecutionHistory](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html)`
+ You can't constrain this action's parameters.

`[ListActivityTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html)`
+ You can't constrain this action's parameters.

`[ListClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html)`
+ `tagFilter.tag` – String constraint. The key is `swf:tagFilter.tag`
+ `typeFilter.name` – String constraint. The key is `swf:typeFilter.name`.
+ `typeFilter.version` – String constraint. The key is `swf:typeFilter.version`. 

**Note**  
`ListClosedWorkflowExecutions` requires `typeFilter` and `tagFilter` to be mutually exclusive.

`[ListDomains](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html)`
+ You can't constrain this action's parameters.

`[ListOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListOpenWorkflowExecutions.html)`
+ `tagFilter.tag` – String constraint. The key is `swf:tagFilter.tag`
+ `typeFilter.name` – String constraint. The key is `swf:typeFilter.name`.
+ `typeFilter.version` – String constraint. The key is `swf:typeFilter.version`. 

**Note**  
`ListOpenWorkflowExecutions` requires `typeFilter` and `tagFilter` to be mutually exclusive.

`[ListWorkflowTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html)`
+ You can't constrain this action's parameters.

`[PollForActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForActivityTask.html)`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.

`[PollForDecisionTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html)`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.

`[RecordActivityTaskHeartbeat](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RecordActivityTaskHeartbeat.html)`
+ You can't constrain this action's parameters.

`[RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html)`
+ `defaultTaskList.name` – String constraint. The key is `swf:defaultTaskList.name`. 
+ `name` – String constraint. The key is `swf:name`.
+ `version` – String constraint. The key is `swf:version`.

`[RegisterDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html)`
+ `name` – The name of the domain being registered is available as the resource of this action. 

`[RegisterWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html)`
+ `defaultTaskList.name` – String constraint. The key is `swf:defaultTaskList.name`. 
+ `name` – String constraint. The key is `swf:name`.
+ `version` – String constraint. The key is `swf:version`.

`[RequestCancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html)`
+ You can't constrain this action's parameters.

`[RespondActivityTaskCanceled](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCanceled.html)`
+ You can't constrain this action's parameters.

`[RespondActivityTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCompleted.html)`
+ You can't constrain this action's parameters.

`[RespondActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskFailed.html)`
+ You can't constrain this action's parameters.

`[RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)`
+ `decisions.member.N` – Restricted indirectly through pseudo API permissions. For details, see [Pseudo API](#swf-dev-iam.api.pseudo).

`[SignalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalWorkflowExecution.html)`
+ You can't constrain this action's parameters.

`[StartWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html)`
+ `tagList.member.0` – String constraint. The key is `swf:tagList.member.0`
+ `tagList.member.1` – String constraint. The key is `swf:tagList.member.1`
+ `tagList.member.2` – String constraint. The key is `swf:tagList.member.2`
+ `tagList.member.3` – String constraint. The key is `swf:tagList.member.3`
+ `tagList.member.4` – String constraint. The key is `swf:tagList.member.4`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.
+ `workflowType.name` – String constraint. The key is `swf:workflowType.name`.
+ `workflowType.version` – String constraint. The key is `swf:workflowType.version`.

**Note**  
You can't constrain more than five tags.

`[TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)`
+ You can't constrain this action's parameters.

## Pseudo API
<a name="swf-dev-iam.api.pseudo"></a>

This section lists the members of the pseudo API, which represent the decisions included in `[RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)`. If you have granted permission to use `RespondDecisionTaskCompleted`, your policy can express permissions for the members of this API in the same way as the regular API. You can further restrict some members of the pseudo-API by setting conditions on one or more parameters. This section lists the pseudo API members, and briefly describes the parameters that can be constrained and the associated keys.

**Note**  
The `aws:SourceIP`, `aws:UserAgent`, and `aws:SecureTransport` keys are not available for the pseudo API. If your intended security policy requires these keys to control access to the pseudo API, you can use them with the `RespondDecisionTaskCompleted` action. 

`CancelTimer`
+ You can't constrain this action's parameters.

`CancelWorkflowExecution`
+ You can't constrain this action's parameters.

`CompleteWorkflowExecution`
+ You can't constrain this action's parameters.

`ContinueAsNewWorkflowExecution`
+ `tagList.member.0` – String constraint. The key is `swf:tagList.member.0`
+ `tagList.member.1` – String constraint. The key is `swf:tagList.member.1`
+ `tagList.member.2` – String constraint. The key is `swf:tagList.member.2`
+ `tagList.member.3` – String constraint. The key is `swf:tagList.member.3`
+ `tagList.member.4` – String constraint. The key is `swf:tagList.member.4`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.
+ `workflowTypeVersion` – String constraint. The key is `swf:workflowTypeVersion`.

**Note**  
You can't constrain more than five tags.

`FailWorkflowExecution`
+ You can't constrain this action's parameters.

`RecordMarker`
+ You can't constrain this action's parameters.

`RequestCancelActivityTask`
+ You can't constrain this action's parameters.

`RequestCancelExternalWorkflowExecution`
+ You can't constrain this action's parameters.

`ScheduleActivityTask`
+ `activityType.name` – String constraint. The key is `swf:activityType.name`.
+ `activityType.version` – String constraint. The key is `swf:activityType.version`.
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.

`SignalExternalWorkflowExecution`
+ You can't constrain this action's parameters.

`StartChildWorkflowExecution`
+ `tagList.member.0` – String constraint. The key is `swf:tagList.member.0`
+ `tagList.member.1` – String constraint. The key is `swf:tagList.member.1`
+ `tagList.member.2` – String constraint. The key is `swf:tagList.member.2`
+ `tagList.member.3` – String constraint. The key is `swf:tagList.member.3`
+ `tagList.member.4` – String constraint. The key is `swf:tagList.member.4`
+ `taskList.name` – String constraint. The key is `swf:taskList.name`.
+ `workflowType.name` – String constraint. The key is `swf:workflowType.name`.
+ `workflowType.version` – String constraint. The key is `swf:workflowType.version`.

**Note**  
You can't constrain more than five tags.

`StartTimer`
+ You can't constrain this action's parameters.