# Configuring runtime logs

Runtime log configurations control device-side logging behavior for individual managed
things. Use [PutRuntimeLogConfiguration](../APIReference/API_PutRuntimeLogConfiguration.md "../APIReference/API_PutRuntimeLogConfiguration.md")
to set the runtime log configuration for a specific managed thing:

```
aws iot-managed-integrations put-runtime-log-configuration \
    --managed-thing-id "`your-managed-thing-id`" \
    --runtime-log-configurations '{"LogLevel":"ERROR","UploadLog":true,"UploadPeriodMinutes":5}'
```

Use [GetRuntimeLogConfiguration](../APIReference/API_GetRuntimeLogConfiguration.md "../APIReference/API_GetRuntimeLogConfiguration.md")
to retrieve the current configuration, or [ResetRuntimeLogConfiguration](../APIReference/API_ResetRuntimeLogConfiguration.md "../APIReference/API_ResetRuntimeLogConfiguration.md")
to reset it to defaults.
