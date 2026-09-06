

# List of Amazon SWF Actions by Category
<a name="swf-api-by-category"></a>

This section lists the reference topics for Amazon SWF actions in the Amazon SWF application programming interface (API). These are listed by *functional category*.

For an *alphabetic* list of actions, see the [Amazon Simple Workflow Service API Reference](https://docs.aws.amazon.com/amazonswf/latest/apireference/).

**Topics**
+ [Actions Related to Activities](#swf-api-activities)
+ [Actions Related to Deciders](#swf-api-deciders)
+ [Actions Related to Workflow Executions](#swf-api-executions)
+ [Actions Related to Administration](#swf-api-administration)
+ [Visibility Actions](#swf-api-visibility)

## Actions Related to Activities
<a name="swf-api-activities"></a>

Activity workers use `PollForActivityTask` to get new activity tasks. After a worker receives an activity task from Amazon SWF, it performs the task and responds using `RespondActivityTaskCompleted` if successful or `RespondActivityTaskFailed` if unsuccessful.

The following are actions that are performed by activity workers.
+ `[PollForActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForActivityTask.html)`
+ `[RespondActivityTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCompleted.html)`
+ `[RespondActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskFailed.html)`
+ `[RespondActivityTaskCanceled](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCanceled.html)`
+ `[RecordActivityTaskHeartbeat](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RecordActivityTaskHeartbeat.html)`

## Actions Related to Deciders
<a name="swf-api-deciders"></a>

Deciders use `PollForDecisionTask` to get decision tasks. After a decider receives a decision task from Amazon SWF, it examines its workflow execution history and decides what to do next. It calls `RespondDecisionTaskCompleted` to complete the decision task and provides zero or more next decisions.

The following are actions that are performed by deciders.
+ `[PollForDecisionTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html)`
+ `[RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)`

## Actions Related to Workflow Executions
<a name="swf-api-executions"></a>

The following actions operate on a workflow execution.
+ `[RequestCancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html)`
+ `[StartWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html)`
+ `[SignalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalWorkflowExecution.html)`
+ `[TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)`

## Actions Related to Administration
<a name="swf-api-administration"></a>

Although you can perform administrative tasks from the Amazon SWF console, you can use the actions in this section to automate functions or build your own administrative tools.

### Activity Management
<a name="activity-management"></a>
+ `[RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html)`
+ `[DeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateActivityType.html)`
+ `[UndeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateActivityType.html)`
+ `[DeleteActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteActivityType.html)`

### Workflow Management
<a name="workflow-management"></a>
+ `[RegisterWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html)`
+ `[DeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateWorkflowType.html)`
+ `[UndeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateWorkflowType.html)`
+ `[DeleteWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteWorkflowType.html)`

### Domain Management
<a name="domain-management"></a>

These actions allow you to register and deprecate Amazon SWF domains.
+ `[RegisterDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html)`
+ `[DeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html)`
+ `[UndeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateDomain.html)`

For more information and examples of these domain management actions, see [Registering a Domain with Amazon SWF](swf-dg-register-domain-api.md).

### Workflow Execution Management
<a name="workflow-execution-management"></a>
+ `[RequestCancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html)`
+ `[TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)`

## Visibility Actions
<a name="swf-api-visibility"></a>

Although you can perform visibility actions from the Amazon SWF console, you can use the actions in this section to build your own console or administrative tools.

### Activity Visibility
<a name="activity-visibility"></a>
+ `[ListActivityTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html)`
+ `[DescribeActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html)`

### Workflow Visibility
<a name="workflow-visibility"></a>
+ [ListWorkflowTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html)
+ [DescribeWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html)

### Workflow Execution Visibility
<a name="workflow-execution-visibility"></a>
+ `[DescribeWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowExecution.html)`
+ `[ListOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListOpenWorkflowExecutions.html)`
+ `[ListClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html)`
+ `[CountOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountOpenWorkflowExecutions.html)`
+ `[CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html)`
+ `[GetWorkflowExecutionHistory](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html)`

### Domain Visibility
<a name="domain-visibility"></a>
+ `[ListDomains](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html)`
+ `[DescribeDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html)`

### Task List Visibility
<a name="task-list-visibility"></a>
+ `[CountPendingActivityTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingActivityTasks.html)`
+ `[CountPendingDecisionTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingDecisionTasks.html)`