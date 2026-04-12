# Updating event log configurations

You can change the log level at any time using [UpdateEventLogConfiguration](../APIReference/API_UpdateEventLogConfiguration.md "../APIReference/API_UpdateEventLogConfiguration.md"):

```
aws iot-managed-integrations update-event-log-configuration \
    --id "`your-configuration-id`" \
    --event-log-level "DEBUG"
```

To remove an event log configuration, use [DeleteEventLogConfiguration](../APIReference/API_DeleteEventLogConfiguration.md "../APIReference/API_DeleteEventLogConfiguration.md").

###### Important

Enabling `DEBUG` logging generates significantly more log entries and
increases CloudWatch Logs costs. We recommend starting with `ERROR` and only
increasing the level when actively troubleshooting an issue.
