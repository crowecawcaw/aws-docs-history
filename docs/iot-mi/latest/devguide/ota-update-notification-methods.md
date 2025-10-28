# Monitor OTA notifications

You can monitor OTA updates using two different methods:

## Push notifications through Kinesis Data Streams

When OTA notifications are enabled, update status events are automatically pushed to your Kinesis stream. This provides real-time visibility into the progress of firmware updates across devices.

## Monitor with ListOtaTaskExecutions API

You can use the
[ListOtaTaskExecutions](../APIReference/API_ListOtaTaskExecutions.md "../APIReference/API_ListOtaTaskExecutions.md")
API to manually check the status of OTA updates for your managed things:

```
aws iotmanagedintegrations list-ota-task-executions \
  --task-id "task-123456789" \
  --max-results 25
```

The response provides detailed execution status for each managed thing:

```
{
  "taskExecutionSummaries": [
    {
      "taskExecutionSummary": {
        "executionNumber": 1,
        "lastUpdatedAt": 1634567890,
        "queuedAt": 1634567800,
        "startedAt": 1634567830,
        "status": "SUCCEEDED",
        "retryAttempt": 0
      },
      "managedThingId": "device-001"
    },
    {
      "taskExecutionSummary": {
        "executionNumber": 1,
        "lastUpdatedAt": 1634567920,
        "queuedAt": 1634567800,
        "startedAt": 1634567840,
        "status": "IN_PROGRESS",
        "retryAttempt": 0
      },
      "managedThingId": "device-002"
    }
  ],
  "nextToken": "NEXT_TOKEN"
}
```

This API allows you to retrieve detailed execution status for each managed thing targeted by a specific OTA task, including timestamps and current status.
