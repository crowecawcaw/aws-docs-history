

# Viewing schedule actions
<a name="feed-scheduling-list"></a>

To view the schedule actions on a feed, use the `list-schedule-actions` command. The response includes the status of each action. If an action failed, the response also includes an `error` that describes the failure.

```
aws elemental-inference list-schedule-actions \
  --id <{{feed-id}}>
```

The following example shows a response.

```
{
  "scheduleActions": [
    {
      "actionName": "enable-smartcrop-game-1",
      "startConfiguration": {
        "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T19:00:00Z" }
      },
      "operations": [
        { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "ENABLED" } }
      ],
      "status": "COMPLETED"
    },
    {
      "actionName": "game-2-handoff",
      "startConfiguration": {
        "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T20:45:00Z" }
      },
      "operations": [
        { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "ENABLED" } },
        {
          "updateClippingDataSourceConfiguration": {
            "outputName": "event-clip-output",
            "dataSourceConfiguration": { "fixtureId": "{{fixture-id}}" }
          }
        }
      ],
      "status": "FAILED",
      "error": {
        "errorCode": "INVALID_ACTION_TARGET",
        "errorMessage": "Output 'event-clip-output' not found in current feed config"
      }
    }
  ]
}
```

To control the number of results for each page, use the `--max-results` option (1–100). To get the next page, use the `--next-token` option.