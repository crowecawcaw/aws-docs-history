# Monitoring CodePipeline events

You can monitor CodePipeline events in EventBridge, which delivers a stream of real-time data from your
own applications, software-as-a-service (SaaS) applications, and AWS services. EventBridge routes that
data to targets such as AWS Lambda and Amazon Simple Notification Service. These events are the same as those that appear
in Amazon CloudWatch Events, which delivers a near real-time stream of system events that describe changes in
AWS resources. For more information, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md") in
the _Amazon EventBridge User Guide_.

###### Note

Amazon EventBridge is the preferred way to manage your events. Amazon CloudWatch Events and EventBridge are the same
underlying service and API, but EventBridge provides more features. Changes you make in either CloudWatch Events
or EventBridge will appear in each console.

Events are composed of rules. A rule is configured by choosing the following:

- **Event Pattern.** Each rule is expressed as an event
  pattern with the source and type of events to monitor, and event targets. To monitor events,
  you create a rule with the service you are monitoring as the event source, such as CodePipeline.
  For example, you can create a rule with an event pattern that that uses CodePipeline as an event
  source to trigger the rule when there are changes in the state of a pipeline, stage, or
  action.
- **Targets.** The new rule receives a selected service as
  the event target. You might want to set up a target service to send notifications, capture
  state information, take corrective action, initiate events, or take other actions. When you
  add your target, you must also grant permissions to EventBridge to allow it to invoke the selected
  target service.
  Each type of execution state change event emits notifications with specific message content,
  where:

- The initial `version` entry shows the version number for the event.
- The `version` entry under pipeline `detail` shows the pipeline
  structure version number.
- The `execution-id` entry under pipeline `detail` shows the
  execution ID for the pipeline execution that caused the state change. Refer to the
  **GetPipelineExecution** API call in the [AWS CodePipeline API Reference](../APIReference.md "../APIReference.md").
- The `pipeline-execution-attempt` entry shows the number of attempts, or
  retries, for the specific execution ID.
  CodePipeline reports an event to EventBridge whenever the state of a resource in your AWS account
  changes. Events are emitted on a guaranteed, at-least-once basis for the following
  resources:

- Pipeline executions
- Stage executions
- Action executions
  Events are emitted by EventBridge with the event pattern and schema detailed above. For processed
  events, such as events you receive through notifications you have configured in the Developer
  Tools console, the event message includes event pattern fields with some variation. For example,
  the `detail-type` field is converted to `detailType`. For more
  information, refer to the **PutEvents** API call in the [Amazon EventBridge API Reference](../../../eventbridge/latest/APIReference.md "../../../eventbridge/latest/APIReference.md").

The following examples show events for CodePipeline. Where possible, each example shows the schema
for an emitted event along with the schema for a processed event.

###### Topics

- [Detail types](#detect-state-events-types "#detect-state-events-types")
- [Pipeline-level events](#detect-state-events-pipeline "#detect-state-events-pipeline")
- [Stage-level events](#detect-state-events-stage "#detect-state-events-stage")
- [Action-level events](#detect-state-events-action "#detect-state-events-action")
- [Create a Rule That Sends a Notification on a
  Pipeline Event](#create-cloudwatch-notifications "#create-cloudwatch-notifications")

## Detail types

When you set up events to monitor, you can choose the detail type for the event.

You can configure notifications to be sent when the state changes for:

- Specified pipelines or all your pipelines. You control this by using
  `"detail-type":`
  `"CodePipeline Pipeline Execution State Change"`.
- Specified stages or all your stages, within a specified pipeline or all your
  pipelines. You control this by using `"detail-type":`
  `"CodePipeline Stage Execution State Change"`.
- Specified actions or all actions, within a specified stage or all stages, within a
  specified pipeline or all your pipelines. You control this by using
  `"detail-type":`
  `"CodePipeline Action Execution State Change"`.

###### Note

Events emitted by EventBridge contain the `detail-type` parameter, which is
converted to `detailType` when events are processed.

| Detail type                                  | State                                                                                                                                                            | Description                                                                             |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| CodePipeline Pipeline Execution State Change | CANCELED                                                                                                                                                         | The pipeline execution was canceled because the pipeline structure was<br>updated.      |
| FAILED                                       | The pipeline execution was not completed successfully.                                                                                                           |
| RESUMED                                      | A failed pipeline execution has been retried in response to the<br>`RetryStageExecution` API call.                                                               |
| STARTED                                      | The pipeline execution is currently running.                                                                                                                     |
| STOPPED                                      | The stopping process is complete, and the pipeline execution is stopped.                                                                                         |
| STOPPING                                     | The pipeline execution is stopping due to a request to either stop and wait or<br>stop and abandon the pipeline execution.                                       |
| SUCCEEDED                                    | The pipeline execution was completed successfully.                                                                                                               |
| SUPERSEDED                                   | While this pipeline execution was waiting for the next stage to be completed, a<br>newer pipeline execution advanced and continued through the pipeline instead. |
| CodePipeline Stage Execution State Change    | CANCELED                                                                                                                                                         | The stage was canceled because the pipeline structure was updated.                      |
| FAILED                                       | The stage was not completed successfully.                                                                                                                        |
| RESUMED                                      | A failed stage has been retried in response to the<br>`RetryStageExecution` API call.                                                                            |
| STARTED                                      | The stage is currently running.                                                                                                                                  |
| STOPPED                                      | The stopping process is complete, and the stage execution is stopped.                                                                                            |
| STOPPING                                     | The stage execution is stopping due to a request to either stop and wait or stop<br>and abandon the pipeline execution.                                          |
| SUCCEEDED                                    | The stage was completed successfully.                                                                                                                            |
| CodePipeline Action Execution State Change   | ABANDONED                                                                                                                                                        | The action is abandoned due to a request to stop and abandon the pipeline<br>execution. |
| CANCELED                                     | The action was canceled because the pipeline structure was updated.                                                                                              |
| FAILED                                       | For approval actions, the FAILED state means the action was either rejected by<br>the reviewer or failed due to an incorrect action configuration.               |
| STARTED                                      | The action is currently running.                                                                                                                                 |
| SUCCEEDED                                    | The action was completed successfully.                                                                                                                           |

## Pipeline-level events

Pipeline-level events are emitted when there is a state change for a pipeline
execution.

###### Topics

- [Pipeline STARTED event](#detect-state-events-pipeline-started "#detect-state-events-pipeline-started")
- [Pipeline STOPPING event](#detect-state-events-pipeline-stopping "#detect-state-events-pipeline-stopping")
- [Pipeline SUCCEEDED event](#detect-state-events-pipeline-succeeded "#detect-state-events-pipeline-succeeded")
- [Pipeline SUCCEEDED (example with Git tags)](#w2aac42c13c29c15 "#w2aac42c13c29c15")
- [Pipeline FAILED event](#detect-state-events-pipeline-failed "#detect-state-events-pipeline-failed")
- [Pipeline FAILED (example with Git tags)](#w2aac42c13c29c23 "#w2aac42c13c29c23")

### Pipeline STARTED event

When a pipeline execution starts, it emits an event that sends notifications with the
following content. This example is for the pipeline named `"myPipeline"` in the
`us-east-1` Region. The `id` field represents the event ID, and the
`account` field represents the account ID where the pipeline is created.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:03:07Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "execution-trigger": {
            "trigger-type": "StartPipelineExecution",
            "trigger-detail": "arn:aws:sts::123456789012:assumed-role/Admin/my-user"
        },
        "state": "STARTED",
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Pipeline Execution State Change",
    "region": "us-east-1",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:44:50Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "execution-trigger": {
            "trigger-type": "StartPipelineExecution",
            "trigger-detail": "arn:aws:sts::123456789012:assumed-role/Admin/my-user"
        },
        "state": "STARTED",
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "additionalAttributes": {}
}
```

### Pipeline STOPPING event

When a pipeline execution is stopping, it emits an event that sends notifications with
the following content. This example is for the pipeline named `myPipeline` in the
`us-west-2` Region.

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:02:20Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "state": "STOPPING",
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
        "stop-execution-comments": "Stopping the pipeline for an update"
    }
}
```

### Pipeline SUCCEEDED event

When a pipeline execution succeeds, it emits an event that sends notifications with the
following content. This example is for the pipeline named `myPipeline` in the
`us-east-1` Region.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:03:44Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "state": "SUCCEEDED",
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Pipeline Execution State Change",
    "region": "us-east-1",
    "source": "aws.codepipeline",
    "time": "2021-06-30T22:13:51Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "state": "SUCCEEDED",
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "additionalAttributes": {}
}
```

### Pipeline SUCCEEDED (example with Git tags)

When a pipeline execution has a stage that has been retried and succeeded, it emits an
event that sends notifications with the following content. This example is for the pipeline
named `myPipeline` in the `eu-central-1` Region where the
`execution-trigger` is configured for Git tags.

###### Note

The `execution-trigger` field will have either `tag-name` or
`branch-name`, depending on what kind of event triggered the pipeline.

```
{
    "version": "0",
    "id": "b128b002-09fd-4574-4eba-27152726c777",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2023-10-26T13:50:53Z",
    "region": "eu-central-1",
    "resources": [
        "arn:aws:codepipeline:eu-central-1:123456789012:BuildFromTag"
    ],
    "detail": {
        "pipeline": "BuildFromTag",
        "execution-id": "e17b5773-cc0d-4db2-9ad7-594c73888de8",
        "start-time": "2023-10-26T13:49:39.208Z",
        "execution-trigger": {
            "author-display-name": "Mary Major",
            "full-repository-name": "mmajor/sample-project",
            "provider-type": "GitLab",
            "author-email": "email_address",
            "commit-message": "Update file README.md",
            "author-date": "2023-08-16T21:08:08Z",
            "tag-name": "gitlab-v4.2.1",
            "commit-id": "`commit_ID`",
            "connection-arn": "arn:aws:codestar-connections:eu-central-1:123456789012:connection/0f5b706a-1a1d-46c5-86b6-f177321bcfb2",
            "author-id": "Mary Major"
        },
        "state": "SUCCEEDED",
        "version": 32.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

### Pipeline FAILED event

When a pipeline execution fails, it emits an event that sends notifications with the
following content. This example is for the pipeline named `"myPipeline"` in the
`us-west-2` Region.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-31T18:55:43Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "state": "FAILED",
        "version": 4.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Pipeline Execution State Change",
    "region": "us-west-2",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:46:16Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "state": "FAILED",
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "additionalAttributes": {
        "failedActionCount": 1,
        "failedActions": [
            {
                "action": "Deploy",
                "additionalInformation": "Deployment <ID> failed"
            }
        ],
        "failedStage": "Deploy"
    }

```

### Pipeline FAILED (example with Git tags)

Unless it fails at the source stage, for a pipeline configure with triggers, it emits an
event that sends notifications with the following content. This example is for the pipeline
named `myPipeline` in the `eu-central-1` Region where the
`execution-trigger` is configured for Git tags.

###### Note

The `execution-trigger` field will have either `tag-name` or
`branch-name`, depending on what kind of event triggered the pipeline.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Pipeline Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-31T18:55:43Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "execution-trigger": {
            "author-display-name": "Mary Major",
            "full-repository-name": "mmajor/sample-project",
            "provider-type": "GitLab",
            "author-email": "email_address",
            "commit-message": "Update file README.md",
            "author-date": "2023-08-16T21:08:08Z",
            "tag-name": "gitlab-v4.2.1",
            "commit-id": "`commit_ID`",
            "connection-arn": "arn:aws:codestar-connections:eu-central-1:123456789012:connection/0f5b706a-1a1d-46c5-86b6-f177321bcfb2",
            "author-id": "Mary Major"
        },
        "state": "FAILED",
        "version": 4.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Pipeline Execution State Change",
    "region": "us-west-2",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:46:16Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "execution-trigger": {
            "author-display-name": "Mary Major",
            "full-repository-name": "mmajor/sample-project",
            "provider-type": "GitLab",
            "author-email": "email_address",
            "commit-message": "Update file README.md",
            "author-date": "2023-08-16T21:08:08Z",
            "tag-name": "gitlab-v4.2.1",
            "commit-id": "`commit_ID`",
            "connection-arn": "arn:aws:codestar-connections:eu-central-1:123456789012:connection/0f5b706a-1a1d-46c5-86b6-f177321bcfb2",
            "author-id": "Mary Major"
        },
        "state": "FAILED",
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "additionalAttributes": {
        "failedActionCount": 1,
        "failedActions": [
            {
                "action": "Deploy",
                "additionalInformation": "Deployment <ID> failed"
            }
        ],
        "failedStage": "Deploy"
    }

```

## Stage-level events

Stage-level events are emitted when there is a state change for a stage execution.

###### Topics

- [Stage STARTED event](#detect-state-events-stage-started "#detect-state-events-stage-started")
- [Stage STOPPING event](#detect-state-events-stage-stopping "#detect-state-events-stage-stopping")
- [Stage STOPPED event](#detect-state-events-stage-stopped "#detect-state-events-stage-stopped")
- [Stage RESUMED after stage retry event](#w2aac42c13c31c15 "#w2aac42c13c31c15")

### Stage STARTED event

When a stage execution starts, it emits an event that sends notifications with the
following content. This example is for the pipeline named `"myPipeline"` in the
`us-east-1` Region, for the stage `Prod`.

Emitted event

```
{
    "version": "0",
    "id": 01234567-EXAMPLE,
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "account": 123456789012,
    "time": "2020-01-24T22:03:07Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "version": 1.0,
        "execution-id": 12345678-1234-5678-abcd-12345678abcd,
        "start-time": "2023-10-26T13:49:39.208Z",
        "stage": "Prod",
        "state": "STARTED",
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Stage Execution State Change",
    "region": "us-east-1",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:45:40Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "stage": "Source",
        "state": "STARTED",
        "version": 1.0,
        "pipeline-execution-attempt": 0.0
    },
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "additionalAttributes": {
        "sourceActions": [
            {
                "sourceActionName": "Source",
                "sourceActionProvider": "CodeCommit",
                "sourceActionVariables": {
                    "BranchName": "main",
                    "CommitId": "<ID>",
                    "RepositoryName": "my-repo"
                }
            }
        ]
    }
}
```

### Stage STOPPING event

When a stage execution is stopping, it emits an event that sends notifications with the
following content. This example is for the pipeline named `myPipeline` in the
`us-west-2` Region, for the stage `Deploy`.

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:02:20Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "stage": "Deploy",
        "state": "STOPPING",
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

### Stage STOPPED event

When a stage execution is stopped, it emits an event that sends notifications with the
following content. This example is for the pipeline named `myPipeline` in the
`us-west-2` Region, for the stage `Deploy`.

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-31T18:21:39Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:49:39.208Z",
        "stage": "Deploy",
        "state": "STOPPED",
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

### Stage RESUMED after stage retry event

When a stage execution is resumed and has a stage that has been retried, it emits an
event that sends notifications with the following content.

When a stage has been retried, the `stage-last-retry-attempt-time` field
displays, as shown in the example. The field displays on all stage events if a retry was
performed.

###### Note

The `stage-last-retry-attempt-time` field will be present in all the
subsequent stage events after a stage has been retried.

```
{
    "version": "0",
    "id": "38656bcd-a798-5f92-c738-02a71be484e1",
    "detail-type": "CodePipeline Stage Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2023-10-26T14:14:56Z",
    "region": "eu-central-1",
    "resources": [
        "arn:aws:codepipeline:eu-central-1:123456789012:BuildFromTag"
    ],
    "detail": {
        "pipeline": "BuildFromTag",
        "execution-id": "05dafb6a-5a56-4951-a858-968795364846",
        "stage-last-retry-attempt-time": "2023-10-26T14:14:56.305Z",
        "stage": "Build",
        "state": "RESUMED",
        "version": 32.0,
        "pipeline-execution-attempt": 2.0
    }
}
```

## Action-level events

Action-level events are emitted when there is a state change for an action
execution.

###### Topics

- [Action STARTED event](#detect-state-events-action-started "#detect-state-events-action-started")
- [Action SUCCEEDED event](#detect-state-events-action-succeeded "#detect-state-events-action-succeeded")
- [Action FAILED event](#detect-state-events-action-failed "#detect-state-events-action-failed")
- [Action ABANDONED event](#detect-state-events-action-abandoned "#detect-state-events-action-abandoned")

### Action STARTED event

When an action execution starts, it emits an event that sends notifications with the
following content. This example is for the pipeline named `myPipeline` in the
`us-east-1` Region, for the deployment action `myAction`.

Emitted event

```
{
    "version": "0",
    "id": 01234567-EXAMPLE,
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "account": 123456789012,
    "time": "2020-01-24T22:03:07Z",
    "region": "us-east-1",
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": 12345678-1234-5678-abcd-12345678abcd,
        "start-time": "2023-10-26T13:51:09.981Z",
        "stage": "Prod",
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "myAction",
        "state": "STARTED",
        "type": {
            "owner": "AWS",
            "category": "Deploy",
            "provider": "CodeDeploy",
            "version": "1"
        },
        "version": 2.0
        "pipeline-execution-attempt": 1.0
        "input-artifacts": [
            {
                "name": "SourceArtifact",
                "s3location": {
                    "bucket": "codepipeline-us-east-1-BUCKETEXAMPLE",
                    "key": "myPipeline/SourceArti/KEYEXAMPLE"
                }
            }
        ]
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Action Execution State Change",
    "region": "us-west-2",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:45:44Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:51:09.981Z",
        "stage": "Deploy",
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Deploy",
        "input-artifacts": [
            {
                "name": "SourceArtifact",
                "s3location": {
                    "bucket": "codepipeline-us-east-1-EXAMPLE",
                    "key": "myPipeline/SourceArti/EXAMPLE"
                }
            }
        ],
        "state": "STARTED",
        "region": "us-east-1",
        "type": {
            "owner": "AWS",
            "provider": "CodeDeploy",
            "category": "Deploy",
            "version": "1"
        },
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-east-1:123456789012:myPipeline"
    ],
    "additionalAttributes": {}
}

```

### Action SUCCEEDED event

When an action execution succeeds, it emits an event that sends notifications with the
following content. This example is for the pipeline named `"myPipeline"` in the
`us-west-2` Region, for the source action `"Source"`. For this event
type, there are two different `region` fields. The event `region`
field specifies the Region for the pipeline event. The `region` field under the
`detail` section specifies the Region for the action.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-24T22:03:11Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:51:09.981Z",
        "stage": "Source",
        "execution-result": {
            "external-execution-url": "https://us-west-2.console.aws.amazon.com/codecommit/home#/repository/my-repo/commit/8cf40f2EXAMPLE",
            "external-execution-summary": "Added LICENSE.txt",
            "external-execution-id": "8cf40fEXAMPLE"
        },
        "output-artifacts": [
            {
                "name": "SourceArtifact",
                "s3location": {
                    "bucket": "codepipeline-us-west-2-BUCKETEXAMPLE",
                    "key": "myPipeline/SourceArti/KEYEXAMPLE"
                }
            }
        ],
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Source",
        "state": "SUCCEEDED",
        "region": "us-west-2",
        "type": {
            "owner": "AWS",
            "provider": "CodeCommit",
            "category": "Source",
            "version": "1"
        },
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Action Execution State Change",
    "region": "us-west-2",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:45:44Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:ACCOUNT:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "arn:aws:codepipeline:us-west-2:123456789012:myPipeline",
        "start-time": "2023-10-26T13:51:09.981Z",
        "stage": "Source",
        "execution-result": {
            "external-execution-url": "https://us-west-2.console.aws.amazon.com/codecommit/home#/repository/my-repo/commit/8cf40f2EXAMPLE",
            "external-execution-summary": "Edited index.html",
            "external-execution-id": "36ab3ab7EXAMPLE"
        },
        "output-artifacts": [
            {
                "name": "SourceArtifact",
                "s3location": {
                    "bucket": "codepipeline-us-west-2-EXAMPLE",
                    "key": "myPipeline/SourceArti/EXAMPLE"
                }
            }
        ],
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Source",
        "state": "SUCCEEDED",
        "region": "us-west-2",
        "type": {
            "owner": "AWS",
            "provider": "CodeCommit",
            "category": "Source",
            "version": "1"
        },
        "version": 1.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "additionalAttributes": {}
}

```

### Action FAILED event

When an action execution fails, it emits an event that sends notifications with the
following content. This example is for the pipeline named `"myPipeline"` in the
`us-west-2` Region, for the action `"Deploy"`.

Emitted event

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-31T18:55:43Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "start-time": "2023-10-26T13:51:09.981Z",
        "stage": "Deploy",
        "execution-result": {
            "external-execution-url": "https://us-west-2.console.aws.amazon.com/codedeploy/home?#/deployments/<ID>",
            "external-execution-summary": "Deployment <ID> failed",
            "external-execution-id": "<ID>",
            "error-code": "JobFailed"
        },
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Deploy",
        "state": "FAILED",
        "region": "us-west-2",
        "type": {
            "owner": "AWS",
            "provider": "CodeDeploy",
            "category": "Deploy",
            "version": "1"
        },
        "version": 4.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

Processed event

```
{
    "account": "123456789012",
    "detailType": "CodePipeline Action Execution State Change",
    "region": "us-west-2",
    "source": "aws.codepipeline",
    "time": "2021-06-24T00:46:16Z",
    "notificationRuleArn": "arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/a69c62c21EXAMPLE",
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "stage": "Deploy",
        "execution-result": {
            "external-execution-url": "https://console.aws.amazon.com/codedeploy/home?region=us-west-2#/deployments/<ID>",
            "external-execution-summary": "Deployment <ID> failed",
            "external-execution-id": "<ID>",
            "error-code": "JobFailed"
        },
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Deploy",
        "state": "FAILED",
        "region": "us-west-2",
        "type": {
            "owner": "AWS",
            "provider": "CodeDeploy",
            "category": "Deploy",
            "version": "1"
        },
        "version": 13.0,
        "pipeline-execution-attempt": 1.0
    },
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "additionalAttributes": {
        "additionalInformation": "Deployment <ID> failed"
    }
}
```

### Action ABANDONED event

When an action execution is abandoned, it emits an event that sends notifications with
the following content. This example is for the pipeline named `"myPipeline"` in
the `us-west-2` Region, for the action `"Deploy"`.

```
{
    "version": "0",
    "id": "01234567-EXAMPLE",
    "detail-type": "CodePipeline Action Execution State Change",
    "source": "aws.codepipeline",
    "account": "123456789012",
    "time": "2020-01-31T18:21:39Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:codepipeline:us-west-2:123456789012:myPipeline"
    ],
    "detail": {
        "pipeline": "myPipeline",
        "execution-id": "12345678-1234-5678-abcd-12345678abcd",
        "stage": "Deploy",
        "action-execution-id": "47f821c5-a902-44b2-ae61-b878d31ecd21",
        "action": "Deploy",
        "state": "ABANDONED",
        "region": "us-west-2",
        "type": {
            "owner": "AWS",
            "provider": "CodeDeploy",
            "category": "Deploy",
            "version": "1"
        },
        "version": 3.0,
        "pipeline-execution-attempt": 1.0
    }
}
```

## Create a Rule That Sends a Notification on a

Pipeline Event

A rule watches for certain events and then routes them to AWS targets that you choose. You
can create a rule that performs an AWS action automatically when another AWS action happens,
or a rule that performs an AWS action regularly on a set schedule.

###### Topics

- [Send a Notification When Pipeline
  State Changes (Console)](#monitoring-cloudwatch-events-console "#monitoring-cloudwatch-events-console")
- [Send a Notification When Pipeline State
  Changes (CLI)](#monitoring-cloudwatch-events-cli "#monitoring-cloudwatch-events-cli")

### Send a Notification When Pipeline

State Changes (Console)

These steps show how to use the EventBridge console to create a rule to send notifications of
changes in CodePipeline.

###### To create an EventBridge rule that targets your pipeline with an Amazon S3 source

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**. Leave the default bus
   selected or choose an event bus. Choose **Create rule**.
3. In **Name**, enter a name for your rule.
4. Under **Rule type**, choose **Rule with an event
   pattern**. Choose **Next**.
5. Under **Event pattern**, choose **AWS
   services**.
6. From the **Event Type** drop-down list, choose the level of state
   change for the notification.
   - For a rule that applies to pipeline-level events, choose **CodePipeline
     Pipeline Execution State Change**.
   - For a rule that applies to stage-level events, choose **CodePipeline
     Stage Execution State Change**.
   - For a rule that applies to action-level events, choose **CodePipeline
     Action Execution State Change**.

7. Specify the state changes the rule applies to:
   - For a rule that applies to all state changes, choose **Any
     state**.
   - For a rule that applies to some state changes only, choose **Specific
     state(s)**, and then choose one or more state values from the
     list.

8. For event patterns that are more detailed than the selectors allow, you can also use
   the **Edit pattern** option in the **Event pattern**
   window to designate an event pattern in JSON format.

###### Note

If not otherwise specified, then the event pattern is created for all
pipelines/stages/actions and states.

For more detailed event patterns, you can copy and paste the following example event
patterns into the **Event pattern** window.

    * Use this sample event pattern to capture failed deploy and build actions
     across all the pipelines.



    ```
    {
    "source": [
        "aws.codepipeline"
      ],
      "detail-type": [
        "CodePipeline Action Execution State Change"
      ],
      "detail": {
        "state": [
          "FAILED"
        ],
        "type": {
          "category": ["Deploy", "Build"]
        }
      }
    }
    ```
    * Use this sample event pattern to capture all rejected or failed approval
     actions across all the pipelines.



    ```
    {
     "source": [
        "aws.codepipeline"
      ],
      "detail-type": [
        "CodePipeline Action Execution State Change"
      ],
      "detail": {
        "state": [
          "FAILED"
        ],
        "type": {
          "category": ["Approval"]
        }
      }
    }
    ```
    * Use this sample event pattern to capture all the events from the specified
     pipelines.



    ```
    {
    "source": [
        "aws.codepipeline"
      ],
      "detail-type": [
        "CodePipeline Pipeline Execution State Change",
        "CodePipeline Action Execution State Change",
        "CodePipeline Stage Execution State Change"
      ],
      "detail": {
        "pipeline": ["myPipeline", "my2ndPipeline"]
      }
    }
    ```

9. Choose **Next**.
10. In **Target types**, choose **AWS
    service**.
11. In **Select a target**, choose **CodePipeline**.
    In **Pipeline ARN**, enter the pipeline ARN for the pipeline to be
    started by this rule.

###### Note

To get the pipeline ARN, run the **get-pipeline** command. The
pipeline ARN appears in the output. It is constructed in this format:

arn:aws:codepipeline:`region`:`account`:`pipeline-name`

Sample pipeline ARN:

arn:aws:codepipeline:us-east-2:80398EXAMPLE:MyFirstPipeline 12. To create or specify an IAM service role that grants EventBridge permissions to invoke
the target associated with your EventBridge rule (in this case, the target is CodePipeline):

    * Choose **Create a new role for this specific resource** to
     create a service role that gives EventBridge permissions to your start your pipeline
     executions.
    * Choose **Use existing role** to enter a service role that gives
     EventBridge permissions to your start your pipeline executions.

13. Choose **Next**.
14. On the **Tags** page, choose **Next**.
15. On the **Review and create** page, review the rule configuration.
    If you're satisfied with the rule, choose **Create rule**.

### Send a Notification When Pipeline State

Changes (CLI)

These steps show how to use the CLI to create an CloudWatch Events rule to send notifications of
changes in CodePipeline.

To use the AWS CLI to create a rule, call the **put-rule** command,
specifying:

- A name that uniquely identifies the rule you are creating. This name must be unique
  across all of the pipelines you create with CodePipeline associated with your AWS
  account.
- The event pattern for the source and detail fields used by the rule. For more
  information, see [Amazon EventBridge and Event Patterns](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

###### To create an EventBridge rule with CodePipeline as the event source

1. Call the **put-rule** command to create a rule specifying the event
   pattern. (See the preceding tables for valid states.)

The following sample command uses **--event-pattern** to create a
rule called `“MyPipelineStateChanges”` that emits the CloudWatch event when a
pipeline execution fails for the pipeline named "myPipeline."

```
aws events put-rule --name "MyPipelineStateChanges" --event-pattern "{\"source\":[\"aws.codepipeline\"],\"detail-type\":[\"CodePipeline Pipeline Execution State Change\"],\"detail\":{\"pipeline\":[\"myPipeline\"],\"state\":[\"FAILED\"]}}"
```

2.  Call the **put-targets** command and include the following
    parameters:

        * The `--rule` parameter is used with the `rule_name` you
         created by using **put-rule**.
        * The `--targets` parameter is used with the list `Id` of
         the target in the list of targets and the `ARN` of the Amazon SNS
         topic.

    The following sample command specifies that for the rule called
    `MyPipelineStateChanges`, the target `Id` is composed of the
    number one, indicating that in a list of targets for the rule, this is target 1. The
    sample command also specifies an example `ARN` for the Amazon SNS topic.

```
aws events put-targets --rule MyPipelineStateChanges --targets Id=1,Arn=arn:aws:sns:us-west-2:11111EXAMPLE:MyNotificationTopic
```

3. Add permissions for EventBridge to use the designated target service to invoke the
   notification. For more information, see [Using resource-based policies for Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-resource-based.md "../../../eventbridge/latest/userguide/eb-use-resource-based.md").
