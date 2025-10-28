# Actors in Amazon SWF

###### Topics

- [What is an Actor in Amazon SWF?](#what-is-an-actor-swf "#what-is-an-actor-swf")
- [Workflow Starters](#swf-dev-actors-starters "#swf-dev-actors-starters")
- [Deciders](#swf-dev-actors-deciders "#swf-dev-actors-deciders")
- [Activity Workers](#swf-dev-actors-activities "#swf-dev-actors-activities")
- [Data Exchange Between Actors](#swf-dev-actors-dataex "#swf-dev-actors-dataex")

## What is an Actor in Amazon SWF?

In the course of its operations, Amazon SWF interacts with a number of different types of programmatic
_actors_. Actors can be [workflow starters](#swf-dev-actors-starters "#swf-dev-actors-starters"),
[deciders](#swf-dev-actors-deciders "#swf-dev-actors-deciders"), or [activity
workers](#swf-dev-actors-activities "#swf-dev-actors-activities"). These actors communicate with Amazon SWF through its API. You can develop these actors in any
programming language.

The following diagram shows the Amazon SWF architecture, including Amazon SWF and its actors.

![The different entities or "actors" in an Amazon SWF workflow.](images/swf-overview-actors.png)

## Workflow Starters

A workflow starter is any application that can initiate workflow executions. In the e-commerce example, one
workflow starter could be the website at which the customer places an order. Another workflow starter could be a
mobile application or system used by a customer service representative to place the order on behalf of the
customer.

## Deciders

A decider is an implementation of a workflow's coordination logic. Deciders control the
flow of activity tasks in a workflow execution. Whenever a change occurs during a workflow
execution, such as the completion of a task, a decision task including the entire workflow
history will be passed to a decider. When the decider receives the decision task from
Amazon SWF, it analyzes the workflow execution history to determine the next appropriate steps
in the workflow execution. The decider communicates these steps back to Amazon SWF using
_decisions_. A decision is an Amazon SWF data type that can represent
various next actions. For a list of the possible decisions, go to [Decision](../apireference/API_Decision.md "../apireference/API_Decision.md") in the Amazon Simple Workflow Service API Reference.

Here is an example of a decision in JSON format, the format in which it is transmitted to Amazon SWF. This decision
schedules a new activity task.

```
{
   "decisionType" : "ScheduleActivityTask",
   "scheduleActivityTaskDecisionAttributes" : {
      "activityType" : {
         "name" : "activityVerify",
         "version" : "1.0"
      },
      "activityId" : "verification-27",
      "control" : "digital music",
      "input" : "5634-0056-4367-0923,12/12,437",
      "scheduleToCloseTimeout" : "900",
      "taskList" : {
         "name": "specialTaskList"
      },
      "scheduleToStartTimeout" : "300",
      "startToCloseTimeout" : "600",
      "heartbeatTimeout" : "120"
   }
}
```

A decider receives a decision task when the workflow execution starts and each time a state change occurs in
the workflow execution. Deciders continue to move the workflow execution forward by receiving decision tasks and
responding to Amazon SWF with more decisions until the decider determines that the workflow execution is complete. It then
responds with a decision to close the workflow execution. After the workflow execution closes, Amazon SWF will not
schedule additional tasks for that execution.

In the e-commerce example, the decider determines if each step was performed correctly, and then either
schedules the next step or manages any error conditions.

A decider represents a single computer process or thread. Multiple deciders can process tasks for the same
workflow type.

## Activity Workers

An activity worker is a process or thread that performs the _activity
tasks_ that are part of your workflow. The activity task represents one of the tasks that you
identified in your application.

To use an activity task in your workflow, you must register it using either the Amazon SWF console or the [RegisterActivityType](../apireference/API_RegisterActivityType.md "../apireference/API_RegisterActivityType.md") action.

Each activity worker polls Amazon SWF for new tasks that are appropriate for that activity worker to perform;
certain tasks can be performed only by certain activity workers. After receiving a task, the activity worker
processes the task to completion and then reports to Amazon SWF that the task was completed and provides the result.
The activity worker then polls for a new task. The activity workers associated with a workflow execution continue
in this way, processing tasks until the workflow execution itself is complete. In the e-commerce example, activity
workers are independent processes and applications used by people, such as credit card processors and warehouse
employees, that perform individual steps in the process.

An activity worker represents a single computer process (or thread). Multiple activity workers can process
tasks of the same activity type.

## Data Exchange Between Actors

Input data can be provided to a workflow execution when it is started. Similarly, input data can be provided
to activity workers when they schedule activity tasks. When an activity task is complete, the activity worker can
return results to Amazon SWF. Similarly, a decider can report the results of a workflow execution when the execution is
complete. Each actor can send data to, and receive data from, Amazon SWF through strings, the form of which is
user-defined. Depending on the size and sensitivity of the data, you can pass data directly or pass a pointer to
data stored on another system or service (such as Amazon S3 or DynamoDB). Both the data passed directly and the pointers
to other data stores are recorded in the workflow execution history; however, Amazon SWF doesn't copy or cache any of
the data from external stores as part of the history.

Because Amazon SWF maintains the complete execution state of each workflow execution, including the inputs and
the results of tasks, all actors can be stateless. As a result, workflow processing is highly scalable. As the
load on your system grows, you can simply add more actors to increase capacity.
