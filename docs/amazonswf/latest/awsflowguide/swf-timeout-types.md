# Amazon SWF Timeout Types

To ensure that workflow executions run correctly, you can set different types of timeouts with Amazon SWF. Some
timeouts specify how long the workflow can run in its entirety. Other timeouts specify how long activity tasks can
take before being assigned to a worker and how long they can take to complete from the time they are scheduled. All
timeouts in the Amazon SWF API are specified in seconds. Amazon SWF also supports the string `NONE` as a timeout value, which
indicates no timeout.

For timeouts related to decision tasks and activity tasks, Amazon SWF adds an event to the workflow execution
history. The attributes of the event provide information about what type of timeout occurred and which decision task
or activity task was affected. Amazon SWF also schedules a decision task. When the decider receives the new decision task,
it will see the timeout event in the history and take an appropriate action by calling the [RespondDecisionTaskCompleted](../apireference/API_RespondDecisionTaskCompleted.md "../apireference/API_RespondDecisionTaskCompleted.md") action.

A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported
as open while a worker is processing it. A task is closed when a worker reports it as [completed](../apireference/API_RespondActivityTaskCompleted.md "../apireference/API_RespondActivityTaskCompleted.md"), [canceled](../apireference/API_RespondActivityTaskCanceled.md "../apireference/API_RespondActivityTaskCanceled.md"), or [failed](../apireference/API_RespondActivityTaskFailed.md "../apireference/API_RespondActivityTaskFailed.md"). A task may also be closed by Amazon SWF as
the result of a timeout.

## Timeouts in Workflow and Decision Tasks

The following diagram shows how workflow and decision timeouts are related to the lifetime of a
workflow:

![A workflow's lifetime, with timeouts](images/workflow_timeouts.png)

There are two timeout types that are relevant to workflow and decision tasks:

- **Workflow Start to Close (`timeoutType: START_TO_CLOSE`)** –
  This timeout specifies the maximum time that a workflow execution can take to complete. It is set as a default during
  workflow registration, but it can be overridden with a different value when the workflow is started. If this
  timeout is exceeded, Amazon SWF closes the workflow execution and adds an [event](../apireference/API_HistoryEvent.md "../apireference/API_HistoryEvent.md") of type [WorkflowExecutionTimedOut](../apireference/API_WorkflowExecutionTimedOutEventAttributes.md "../apireference/API_WorkflowExecutionTimedOutEventAttributes.md")
  to the workflow execution history. In addition to the `timeoutType`, the event attributes specify
  the `childPolicy` that is in effect for this workflow execution. The child policy specifies how
  child workflow executions are handled if the parent workflow execution times out or otherwise terminates.
  For example, if the `childPolicy` is set to TERMINATE, then child workflow executions will be
  terminated. Once a workflow execution has timed out, you can't take any action on it other than visibility
  calls.
- **Decision Task Start to Close (`timeoutType: START_TO_CLOSE`)** –
  This timeout specifies the maximum time that the corresponding decider can take to complete a decision task. It
  is set during workflow type registration. If this timeout is exceeded, the task is marked as timed out in
  the workflow execution history, and Amazon SWF adds an event of type [DecisionTaskTimedOut](../apireference/API_DecisionTaskTimedOutEventAttributes.md "../apireference/API_DecisionTaskTimedOutEventAttributes.md")
  to the workflow history. The event attributes will include the IDs for the events that correspond to when
  this decision task was scheduled (`scheduledEventId`) and when it was started
  (`startedEventId`). In addition to adding the event, Amazon SWF also schedules a new decision
  task to alert the decider that this decision task timed out. After this timeout occurs, an attempt to
  complete the timed-out decision task using `RespondDecisionTaskCompleted` will fail.

## Timeouts in Activity Tasks

The following diagram shows how timeouts are related to the lifetime of an activity task:

![A task's lifetime, with timeouts](images/activity_timeouts.png)

There are four timeout types that are relevant to activity tasks:

- **Activity Task Start to Close (`timeoutType: START_TO_CLOSE`)** –
  This timeout specifies the maximum time that an activity worker can take to process a task after the worker has
  received the task. Attempts to close a timed out activity task using [RespondActivityTaskCanceled](../apireference/API_RespondActivityTaskCanceled.md "../apireference/API_RespondActivityTaskCanceled.md"),
  [RespondActivityTaskCompleted](../apireference/API_RespondActivityTaskCompleted.md "../apireference/API_RespondActivityTaskCompleted.md"),
  and [RespondActivityTaskFailed](../apireference/API_RespondActivityTaskFailed.md "../apireference/API_RespondActivityTaskFailed.md")
  will fail.
- **Activity Task Heartbeat (`timeoutType: HEARTBEAT`)** – This timeout
  specifies the maximum time that a task can run before providing its progress through the
  `RecordActivityTaskHeartbeat` action.
- **Activity Task Schedule to Start (`timeoutType: SCHEDULE_TO_START`)** –
  This timeout specifies how long Amazon SWF waits before timing out the activity task if no workers are
  available to perform the task. Once timed out, the expired task will not be assigned to another
  worker.
- **Activity Task Schedule to Close (`timeoutType: SCHEDULE_TO_CLOSE`)** –
  This timeout specifies how long the task can take from the time it is scheduled to the time it is complete.
  As a best practice, this value should not be greater than the sum of the task schedule-to-start timeout and
  the task start-to-close timeout.

###### Note

Each of the timeout types has a default value, which is generally set to `NONE` (infinite). The maximum
time for any activity execution is limited to one year, however.

You set default values for these during activity type registration, but you can override them with new
values when you [schedule](../apireference/API_ScheduleActivityTaskDecisionAttributes.md "../apireference/API_ScheduleActivityTaskDecisionAttributes.md")
the activity task. When one of these timeouts occurs, Amazon SWF will add an [event](../apireference/API_HistoryEvent.md "../apireference/API_HistoryEvent.md") of type [ActivityTaskTimedOut](../apireference/API_ActivityTaskTimedOutEventAttributes.md "../apireference/API_ActivityTaskTimedOutEventAttributes.md") to the
workflow history. The `timeoutType` value attribute of this event will specify which of these timeouts occurred. For
each of the timeouts, the value of `timeoutType` is shown in parentheses. The event attributes
will also include the IDs for the events that correspond to when the activity task was scheduled
(`scheduledEventId`) and when it was started (`startedEventId`). In addition to adding the
event, Amazon SWF also schedules a new decision task to alert the decider that the timeout occurred.
