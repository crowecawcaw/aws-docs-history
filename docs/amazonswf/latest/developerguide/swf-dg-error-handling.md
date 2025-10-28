# Handling errors in Amazon SWF

There are a number of different types of errors that can occur during the course of a workflow
execution.

###### Topics

- [Validation Errors](#validation-errors "#validation-errors")
- [Errors in Enacting Actions or Decisions](#errors-in-enacting-actions-or-decisions "#errors-in-enacting-actions-or-decisions")
- [Timeouts](#timeouts "#timeouts")
- [Errors raised by user code](#errors-raised-by-user-code "#errors-raised-by-user-code")
- [Errors related to closing a workflow execution](#errors-related-to-closing-a-workflow-execution "#errors-related-to-closing-a-workflow-execution")

## Validation Errors

Validation errors occur when a request to Amazon SWF fails because it isn't properly formed or it contains
invalid data. In this context, a request could be an action such as `DescribeDomain` or
it could be a decision such as `StartTimer`. If the request is an action, Amazon SWF returns an error code in the
response. Check this error code as it may provide information about what aspect of the request caused the
failure. For example, one or more of the arguments passed with the request might be invalid. For a list of
common error codes, go to the topic for the action in the _Amazon Simple Workflow Service API Reference_.

If the request that failed is a decision, an appropriate event will be listed in the workflow execution
history. For example, if the `StartTimer` decision failed, you would see a `StartTimerFailed` event in the history. The decider should check for these events when it
receives the history in response to `PollForDecisionTask` or `GetWorkflowExecutionHistory`. Below
is a list of possible decision failure events that can occur when the decision isn't correctly formed or
contains invalid data.

## Errors in Enacting Actions or Decisions

Even if the request is properly formed, errors may occur when Amazon SWF attempts to carry out the request. In
these cases, one of the following events in the history will indicate that an error occurred. Look at the
`reason` field of the event to determine the cause of failure.

- `CancelTimerFailed`
- `RequestCancelActivityTaskFailed`
- `RequestCancelExternalWorkflowExecutionFailed`
- `ScheduleActivityTaskFailed`
- `SignalExternalWorkflowExecutionFailed`
- `StartChildWorkflowExecutionFailed`
- `StartTimerFailed`

## Timeouts

[Deciders](../apireference/API_RegisterWorkflowType.md "../apireference/API_RegisterWorkflowType.md"), [activity workers](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md"), and [workflow executions](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md") all operate within the constraints
of timeout periods. In this type of error, a task or a child workflow times out. An event will appear in the
history that describes the timeout. The decider should handle this event by, for example, rescheduling the task
or restarting the child workflow. For more information about timeouts, see [Amazon SWF Timeout Types](swf-timeout-types.md "swf-timeout-types.md")

- `ActivityTaskTimedOut`
- `ChildWorkflowExecutionTimedOut`
- `DecisionTaskTimedOut`
- `WorkflowExecutionTimedOut`

## Errors raised by user code

Examples of this type of error condition are activity task failures and child-workflow failures. As with
timeout errors, Amazon SWF adds an appropriate event to the workflow execution history. The decider should handle
this event, possibly by rescheduling the task or restarting the child workflow.

- `ActivityTaskFailed`
- `ChildWorkflowExecutionFailed`

## Errors related to closing a workflow execution

Deciders may also see the following events if they attempt to close a workflow that has a pending decision task.

- `FailWorkflowExecutionFailed`
- `CompleteWorkFlowExecutionFailed`
- `ContinueAsNewWorkflowExecutionFailed`
- `CancelWorkflowExecutionFailed`

For more information about any of the events listed above, see [History Event](../apireference/API_HistoryEvent.md "../apireference/API_HistoryEvent.md") in the Amazon SWF API Reference.
