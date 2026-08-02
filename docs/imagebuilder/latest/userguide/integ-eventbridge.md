# Amazon EventBridge integration in Image Builder

Amazon EventBridge is a serverless event bus service that you can use to connect your Image Builder application
with related data from other AWS services. In EventBridge, a rule matches incoming events and
sends them to targets for processing. A single rule can send an event to multiple
targets, and these events then run in parallel.

With EventBridge, you can automate your AWS services and respond automatically to system events
such as application availability issues or resource changes. AWS services deliver
events to EventBridge in near real time. You can set up rules that react to incoming
events to initiate actions. For example, sending an event to a Lambda function when the
status of an EC2 instance changes from pending to running. EventBridge calls these matching
definitions _event patterns_. To create a rule based on an event
pattern, see [Creating Amazon EventBridge rules that
react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

Image Builder works with EventBridge in two independent directions. Choose the one that matches your
goal:

- **Run a pipeline in response to an event (Image Builder as a
  target).** EventBridge starts a pipeline build when an event matches a rule, or
  when a schedule fires.
- **React to what Image Builder reports (Image Builder as a source).**
  Image Builder publishes events to the default event bus that you can match and route to
  your own targets.
  For step-by-step procedures for both directions, see [Use EventBridge with Image Builder pipelines](ev-rules-for-pipeline.md "ev-rules-for-pipeline.md"). For the event
  catalog, see [Event messages that Image Builder sends](#integ-eb-event-summary "#integ-eb-event-summary").

Actions that can be automatically initiated include the following:

- Invoke an AWS Lambda function
- Invoke Amazon EC2 Run Command
- Relay the event to Amazon Kinesis Data Streams
- Activate an AWS Step Functions state machine
- Notify an Amazon SNS topic or an Amazon SQS queue
  You can also set up scheduling rules for the default event bus to perform an action at
  regular intervals, such as running an Image Builder pipeline to refresh an image on a quarterly
  basis. There are two types of schedule expressions:

- **cron expressions** – The following
  example of a cron expression schedules a task to run every day at noon
  UTC+0:

`cron(0 12 * * ? *)`

For more information about using cron expressions with EventBridge, see [Cron
expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-cron-expressions "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-cron-expressions") in the _Amazon EventBridge User Guide_.

- **rate expressions** – The following
  example of a rate expression schedules a task to run every 12 hours:

`rate(12 hour)`

For more information about using rate expressions with EventBridge, see [Rate
expressions](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md#eb-rate-expressions") in the _Amazon EventBridge User Guide_.
For more information about how EventBridge rules integrate with Image Builder image pipelines, see [Use EventBridge with Image Builder pipelines](ev-rules-for-pipeline.md "ev-rules-for-pipeline.md").

###### Note

A pipeline's built-in schedule and an EventBridge schedule rule are different
mechanisms:

- A **pipeline schedule**
  (`schedule.scheduleExpression`) is part of the pipeline resource.
  Image Builder evaluates it, can gate a build on dependency updates with
  `pipelineExecutionStartCondition`, and can auto-disable a failing
  pipeline with `autoDisablePolicy`.
- An **EventBridge schedule rule** lives in EventBridge in
  your account and always starts a build when the schedule fires; it has no
  dependency gating and no auto-disable behavior.

## Event messages that Image Builder sends

Image Builder sends events to the default EventBridge event bus when an Image Builder resource reaches a
significant point in its lifecycle—for example, when an image changes
state, a scan completes, a workflow step pauses for input, or a pipeline is
automatically disabled. Every event uses the source `aws.imagebuilder`.

The following sections describe each event: when Image Builder sends it, the fields in the
event `detail`, and the resource ARNs in the `resources`
array. To act on these events, see [React to events that Image Builder sends](ev-rules-for-pipeline.md#ev-create-reaction-rule "ev-rules-for-pipeline.md#ev-create-reaction-rule"). The account IDs, Regions, ARNs, and
timestamps in the examples are placeholders—replace them with your
own.

###### Topics

- [EC2 Image Builder Image State Change](#eb-event-state-change "#eb-event-state-change")
- [EC2 Image Builder CVE Detected](#eb-event-cve-detected "#eb-event-cve-detected")
- [EC2 Image Builder Workflow Step Waiting](#eb-event-wf-step-waiting "#eb-event-wf-step-waiting")
- [EC2 Image Builder Image Pipeline Automatically Disabled](#eb-event-pipeline-disabled "#eb-event-pipeline-disabled")

### EC2 Image Builder Image State Change

Image Builder sends this event when the state changes for an image resource
during image creation. For example, when the image status changes from
one state to another, as follows:

- From `building` to `testing`
- From `testing` to `distribution`
- From `testing` to `failed`
- From `integrating` to `available`

```
{
    "version": "0",
    "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "detail-type": "EC2 Image Builder Image State Change",
    "source": "aws.imagebuilder",
    "account": "`111122223333`",
    "time": "2024-01-18T17:50:56Z",
    "region": "`us-west-2`",
    "resources": ["arn:aws:imagebuilder:`us-west-2`:`111122223333`:image/cmkencryptedworkflowtest-`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`/1.0.0/1"],
    "detail": {
        "previous-state": {
            "status": "TESTING"
        },
        "state": {
            "status": "AVAILABLE"
        }
    }
}
```

Image Builder sends this event
each time an image resource changes state during image creation, across the
build transitions shown above.

The event `detail` contains the following fields:

| Field                   | Description                                                     |
| ----------------------- | --------------------------------------------------------------- |
| `previous-state.status` | The image status before the change (for example,<br>`TESTING`). |
| `state.status`          | The new image status (for example,<br>`AVAILABLE`).             |

The build-transition status values are `BUILDING`,
`TESTING`, `DISTRIBUTING`, `INTEGRATING`,
`AVAILABLE`, `CANCELLED`, and `FAILED`.

The `resources` array contains the ARN of the
image resource that changed state.

### EC2 Image Builder CVE Detected

If you have CVE detection enabled for your image, Image Builder sends a message
with the results whenever an image scan completes.

```
{
    "version": "0",
    "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "detail-type": "EC2 Image Builder CVE Detected",
    "source": "aws.imagebuilder",
    "account": "`111122223333`",
    "time": "2023-03-01T16:59:09Z",
    "region": "`us-east-1`",
    "resources": [
        "arn:aws:imagebuilder:`us-east-1`:`111122223333`:image/test-image/1.0.0/1",
        "arn:aws:imagebuilder:`us-east-1`:`111122223333`:image-pipeline/test-pipeline"
    ],
    "detail": {
        "resource-id": "`i-1234567890abcdef0`",
        "finding-severity-counts": {
            "all": 0,
            "critical": 0,
            "high": 0,
            "medium": 0
        }
    }
}
```

Image Builder sends this event
when an image scan completes, and only when you enable image scanning (Amazon Inspector) for
the image. If scanning is off, Image Builder doesn't send this event. To turn on scanning,
see [Configure security scans for Image Builder images in the AWS Management Console](image-security-findings.md#image-config-security-scans "image-security-findings.md#image-config-security-scans").

The event `detail` contains the following fields:

| Field                              | Description                                                           |
| ---------------------------------- | --------------------------------------------------------------------- |
| `resource-id`                      | The ID of the Amazon EC2 test instance that Image Builder<br>scanned. |
| `finding-severity-counts.all`      | Total number of findings across the reported<br>severities.           |
| `finding-severity-counts.critical` | Number of critical-severity findings.                                 |
| `finding-severity-counts.high`     | Number of high-severity findings.                                     |
| `finding-severity-counts.medium`   | Number of medium-severity findings.                                   |

###### Important

`finding-severity-counts` reports `critical`,
`high`, and `medium` counts plus the `all`
total. It does not report `low`, `informational`, or
`untriaged` findings. To review the full set of findings, see the
security findings in the Image Builder console or in Amazon Inspector.

The `resources` array contains the ARN of the
image resource, and the ARN of the image pipeline when the scan ran from a
pipeline.

### EC2 Image Builder Workflow Step Waiting

Image Builder sends a message when a `WaitForAction` workflow step
pauses to wait for an asynchronous action to complete.

```
{
    "version": "0",
    "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "detail-type": "EC2 Image Builder Workflow Step Waiting",
    "source": "aws.imagebuilder",
    "account": "`111122223333`",
    "time": "2024-01-18T16:54:44Z",
    "region": "`us-west-2`",
    "resources": ["arn:aws:imagebuilder:`us-west-2`:`111122223333`:image/workflowstepwaitforactionwithvalidsnstopictest-`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`/1.0.0/1", "arn:aws:imagebuilder:`us-west-2`:`111122223333`:workflow/build/build-workflow-`a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`/1.0.0/1"],
    "detail": {
        "workflow-execution-id": "wf-`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
        "workflow-step-execution-id": "step-`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
        "workflow-step-name": "TestAutoSNSStop"
    }
}
```

Image Builder sends this event
when a `WaitForAction` workflow step pauses to wait for
your response. The workflow stays paused until you respond or the step times
out.

The event `detail` contains the following fields:

| Field                        | Description                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| `workflow-execution-id`      | The ID of the running workflow that contains the paused<br>step.              |
| `workflow-step-execution-id` | The ID of the specific step execution that is<br>waiting.                     |
| `workflow-step-name`         | The name of the `WaitForAction` step, as<br>defined in the workflow document. |

The `resources` array contains the ARN of the
image resource and the ARN of the workflow.

To respond, call
`SendWorkflowStepAction` with the
`workflow-step-execution-id` from the event and an `action`
of `RESUME` to continue, or `STOP` to end the build. See
[WaitForAction](wfdoc-step-actions.md#wfdoc-step-action-waitfor "wfdoc-step-actions.md#wfdoc-step-action-waitfor"). To drive this from an event
automatically, see [React to events that Image Builder sends](ev-rules-for-pipeline.md#ev-create-reaction-rule "ev-rules-for-pipeline.md#ev-create-reaction-rule").

### EC2 Image Builder Image Pipeline Automatically Disabled

If you've configured the `autoDisablePolicy` for your pipeline, then
Image Builder disables the pipeline and sends an event message to EventBridge when the number of
consecutive scheduled pipeline execution failures exceeds the maximum number that's
allowed per the policy.

```
{
    "version": "0",
    "id": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
    "detail-type": "EC2 Image Builder Image Pipeline Automatically Disabled",
    "source": "aws.imagebuilder",
    "account": "`111122223333`",
    "time": "2025-09-18T16:54:44Z",
    "region": "`us-west-2`",
    "resources": ["arn:aws:imagebuilder:`us-west-2`:`111122223333`:`image-pipeline/disabled-image-pipeline-name`"],
    "detail": {
        "consecutive-failures": "5"
    }
}
```

If you configure an
`autoDisablePolicy` on a pipeline's schedule, Image Builder counts consecutive
failures of **scheduled** builds. When the count
reaches the policy's `failureCount`, Image Builder disables the pipeline and
sends this event.

The event `detail` contains the following fields:

| Field                  | Description                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------- |
| `consecutive-failures` | The number of consecutive scheduled-build failures that<br>triggered the auto-disable. |

The `resources` array contains the ARN of the
pipeline that was disabled.

###### Note

Only scheduled builds count toward the total. A manual build that fails
does not increase it; a manual or scheduled build that succeeds—and
creating or updating the pipeline—resets it to zero. See
`autoDisablePolicy` in the
_EC2 Image Builder API Reference_.
