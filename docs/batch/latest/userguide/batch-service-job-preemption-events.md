

# Service job preemption events
<a name="batch-service-job-preemption-events"></a>

Preemption events are published whenever a preemption sequence starts or completes. A started event is created when preemption is first triggered to reclaim borrowed capacity. A completed event is created when the preemption sequence finishes and includes a summary of the preempted attempts.

**Example Service Job Preemption Started Event**  
Service job preemption started events are delivered in the following format. For more information about EventBridge parameters, see [Events and Event Patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html) in the *Amazon EventBridge User Guide*.  

```
{
  "version": "0",
  "id": "1b4a511e-2737-226a-a1e7-fc97f1cd9681",
  "detail-type": "Batch Service Job Preemption Started",
  "source": "aws.batch",
  "account": "{{123456789012}}",
  "time": "2026-03-16T19:57:27Z",
  "region": "{{us-east-1}}",
  "resources": [
    "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/51f245a9-2995-4a53-bced-7b3c00028f84"
  ],
  "detail": {
    "statusReason": "PREEMPTION_IN_PROGRESS: Cross-share preemption triggered to reclaim borrowed capacity",
    "preemptedJobArn": "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/51f245a9-2995-4a53-bced-7b3c00028f84",
    "status": "RUNNING"
  }
}
```

**Example Service Job Preemption Completed Event**  
Service job preemption completed events are delivered in the following format. The `preemptionSummary` field contains details about the preempted attempts, including the count and the most recent preempted attempt information.  

```
{
  "version": "0",
  "id": "2b1c6151-c166-edf5-822c-211b3bfd46b2",
  "detail-type": "Batch Service Job Preemption Completed",
  "source": "aws.batch",
  "account": "{{123456789012}}",
  "time": "2026-03-16T19:57:47Z",
  "region": "{{us-east-1}}",
  "resources": [
    "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/51f245a9-2995-4a53-bced-7b3c00028f84"
  ],
  "detail": {
    "preemptedJobArn": "arn:aws:batch:{{us-east-1}}:{{123456789012}}:service-job/51f245a9-2995-4a53-bced-7b3c00028f84",
    "preemptionSummary": {
      "preemptedAttemptCount": 1,
      "recentPreemptedAttempts": [
        {
          "serviceResourceId": {
            "name": "TrainingJobArn",
            "value": "arn:aws:sagemaker:us-east-1:123456789012:training-job/AWSBatchqm-training-job9b2f08f911cf3dd794c1b3e72ae7ca5f"
          },
          "startedAt": 1773690923359,
          "stoppedAt": 1773691064669,
          "statusReason": "Cross-share preemption triggered to reclaim borrowed capacity"
        }
      ]
    },
    "status": "RUNNABLE"
  }
}
```