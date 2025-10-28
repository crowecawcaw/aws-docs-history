# Client initialization

To start using the `DeviceSDKClient`, initialize it with a client ID.

```
iotmi_statusCode_t DeviceSDKClient(const std::string& clientId)
```

This creates a new `DeviceSDKClient` instance with the specified `clientId`. The `clientId` must match the one you register with managed integrations.

**Parameters**

`clientId` (string) - The client ID for this instance.

```
connect()
```

Connects the `DeviceSDKClient` instance to managed integrations.

**Returns**

- `IOTMI_STATUS_OK` - The connection was successful.
- `IOTMI_STATUS_CUSTOM_PLUGIN_CONNECTION_ERROR` - An error occurred while connecting to managed integrations.
