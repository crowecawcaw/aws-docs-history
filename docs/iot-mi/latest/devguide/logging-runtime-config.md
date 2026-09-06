

# Configuring runtime logs
<a name="logging-runtime-config"></a>

Runtime log configurations control device-side logging behavior for individual managed things. Use [PutRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutRuntimeLogConfiguration.html) to set the runtime log configuration for a specific managed thing:

```
aws iot-managed-integrations put-runtime-log-configuration \
    --managed-thing-id "{{your-managed-thing-id}}" \
    --runtime-log-configurations '{"LogLevel":"ERROR","UploadLog":true,"UploadPeriodMinutes":5}'
```

Use [GetRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetRuntimeLogConfiguration.html) to retrieve the current configuration, or [ResetRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ResetRuntimeLogConfiguration.html) to reset it to defaults.