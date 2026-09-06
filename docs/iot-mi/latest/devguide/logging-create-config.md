

# Creating event log configurations
<a name="logging-create-config"></a>

Use the [CreateEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateEventLogConfiguration.html) API action to enable event logging for a resource type. We recommend creating a separate configuration for each resource type, using `*` as the resource identifier to capture logs for all resources of that type. Start at the `ERROR` log level to receive all failure logs without generating excessive volume or cost.

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

After you call `CreateEventLogConfiguration`, logs are pushed to the `/aws/iotmanagedintegrations/EventLog` log group in CloudWatch Logs. Use [ListEventLogConfigurations](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListEventLogConfigurations.html) to view all configurations, or [GetEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetEventLogConfiguration.html) to retrieve a specific configuration by ID.