

# Handling errors in Amazon SWF
<a name="swf-dg-error-handling"></a>

There are a number of different types of errors that can occur during the course of a workflow execution.

**Topics**
+ [Validation Errors](#validation-errors)
+ [Errors in Enacting Actions or Decisions](#errors-in-enacting-actions-or-decisions)
+ [Timeouts](#timeouts)
+ [Errors raised by user code](#errors-raised-by-user-code)
+ [Errors related to closing a workflow execution](#errors-related-to-closing-a-workflow-execution)

## Validation Errors
<a name="validation-errors"></a>

Validation errors occur when a request to Amazon SWF fails because it isn't properly formed or it contains invalid data. In this context, a request could be an action such as `DescribeDomain` or it could be a decision such as `StartTimer`. If the request is an action, Amazon SWF returns an error code in the response. Check this error code as it may provide information about what aspect of the request caused the failure. For example, one or more of the arguments passed with the request might be invalid. For a list of common error codes, go to the topic for the action in the *Amazon Simple Workflow Service API Reference*. 

If the request that failed is a decision, an appropriate event will be listed in the workflow execution history. For example, if the `StartTimer` decision failed, you would see a `StartTimerFailed` event in the history. The decider should check for these events when it receives the history in response to `PollForDecisionTask` or `GetWorkflowExecutionHistory`. Below is a list of possible decision failure events that can occur when the decision isn't correctly formed or contains invalid data. 

## Errors in Enacting Actions or Decisions
<a name="errors-in-enacting-actions-or-decisions"></a>

Even if the request is properly formed, errors may occur when Amazon SWF attempts to carry out the request. In these cases, one of the following events in the history will indicate that an error occurred. Look at the `reason` field of the event to determine the cause of failure. 
+ `[CancelTimerFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CancelTimerFailedEventAttributes.html)`
+ `[RequestCancelActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelActivityTaskFailedEventAttributes.html)`
+ `[RequestCancelExternalWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelExternalWorkflowExecutionFailedEventAttributes.html)`
+ `[ScheduleActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ScheduleActivityTaskFailedEventAttributes.html)`
+ `[SignalExternalWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalExternalWorkflowExecutionFailedEventAttributes.html)`
+ `[StartChildWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartChildWorkflowExecutionFailedEventAttributes.html)`
+ `[StartTimerFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartTimerFailedEventAttributes.html)`

## Timeouts
<a name="timeouts"></a>

[Deciders](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html), [activity workers](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html), and [workflow executions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html) all operate within the constraints of timeout periods. In this type of error, a task or a child workflow times out. An event will appear in the history that describes the timeout. The decider should handle this event by, for example, rescheduling the task or restarting the child workflow. For more information about timeouts, see [Amazon SWF Timeout Types](swf-timeout-types.md)
+ `[ActivityTaskTimedOut](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskTimedOutEventAttributes.html)`
+ `[ChildWorkflowExecutionTimedOut](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ChildWorkflowExecutionTimedOutEventAttributes.html)`
+ `[DecisionTaskTimedOut](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DecisionTaskTimedOutEventAttributes.html)`
+ `[WorkflowExecutionTimedOut](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_WorkflowExecutionTimedOutEventAttributes.html)`

## Errors raised by user code
<a name="errors-raised-by-user-code"></a>

Examples of this type of error condition are activity task failures and child-workflow failures. As with timeout errors, Amazon SWF adds an appropriate event to the workflow execution history. The decider should handle this event, possibly by rescheduling the task or restarting the child workflow. 
+ `[ActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ActivityTaskFailedEventAttributes.html)`
+ `[ChildWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ChildWorkflowExecutionFailedEventAttributes.html)`

## Errors related to closing a workflow execution
<a name="errors-related-to-closing-a-workflow-execution"></a>

Deciders may also see the following events if they attempt to close a workflow that has a pending decision task.
+ `[FailWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_FailWorkflowExecutionFailedEventAttributes.html)`
+ `[CompleteWorkFlowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CompleteWorkflowExecutionFailedEventAttributes.html)`
+ `[ContinueAsNewWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ContinueAsNewWorkflowExecutionFailedEventAttributes.html)`
+ `[CancelWorkflowExecutionFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CancelWorkflowExecutionFailedEventAttributes.html)`

For more information about any of the events listed above, see [History Event](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_HistoryEvent.html) in the Amazon SWF API Reference.