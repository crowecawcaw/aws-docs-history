

# Service job queue blocked events
<a name="batch-service-job-queue-blocked-events"></a>

Anytime that AWS Batch detects a blocked queue, an event is created in Amazon CloudWatch Events. The reason for the blocked queue is available in the `statusReason` field in the [`DescribeServiceJob`](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html) API action.

**Example Service Job Queue Blocked Event**  
Service job queue blocked events are delivered in the following format. The `detail` section resembles the response that's returned from the [DescribeServiceJob](https://docs.aws.amazon.com/batch/latest/APIReference/API_DescribeServiceJob.html) API operation in the *AWS Batch API Reference*. For more information about EventBridge parameters, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.  
The `tags` and `serviceRequestPayload` fields are not included in the event `detail`.

```
{
  "version": "0",
  "id": "c8f9c4b5-76e5-d76a-f980-7011e206042b",
  "detail-type": "Batch Service Job Queue Blocked",
  "source": "aws.batch",
  "account": "{{123456789012}}",
  "time": "2022-01-11T23:36:40Z",
  "region": "{{us-east-1}}",
  "resources": [
    "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8"
  ],
  "detail": {
    "attempts": [],
    "createdAt": 1641944200058,
    "jobArn": "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/4c7599ae-0a82-49aa-ba5a-4727fcce14a8",
    "jobId": "6271dfdf-d8a7-41b1-a4d2-55a2224f5375",
    "jobName": "event-test",
    "jobQueue": "arn:aws:batch:{{us-east-1}}:{{123456789012}}:job-queue/HappyPathJobQueue",
    "serviceJobType": "SAGEMAKER_TRAINING",
    "status": "RUNNABLE",
    "statusReason": "{{blocked-reason}}",
    "timeoutConfig": {
      "attemptDurationSeconds": 60
    }
  }
}
```