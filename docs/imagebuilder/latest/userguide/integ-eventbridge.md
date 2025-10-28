# Amazon EventBridge integration in Image Builder

Amazon EventBridge is a serverless event bus service that you can use to connect your Image Builder application
with related data from other AWS services. In EventBridge, a rule matches incoming events and
sends them to targets for processing. A single rule can send an event to multiple
targets, and these events then run in parallel.

With EventBridge, you can automate your AWS services and respond automatically to system events
such as application availability issues or resource changes. Events from AWS services
are delivered to EventBridge in near real time. You can set up rules that react to incoming
events to initiate actions. For example, sending an event to a Lambda function when the
status of an EC2 instance changes from pending to running. These are called
_patterns_. To create a rule based on an event pattern, see
[Creating Amazon EventBridge rules that react to
events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

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
For more information about how EventBridge rules integrate with Image Builder image pipelines, see [Use EventBridge rules with Image Builder pipelines](ev-rules-for-pipeline.md "ev-rules-for-pipeline.md").

## Event messages that Image Builder sends

Image Builder sends event messages to EventBridge when there are significant changes in status for
Image Builder resources. For example, when there's a state change for an image. The following
examples show typical JSON event messages that Image Builder might send.

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
