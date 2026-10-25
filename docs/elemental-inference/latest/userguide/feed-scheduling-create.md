

# Creating a schedule action
<a name="feed-scheduling-create"></a>

To create a schedule action, use the `create-schedule-action` command. Specify the feed ID, a name for the action, the start configuration, and the operations. In the examples that follow, replace `{{feed-id}}` with the ID of your feed, and `{{fixture-id}}` with the ID of the game that you want to clip.

The following AWS CLI command enables a smart crop output at `2026-07-25T19:00:00Z`.

```
aws elemental-inference create-schedule-action \
  --id <{{feed-id}}> \
  --action-name "enable-smartcrop-game-1" \
  --start-configuration '{
    "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T19:00:00Z" }
  }' \
  --operations '[
    { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "ENABLED" } }
  ]'
```

If the request succeeds, the response contains the new action, with a status of `PENDING`. If the feed already has an action with the same name, the request returns a `ValidationException`. Choose a different name, or delete the existing action first.

```
{
  "actionName": "enable-smartcrop-game-1",
  "startConfiguration": {
    "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T19:00:00Z" }
  },
  "operations": [
    { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "ENABLED" } }
  ],
  "status": "PENDING"
}
```

The following AWS CLI command enables a smart crop output and attaches a new game to an event clipping output at the same time. Elemental Inference applies both changes together, or neither.

```
aws elemental-inference create-schedule-action \
  --id <{{feed-id}}> \
  --action-name "game-2-handoff" \
  --start-configuration '{
    "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T20:45:00Z" }
  }' \
  --operations '[
    { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "ENABLED" } },
    {
      "updateClippingDataSourceConfiguration": {
        "outputName": "event-clip-output",
        "dataSourceConfiguration": { "fixtureId": "<{{fixture-id}}>" }
      }
    }
  ]'
```

The following AWS CLI command disables the smart crop output after the game.

```
aws elemental-inference create-schedule-action \
  --id <{{feed-id}}> \
  --action-name "disable-smartcrop-game-1" \
  --start-configuration '{
    "fixedModeScheduleActionStartSettings": { "scheduledAt": "2026-07-25T21:00:00Z" }
  }' \
  --operations '[
    { "updateOutputStatus": { "outputName": "smart-crop-output", "status": "DISABLED" } }
  ]'
```