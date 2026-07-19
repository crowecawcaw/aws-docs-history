# Failure mode finding resolved event

The following is an example event emitted when a failure mode finding is marked as
Resolved or Irrelevant.

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Failure Mode Finding Resolved",
  "source": "aws.resiliencehub",
  "account": "111122223333",
  "time": "2026-01-15T10:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:resiliencehub:us-east-1:111122223333:service/my-service:abc123"
  ],
  "detail": {
    "findingId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "status": "RESOLVED",
    "severity": "HIGH",
    "category": "SINGLE_POINT_OF_FAILURE"
  }
}
```

The `detail` object contains the following fields:

| Field       | Description                                                                              |
| ----------- | ---------------------------------------------------------------------------------------- |
| `findingId` | The unique identifier of the resolved finding.                                           |
| `status`    | The resolution status. Values: `RESOLVED`,<br>`IRRELEVANT`.                              |
| `severity`  | The severity of the finding. Values: `HIGH`,<br>`MEDIUM`, `LOW`.                         |
| `category`  | The failure mode category (for example,<br>`SINGLE_POINT_OF_FAILURE`,<br>`SHARED_FATE`). |
