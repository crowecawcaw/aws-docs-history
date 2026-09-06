

# Updating event log configurations
<a name="logging-update-config"></a>

You can change the log level at any time using [UpdateEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateEventLogConfiguration.html):

```
aws iot-managed-integrations update-event-log-configuration \
    --id "{{your-configuration-id}}" \
    --event-log-level "DEBUG"
```

To remove an event log configuration, use [DeleteEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeleteEventLogConfiguration.html).

**Important**  
Enabling `DEBUG` logging generates significantly more log entries and increases CloudWatch Logs costs. We recommend starting with `ERROR` and only increasing the level when actively troubleshooting an issue.