# Control task subscription

Use these methods to subscribe to control-related tasks from the managed integrations components.

```
iotmi_statusCode_t iotmi_control_subscribe_to_tasks(DeviceSDKClient_SubscriberCallback callback, char context)
```

Subscribes to control-related tasks (for example, device control requests) from the managed integrations components.

**Parameters**

- `callback` (DeviceSDKClient_SubscriberCallback) - A callback function that executes when a task is received.
- `context` (char) - A custom context passed to the callback function.

**Returns**

- `IOTMI_STATUS_OK` - The subscription was successful.
- `IOTMI_STATUS_CUSTOM_PLUGIN_CLIENT_NOT_CONNECTED` - The `DeviceSDKClient` instance is not connected to managed integrations.
- `IOTMI_STATUS_CUSTOM_PLUGIN_SUBSCRIBE_ERROR` - An error occurred while subscribing to the tasks.
