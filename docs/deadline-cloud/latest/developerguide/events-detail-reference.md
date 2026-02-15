# Deadline Cloud events detail reference

All events from AWS services have a common set of fields containing
metadata about the event, such as the AWS service that is the source of
the event, the time the event was generated, the account and region in which the event
took place, and others. For definitions of these general fields, see [Event structure reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User
Guide_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The reference below defines the detail fields for the various
Deadline Cloud events.

When using EventBridge to select and manage Deadline Cloud events, it's useful to keep
the following in mind:

- The `source` field for all events from Deadline Cloud is set to
  `aws.deadline`.
- The `detail-type` field specifies the event type.

For example, `Fleet Size Recommendation Change`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match Deadline Cloud
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

###### Topics

- [Budget Threshold Reached event](#event-detail-budget-threshold-reached "#event-detail-budget-threshold-reached")
- [Fleet Size Recommendation Change event](#event-detail-fleet-size-recommendation-change "#event-detail-fleet-size-recommendation-change")
- [Job Lifecycle Status Change event](#event-detail-job-lifecycle-status-change "#event-detail-job-lifecycle-status-change")
- [Job Run Status Change event](#event-detail-job-run-status-change "#event-detail-job-run-status-change")
- [Step Lifecycle Status Change event](#event-detail-step-lifecycle-status-change "#event-detail-step-lifecycle-status-change")
- [Step Run Status Change event](#event-detail-step-run-status-change "#event-detail-step-run-status-change")
- [Task Run Status Change event](#event-detail-task-run-status-change "#event-detail-task-run-status-change")

## Budget Threshold Reached event

You can use the Budget Threshold Reached event to monitor the percentage of a budget that
has been used. Deadline Cloud sends events when the percentage used passes the following
thresholds:

- 10, 20, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 96, 97, 98, 99, 100

The frequency that Deadline Cloud sends Budget Threshold Reached events increases as the budget nears
its limit. This frequency enables you to closely monitor a budget as it approaches its limit
and to take action to keep from overspending. You can also set your own budget
thresholds. Deadline Cloud sends an event when usage passes your custom thresholds.

If you change the amount of a budget, the next time Deadline Cloud sends a Budget Threshold Reached
event it is based on the current percentage of the budget that has been used. For
example, if you add $50 to an $100 budget that has reached its limit, the next
Budget Threshold Reached event indicates that the budget is at 75 percent.

Below are the detail fields for the `Budget Threshold Reached` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Budget Threshold Reached",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "budgetId": "budget-12345678900000000000000000000000",
        "thresholdInPercent": 0
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Budget Threshold Reached`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`budgetId`

The identifier of the budget that has reached a threshold.

`thresholdInPercent`

The percentage of the budget that has been used.

## Fleet Size Recommendation Change event

When you configure your fleet to use event-based auto scaling, Deadline Cloud sends out
events that you can use to manage your fleets. Each of these events contains
information about the current size and requested size of a fleet. For an example of
using an EventBridge event and an example Lambda function to handle the event, see [Auto scale your Amazon EC2 fleet with Deadline Cloud scale recommendation
feature](../userguide/create-auto-scaling.md#autoscale-ec2-fleet "../userguide/create-auto-scaling.md#autoscale-ec2-fleet").

The fleet size recommendation change event is sent when the following
occur:

- When the recommended fleet size changes and oldFleetSize is different from
  newFleetSize.
- When the service detects that the actual fleet size does not match the
  recommended fleet size. You can get the actual fleet size from the
  workerCount in the GetFleet operation response. This may happen when an
  active Amazon EC2 instance fails to register as a Deadline Cloud
  worker.

Below are the detail fields for the `Fleet Size Recommendation Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Fleet Size Recommendation Change",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "fleetId": "fleet-12345678900000000000000000000000",
        "oldFleetSize": 1,
        "newFleetSize": 5,
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Fleet Size Recommendation Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`fleetId`

The identifier of the fleet that needs a size change.

`oldFleetSize`

The current size of the fleet.

`newFleetSize`

The recommended new size for the fleet.

## Job Lifecycle Status Change event

When you create or update a job, Deadline Cloud sets the lifecycle status to show status of
the most recent user initiated action.

A job lifecycle status change event is sent for any lifecycle status change,
including when the job is created.

Below are the detail fields for the `Job Lifecycle Status Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Job Lifecycle Status Change",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "queueId": "queue-12345678900000000000000000000000",
        "jobId": "job-12345678900000000000000000000000",
        "previousLifecycleStatus": "UPDATE_IN_PROGRESS",
        "lifecycleStatus": "UPDATE_SUCCEEDED"
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Job Lifecycle Status Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`queueId`

The identifier of the queue that contains the job.

`jobId`

The identifier of the job.

`previousLifecycleStatus`

The lifecycle state that the job is leaving. This field is
not included when you first submit a job.

`lifecycleStatus`

The lifecycle state that the job is entering.

## Job Run Status Change event

A job is composed of many tasks. Each task has a status. The status of all tasks
are combined to give an overall status for a job. For more information, see [Job
states in Deadline Cloud](../userguide/jobs-states.md "../userguide/jobs-states.md") in the _AWS Deadline Cloud User Guide_.

A job run status change event is sent when:

- The combined [taskRunStatus](#job-run-status-change-field-5 "#job-run-status-change-field-5") field
  changes.
- The job is requeued, unless the job is in the READY state.

A job run status change event is NOT sent when:

- The job is first created. To monitor job creation, monitor Job Lifecycle Status Change
  events for changes.
- The job's [taskRunStatusCounts](#job-run-status-change-field-6 "#job-run-status-change-field-6") field changes
  but the combined job task run status does not change.

Below are the detail fields for the `Job Run Status Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Job Run Status Change",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "queueId": "queue-12345678900000000000000000000000",
        "jobId": "job-12345678900000000000000000000000",
        "previousTaskRunStatus": "RUNNING",
        "taskRunStatus": "SUCCEEDED",
        "taskRunStatusCounts": {
            "PENDING": 0,
            "READY": 0,
            "RUNNING": 0,
            "ASSIGNED": 0,
            "STARTING": 0,
            "SCHEDULED": 0,
            "INTERRUPTING": 0,
            "SUSPENDED": 0,
            "CANCELED": 0,
            "FAILED": 0,
            "SUCCEEDED": 20,
            "NOT_COMPATIBLE": 0
       }
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Job Run Status Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`queueId`

The identifier of the queue that contains the job.

`jobId`

The identifier of the job.

`previousTaskRunStatus`

The task run state that the job is leaving.

`taskRunStatus`

The task run state that the job is entering.

`taskRunStatusCounts`

The number of the job's tasks in each state.

## Step Lifecycle Status Change event

When you create or update an event, Deadline Cloud sets the job's lifecycle status to
describe the status of the most recent user initiated action.

A step lifecycle status change event is sent when:

- A step update starts (UPDATE_IN_PROGRESS).
- A step update completed successfully (UPDATE_SUCCEEDED).
- A step update failed (UPDATE_FAILED).

An event is not sent when the step is first created. To monitor step creation,
monitor Job Lifecycle Status Change events for changes.

Below are the detail fields for the `Step Lifecycle Status Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Step Lifecycle Status Change",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "queueId": "queue-12345678900000000000000000000000",
        "jobId": "job-12345678900000000000000000000000",
        "stepId": "step-12345678900000000000000000000000",
        "previousLifecycleStatus": "UPDATE_IN_PROGRESS",
        "lifecycleStatus": "UPDATE_SUCCEEDED"
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Step Lifecycle Status Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`queueId`

The identifier of the queue that contains the job.

`jobId`

The identifier of the job.

`stepId`

The identifier of the current job step.

`previousLifecycleStatus`

The lifecycle state that the step is leaving.

`lifecycleStatus`

The lifecycle state that the step is entering.

## Step Run Status Change event

Each step in a job is composed of many tasks. Each task has a status. The task
statuses are combined to give an overall status for steps and jobs.

A step run status change event is sent when:

- The combined [taskRunStatus](#step-run-status-change-field-6 "#step-run-status-change-field-6")
  changes.
- The step is requeued, unless that step is in the READY state.

An event is not sent when:

- The step is first created. To monitor step creation, monitor
  Job Lifecycle Status Change events for changes.
- The step's [taskRunStatusCounts](#step-run-status-change-field-7 "#step-run-status-change-field-7") changes but
  the combined step task run status does not change.

Below are the detail fields for the `Step Run Status Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Step Run Status Change",
    "source": "aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "queueId": "queue-12345678900000000000000000000000",
        "jobId": "job-12345678900000000000000000000000",
        "stepId": "step-12345678900000000000000000000000",
        "previousTaskRunStatus": "RUNNING",
        "taskRunStatus": "SUCCEEDED",
        "taskRunStatusCounts": {
            "PENDING": 0,
            "READY": 0,
            "RUNNING": 0,
            "ASSIGNED": 0,
            "STARTING": 0,
            "SCHEDULED": 0,
            "INTERRUPTING": 0,
            "SUSPENDED": 0,
            "CANCELED": 0,
            "FAILED": 0,
            "SUCCEEDED": 20,
            "NOT_COMPATIBLE": 0
       }
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Step Run Status Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`queueId`

The identifier of the queue that contains the job.

`jobId`

The identifier of the job.

`stepId`

The identifier of the current job step.

`previousTaskRunStatus`

The run state that the step is leaving.

`taskRunStatus`

The run state that the step is entering.

`taskRunStatusCounts`

The number of the step's tasks in each state.

## Task Run Status Change event

The [runStatus](#task-run-status-change-field-7 "#task-run-status-change-field-7") field is updated as the task
runs. An event is sent when:

- The task's run status changes.
- The task is requeued, unless the task is in the READY state.

An event is not sent when:

- The task is first created. To monitor task creation, monitor
  Job Lifecycle Status Change events for changes.

Below are the detail fields for the `Task Run Status Change` event.

The `source` and `detail-type` fields are included below because they contain specific values for Deadline Cloud events. For
definitions of the other metadata fields that are included in all events, see [Event structure
reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User Guide_.

```
{
    "version": "0",
    "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "detail-type": "Task Run Status Change",
    "source": "aws.aws.deadline",
    "account": "111122223333",
    "time": "2017-12-22T18:43:48Z",
    "region": "aa-example-1",
    "resources": [],
    "detail": {
        "farmId": "farm-12345678900000000000000000000000",
        "queueId": "queue-12345678900000000000000000000000",
        "jobId": "job-12345678900000000000000000000000",
        "stepId": "step-12345678900000000000000000000000",
        "taskId": "task-12345678900000000000000000000000-0",
        "previousRunStatus": "RUNNING",
        "runStatus": "SUCCEEDED"
    }
}
```

`detail-type`

Identifies the type of event.

For this event, this value is `Fleet Size Recommendation Change`.

`source`

Identifies the service that generated the event. For Deadline Cloud events,
this value is `aws.deadline`.

`detail`

A JSON object that contains information about the event. The service
generating the event determines the content of this field.

For this event, this data includes:

`farmId`

The identifier of the farm that contains the job.

`queueId`

The identifier of the queue that contains the job.

`jobId`

The identifier of the job.

stepId

The identifier of the current job step.

`taskId`

The identifier of the running task.

`previousRunStatus`

The run state that the task is leaving.

`runStatus`

The run status that the task is entering.
