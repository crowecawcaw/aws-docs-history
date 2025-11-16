# CloudWatch | Modify Log Retention Period

Modify the retention period for Amazon CloudWatch log groups. This change performs direct API actions whether or not the CloudWatch log group is part of a stack, which can cause stack drift.

**Full classification:** Management | Monitoring and notification | CloudWatch | Modify log retention period

## Change Type Details

|                             |                  |
| --------------------------- | ---------------- |
| Change type ID              | ct-0vfx8rwd1mcnn |
| Current version             | 1.0              |
| Expected execution duration | 60 minutes       |
| AWS approval                | Required         |
| Customer approval           | Not required     |
| Execution mode              | Automated        |

## Additional Information

Info not available.

## Execution Input Parameters

For detailed information about the execution input parameters, see
[Schema for Change Type ct-0vfx8rwd1mcnn](schemas.md#ct-0vfx8rwd1mcnn-schema-section "schemas.md#ct-0vfx8rwd1mcnn-schema-section").

## Example: Required Parameters

```
{
  "DocumentName": "AWSManagedServices-ModifyCloudWatchLogRetentionPeriod",
  "Region": "us-east-1",
  "Parameters": {
    "LogGroupNames": [
      "my-log-group"
    ],
    "RetentionDays": "90"
  }
}
```

## Example: All Parameters

```
Example not available.
```
