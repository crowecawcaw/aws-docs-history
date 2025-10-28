# Control task publication

Use these methods to publish control-related requests to the managed integrations components.

```
iotmi_statusCode_t iotmi_control_publish_request(DataModel::iotmi_client_request_t request)
```

Publishes a control-related request to the managed integrations components. For example, unsolicited events, command requests, or device state queries.

**Parameters**

`request` (DataModel::iotmi_client_request_t) - A pointer to a request structure containing the details.

**Returns**

- `IOTMI_STATUS_OK` - The request was published successfully.
- `IOTMI_STATUS_CUSTOM_PLUGIN_CLIENT_NOT_CONNECTED` - The DeviceSDKClient instance is not connected to managed integrations.
- `IOTMI_STATUS_INVALID_PARAMETER` - One or more parameters in the request are invalid.
- `IOTMI_STATUS_INVALID_JSON_OBJECT` - The request payload is not a valid JSON object.
- `IOTMI_STATUS_NO_MEMORY` - A memory allocation error occurred.
