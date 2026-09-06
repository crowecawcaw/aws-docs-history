

# Failure mode assessment failed event
<a name="next-gen-eventbridge-assessment-failed"></a>

The following is an example event emitted when a failure mode assessment fails.

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Failure Mode Assessment Failed",
  "source": "aws.resiliencehub",
  "account": "111122223333",
  "time": "2026-01-15T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:resiliencehub:us-east-1:111122223333:service/my-service:abc123"
  ],
  "detail": {
    "assessmentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "FAILED",
    "failureReason": "Unable to assume the invoker role specified in the service configuration."
  }
}
```

The `detail` object contains the following fields:


| Field | Description | 
| --- | --- | 
| assessmentId | The unique identifier of the failed assessment. | 
| status | The assessment status. Value: FAILED. | 
| failureReason | A description of why the assessment failed. | 