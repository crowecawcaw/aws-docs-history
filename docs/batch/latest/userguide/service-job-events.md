# Service job state change events

Anytime that an existing service job changes states, an event is created.
For more information about service job states, see [Mapping AWS Batch service job status to SageMaker AI
status](service-job-status.md "service-job-status.md").

###### Note

Events aren't created for the initial job submission.

###### Example Service Job State Change Event

Service job state change events are delivered in the following format. The
`detail` section resembles the response that's returned from a
[DescribeServiceJob](../APIReference/API_DescribeServiceJob.md "../APIReference/API_DescribeServiceJob.md") API operation in the
_AWS Batch API Reference_. For
more information about EventBridge parameters, see [Events and Event
Patterns](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User Guide_.

###### Note

The `tags` and
`serviceRequestPayload` fields are not included in the event `detail`.

```
{
  "version": "0",
  "id": "c8f9c4b5-76e5-d76a-f980-7011e206042b",
  "detail-type": "Batch Service Job State Change",
  "source": "aws.batch",
  "account": "`123456789012`",
  "time": "2022-01-11T23:36:40Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:batch:`us-east-1`:`123456789012`:service-job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8"
  ],
  "detail": {
    "attempts": [
      {
        "serviceResourceId": {
          "name": "TrainingJobArn",
          "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/AWSBatchmy-training-job88b610a69aa8380ca5b0a7aba3f81cb8"
        },
        "startedAt": 1641944300058,
        "stoppedAt": 1641944400058,
        "statusReason": "Received status from SageMaker: Training job completed"
      }
    ],
    "createdAt": 1641944200058,
    "jobArn": "arn:aws:batch:`us-east-1`:`123456789012`:service-job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8",
    "jobId": "0bb17543-ece6-4480-b1a7-a556d344746b",
    "jobName": "event-test",
    "jobQueue": "arn:aws:batch:`us-east-1`:`123456789012`:job-queue/HappyPathJobQueue",
    "latestAttempt": {
      "serviceResourceId": {
        "name": "TrainingJobArn",
        "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/AWSBatchmy-training-job88b610a69aa8380ca5b0a7aba3f81cb8"
      }
    },
    "serviceJobType": "SAGEMAKER_TRAINING",
    "startedAt": 1641944300058,
    "status": "SUCCEEDED",
    "statusReason": "Received status from SageMaker: Training job completed",
    "stoppedAt": 1641944400058,
    "timeoutConfig": {
      "attemptDurationSeconds": 60
    }
  }
}
```
