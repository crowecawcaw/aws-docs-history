# Setting task priority in Amazon SWF

By default, tasks on a task list are delivered based upon their _arrival
time_: tasks that are scheduled first are generally run first, as far as possible.
By setting an optional _task priority_, you can give priority to certain
tasks: Amazon SWF will attempt to deliver higher-priority tasks on a task list before those with
lower priority.

###### Note

Tasks that are scheduled first generally run first, but this is not guaranteed.

You can set task priorities for both workflows and activities. A workflow's task priority
doesn't affect the priority of any activity tasks it schedules, nor does it affect any child
workflows it starts. The default priority for an activity or workflow is set (either by you or
by Amazon SWF) during registration, and the registered task priority is always used unless it is
overridden while scheduling the activity or starting a workflow execution.

Task priority values can range from "-2147483648" to "2147483647", with higher numbers
indicating higher priority. If you don't set the task priority for an activity or workflow, it
will be assigned a priority of zero ("0").

###### Topics

- [Setting Task Priority for Workflows](#task-priority-workflows "#task-priority-workflows")
- [Setting Task Priority for Activities](#task-priority-activities "#task-priority-activities")
- [Actions that Return Task Priority
  Information](#task-priority-responses "#task-priority-responses")

## Setting Task Priority for Workflows

You can set the task priority for a workflow when you register it or start it. The task
priority that is set when the workflow type is registered is used as the default for any
workflow executions of that type, unless it is overridden when starting the workflow
execution.

To register a workflow type with a default task priority, set the
_defaultTaskPriority_ option when using the [RegisterWorkflowType](../apireference/API_RegisterWorkflowType.md "../apireference/API_RegisterWorkflowType.md") action:

```
{
  "domain": "867530901",
  "name": "expeditedOrderWorkflow",
  "version": "1.0",
  "description": "Expedited customer orders workflow",
  "defaultTaskStartToCloseTimeout": "600",
  "defaultExecutionStartToCloseTimeout": "3600",
  "defaultTaskList": {"name": "mainTaskList"},
  "defaultTaskPriority": "10",
  "defaultChildPolicy": "TERMINATE"
}
```

You can override a workflow type's registered task priority when you start a workflow
execution with [StartWorkflowExecution](../apireference/API_StartWorkflowExecution.md "../apireference/API_StartWorkflowExecution.md"):

```
{
  "childPolicy": "TERMINATE",
  "domain": "867530901",
  "executionStartToCloseTimeout": "1800",
  "input": "arbitrary-string-that-is-meaningful-to-the-workflow",
  "tagList": ["music purchase", "digital", "ricoh-the-dog"],
  "taskList": {"name": "specialTaskList"},
  "taskPriority": "-20",
  "taskStartToCloseTimeout": "600",
  "workflowId": "20110927-T-1",
  "workflowType": {"name": "customerOrderWorkflow", "version": "1.0"},
}
```

You can also override the registered task priority when starting a child workflow or when
continuing a workflow as new, such as when responding to a decision with [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md").

To set a child workflow's task priority, provide the value in
`startChildWorkflowExecutionDecisionAttributes`:

```
{
  "taskToken": "AAAAKgAAAAEAAAAAAAAAA...",
  "decisions": [
    {
      "decisionType": "StartChildWorkflowExecution",
      "startChildWorkflowExecutionDecisionAttributes": {
        "childPolicy": "TERMINATE",
        "control": "digital music",
        "executionStartToCloseTimeout": "900",
        "input": "201412-Smith-011x",
        "taskList": {"name": "specialTaskList"},
        "taskPriority": "5",
        "taskStartToCloseTimeout": "600",
        "workflowId": "verification-workflow",
        "workflowType": {
          "name": "MyChildWorkflow",
          "version": "1.0"
        }
      }
    }
  ]
}
```

When continuing a workflow as new, set the task priority in
`continueAsNewWorkflowExecutionDecisionAttributes`:

```
{
  "taskToken": "AAAAKgAAAAEAAAAAAAAAA...",
  "decisions": [
    {
      "decisionType": "ContinueAsNewWorkflowExecution",
      "continueAsNewWorkflowExecutionDecisionAttributes": {
        "childPolicy": "TERMINATE",
        "executionStartToCloseTimeout": "1800",
        "input": "5634-0056-4367-0923,12/12,437",
        "taskList": {"name": "specialTaskList"},
        "taskStartToCloseTimeout": "600",
        "taskPriority": "100",
        "workflowTypeVersion": "1.0"
      }
    }
  ]
}
```

## Setting Task Priority for Activities

You can set the task priority for an activity either when registering it or when
scheduling it. The task priority that is set when registering an activity type is used as the
default priority when the activity is run, unless it is overridden when scheduling the
activity.

To set task priority when registering an activity type, set the
_defaultTaskPriority_ option when using the [RegisterActivityType](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md") action:

```
{
  "defaultTaskHeartbeatTimeout": "120",
  "defaultTaskList": {"name": "mainTaskList"},
  "defaultTaskPriority": "10",
  "defaultTaskScheduleToCloseTimeout": "900",
  "defaultTaskScheduleToStartTimeout": "300",
  "defaultTaskStartToCloseTimeout": "600",
  "description": "Verify the customer credit card",
  "domain": "867530901",
  "name": "activityVerify",
  "version": "1.0"
}
```

To schedule a task with a task priority, use the _taskPriority_ option
when scheduling the activity with the [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md") action:

```
{
  "taskToken": "AAAAKgAAAAEAAAAAAAAAA...",
  "decisions": [
    {
      "decisionType": "ScheduleActivityTask",
      "scheduleActivityTaskDecisionAttributes": {
        "activityId": "verify-account",
        "activityType": {
            "name": "activityVerify",
            "version": "1.0"
        },
        "control": "digital music",
        "input": "abab-101",
        "taskList": {"name": "mainTaskList"},
        "taskPriority": "15"
      }
    }
  ]
}
```

## Actions that Return Task Priority

Information

You can get information about the set task priority (or set default task priority) from
the following Amazon SWF actions:

- [DescribeActivityType](../apireference/API_DescribeActivityType.md "../apireference/API_DescribeActivityType.md") returns the _defaultTaskPriority_ of
  the activity type in the `configuration` section of the response.
- [DescribeWorkflowExecution](../apireference/API_DescribeWorkflowExecution.md "../apireference/API_DescribeWorkflowExecution.md") returns the _taskPriority_ of the
  workflow execution in the `executionConfiguration` section of the
  response.
- [DescribeWorkflowType](../apireference/API_DescribeWorkflowType.md "../apireference/API_DescribeWorkflowType.md") returns the _defaultTaskPriority_ of
  the workflow type in the `configuration` section of the response.
- [GetWorkflowExecutionHistory](../apireference/API_GetWorkflowExecutionHistory.md "../apireference/API_GetWorkflowExecutionHistory.md") and [PollForDecisionTask](../apireference/API_PollForDecisionTask.md "../apireference/API_PollForDecisionTask.md") provide task priority information in the
  `activityTaskScheduledEventAttributes`,
  `decisionTaskScheduledEventAttributes`,
  `workflowExecutionContinuedAsNewEventAttributes`, and
  `workflowExecutionStartedEventAttributes` sections of the response.
