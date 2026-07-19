# Failure mode assessment completed event

The following is an example event emitted when a failure mode assessment completes
successfully.

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Failure Mode Assessment Completed",
  "source": "aws.resiliencehub",
  "account": "111122223333",
  "time": "2026-01-15T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:resiliencehub:us-east-1:111122223333:service/my-service:abc123"
  ],
  "detail": {
    "assessmentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "SUCCESS",
    "findingsCount": 5,
    "highSeverityCount": 2
  }
}
```

The `detail` object contains the following fields:

| Field               | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `assessmentId`      | The unique identifier of the completed assessment.    |
| `status`            | The assessment status. Value: `SUCCESS`.              |
| `findingsCount`     | The total number of failure mode findings identified. |
| `highSeverityCount` | The number of high-severity findings identified.      |
