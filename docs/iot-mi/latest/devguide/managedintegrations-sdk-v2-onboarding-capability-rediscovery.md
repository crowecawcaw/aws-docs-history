# Capability rediscovery

This section describes the steps to relearn device capability information for hub-connected devices
using capability rediscovery.

## Prerequisites

Complete these steps before attempting capability rediscovery:

- Onboard a hub device to the managed integrations hub.
- Onboard one or more end devices to the hub.
- Install the latest version of AWS CLI from the [Managed Integrations AWS CLI Command Reference](../../../cli/latest/reference/iot-managed-integrations.md "../../../cli/latest/reference/iot-managed-integrations.md")
- (Optional) Subscribe to [DEVICE_DISCOVERY_STATUS](managedintegrations-notifications.md#managedintegrations-notification-setup "managedintegrations-notifications.md#managedintegrations-notification-setup") event notifications.

## When to use capability rediscovery

Use capability rediscovery in the following scenarios:

- After a firmware update to an end device that adds or modifies device capabilities
- After a hub software update that enables support for new device features
- When device capabilities are not accurately reflected in managed integrations
- To refresh the capability information for a single device or all devices connected to a hub

## Start capability rediscovery

Start capability rediscovery for your hub to update device capabilities.

###### To start capability rediscovery

- Use the [start-device-discovery](../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md "../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md") command with the `CONTROLLER_CAPABILITY_REDISCOVERY` discovery type.

**start-device-discovery example**

```
# For a single device
aws iot-managed-integrations start-device-discovery \
  --discovery-type CONTROLLER_CAPABILITY_REDISCOVERY \
  --controller-identifier `HUB_MANAGED_THING_ID` \
  --protocol `PROTOCOL` \
  --end-device-identifier `DEVICE_MANAGED_THING_ID`

# For all devices on a protocol
aws iot-managed-integrations start-device-discovery \
  --discovery-type CONTROLLER_CAPABILITY_REDISCOVERY \
  --controller-identifier `HUB_MANAGED_THING_ID` \
  --protocol `PROTOCOL`
```

**Response:**

```
{
    "Id": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "StartedAt": "2026-01-12T23:07:49.275Z"
}
```

###### Note

The `--protocol` parameter accepts `ZIGBEE`, `ZWAVE`, or `CUSTOM`.

If the optional `--end-device-identifier` parameter is not provided, all devices associated with the hub for the selected protocol are rediscovered.

For more information, see the [start-device-discovery](../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md "../../../cli/latest/reference/iot-managed-integrations/start-device-discovery.md") command in the managed integrations AWS CLI _Command
Reference_.

To verify that the device capabilities have been updated, see [Get managed thing capabilities](managedintegrations-sdk-v2-cookbook-ugs.md#managedintegrations-sdk-v2-cookbook-check-device-capabilties "managedintegrations-sdk-v2-cookbook-ugs.md#managedintegrations-sdk-v2-cookbook-check-device-capabilties").

## Troubleshooting

Use the following guidance to troubleshoot common issues with capability rediscovery.
When capability rediscovery is in progress, managed integrations sends notifications through Kinesis or EventBridge
as JSON messages.

### Success notifications

**Per device being processed:**

```
{
    "messageType": "DEVICE_DISCOVERY_STATUS",
    // Capability rediscovery with controller and end device
    "resources": ["arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/abc123def456", "arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/xyz789uvw012"],
    "payload": {
        "deviceDiscoveryId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "status": "RUNNING",
        "deviceCount": 1
    }
}
```

**Completion:**

```
{
    "messageType": "DEVICE_DISCOVERY_STATUS",
    // Capability rediscovery with controller only
    "resources": ["arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/abc123def456"],
    "payload": {
        "deviceDiscoveryId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "status": "SUCCEEDED",
        "deviceCount": 0
    }
}
```

### Failure notifications

**Device failure:**

```
{
    "messageType": "DEVICE_DISCOVERY_STATUS",
    // Capability rediscovery with controller and end device
    "resources": ["arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/abc123def456", "arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/ghi345jkl678"],
    "payload": {
        "deviceDiscoveryId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "status": "RUNNING",
        "deviceCount": 1,
        "error": {
            "code": "500",
            "message": "Device unreachable",
            "managedThingId": "ghi345jkl678"
        }
    }
}
```

**Complete failure:**

```
{
    "messageType": "DEVICE_DISCOVERY_STATUS",
    // Capability rediscovery with controller only
    "resources": ["arn:aws:iotmanagedintegrations:us-east-1:123456789012:managed-thing/abc123def456"],
    "payload": {
        "deviceDiscoveryId": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
        "status": "FAILED",
        "deviceCount": 0,
        "error": {
            "code": "404",
            "message": "Specified controller does not exist"
        }
    }
}
```

### No notifications received

If you do not receive notifications about the discovery status, verify that you have
subscribed to `DEVICE_DISCOVERY_STATUS` event notifications. For more information
on setting up notifications, see [Set up managed integrations
notifications](managedintegrations-notifications.md#managedintegrations-notification-setup "managedintegrations-notifications.md#managedintegrations-notification-setup").

### Some devices not updated

If some devices fail to update during capability rediscovery, check the error messages
in the `DEVICE_DISCOVERY_STATUS` notifications. Common error messages include:

- `Device unreachable` - The device is offline or not responding
- `Timeout querying device` - The device is not responding within the expected timeframe
- `Invalid capability report` - The device firmware may have an issue

To resolve these issues, ensure the affected devices are powered on and reachable, then
retry capability rediscovery for the failed devices individually using the
`--end-device-identifier` parameter.

### Discovery never completes

If the capability rediscovery process does not complete, check the discovery status
using the discovery job ID returned from the `start-device-discovery` command:

```
aws iot-managed-integrations get-device-discovery \
  --identifier `DISCOVERY_JOB_ID`
```

If the discovery is stuck:

- Verify that the hub is online and connected to managed integrations
- Wait up to 15 minutes for the discovery to timeout automatically
- Retry the capability rediscovery after confirming the hub and devices are operational
