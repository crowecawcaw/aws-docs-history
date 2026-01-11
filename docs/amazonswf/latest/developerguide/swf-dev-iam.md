# API Summary

This section briefly describes how you can use IAM policies to control how an actor
can use each API and pseudo API to access Amazon SWF resources.

- For all actions except `RegisterDomain` and `ListDomains`,
  you can allow or deny access to any or all of an account's domains by expressing
  permissions for the domain resource.
- You can allow or deny permission for any member of the regular API and, if you
  grant permission to call `RespondDecisionTaskCompleted`, any member of the pseudo API.
- You can use a Condition to constrain some parameters' allowable values.
  The following sections list the parameters that can be constrained for each member of
  the regular and pseudo API and provide the associated key, and note any limitations on how
  you can control domain access.

## Regular API

This section lists the regular API members, and briefly describes the parameters that
can be constrained and the associated keys. It also notes any limitations on how you can
control domain access.

`CountClosedWorkflowExecutions`

- `tagFilter.tag` – String constraint. The key is
  `swf:tagFilter.tag`
- `typeFilter.name` – String constraint. The key is
  `swf:typeFilter.name`.
- `typeFilter.version` – String constraint. The key is
  `swf:typeFilter.version`.

###### Note

`CountClosedWorkflowExecutions` requires `typeFilter` and
`tagFilter` to be mutually exclusive.

`CountOpenWorkflowExecutions`

- `tagFilter.tag` – String constraint. The key is
  `swf:tagFilter.tag`
- `typeFilter.name` – String constraint. The key is
  `swf:typeFilter.name`.
- `typeFilter.version` – String constraint. The key is
  `swf:typeFilter.version`.

###### Note

`CountOpenWorkflowExecutions` requires `typeFilter` and
`tagFilter` to be mutually exclusive.

`CountPendingActivityTasks`

- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.

`CountPendingDecisionTasks`

- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.

`DeleteActivityType`

- `activityType.name` – String constraint. The key is
  `swf:activityType.name`.
- `activityType.version` – String constraint. The key is
  `swf:activityType.version`.

`DeprecateActivityType`

- `activityType.name` – String constraint. The key is
  `swf:activityType.name`.
- `activityType.version` – String constraint. The key is
  `swf:activityType.version`.

`DeprecateDomain`

- You can't constrain this action's parameters.

`DeleteWorkflowType`

- `workflowType.name` – String constraint. The key is
  `swf:workflowType.name`.
- `workflowType.version` – String constraint. The key is
  `swf:workflowType.version`.

`DeprecateWorkflowType`

- `workflowType.name` – String constraint. The key is
  `swf:workflowType.name`.
- `workflowType.version` – String constraint. The key is
  `swf:workflowType.version`.

`DescribeActivityType`

- `activityType.name` – String constraint. The key is
  `swf:activityType.name`.
- `activityType.version` – String constraint. The key is
  `swf:activityType.version`.

`DescribeDomain`

- You can't constrain this action's parameters.

`DescribeWorkflowExecution`

- You can't constrain this action's parameters.

`DescribeWorkflowType`

- `workflowType.name` – String constraint. The key is
  `swf:workflowType.name`.
- `workflowType.version` – String constraint. The key is
  `swf:workflowType.version`.

`GetWorkflowExecutionHistory`

- You can't constrain this action's parameters.

`ListActivityTypes`

- You can't constrain this action's parameters.

`ListClosedWorkflowExecutions`

- `tagFilter.tag` – String constraint. The key is
  `swf:tagFilter.tag`
- `typeFilter.name` – String constraint. The key is
  `swf:typeFilter.name`.
- `typeFilter.version` – String constraint. The key is
  `swf:typeFilter.version`.

###### Note

`ListClosedWorkflowExecutions` requires `typeFilter` and
`tagFilter` to be mutually exclusive.

`ListDomains`

- You can't constrain this action's parameters.

`ListOpenWorkflowExecutions`

- `tagFilter.tag` – String constraint. The key is
  `swf:tagFilter.tag`
- `typeFilter.name` – String constraint. The key is
  `swf:typeFilter.name`.
- `typeFilter.version` – String constraint. The key is
  `swf:typeFilter.version`.

###### Note

`ListOpenWorkflowExecutions` requires `typeFilter` and
`tagFilter` to be mutually exclusive.

`ListWorkflowTypes`

- You can't constrain this action's parameters.

`PollForActivityTask`

- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.

`PollForDecisionTask`

- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.

`RecordActivityTaskHeartbeat`

- You can't constrain this action's parameters.

`RegisterActivityType`

- `defaultTaskList.name` – String constraint. The key is
  `swf:defaultTaskList.name`.
- `name` – String constraint. The key is
  `swf:name`.
- `version` – String constraint. The key is
  `swf:version`.

`RegisterDomain`

- `name` – The name of the domain being registered is available
  as the resource of this action.

`RegisterWorkflowType`

- `defaultTaskList.name` – String constraint. The key is
  `swf:defaultTaskList.name`.
- `name` – String constraint. The key is
  `swf:name`.
- `version` – String constraint. The key is
  `swf:version`.

`RequestCancelWorkflowExecution`

- You can't constrain this action's parameters.

`RespondActivityTaskCanceled`

- You can't constrain this action's parameters.

`RespondActivityTaskCompleted`

- You can't constrain this action's parameters.

`RespondActivityTaskFailed`

- You can't constrain this action's parameters.

`RespondDecisionTaskCompleted`

- `decisions.member.N` – Restricted indirectly through pseudo
  API permissions. For details, see [Pseudo API](#swf-dev-iam.api.pseudo "#swf-dev-iam.api.pseudo").

`SignalWorkflowExecution`

- You can't constrain this action's parameters.

`StartWorkflowExecution`

- `tagList.member.0` – String constraint. The key is
  `swf:tagList.member.0`
- `tagList.member.1` – String constraint. The key is
  `swf:tagList.member.1`
- `tagList.member.2` – String constraint. The key is
  `swf:tagList.member.2`
- `tagList.member.3` – String constraint. The key is
  `swf:tagList.member.3`
- `tagList.member.4` – String constraint. The key is
  `swf:tagList.member.4`
- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.
- `workflowType.name` – String constraint. The key is
  `swf:workflowType.name`.
- `workflowType.version` – String constraint. The key is
  `swf:workflowType.version`.

###### Note

You can't constrain more than five tags.

`TerminateWorkflowExecution`

- You can't constrain this action's parameters.

## Pseudo API

This section lists the members of the pseudo API, which represent the decisions
included in `RespondDecisionTaskCompleted`. If you have granted permission to
use `RespondDecisionTaskCompleted`, your policy can express permissions for
the members of this API in the same way as the regular API. You can further restrict
some members of the pseudo-API by setting conditions on one or more parameters. This
section lists the pseudo API members, and briefly describes the parameters that can be
constrained and the associated keys.

###### Note

The `aws:SourceIP`, `aws:UserAgent`, and
`aws:SecureTransport` keys are not available for the pseudo API. If
your intended security policy requires these keys to control access to the pseudo
API, you can use them with the `RespondDecisionTaskCompleted` action.

`CancelTimer`

- You can't constrain this action's parameters.

`CancelWorkflowExecution`

- You can't constrain this action's parameters.

`CompleteWorkflowExecution`

- You can't constrain this action's parameters.

`ContinueAsNewWorkflowExecution`

- `tagList.member.0` – String constraint. The key is
  `swf:tagList.member.0`
- `tagList.member.1` – String constraint. The key is
  `swf:tagList.member.1`
- `tagList.member.2` – String constraint. The key is
  `swf:tagList.member.2`
- `tagList.member.3` – String constraint. The key is
  `swf:tagList.member.3`
- `tagList.member.4` – String constraint. The key is
  `swf:tagList.member.4`
- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.
- `workflowTypeVersion` – String constraint. The key is
  `swf:workflowTypeVersion`.

###### Note

You can't constrain more than five tags.

`FailWorkflowExecution`

- You can't constrain this action's parameters.

`RecordMarker`

- You can't constrain this action's parameters.

`RequestCancelActivityTask`

- You can't constrain this action's parameters.

`RequestCancelExternalWorkflowExecution`

- You can't constrain this action's parameters.

`ScheduleActivityTask`

- `activityType.name` – String constraint. The key is
  `swf:activityType.name`.
- `activityType.version` – String constraint. The key is
  `swf:activityType.version`.
- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.

`SignalExternalWorkflowExecution`

- You can't constrain this action's parameters.

`StartChildWorkflowExecution`

- `tagList.member.0` – String constraint. The key is
  `swf:tagList.member.0`
- `tagList.member.1` – String constraint. The key is
  `swf:tagList.member.1`
- `tagList.member.2` – String constraint. The key is
  `swf:tagList.member.2`
- `tagList.member.3` – String constraint. The key is
  `swf:tagList.member.3`
- `tagList.member.4` – String constraint. The key is
  `swf:tagList.member.4`
- `taskList.name` – String constraint. The key is
  `swf:taskList.name`.
- `workflowType.name` – String constraint. The key is
  `swf:workflowType.name`.
- `workflowType.version` – String constraint. The key is
  `swf:workflowType.version`.

###### Note

You can't constrain more than five tags.

`StartTimer`

- You can't constrain this action's parameters.
