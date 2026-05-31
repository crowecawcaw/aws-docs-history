# Assessment completion events

Next generation Resilience Hub emits an event to EventBridge when a failure mode assessment completes, enabling
you to trigger automated actions based on assessment results. The following is an example
assessment completion event.

```

{
  "source": "aws.resiliencehub",
  "detail-type": "Assessment Completed",
  "detail": {
    "serviceArn": "arn:aws:resiliencehub:us-east-1:123456789012:service/checkout:abc123",
    "assessmentId": "a1b2c3d4-...",
    "status": "SUCCESS",
    "findingsCount": 5,
    "highSeverityCount": 2
  }
}
```
