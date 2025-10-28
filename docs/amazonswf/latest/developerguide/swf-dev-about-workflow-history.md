# Workflow history in Amazon SWF

Amazon SWF records the progress of every workflow execution in the _workflow history_

- a detailed, complete, and consistent record of every event that occurred since the workflow
  execution started.

An _event_ represents a discrete change in your workflow execution's state, such as a new activity
being scheduled or a running activity being completed. The workflow history contains every event that causes the
execution state of the workflow execution to change, such as scheduled and completed activities, task timeouts, and
signals.

Operations that don't change the state of the workflow execution don't typically appear in the workflow
history. For example, the workflow history doesn't show poll attempts or the use of visibility operations.

The workflow history has several key benefits:

- Applications can be stateless, because all information about a workflow execution is stored in
  its workflow history.
- For each workflow execution, the history provides a record of which activities were scheduled, their
  current status, and their results. The workflow execution uses this information to determine next steps.
- The history provides a detailed audit trail that you can use to monitor running workflow executions and
  verify completed workflow executions.
  The following is a conceptual view of the e-commerce workflow history:

```
Invoice0001

Start Workflow Execution

Schedule Verify Order
Start Verify Order Activity
Complete Verify Order Activity

Schedule Charge Credit Card
Start Charge Credit Card Activity
Complete Charge Credit Card Activity

Schedule Ship Order
Start Ship Order Activity
```

In the preceding example, the order is waiting to ship. In the following example, the order is complete.
Because the workflow history is cumulative, the newer events are appended:

```
Invoice0001

Start Workflow Execution

Schedule Verify Order
Start Verify Order Activity
Complete Verify Order Activity

Schedule Charge Credit Card
Start Charge Credit Card Activity
Complete Charge Credit Card Activity

Schedule Ship Order
Start Ship Order Activity
`Complete Ship Order Activity

Schedule Record Order Completion
Start Record Order Completion Activity
Complete Record Order Completion Activity

Close Workflow`
```

Programmatically, the events in the workflow execution history are represented as JavaScript Object Notation
(JSON) objects. The history itself is a JSON array of these objects. Each event has the following:

- A type, such as [WorkflowExecutionStarted](../apireference/API_WorkflowExecutionStartedEventAttributes.md "../apireference/API_WorkflowExecutionStartedEventAttributes.md")
  or [ActivityTaskCompleted](../apireference/API_ActivityTaskCompletedEventAttributes.md "../apireference/API_ActivityTaskCompletedEventAttributes.md")
- A timestamp in Unix time format
- An ID that uniquely identifies the event
  In addition, each type of event has a distinct set of descriptive attributes that are appropriate to that
  type. For example, the `ActivityTaskCompleted` event has attributes that contain the IDs for the events
  that correspond to the time that the activity task was scheduled and when it was started, as well as an attribute
  that holds result data.

You can obtain a copy of the current state of the workflow execution history by using the [GetWorkflowExecutionHistory](../apireference/API_GetWorkflowExecutionHistory.md "../apireference/API_GetWorkflowExecutionHistory.md") action. In addition,
as part of the interaction between Amazon SWF and the decider for your workflow, the decider periodically receives
copies of the history.

Below is a section of an example workflow execution history in JSON format.

```
[  {
      "eventId": 11,
      "eventTimestamp": 1326671603.102,
      "eventType": "WorkflowExecutionTimedOut",
      "workflowExecutionTimedOutEventAttributes": {
         "childPolicy": "TERMINATE",
         "timeoutType": "START_TO_CLOSE"
      }
   }, {
      "decisionTaskScheduledEventAttributes": {
         "startToCloseTimeout": "600",
         "taskList": {
            "name": "specialTaskList"
         }
      },
      "eventId": 10,
      "eventTimestamp": 1326670566.124,
      "eventType": "DecisionTaskScheduled"
   }, {
      "activityTaskTimedOutEventAttributes": {
         "details": "Waiting for confirmation",
         "scheduledEventId": 8,
         "startedEventId": 0,
         "timeoutType": "SCHEDULE_TO_START"
      },
      "eventId": 9,
      "eventTimestamp": 1326670566.124,
      "eventType": "ActivityTaskTimedOut"
   }, {
      "activityTaskScheduledEventAttributes": {
         "activityId": "verification-27",
         "activityType": {
            "name": "activityVerify",
            "version": "1.0"
         },
         "control": "digital music",
         "decisionTaskCompletedEventId": 7,
         "heartbeatTimeout": "120",
         "input": "5634-0056-4367-0923,12/12,437",
         "scheduleToCloseTimeout": "900",
         "scheduleToStartTimeout": "300",
         "startToCloseTimeout": "600",
         "taskList": {
            "name": "specialTaskList"
         }
      },
      "eventId": 8,
      "eventTimestamp": 1326670266.115,
      "eventType": "ActivityTaskScheduled"
   }, {
      "decisionTaskCompletedEventAttributes": {
         "executionContext": "Black Friday",
         "scheduledEventId": 5,
         "startedEventId": 6
      },
      "eventId": 7,
      "eventTimestamp": 1326670266.103,
      "eventType": "DecisionTaskCompleted"
   }, {
      "decisionTaskStartedEventAttributes": {
         "identity": "Decider01",
         "scheduledEventId": 5
      },
      "eventId": 6,
      "eventTimestamp": 1326670161.497,
      "eventType": "DecisionTaskStarted"
   }, {
      "decisionTaskScheduledEventAttributes": {
         "startToCloseTimeout": "600",
         "taskList": {
            "name": "specialTaskList"
         }
      },
      "eventId": 5,
      "eventTimestamp": 1326668752.66,
      "eventType": "DecisionTaskScheduled"
   }, {
      "decisionTaskTimedOutEventAttributes": {
         "scheduledEventId": 2,
         "startedEventId": 3,
         "timeoutType": "START_TO_CLOSE"
      },
      "eventId": 4,
      "eventTimestamp": 1326668752.66,
      "eventType": "DecisionTaskTimedOut"
   }, {
      "decisionTaskStartedEventAttributes": {
         "identity": "Decider01",
         "scheduledEventId": 2
      },
      "eventId": 3,
      "eventTimestamp": 1326668152.648,
      "eventType": "DecisionTaskStarted"
   }, {
      "decisionTaskScheduledEventAttributes": {
         "startToCloseTimeout": "600",
         "taskList": {
            "name": "specialTaskList"
         }
      },
      "eventId": 2,
      "eventTimestamp": 1326668003.094,
      "eventType": "DecisionTaskScheduled"
   }
]
```

For a detailed list of the different types of events that can appear in the workflow execution history, see
the [HistoryEvent](../apireference/API_HistoryEvent.md "../apireference/API_HistoryEvent.md") data
type in the _Amazon Simple Workflow Service API Reference_.

Amazon SWF stores the complete history of all workflow executions for a configurable number of days after the
execution closes. This period, which is known as the workflow history retention period, is specified when you
register a _Domain_ for your workflow. Domains are discussed in greater detail later in this
section.
