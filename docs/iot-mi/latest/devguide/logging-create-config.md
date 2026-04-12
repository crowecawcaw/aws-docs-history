# Creating event log configurations

Use the [CreateEventLogConfiguration](../APIReference/API_CreateEventLogConfiguration.md "../APIReference/API_CreateEventLogConfiguration.md")
API action to enable event logging for a resource type. We recommend creating a separate
configuration for each resource type, using `*` as the resource identifier to
capture logs for all resources of that type. Start at the `ERROR` log level to
receive all failure logs without generating excessive volume or cost.

```
aws iot-managed-integrations create-event-log-configuration \
    --resource-type "managed-thing" \
    --resource-id "*" \
    --event-log-level "ERROR"
```

Repeat for each resource type:

```
aws iot-managed-integrations create-event-log-configuration \
    --resource-type "credential-locker" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "provisioning-profile" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "ota-task" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "account-association" \
    --resource-id "*" \
    --event-log-level "ERROR"
```

After you call `CreateEventLogConfiguration`, logs are pushed to the
`/aws/iotmanagedintegrations/EventLog` log group in CloudWatch Logs. Use [ListEventLogConfigurations](../APIReference/API_ListEventLogConfigurations.md "../APIReference/API_ListEventLogConfigurations.md")
to view all configurations, or [GetEventLogConfiguration](../APIReference/API_GetEventLogConfiguration.md "../APIReference/API_GetEventLogConfiguration.md")
to retrieve a specific configuration by ID.
