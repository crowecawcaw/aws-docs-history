# List of Amazon SWF Actions by Category

This section lists the reference topics for Amazon SWF actions in the Amazon SWF application programming interface (API).
These are listed by _functional category_.

For an _alphabetic_ list of actions, see the [Amazon Simple Workflow Service API Reference](../apireference.md "../apireference.md").

###### Topics

- [Actions Related to Activities](#swf-api-activities "#swf-api-activities")
- [Actions Related to Deciders](#swf-api-deciders "#swf-api-deciders")
- [Actions Related to Workflow Executions](#swf-api-executions "#swf-api-executions")
- [Actions Related to Administration](#swf-api-administration "#swf-api-administration")
- [Visibility Actions](#swf-api-visibility "#swf-api-visibility")

## Actions Related to Activities

Activity workers use `PollForActivityTask` to get new activity tasks. After a
worker receives an activity task from Amazon SWF, it performs the task and responds using
`RespondActivityTaskCompleted` if successful or
`RespondActivityTaskFailed` if unsuccessful.

The following are actions that are performed by activity workers.

- `PollForActivityTask`
- `RespondActivityTaskCompleted`
- `RespondActivityTaskFailed`
- `RespondActivityTaskCanceled`
- `RecordActivityTaskHeartbeat`

## Actions Related to Deciders

Deciders use `PollForDecisionTask` to get decision tasks. After a decider
receives a decision task from Amazon SWF, it examines its workflow execution history and decides
what to do next. It calls `RespondDecisionTaskCompleted` to complete the
decision task and provides zero or more next decisions.

The following are actions that are performed by deciders.

- `PollForDecisionTask`
- `RespondDecisionTaskCompleted`

## Actions Related to Workflow Executions

The following actions operate on a workflow execution.

- `RequestCancelWorkflowExecution`
- `StartWorkflowExecution`
- `SignalWorkflowExecution`
- `TerminateWorkflowExecution`

## Actions Related to Administration

Although you can perform administrative tasks from the Amazon SWF console, you can use the actions in this
section to automate functions or build your own administrative tools.

### Activity Management

- `RegisterActivityType`
- `DeprecateActivityType`
- `UndeprecateActivityType`
- `DeleteActivityType`

### Workflow Management

- `RegisterWorkflowType`
- `DeprecateWorkflowType`
- `UndeprecateWorkflowType`
- `DeleteWorkflowType`

### Domain Management

These actions allow you to register and deprecate Amazon SWF domains.

- `RegisterDomain`
- `DeprecateDomain`
- `UndeprecateDomain`

For more information and examples of these domain management actions, see [Registering a Domain with Amazon SWF](swf-dg-register-domain-api.md "swf-dg-register-domain-api.md").

### Workflow Execution Management

- `RequestCancelWorkflowExecution`
- `TerminateWorkflowExecution`

## Visibility Actions

Although you can perform visibility actions from the Amazon SWF console, you can use the actions in this section to
build your own console or administrative tools.

### Activity Visibility

- `ListActivityTypes`
- `DescribeActivityType`

### Workflow Visibility

- [ListWorkflowTypes](../apireference/API_ListWorkflowTypes.md "../apireference/API_ListWorkflowTypes.md")
- [DescribeWorkflowType](../apireference/API_DescribeWorkflowType.md "../apireference/API_DescribeWorkflowType.md")

### Workflow Execution Visibility

- `DescribeWorkflowExecution`
- `ListOpenWorkflowExecutions`
- `ListClosedWorkflowExecutions`
- `CountOpenWorkflowExecutions`
- `CountClosedWorkflowExecutions`
- `GetWorkflowExecutionHistory`

### Domain Visibility

- `ListDomains`
- `DescribeDomain`

### Task List Visibility

- `CountPendingActivityTasks`
- `CountPendingDecisionTasks`
