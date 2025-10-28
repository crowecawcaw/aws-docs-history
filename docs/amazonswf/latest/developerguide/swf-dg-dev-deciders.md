# Developing deciders in Amazon SWF

A decider is an implementation of the coordination logic of your workflow type that runs during the execution
of your workflow. You can run multiple deciders for a single workflow type.

Because the execution state for a workflow execution is stored in its workflow history, deciders can be
stateless. Amazon SWF maintains the workflow execution history and provides it to a decider with each decision task. This
enables you to dynamically add and remove deciders as necessary, which makes the processing of your workflows highly
scalable. As the load on your system grows, you simply add more deciders to handle the increased capacity. Note,
however, that there can be only one decision task open at any time for a given workflow execution.

Every time a state change occurs for a workflow execution, Amazon SWF schedules a decision task. Each time a decider
receives a decision task, it does the following:

- Interprets the workflow execution history provided with the decision task
- Applies the coordination logic based on the workflow execution history and makes decisions on what to do
  next. Each decision is represented by a Decision structure
- Completes the decision task and provides a list of decisions to Amazon SWF.
  This section describes how to develop a decider, which involves:

- Programming your decider to poll for decision tasks
- Programming your decider to interpret the workflow execution history and make decisions
- Programming your decider to respond to a decision task.
  The examples in this section show how you might program a decider for the e-commerce example workflow.

You can implement the decider in any language that you like and run it anywhere, as long as it can communicate
with Amazon SWF through its service API.

###### Topics

- [Defining Coordination Logic](#swf-dg-coordination-logic "#swf-dg-coordination-logic")
- [Polling for Decision Tasks](#swf-dg-polling-decision-tasks "#swf-dg-polling-decision-tasks")
- [Applying the Coordination Logic](#swf-dg-apply-coord-logic "#swf-dg-apply-coord-logic")
- [Responding with Decisions](#swf-dg-responding-with-decisions "#swf-dg-responding-with-decisions")
- [Closing a Workflow Execution](#swf-dg-closing-workflows "#swf-dg-closing-workflows")
- [Launching Deciders](#swf-dg-deciders-launch "#swf-dg-deciders-launch")

## Defining Coordination Logic

The first thing to do when developing a decider is to define the coordination logic. In the e-commerce
example, coordination logic that schedules each activity after the previous activity completes might look similar
to the following:

```
IF lastEvent = "StartWorkflowInstance"
 addToDecisions ScheduleVerifyOrderActivity

ELSIF lastEvent = "CompleteVerifyOrderActivity"
 addToDecisions ScheduleChargeCreditCardActivity

ELSIF lastEvent = "CompleteChargeCreditCardActivity"
 addToDecisions ScheduleCompleteShipOrderActivity

ELSIF lastEvent = "CompleteShipOrderActivity"
 addToDecisions ScheduleRecordOrderCompletion

ELSIF lastEvent = "CompleteRecordOrderCompletion"
 addToDecisions CloseWorkflow

ENDIF
```

The decider applies the coordination logic to the workflow execution history, and creates a list of
decisions when completing the decision task using the `RespondDecisionTaskCompleted` action.

## Polling for Decision Tasks

Each decider polls for decision tasks. The decision tasks contain the information that the decider uses to
generate decisions such as scheduling activity tasks. To poll for decision tasks, the decider uses the `PollForDecisionTask` action.

In this example, the decider polls for a decision task, specifying the
`customerOrderWorkflow-0.1` tasklist.

```
https://swf.us-east-1.amazonaws.com
PollForDecisionTask
{
  "domain": "867530901",
  "taskList": {"name": "customerOrderWorkflow-v0.1"},
  "identity": "Decider01",
  "maximumPageSize": 50,
  "reverseOrder": true
}
```

If a decision task is available from the task list specified, Amazon SWF returns it immediately. If no decision
task is available, Amazon SWF holds the connection open for up to 60 seconds, and returns a task as soon as it becomes
available. If no task becomes available, Amazon SWF returns an empty response. An empty response is a `Task`
structure in which the value of `taskToken` is an empty string. Make sure to program your decider to
poll for another task if it receives an empty response.

If a decision task is available, Amazon SWF returns a response that contains the decision task as well as a
paginated view of the workflow execution history.

In this example, the type of the most recent event indicates the workflow execution started and the input
element contains the information needed to perform the first task.

```
{
  "events": [
    {
      "decisionTaskStartedEventAttributes": {
        "identity": "Decider01",
        "scheduledEventId": 2
      },
      "eventId": 3,
      "eventTimestamp": 1326593394.566,
      "eventType": "DecisionTaskStarted"
    }, {
      "decisionTaskScheduledEventAttributes": {
        "startToCloseTimeout": "600",
        "taskList": { "name": "specialTaskList" }
      },
      "eventId": 2,
      "eventTimestamp": 1326592619.474,
      "eventType": "DecisionTaskScheduled"
    }, {
      "eventId": 1,
      "eventTimestamp": 1326592619.474,
      "eventType": "WorkflowExecutionStarted",
      "workflowExecutionStartedEventAttributes": {
        "childPolicy" : "TERMINATE",
        "executionStartToCloseTimeout" : "3600",
        "input" : "data-used-decider-for-first-task",
        "parentInitiatedEventId": 0,
        "tagList" : ["music purchase", "digital", "ricoh-the-dog"],
        "taskList": { "name": "specialTaskList" },
        "taskStartToCloseTimeout": "600",
        "workflowType": {
          "name": "customerOrderWorkflow",
          "version": "1.0"
        }
      }
    }
  ],
  ...
}
```

After receiving the workflow execution history, the decider interprets history and makes decisions based on
its coordination logic.

Because the number of workflow history events for a single workflow execution might be large, the result
returned might be split up across a number of pages. To retrieve subsequent pages, make additional calls to `PollForDecisionTask` using the _nextPageToken_ returned by the initial call.
Note that you do _not_ call `GetWorkflowExecutionHistory` with this _nextPageToken_. Instead, call
`PollForDecisionTask` again.

## Applying the Coordination Logic

After the decider receives a decision task, program it to interpret the workflow execution history to
determine what has happened so far. Based on this, it should generate a list of decisions.

In the e-commerce example, we are concerned only with the last event in the workflow history, so we define
the following logic.

```
IF lastEvent = "StartWorkflowInstance"
 addToDecisions ScheduleVerifyOrderActivity

ELSIF lastEvent = "CompleteVerifyOrderActivity"
 addToDecisions ScheduleChargeCreditCardActivity

ELSIF lastEvent = "CompleteChargeCreditCardActivity"
 addToDecisions ScheduleCompleteShipOrderActivity

ELSIF lastEvent = "CompleteShipOrderActivity"
 addToDecisions ScheduleRecordOrderCompletion

ELSIF lastEvent = "CompleteRecordOrderCompletion"
 addToDecisions CloseWorkflow

ENDIF
```

If the lastEvent is `CompleteVerifyOrderActivity`, you would add the `ScheduleChargeCreditCardActivity` activity to the list of decisions.

After the decider determines the decision(s) to make, it can respond to Amazon SWF with appropriate
decisions.

## Responding with Decisions

After interpreting the workflow history and generating a list of decisions, the decider is ready to respond
back to Amazon SWF with those decisions.

Program your decider to extract the data that it needs from the workflow execution history, then create
decisions that specify the next appropriate actions for the workflow. The decider transmits these decision back to
Amazon SWF using the `RespondDecisionTaskCompleted` action. See the _Amazon Simple Workflow Service API Reference_ for a list of the available
[decision types](../apireference/API_Decision.md "../apireference/API_Decision.md").

In the e-commerce example, when the decider responds with the set of decisions that it generated, it also
includes the credit card input from the workflow execution history. The activity worker then has the information
it needs to perform the activity task.

When all activities in the workflow execution are complete, the decider closes the workflow
execution.

```
https://swf.us-east-1.amazonaws.com
RespondDecisionTaskCompleted
{
  "taskToken" : "12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "decisions" : [
    {
      "decisionType" :"ScheduleActivityTask",
      "scheduleActivityTaskDecisionAttributes" : {
        "control" :"OPTIONAL_DATA_FOR_DECIDER",
        "activityType" : {
          "name" :"ScheduleChargeCreditCardActivity",
          "version" :"1.1"
        },
        "activityId" :"3e2e6e55-e7c4-beef-feed-aa815722b7be",
        "scheduleToCloseTimeout" :"360",
        "taskList" : { "name" :"CC_TASKS" },
        "scheduleToStartTimeout" :"60",
        "startToCloseTimeout" :"300",
        "heartbeatTimeout" :"60",
        "input" : "4321-0001-0002-1234: 0212 : 234"
      }
    }
  ]
}
```

## Closing a Workflow Execution

When the decider determines that the business process is complete, that is, that there are no more
activities to perform, the decider generates a decision to close the workflow execution.

To close a workflow execution, program your decider to interpret the events in the workflow history to
determine what has happened in the execution so far and see if the workflow execution should be closed.

If the workflow has completed successfully, then close the workflow execution by calling `RespondDecisionTaskCompleted` with the `CompleteWorkflowExecution` decision. Alternatively, you can fail an erroneous
execution using the `FailWorkflowExecution` decision.

In the e-commerce example, the decider reviews the history and based on the coordination logic adds a
decision to close the workflow execution to its list of decisions, and initiates a `RespondDecisionTaskCompleted` action with a close workflow decision.

###### Note

There are some cases where closing a workflow execution fails. For example, if a signal is received while
the decider is closing the workflow execution, the close decision will fail. To handle this possibility,
ensure that the decider continues polling for decision tasks. Also, ensure that the decider that receives the
next decision task responds to the event—in this case, a signal—that prevented the execution from
closing.

You might also support cancellation of workflow executions. This could be especially useful for long running
workflows. To support cancellation, your decider should handle the `WorkflowExecutionCancelRequested` event in the history. This event indicates that cancellation
of the execution has been requested. Your decider should perform appropriate clean-up actions, such as canceling
ongoing activity tasks, and closing the workflow calling the `RespondDecisionTaskCompleted`
action with the `CancelWorkflowExecution` decision.

The following example calls `RespondDecisionTaskCompleted` to specify that the
current workflow execution is canceled.

```
https://swf.us-east-1.amazonaws.com
RespondDecisionTaskCompleted
{
  "taskToken" : "12342e17-80f6-FAKE-TASK-TOKEN32f0223",
  "decisions" : [
    {
      "decisionType":"CancelWorkflowExecution",
      "CancelWorkflowExecutionAttributes":{
        "Details": "Customer canceled order"
      }
    }
  ]
}
```

Amazon SWF checks to ensure that the decision to close or cancel the workflow execution is the last decision sent
by the decider. That is, it isn't valid to have a set of decisions in which there are decisions after the one that
closes the workflow.

## Launching Deciders

After completing decider development, you are ready to launch one or more deciders.

To launch deciders, package your coordination logic into an executable that you can use on your decider
platform. For example, you might package your decider code as a Java executable that you can run on both Linux and
Windows computers.

Once launched, your deciders should start polling Amazon SWF for tasks. Until you start workflow executions and
Amazon SWF schedules decision tasks, these polls will time out and get empty responses. An empty response is a
`Task` structure in which the value of `taskToken` is an empty string. Your deciders should
simply continue to poll.

Amazon SWF ensures that only one decision task can be active for a workflow execution at any time. This prevents
issues such as conflicting decisions. Additionally, Amazon SWF ensures that a single decision task is assigned to a
single decider, regardless of the number of deciders that are running.

If something occurs that generates a decision task while a decider is processing another decision task,
Amazon SWF queues the new task until the current task completes. After the current task completes, Amazon SWF makes the new
decision task available. Also, decision tasks are batched in the sense that, if multiple activities complete while
a decider is processing a decision task, Amazon SWF will create only a single new decision task to account for the
multiple task completions. However, each task completion will receive an individual event in the workflow
execution history.

Because polls are outbound requests, deciders can run on any network that has access to the Amazon SWF
endpoint.

In order for workflow executions to progress, one or more deciders must be running. You can launch as many
deciders as you like. Amazon SWF supports multiple deciders polling on the same task list.
